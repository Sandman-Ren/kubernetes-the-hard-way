#!/usr/bin/env python3
"""Build the Two Point Hospital compendium single-file HTML from the markdown docs."""
import html as html_mod
import json
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent
OUT = DOCS / "compendium.html"

SECTIONS = [
    ("overview", "01", "Overview & Core Mechanics", "01-overview-and-core-mechanics.md", "How the hospital actually works"),
    ("rooms", "02", "Rooms", "02-rooms.md", "All 51 rooms: costs, sizes, staff, machines"),
    ("items", "03", "Items", "03-items.md", "Boost items, needs, prestige, Kudosh"),
    ("staff", "04", "Staff", "04-staff.md", "Types, qualifications, traits, training"),
    ("illnesses", "05", "Illnesses", "05-illnesses.md", "All 278 illnesses and their cures"),
    ("research", "06", "Research", "06-research.md", "The in-hospital tech tree"),
    ("superbug", "07", "Superbug Initiative", "07-superbug-initiative.md", "Global co-op research projects"),
    ("maps-base", "08", "Maps: Base Game", "08-maps-base-game.md", "15 hospitals + R.E.M.I.X, 3-star plans"),
    ("maps-dlc", "09", "Maps: DLC", "09-maps-dlc.md", "21 hospitals across 7 expansions"),
    ("strategy", "10", "Strategy Playbook", "10-general-strategy.md", "The distilled meta guide"),
    ("progression", "11", "Progression & Unlocks", "11-progression-and-unlocks.md", "Career structure and the unlock chain"),
]

INLINE_PATTERNS = [
    (re.compile(r"\*\*(.+?)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\w*])\*([^*]+?)\*(?![\w*])"), r"<em>\1</em>"),
    (re.compile(r"`([^`]+?)`"), r"<code>\1</code>"),
    (re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)"), r'<a href="\2" target="_blank" rel="noopener">\1</a>'),
    (re.compile(r"\[([^\]]+)\]\(([^)\s]+\.md)\)"), r"\1"),  # intra-repo links: plain text in the artifact
]


def inline(text: str) -> str:
    text = html_mod.escape(text, quote=False)
    for pat, rep in INLINE_PATTERNS:
        text = pat.sub(rep, text)
    return text


def slugify(text: str, seen: set) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "s"
    base, n = s, 2
    while s in seen:
        s = f"{base}-{n}"
        n += 1
    seen.add(s)
    return s


def md_to_html(md: str, sec_id: str):
    lines = md.split("\n")
    out, toc = [], []
    seen = set()
    i, n = 0, len(lines)
    in_ul, in_ol, in_quote = False, False, False

    def close_lists():
        nonlocal in_ul, in_ol, in_quote
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False
        if in_quote:
            out.append("</blockquote>")
            in_quote = False

    while i < n:
        line = lines[i]
        stripped = line.strip()
        # table
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            close_lists()
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append('<div class="tablewrap"><table><thead><tr>')
            out.extend(f"<th>{inline(h)}</th>" for h in header)
            out.append("</tr></thead><tbody>")
            for r in rows:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table></div>")
            continue
        # headers
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            close_lists()
            level = len(m.group(1))
            text = m.group(2).strip()
            if level == 1:
                pass  # section title comes from the shell, skip doc h1
            else:
                hid = f"{sec_id}--{slugify(text, seen)}"
                if level == 2:
                    toc.append((hid, re.sub(r"<[^>]+>", "", inline(text))))
                out.append(f'<h{level+1} id="{hid}">{inline(text)}</h{level+1}>')
            i += 1
            continue
        # hr
        if re.match(r"^-{3,}$", stripped):
            close_lists()
            out.append("<hr>")
            i += 1
            continue
        # blockquote
        if stripped.startswith(">"):
            if not in_quote:
                close_lists()
                out.append("<blockquote>")
                in_quote = True
            out.append(f"<p>{inline(stripped.lstrip('> '))}</p>")
            i += 1
            continue
        # lists
        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if m:
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if in_quote:
                out.append("</blockquote>")
                in_quote = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            nested = "nested" if len(m.group(1)) >= 2 else ""
            out.append(f'<li class="{nested}">{inline(m.group(2))}</li>')
            i += 1
            continue
        m = re.match(r"^(\s*)\d+[.)]\s+(.*)$", line)
        if m:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_quote:
                out.append("</blockquote>")
                in_quote = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline(m.group(2))}</li>")
            i += 1
            continue
        # blank
        if not stripped:
            close_lists()
            i += 1
            continue
        # paragraph: merge continuation lines
        close_lists()
        para = [stripped]
        while i + 1 < n:
            nxt = lines[i + 1].strip()
            if not nxt or nxt.startswith(("#", "|", "-", "*", ">")) or re.match(r"^\d+[.)]\s", nxt):
                break
            para.append(nxt)
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
        i += 1
    close_lists()
    return "\n".join(out), toc


def extract_illness_index():
    md = (DOCS / "05-illnesses.md").read_text()
    section = md[md.index("## Alphabetical index"):]
    nxt = section.find("\n## ", 1)
    if nxt != -1:
        section = section[:nxt]
    rows = []
    for line in section.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] == "Illness" or set(cells[0]) <= {"-", ":", " "}:
            continue
        rows.append({"n": cells[0].replace("**", ""), "r": cells[1], "o": cells[2]})
    return rows


sections_html = []
nav_html = []
toc_json = {}
for sid, num, title, fname, blurb in SECTIONS:
    body, toc = md_to_html((DOCS / fname).read_text(), sid)
    filt = ""
    if sid in ("illnesses", "rooms", "items", "staff"):
        filt = (f'<div class="filterbar"><input type="search" class="secfilter" data-sec="{sid}" '
                f'placeholder="Filter tables in this section&hellip;" aria-label="Filter table rows"></div>')
    sections_html.append(
        f'<section class="doc" id="sec-{sid}" hidden>'
        f'<div class="dochead"><span class="signcode">{num}</span>'
        f'<div><h2 class="doctitle">{title}</h2><p class="docblurb">{blurb}</p></div></div>'
        f"{filt}{body}</section>"
    )
    nav_html.append(
        f'<a class="navitem" href="#/{sid}" data-sec="{sid}">'
        f'<span class="signcode">{num}</span><span class="navlabel">{title}</span></a>'
    )
    toc_json[sid] = [{"id": h, "t": t} for h, t in toc]

illness_index = extract_illness_index()

home = f"""
<section class="doc" id="sec-home">
  <div class="hero">
    <p class="eyebrow">Two Point County Department of Health</p>
    <h2 class="herotitle">Two Point Hospital<br>Compendium</h2>
    <p class="herosub">Reference &amp; strategy for the base game and all seven expansions,
    compiled from the community wiki, archived walkthroughs, and cross-checked guides.
    Look up a cure, plan a build, or take any map to three stars.</p>
  </div>
  <div class="statrow">
    <div class="stat"><span class="statnum">278</span><span class="statlabel">Illnesses</span></div>
    <div class="stat"><span class="statnum">51</span><span class="statlabel">Rooms</span></div>
    <div class="stat"><span class="statnum">36</span><span class="statlabel">Hospitals</span></div>
    <div class="stat"><span class="statnum">7</span><span class="statlabel">DLCs</span></div>
    <div class="stat"><span class="statnum">33</span><span class="statlabel">Staff traits</span></div>
  </div>
  <h3>Where to start</h3>
  <div class="cardrow">
    <a class="card" href="#/overview"><strong>New to the game?</strong><span>Read the core mechanics — the patient lifecycle, diagnosis math, and what actually moves reputation.</span></a>
    <a class="card" href="#/illnesses"><strong>Mid-game lookup</strong><span>“What cures Mock Star?” — the illness compendium, searchable by name, cure room, and origin.</span></a>
    <a class="card" href="#/maps-base"><strong>Stuck on a map?</strong><span>Per-hospital star requirements and concrete 3-star strategies, base game and DLC.</span></a>
    <a class="card" href="#/strategy"><strong>The meta</strong><span>GP throughput doctrine, the training pipeline, economy discipline, and community cheese tactics.</span></a>
  </div>
  <h3>Honest data notes</h3>
  <p>Each section ends with its sources. Where sources conflict (machine upgrade strength, a few research costs)
  or the wiki publishes no number (per-item prestige values, health-decay rates), the docs say so inline
  rather than inventing figures.</p>
</section>
"""

page = """<title>Two Point Hospital Compendium</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{
  --ground:#F6F9F8; --surface:#FFFFFF; --ink:#1C2B28; --muted:#5B6E69;
  --line:#D9E5E1; --teal:#0E8C7F; --teal-soft:#E2F0ED; --coral:#E2604B;
  --amber:#DE9A2B; --code:#EDF4F2; --shadow:0 1px 3px rgba(28,43,40,.08);
}
@media (prefers-color-scheme: dark){:root{
  --ground:#0F1917; --surface:#16221F; --ink:#E3EDE9; --muted:#93A6A0;
  --line:#24332F; --teal:#3CBCAC; --teal-soft:#1B2E2A; --coral:#F08268;
  --amber:#E8B45A; --code:#1D2C28; --shadow:0 1px 3px rgba(0,0,0,.4);
}}
:root[data-theme="light"]{
  --ground:#F6F9F8; --surface:#FFFFFF; --ink:#1C2B28; --muted:#5B6E69;
  --line:#D9E5E1; --teal:#0E8C7F; --teal-soft:#E2F0ED; --coral:#E2604B;
  --amber:#DE9A2B; --code:#EDF4F2; --shadow:0 1px 3px rgba(28,43,40,.08);
}
:root[data-theme="dark"]{
  --ground:#0F1917; --surface:#16221F; --ink:#E3EDE9; --muted:#93A6A0;
  --line:#24332F; --teal:#3CBCAC; --teal-soft:#1B2E2A; --coral:#F08268;
  --amber:#E8B45A; --code:#1D2C28; --shadow:0 1px 3px rgba(0,0,0,.4);
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.shell{display:grid;grid-template-columns:250px 1fr;min-height:100vh}
/* ---- sidebar: the department directory ---- */
.side{background:var(--surface);border-right:1px solid var(--line);padding:20px 14px;
  position:sticky;top:0;height:100vh;overflow-y:auto}
.brand{display:block;text-decoration:none;color:var(--ink);margin:2px 6px 18px}
.brand .eyebrow{margin:0 0 2px}
.brandname{font-family:"Trebuchet MS","Segoe UI",sans-serif;font-weight:700;
  font-size:1.15rem;line-height:1.25;letter-spacing:-.01em}
.brandname b{color:var(--teal)}
.navitem{display:flex;align-items:center;gap:10px;padding:7px 8px;border-radius:8px;
  text-decoration:none;color:var(--ink);font-size:.92rem;margin-bottom:2px}
.navitem:hover{background:var(--teal-soft)}
.navitem.active{background:var(--teal);color:#fff}
.navitem.active .signcode{background:rgba(255,255,255,.2);color:#fff;border-color:transparent}
.signcode{font-family:"Trebuchet MS","Segoe UI",sans-serif;font-weight:700;font-size:.72rem;
  background:var(--teal-soft);color:var(--teal);border:1px solid var(--line);
  border-radius:6px;padding:2px 6px;min-width:26px;text-align:center;flex-shrink:0;
  font-variant-numeric:tabular-nums}
/* ---- main ---- */
.main{min-width:0;padding:0 clamp(18px,4vw,54px) 80px}
.topbar{position:sticky;top:0;z-index:5;background:var(--ground);
  padding:16px 0 12px;border-bottom:1px solid var(--line);margin-bottom:26px;
  display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.search{position:relative;flex:1;max-width:430px;min-width:220px}
.search input{width:100%;padding:9px 13px;border:1.5px solid var(--line);border-radius:9px;
  background:var(--surface);color:var(--ink);font:inherit;font-size:.94rem}
.search input:focus{outline:none;border-color:var(--teal)}
.results{position:absolute;top:calc(100% + 5px);left:0;right:0;background:var(--surface);
  border:1px solid var(--line);border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.14);
  max-height:330px;overflow-y:auto;display:none}
.results.open{display:block}
.result{display:flex;justify-content:space-between;gap:10px;padding:8px 13px;cursor:pointer;
  border-bottom:1px solid var(--line);font-size:.9rem;align-items:baseline}
.result:last-child{border-bottom:none}
.result:hover,.result.sel{background:var(--teal-soft)}
.result .rn{font-weight:600}
.result .rr{color:var(--teal);font-size:.83rem;white-space:nowrap}
.result .ro{color:var(--muted);font-size:.76rem;white-space:nowrap}
.topnote{color:var(--muted);font-size:.8rem;margin-left:auto}
/* ---- content typography ---- */
.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:600;
  color:var(--teal);margin:0 0 6px}
.hero{padding:34px 0 8px;max-width:720px}
.herotitle{font-family:"Trebuchet MS","Segoe UI",sans-serif;font-weight:700;
  font-size:clamp(1.9rem,4.5vw,2.9rem);line-height:1.08;letter-spacing:-.015em;
  margin:0 0 14px;text-wrap:balance}
.herosub{font-size:1.05rem;color:var(--muted);max-width:58ch}
.statrow{display:flex;gap:12px;flex-wrap:wrap;margin:26px 0 34px}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:12px;
  padding:14px 22px;box-shadow:var(--shadow)}
.statnum{display:block;font-family:"Trebuchet MS","Segoe UI",sans-serif;font-weight:700;
  font-size:1.7rem;color:var(--teal);font-variant-numeric:tabular-nums;line-height:1.1}
.statlabel{font-size:.78rem;text-transform:uppercase;letter-spacing:.09em;color:var(--muted)}
.cardrow{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin:14px 0 30px}
.card{display:flex;flex-direction:column;gap:6px;background:var(--surface);
  border:1px solid var(--line);border-radius:12px;padding:16px 18px;text-decoration:none;
  color:var(--ink);box-shadow:var(--shadow);transition:border-color .15s}
.card:hover{border-color:var(--teal)}
.card strong{font-family:"Trebuchet MS","Segoe UI",sans-serif}
.card span{font-size:.88rem;color:var(--muted)}
.dochead{display:flex;gap:14px;align-items:flex-start;margin:30px 0 6px}
.dochead .signcode{font-size:1rem;padding:6px 11px;margin-top:7px}
.doctitle{font-family:"Trebuchet MS","Segoe UI",sans-serif;font-weight:700;
  font-size:clamp(1.5rem,3vw,2.1rem);letter-spacing:-.01em;margin:0;text-wrap:balance}
.docblurb{color:var(--muted);margin:2px 0 0}
.doc h3{font-family:"Trebuchet MS","Segoe UI",sans-serif;font-size:1.32rem;margin:2.2em 0 .5em;
  padding-top:.6em;border-top:2px solid var(--teal-soft);letter-spacing:-.01em;text-wrap:balance}
.doc h4{font-size:1.05rem;margin:1.6em 0 .4em}
.doc h5{font-size:.95rem;margin:1.4em 0 .3em;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.doc p{max-width:76ch}
.doc ul,.doc ol{max-width:76ch;padding-left:1.4em}
.doc li{margin:.3em 0}
.doc li.nested{list-style:circle;margin-left:1.3em}
.doc code{background:var(--code);border-radius:5px;padding:.1em .4em;font-size:.87em;
  font-family:ui-monospace,"Cascadia Code",Menlo,Consolas,monospace}
.doc a{color:var(--teal)}
.doc hr{border:none;border-top:1px solid var(--line);margin:2em 0}
.doc blockquote{border-left:3px solid var(--teal);margin:1em 0;padding:.2em 0 .2em 1em;color:var(--muted)}
.tablewrap{overflow-x:auto;margin:1em 0;border:1px solid var(--line);border-radius:10px;
  background:var(--surface);box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:.88rem;font-variant-numeric:tabular-nums}
th{background:var(--teal-soft);color:var(--ink);text-align:left;padding:8px 12px;
  font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap}
td{padding:7px 12px;border-top:1px solid var(--line);vertical-align:top}
tbody tr:hover{background:var(--teal-soft)}
.filterbar{position:sticky;top:64px;z-index:4;padding:8px 0;background:var(--ground)}
.secfilter{width:100%;max-width:380px;padding:8px 12px;border:1.5px solid var(--line);
  border-radius:9px;background:var(--surface);color:var(--ink);font:inherit;font-size:.9rem}
.secfilter:focus{outline:none;border-color:var(--coral)}
tr.fhide{display:none}
mark{background:color-mix(in srgb,var(--amber) 35%, transparent);color:inherit;border-radius:3px}
:focus-visible{outline:2px solid var(--coral);outline-offset:2px}
@media (max-width:840px){
  .shell{grid-template-columns:1fr}
  .side{position:static;height:auto;display:flex;flex-wrap:wrap;gap:4px;border-right:none;
    border-bottom:1px solid var(--line)}
  .brand{width:100%}
  .navlabel{font-size:.8rem}
  .filterbar{top:0}
}
@media (prefers-reduced-motion: reduce){*{transition:none!important}}
</style>
<div class="shell">
  <nav class="side">
    <a class="brand" href="#/home">
      <p class="eyebrow">Knowledge Base</p>
      <span class="brandname">Two Point <b>Hospital</b><br>Compendium</span>
    </a>
    __NAV__
  </nav>
  <main class="main">
    <div class="topbar">
      <div class="search">
        <input id="q" type="search" placeholder="Quick lookup: illness &rarr; cure room&hellip;" autocomplete="off" aria-label="Search illnesses">
        <div class="results" id="qr" role="listbox"></div>
      </div>
      <span class="topnote">278 illnesses indexed</span>
    </div>
    __HOME__
    __SECTIONS__
  </main>
</div>
<script>
const ILLNESSES = __ILLNESS_JSON__;
const secs = document.querySelectorAll("section.doc");
const navs = document.querySelectorAll(".navitem");
function show(id){
  secs.forEach(s => s.hidden = s.id !== "sec-" + id);
  navs.forEach(a => a.classList.toggle("active", a.dataset.sec === id));
  window.scrollTo(0,0);
}
function route(){
  const h = location.hash.replace(/^#\\//, "") || "home";
  const [id, anchor] = h.split("@");
  show(document.getElementById("sec-" + id) ? id : "home");
  if (anchor){
    const el = document.getElementById(anchor);
    if (el) el.scrollIntoView();
  }
}
window.addEventListener("hashchange", route);
route();
/* quick search */
const q = document.getElementById("q"), qr = document.getElementById("qr");
let sel = -1;
function renderResults(list){
  qr.innerHTML = list.slice(0, 12).map((x,i) =>
    `<div class="result${i===sel?" sel":""}" data-i="${i}"><span class="rn">${x.n}</span>` +
    `<span class="rr">${x.r}</span><span class="ro">${x.o.replace(" DLC","")}</span></div>`).join("");
  qr.classList.toggle("open", list.length > 0);
}
let hits = [];
q.addEventListener("input", () => {
  sel = -1;
  const v = q.value.trim().toLowerCase();
  if (v.length < 2){ qr.classList.remove("open"); return; }
  hits = ILLNESSES.filter(x => x.n.toLowerCase().includes(v) || x.r.toLowerCase().includes(v));
  renderResults(hits);
});
q.addEventListener("keydown", e => {
  if (!qr.classList.contains("open")) return;
  const max = Math.min(hits.length, 12) - 1;
  if (e.key === "ArrowDown"){ sel = Math.min(sel+1, max); renderResults(hits); e.preventDefault(); }
  else if (e.key === "ArrowUp"){ sel = Math.max(sel-1, 0); renderResults(hits); e.preventDefault(); }
  else if (e.key === "Enter" && sel >= 0){ pick(hits[sel]); }
  else if (e.key === "Escape"){ qr.classList.remove("open"); }
});
qr.addEventListener("mousedown", e => {
  const r = e.target.closest(".result");
  if (r) pick(hits[+r.dataset.i]);
});
function pick(x){
  qr.classList.remove("open");
  location.hash = "#/illnesses";
  const f = document.querySelector('.secfilter[data-sec="illnesses"]');
  if (f){ f.value = x.n; f.dispatchEvent(new Event("input")); }
}
document.addEventListener("click", e => { if (!e.target.closest(".search")) qr.classList.remove("open"); });
/* per-section table filters */
document.querySelectorAll(".secfilter").forEach(f => {
  const sec = document.getElementById("sec-" + f.dataset.sec);
  f.addEventListener("input", () => {
    const v = f.value.trim().toLowerCase();
    sec.querySelectorAll("tbody tr").forEach(tr => {
      tr.classList.toggle("fhide", v !== "" && !tr.textContent.toLowerCase().includes(v));
    });
  });
});
</script>
"""

page = page.replace("__NAV__", "\n".join(nav_html))
page = page.replace("__HOME__", home)
page = page.replace("__SECTIONS__", "\n".join(sections_html))
page = page.replace("__ILLNESS_JSON__", json.dumps(illness_index, ensure_ascii=False))
OUT.write_text(page)
print(f"wrote {OUT} ({OUT.stat().st_size/1024:.0f} KB), {len(illness_index)} illnesses indexed")
