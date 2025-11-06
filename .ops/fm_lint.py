#!/usr/bin/env python3
import os, re, sys, datetime, json, yaml, textwrap
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]  # repo root
SCHEMA_PATH = ROOT / ".ops" / "schema.yml"
TODAY = datetime.date.today().isoformat()

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)

# Folders to scan (adjust for your tree)
SCAN_DIRS = [
    "templates",
    "engines",
    "helpers",
    "workflows",
    "docs",
    "procedures",
]

def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_front_matter(text):
    m = FM_RE.match(text)
    if not m:
        return None, text  # no front matter
    front_raw = m.group(1)
    body = text[m.end():]
    data = yaml.safe_load(front_raw) or {}
    return data, body

def dump_front_matter(data):
    # Keep field order stable
    return "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True).rstrip() + "\n---\n"

def normalize_id(val):
    # enforce repo-wide kebab-case id (no spaces, lowercase)
    v = str(val).strip()
    v = re.sub(r"[^a-zA-Z0-9\-]+", "-", v).strip("-").lower()
    return v

def derive_permalink(fm):
    # /{category}/{id}/ if category present; else /{id}/
    cat = str(fm.get("category","")).strip()
    base = f"/{normalize_id(fm.get('id',''))}/"
    if cat:
        base = f"/{normalize_id(cat)}/{normalize_id(fm.get('id',''))}/"
    return base

def normalize_tags(tags):
    if tags is None:
        return []
    if isinstance(tags, str):
        # support "a, b, c"
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    return sorted(set([str(t).strip().lower() for t in tags]))

def apply_defaults_and_rules(schema, fm, path):
    changed = False
    required = schema.get("required", [])
    defaults = schema.get("defaults", {})
    enums = schema.get("enums", {})

    # Ensure required fields exist (use defaults when available)
    for field in required:
        if field not in fm or fm[field] in (None, ""):
            if field in defaults:
                fm[field] = defaults[field]
                changed = True
            else:
                # create empty placeholder to force author to fill later
                fm[field] = ""
                changed = True

    # Normalize key fields
    if "id" in fm:
        norm = normalize_id(fm["id"])
        if fm["id"] != norm:
            fm["id"] = norm
            changed = True

    if "title" in fm and isinstance(fm["title"], str):
        t = fm["title"].strip()
        if t != fm["title"]:
            fm["title"] = t
            changed = True

    # Normalize tags
    ntags = normalize_tags(fm.get("tags"))
    if fm.get("tags") != ntags:
        fm["tags"] = ntags
        changed = True

    # Enum check
    if "complexity" in fm and enums.get("complexity"):
        if fm["complexity"] not in enums["complexity"]:
            # fallback to default if invalid
            fm["complexity"] = defaults.get("complexity","Medium")
            changed = True
    # Derive permalink if missing
    if "permalink" not in fm or not str(fm["permalink"]).strip():
        fm["permalink"] = derive_permalink(fm)
        changed = True
    # Update last-updated automatically (only when file content changes or the script runs in "touch" mode)
    # For simplicity we always set it to today; you can gate on git diff if desired.
    if fm.get("last-updated") != TODAY:
        fm["last-updated"] = TODAY
        changed = True

    return fm, changed

def process_md(md_path, schema, write=True):
    text = md_path.read_text(encoding="utf-8")
    fm, body = load_front_matter(text)
    if fm is None:
        # Insert minimal front matter if missing
        fm = {
            "id": normalize_id(md_path.stem),
            "title": md_path.stem.replace("-", " ").title(),
            "description": "",
            "role": "",
            "category": "",
            "complexity": "Medium",
            "output-format": "Markdown",
            "tags": [],
            "version": "0.1",
            "last-updated": TODAY,
        }
        new_text = dump_front_matter(fm) + body
        md_path.write_text(new_text, encoding="utf-8")
        return True

    fm2, changed = apply_defaults_and_rules(schema, fm, md_path)
    if changed:
        new_text = dump_front_matter(fm2) + body
        if write:
            md_path.write_text(new_text, encoding="utf-8")
    return changed
def main():
    schema = load_schema()
    changed_any = False

    targets = []
    for d in SCAN_DIRS:
        p = ROOT / d
        if p.exists():
            targets += list(p.rglob("*.md"))

    # also include root *.md if you want
    # targets += list(ROOT.glob("*.md"))

    for md in targets:
        if md.name.lower() in ("readme.md", "license.md", "index.md"):
            continue
        if process_md(md, schema, write=True):
            print(f"FIXED: {md}")
            changed_any = True

    if changed_any:
        # Write a machine-readable manifest for Jekyll index if you want
        manifest = []
        for md in targets:
            t = md.read_text(encoding="utf-8")
            fm, _ = load_front_matter(t)
            if fm:
                manifest.append({
                    "path": str(md.relative_to(ROOT)),
                    "id": fm.get("id"),
                    "title": fm.get("title"),
                    "category": fm.get("category"),
                    "complexity": fm.get("complexity"),
                    "tags": fm.get("tags"),
                    "permalink": fm.get("permalink"),
                    "last_updated": fm.get("last-updated"),
                })
        (ROOT / ".ops" / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print("changed_any=" + ("1" if changed_any else "0"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
