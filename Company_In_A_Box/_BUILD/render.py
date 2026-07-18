#!/usr/bin/env python3
"""v2 renderer: front-matter markdown -> house-style HTML (cover + control block + body + sources).
Usage: python3 render.py <doc.md>   -> writes <doc.html> next to it.
Front matter (--- fenced, at top of .md):
  title, subtitle, pack, purpose, status, reading_time, date
"""
import sys, re, pathlib, markdown

CSS = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
* { box-sizing: border-box; }
body { font-family: 'Helvetica Neue', Arial, sans-serif; color:#1a1f2b; font-size:10.5pt; line-height:1.5; margin:0; }
/* ---------- COVER ---------- */
.cover { position:relative; height:247mm; background:#0f3d5c; color:#fff; padding:26mm 20mm; page-break-after:always; display:flex; flex-direction:column; }
.cover .kicker { color:#e6b866; font-weight:700; letter-spacing:2px; font-size:10pt; text-transform:uppercase; }
.cover h1 { font-size:30pt; line-height:1.15; margin:10mm 0 6mm 0; font-weight:800; }
.cover .rule { width:60mm; height:3px; background:#c8862a; margin:4mm 0 6mm 0; }
.cover .subtitle { font-size:13pt; color:#cdd9e4; max-width:130mm; }
.cover .meta { margin-top:auto; border-top:1px solid rgba(255,255,255,.25); padding-top:6mm; font-size:9.5pt; color:#cdd9e4; }
.cover .meta b { color:#fff; font-weight:700; }
.cover .classification { color:#e6b866; font-weight:700; }
.cover .pack-badge { display:inline-block; border:1px solid #e6b866; color:#e6b866; padding:2px 10px; border-radius:3px; font-size:9pt; font-weight:700; }
/* ---------- CONTROL BLOCK ---------- */
.control { border:1px solid #d8dee6; border-left:4px solid #0f3d5c; background:#f4f7fa; padding:8px 12px; margin:0 0 16px 0; font-size:9pt; color:#3a3f4b; }
.control table { width:100%; border-collapse:collapse; }
.control td { padding:2px 8px 2px 0; vertical-align:top; border:none; }
.control td.k { color:#0f3d5c; font-weight:700; white-space:nowrap; width:32mm; }
/* ---------- TYPE ---------- */
h2 { color:#0f3d5c; font-size:14.5pt; border-bottom:2px solid #0f3d5c; padding-bottom:4px; margin:24px 0 10px; break-after:avoid; }
h3 { color:#14506f; font-size:12pt; margin:16px 0 6px; break-after:avoid; }
h4 { color:#14506f; font-size:10.5pt; margin:12px 0 4px; break-after:avoid; }
p { margin:6px 0; }
strong { color:#0f3d5c; }
a { color:#12856f; text-decoration:none; }
ul,ol { margin:6px 0; padding-left:20px; } li { margin:3px 0; }
/* ---------- TABLES ---------- */
table { border-collapse:collapse; width:100%; margin:12px 0; font-size:9.2pt; break-inside:avoid; }
th { background:#0f3d5c; color:#fff; text-align:left; padding:6px 8px; font-weight:600; }
td { border:1px solid #d8dee6; padding:5px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#f4f7fa; }
/* ---------- COMPONENTS ---------- */
blockquote { break-inside:avoid; }
.bluf { background:#eef4f8; border:1px solid #cfe0ec; border-left:4px solid #12856f; padding:10px 14px; margin:14px 0; break-inside:avoid; }
.bluf .lbl { color:#12856f; font-weight:700; text-transform:uppercase; font-size:8.5pt; letter-spacing:1px; }
.callout { background:#fbf6ee; border:1px solid #ecdcc0; border-left:4px solid #c8862a; padding:10px 14px; margin:12px 0; break-inside:avoid; }
.callout .lbl { color:#b8791f; font-weight:700; text-transform:uppercase; font-size:8.5pt; letter-spacing:1px; }
.warn { background:#fdf3f3; border:1px solid #f0d4d4; border-left:4px solid #c0392b; padding:10px 14px; margin:12px 0; break-inside:avoid; }
.warn .lbl { color:#c0392b; font-weight:700; text-transform:uppercase; font-size:8.5pt; letter-spacing:1px; }
.tiles { display:flex; gap:10px; margin:14px 0; break-inside:avoid; }
.tile { flex:1; border:1px solid #d8dee6; border-top:3px solid #c8862a; border-radius:4px; padding:10px 12px; text-align:center; background:#fff; }
.tile .n { font-size:20pt; font-weight:800; color:#0f3d5c; line-height:1; }
.tile .l { font-size:8pt; color:#5a6472; text-transform:uppercase; letter-spacing:.5px; margin-top:4px; }
figure { break-inside:avoid; margin:14px 0; text-align:center; }
figure img { max-width:100%; border:1px solid #e2e8ef; border-radius:4px; }
figure figcaption { font-size:8.5pt; color:#5a6472; margin-top:5px; font-style:italic; }
.exhibit-cap { font-size:8.5pt; color:#0f3d5c; font-weight:700; text-transform:uppercase; letter-spacing:.5px; margin-bottom:3px; }
.sources { margin-top:22px; border-top:2px solid #0f3d5c; padding-top:8px; }
.sources h2 { border:none; font-size:11pt; margin-bottom:6px; }
.sources table { font-size:8.3pt; }
hr { border:none; border-top:1px solid #d8dee6; margin:20px 0; }
.tag-v{color:#12856f;font-weight:700;} .tag-a{color:#b8791f;font-weight:700;} .tag-o{color:#c0392b;font-weight:700;}
"""

def parse_front_matter(text):
    meta = {}
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    else:
        body = text
    return meta, body

def build(md_path):
    text = pathlib.Path(md_path).read_text(encoding='utf-8')
    meta, body_md = parse_front_matter(text)
    title = meta.get('title', pathlib.Path(md_path).stem.replace('_', ' '))
    subtitle = meta.get('subtitle', '')
    pack = meta.get('pack', '')
    purpose = meta.get('purpose', '')
    status = meta.get('status', '')
    reading = meta.get('reading_time', '')
    date = meta.get('date', 'July 2026')
    body_html = markdown.markdown(body_md, extensions=['tables', 'fenced_code', 'sane_lists', 'attr_list'])
    control = f"""<div class="control"><table>
<tr><td class="k">Document</td><td>{title}</td></tr>
<tr><td class="k">Purpose</td><td>{purpose}</td></tr>
<tr><td class="k">Status</td><td>{status}</td></tr>
<tr><td class="k">Prepared by</td><td>Waqas Mian &nbsp;·&nbsp; for CEO, RRUP sp. z o.o. / SalesOps CRM</td></tr>
<tr><td class="k">Version / Date</td><td>v2.0 &nbsp;·&nbsp; {date}{(' &nbsp;·&nbsp; Reading time ~'+reading) if reading else ''}</td></tr>
</table></div>"""
    cover = f"""<div class="cover">
<div class="kicker">SalesOps CRM UK &mdash; Company-in-a-Box</div>
<h1>{title}</h1><div class="rule"></div>
<div class="subtitle">{subtitle}</div>
<div class="meta">
<span class="pack-badge">{pack}</span><br><br>
<b>Prepared by</b> Waqas Mian &nbsp;&middot;&nbsp; <b>Prepared for</b> Chief Executive Officer, RRUP sp. z o.o. (SalesOps CRM)<br>
<b>Date</b> {date} &nbsp;&middot;&nbsp; <span class="classification">CONFIDENTIAL &mdash; PARTNER REVIEW</span>
</div></div>"""
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>{cover}{control}{body_html}</body></html>"""
    out = pathlib.Path(md_path).with_suffix('.html')
    out.write_text(html, encoding='utf-8')
    return str(out)

if __name__ == '__main__':
    print(build(sys.argv[1]))
