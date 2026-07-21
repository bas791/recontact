#!/usr/bin/env python3
"""Inject data/customers.json into dashboard/template.html -> dist/index.html."""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "customers.json").read_text(encoding="utf-8"))
blob = json.dumps(data, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")
tpl = (root / "dashboard" / "template.html").read_text(encoding="utf-8")
assert "/*__DATA__*/" in tpl, "template is missing the /*__DATA__*/ placeholder"
out = root / "dist" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(tpl.replace("/*__DATA__*/", blob), encoding="utf-8")
print(f"built {out} ({out.stat().st_size:,} bytes)")
