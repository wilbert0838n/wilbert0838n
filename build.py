"""Generates the animated SVG assets for the wilbert0838n profile README.
Tokyo Night palette. Pure SVG + CSS/SMIL, so GitHub renders the animations
natively inside <img> tags (no JS, no external fonts)."""
from html import escape
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

BG, BG2, BG3 = "#1a1b26", "#24283b", "#2f3549"
FG, DIM, LINE = "#c0caf5", "#565f89", "#3b4261"
BLUE, PURPLE, CYAN = "#7aa2f7", "#bb9af7", "#7dcfff"
GREEN, YELLOW, ORANGE, RED = "#9ece6a", "#e0af68", "#ff9e64", "#f7768e"

MONO = "'JetBrains Mono','Fira Code','Cascadia Code',ui-monospace,SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono',monospace"
SANS = "'Inter','Segoe UI',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif"

REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def e(s):
    return escape(s, quote=True)


def svg(w, h, body, style="", defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" fill="none">\n'
        f"<style>{style}{REDUCED}</style>\n<defs>{defs}</defs>\n{body}\n</svg>\n"
    )


def write(name, content):
    (OUT / name).write_text(content, encoding="utf-8")
    print("wrote", name, len(content), "bytes")


def pct(t, T):
    return f"{max(0.0, min(100.0, t / T * 100)):.3f}%"


def chip_w(text, size):
    return len(text) * size * 0.62 + 24


# ---------------------------------------------------------------- HERO
def hero():
    W, H = 1200, 420
    defs = f"""
<linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="600" y2="0" spreadMethod="repeat">
  <stop offset="0" stop-color="{FG}"/><stop offset=".3" stop-color="{BLUE}"/>
  <stop offset=".55" stop-color="{PURPLE}"/><stop offset=".8" stop-color="{CYAN}"/><stop offset="1" stop-color="{FG}"/>
  <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="600 0" dur="6s" repeatCount="indefinite"/>
</linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient>
<mask id="floorMask"><rect x="0" y="265" width="{W}" height="{H-265}" fill="url(#fade)"/></mask>
<clipPath id="card"><rect width="{W}" height="{H}" rx="20"/></clipPath>
"""
    # perspective floor
    vx, vy = W / 2, 200
    verticals = "".join(
        f'<line x1="{vx}" y1="{vy}" x2="{x}" y2="{H+40}"/>' for x in range(-900, W + 901, 110)
    )
    horizontals = "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(262, H + 30, 22))

    roles = [
        "systems & infra engineer",
        "competitive programmer",
        "problem setter @ TSEC CodeCell",
        "solo builder of ComputeX",
    ]
    T = 12
    role_css = ""
    role_svg = ""
    for i, r in enumerate(roles):
        a = i * 3
        role_css += (
            f"@keyframes r{i}{{0%,{pct(a,T)}{{opacity:0;transform:translateY(14px)}}"
            f"{pct(a+.45,T)},{pct(a+2.55,T)}{{opacity:1;transform:translateY(0)}}"
            f"{pct(a+3,T)},100%{{opacity:0;transform:translateY(-14px)}}}}"
            f".r{i}{{animation:r{i} {T}s ease-in-out infinite}}"
        )
        role_svg += f'<text class="role r{i}" x="{W/2}" y="236" text-anchor="middle">[ {e(r)} ]</text>'

    chips = ["TSEC Mumbai · CE '28", "CodeCell Core Team", "ICPC Regionalist", "600+ problems"]
    size = 14
    widths = [chip_w(c, size) for c in chips]
    gap = 14
    x = W / 2 - (sum(widths) + gap * (len(chips) - 1)) / 2
    chip_svg = ""
    cols = [BLUE, PURPLE, RED, GREEN]
    for i, (c, w) in enumerate(zip(chips, widths)):
        chip_svg += (
            f'<g class="chip" style="animation-delay:{.9+i*.15:.2f}s">'
            f'<rect x="{x:.1f}" y="292" width="{w:.1f}" height="34" rx="17" fill="{BG2}" fill-opacity=".85" stroke="{cols[i]}" stroke-opacity=".55"/>'
            f'<text x="{x+w/2:.1f}" y="314" text-anchor="middle" class="chipt" fill="{cols[i]}">{e(c)}</text></g>'
        )
        x += w + gap

    style = f"""
.mono{{font-family:{MONO}}}
.name{{font-family:{SANS};font-weight:800;font-size:86px;letter-spacing:-2px}}
.role{{font-family:{MONO};font-size:20px;fill:{FG};opacity:0}}
.chipt{{font-family:{MONO};font-size:{size}px;font-weight:600}}
.chip{{opacity:0;animation:up .7s cubic-bezier(.2,.8,.2,1) forwards}}
.nameg{{opacity:0;animation:up 1s cubic-bezier(.2,.8,.2,1) .15s forwards}}
@keyframes up{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:translateY(0)}}}}
.o1{{animation:d1 16s ease-in-out infinite alternate}}
.o2{{animation:d2 19s ease-in-out infinite alternate}}
.o3{{animation:d3 23s ease-in-out infinite alternate}}
@keyframes d1{{to{{transform:translate(260px,90px)}}}}
@keyframes d2{{to{{transform:translate(-300px,-70px)}}}}
@keyframes d3{{to{{transform:translate(-180px,120px)}}}}
.floor{{animation:scroll 1.1s linear infinite}}
@keyframes scroll{{to{{transform:translateY(22px)}}}}
.dot{{animation:pulse 1.6s ease-in-out infinite}}
@keyframes pulse{{50%{{opacity:.25}}}}
.cur{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
{role_css}
"""
    body = f"""
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g filter="url(#blur)">
    <circle class="o1" cx="180" cy="110" r="170" fill="{BLUE}" fill-opacity=".38"/>
    <circle class="o2" cx="1030" cy="300" r="190" fill="{PURPLE}" fill-opacity=".34"/>
    <circle class="o3" cx="720" cy="20" r="150" fill="{CYAN}" fill-opacity=".22"/>
  </g>
  <g mask="url(#floorMask)" stroke="{BLUE}" stroke-opacity=".35" stroke-width="1">
    <g>{verticals}</g>
    <g class="floor">{horizontals}</g>
  </g>
  <text x="34" y="46" class="mono" font-size="15" fill="{DIM}">~/<tspan fill="{BLUE}">wilbert0838n</tspan> $ ./hello<tspan class="cur" fill="{FG}">▍</tspan></text>
  <g class="mono" font-size="15">
    <circle class="dot" cx="{W-196}" cy="41" r="5" fill="{GREEN}"/>
    <text x="{W-182}" y="46" fill="{DIM}">Mumbai · IST</text>
  </g>
  <g class="nameg"><text class="name" x="{W/2}" y="178" text-anchor="middle" fill="url(#shine)" filter="url(#glow)">Wilbert Nadar</text></g>
  {role_svg}
  {chip_svg}
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="19.5" stroke="{LINE}" stroke-width="1.5"/>
</g>
"""
    write("hero.svg", svg(W, H, body, style, defs))


# ---------------------------------------------------------------- SECTION HEADERS
def header(slug, idx, title, sub, color):
    W, H = 1200, 76
    style = f"""
.t{{font-family:{SANS};font-weight:800;font-size:26px;fill:{FG}}}
.i{{font-family:{MONO};font-size:15px;font-weight:700;fill:{color}}}
.s{{font-family:{MONO};font-size:13px;fill:{DIM}}}
.sweep{{animation:sw 4.5s cubic-bezier(.6,0,.4,1) infinite}}
@keyframes sw{{from{{transform:translateX(-260px)}}to{{transform:translateX({W+40}px)}}}}
.in{{opacity:0;animation:in .8s ease forwards}}
@keyframes in{{from{{opacity:0;transform:translateX(-16px)}}to{{opacity:1;transform:none}}}}
"""
    defs = f"""<linearGradient id="sg" x1="0" x2="1"><stop offset="0" stop-color="{color}" stop-opacity="0"/>
<stop offset=".5" stop-color="{color}"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></linearGradient>
<clipPath id="hc"><rect width="{W}" height="{H}" rx="14"/></clipPath>"""
    body = f"""
<g clip-path="url(#hc)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <rect x="0" y="{H-3}" width="{W}" height="3" fill="{LINE}"/>
  <rect class="sweep" x="0" y="{H-3}" width="240" height="3" fill="url(#sg)"/>
</g>
<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="13.25" stroke="{LINE}" stroke-width="1.5"/>
<g class="in">
  <text x="26" y="45" class="i">0x{idx:02d}</text>
  <text x="84" y="46" class="t">{e(title)}</text>
  <text x="{W-26}" y="45" text-anchor="end" class="s">{e(sub)}</text>
</g>
"""
    write(f"h-{slug}.svg", svg(W, H, body, style, defs))


# ---------------------------------------------------------------- NEOFETCH TERMINAL
def terminal():
    W, H = 1200, 490
    T = 18.0
    css = ""
    parts = []
    k = [0]

    def appear(t):
        k[0] += 1
        n = k[0]
        nonlocal_css.append(
            f"@keyframes a{n}{{0%,{pct(t,T)}{{opacity:0}}{pct(t+.35,T)},95%{{opacity:1}}100%{{opacity:0}}}}"
            f".a{n}{{animation:a{n} {T}s linear infinite}}"
        )
        return f"a{n}"

    nonlocal_css = []

    def typed(x, y, text, t0, cps, cls="", size=17):
        k[0] += 1
        n = k[0]
        cw = size * 0.62
        times, vals = [0.0], [0.0]
        t = t0
        times.append(t0 / T)
        vals.append(0)
        for i in range(1, len(text) + 1):
            t += 1 / cps
            times.append(t / T)
            vals.append(i * cw + 2)
        times.append(0.95)
        vals.append(2000)
        times.append(0.999)
        vals.append(0)
        kt = ";".join(f"{v:.4f}" for v in times)
        vv = ";".join(f"{v:.1f}" for v in vals)
        parts.append(
            f'<clipPath id="c{n}"><rect x="{x-2}" y="{y-size-4}" height="{size+10}" width="0">'
            f'<animate attributeName="width" dur="{T}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{kt}" values="{vv}"/></rect></clipPath>'
        )
        return f'<text x="{x}" y="{y}" clip-path="url(#c{n})" class="{cls}" font-size="{size}">{e(text)}</text>', t

    body_items = []
    # window chrome
    body_items.append(f'<rect width="{W}" height="{H}" rx="18" fill="{BG}"/>')
    body_items.append(f'<path d="M0 18a18 18 0 0 1 18-18h{W-36}a18 18 0 0 1 18 18v26H0z" fill="{BG2}"/>')
    for i, c in enumerate([RED, YELLOW, GREEN]):
        body_items.append(f'<circle cx="{26+i*22}" cy="22" r="6.5" fill="{c}"/>')
    body_items.append(f'<text x="{W/2}" y="27" text-anchor="middle" class="m" font-size="14" fill="{DIM}">wilbert@tsec: ~</text>')

    px, py = 36, 86
    body_items.append(f'<text x="{px}" y="{py}" class="m" font-size="17" fill="{GREEN}">➜</text>')
    body_items.append(f'<text x="{px+22}" y="{py}" class="m" font-size="17" fill="{CYAN}">~</text>')
    t_cmd, t_end = typed(px + 44, py, "neofetch --flex", 0.5, 14, "m fg")
    body_items.append(t_cmd)
    t = t_end + 0.35

    # vector monogram: hexagon "container" with a self-drawing W
    import math
    cx0, cy0, R = 200, 250, 118
    hexpts = " ".join(
        f"{cx0+R*math.cos(math.radians(a)):.1f},{cy0+R*math.sin(math.radians(a)):.1f}" for a in range(-90, 270, 60)
    )
    hexin = " ".join(
        f"{cx0+(R-18)*math.cos(math.radians(a)):.1f},{cy0+(R-18)*math.sin(math.radians(a)):.1f}" for a in range(-90, 270, 60)
    )
    ca = appear(t)
    k[0] += 1
    dn = k[0]
    L = 380
    nonlocal_css.append(
        f"@keyframes w{dn}{{0%,{pct(t+.1,T)}{{stroke-dashoffset:{L}}}{pct(t+1.6,T)},100%{{stroke-dashoffset:0}}}}"
        f".wdraw{{stroke-dasharray:{L};stroke-dashoffset:{L};animation:w{dn} {T}s cubic-bezier(.6,0,.2,1) infinite}}"
        f".hexspin{{transform-origin:{cx0}px {cy0}px;animation:spin 24s linear infinite}}"
        f"@keyframes spin{{to{{transform:rotate(360deg)}}}}"
    )
    wpath = f"M{cx0-62} {cy0-48} L{cx0-32} {cy0+50} L{cx0} {cy0-12} L{cx0+32} {cy0+50} L{cx0+62} {cy0-48}"
    orbit = f"M{cx0+R+22} {cy0} a{R+22} {R+22} 0 1 1 -{2*(R+22)} 0 a{R+22} {R+22} 0 1 1 {2*(R+22)} 0"
    body_items.append(
        f'<g class="{ca}">'
        f'<circle cx="{cx0}" cy="{cy0}" r="{R-10}" fill="url(#core)"/>'
        f'<polygon class="hexspin" points="{hexpts}" stroke="url(#artg)" stroke-width="2" stroke-dasharray="10 8" fill="none"/>'
        f'<polygon points="{hexin}" stroke="{LINE}" stroke-width="1.5" fill="{BG2}" fill-opacity=".6"/>'
        f'<path class="wdraw" d="{wpath}" stroke="url(#artg)" stroke-width="15" stroke-linecap="round" stroke-linejoin="round" fill="none" filter="url(#aglow)"/>'
        f'<path d="{orbit}" stroke="{LINE}" stroke-opacity=".6" stroke-dasharray="2 6" fill="none"/>'
        f'<circle r="5" fill="{CYAN}"><animateMotion dur="6s" repeatCount="indefinite" path="{orbit}"/></circle>'
        f'<circle r="4" fill="{PURPLE}"><animateMotion dur="6s" begin="-3s" repeatCount="indefinite" path="{orbit}"/></circle>'
        f"</g>"
    )

    info = [
        ("", "wilbert@tsec"),
        ("", "─" * 34),
        ("OS", "Computer Engineering · TSEC, Mumbai ('28)"),
        ("Host", "TSEC CodeCell · Core Committee"),
        ("Kernel", "Java 21 · C++ · TypeScript · Python"),
        ("Uptime", "600+ problems solved and counting"),
        ("Packages", "Spring Boot · React · Docker · RabbitMQ"),
        ("Shell", "problem setter for CodeCell contests"),
        ("Building", "ComputeX · Rooted"),
        ("Contest", "ICPC Asia West · Chennai 2026 (W Coders)"),
        ("Rank", "CodeChef Global #297"),
    ]
    ix, iy = 430, 124
    for i, (k_, v) in enumerate(info):
        t += 0.22
        cls = appear(t)
        y = iy + i * 26
        if i == 0:
            body_items.append(
                f'<text x="{ix}" y="{y}" class="m {cls}" font-size="17" font-weight="700"><tspan fill="{BLUE}">wilbert</tspan><tspan fill="{FG}">@</tspan><tspan fill="{PURPLE}">tsec</tspan></text>'
            )
        elif i == 1:
            body_items.append(f'<text x="{ix}" y="{y}" class="m {cls}" font-size="17" fill="{LINE}">{v}</text>')
        else:
            body_items.append(
                f'<text x="{ix}" y="{y}" class="m {cls}" font-size="16" xml:space="preserve"><tspan fill="{BLUE}" font-weight="700">{e(k_)}</tspan><tspan fill="{DIM}">: </tspan><tspan fill="{FG}">{e(v)}</tspan></text>'
            )
    # palette
    t += 0.3
    cls = appear(t)
    pal = [BG3, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, FG]
    blocks = "".join(f'<rect x="{ix+i*34}" y="{iy+11*26-6}" width="30" height="18" rx="3" fill="{c}"/>' for i, c in enumerate(pal))
    body_items.append(f'<g class="{cls}">{blocks}</g>')

    # prompt 2
    t += 0.6
    py2 = 458
    cls = appear(t)
    body_items.append(
        f'<g class="{cls}"><text x="{px}" y="{py2}" class="m" font-size="17" fill="{GREEN}">➜</text>'
        f'<text x="{px+22}" y="{py2}" class="m" font-size="17" fill="{CYAN}">~</text></g>'
    )
    t2, t_end2 = typed(px + 44, py2, 'echo "open to internships · let\'s build"', t + 0.4, 16, "m fg")
    body_items.append(t2)
    cls = appear(t_end2)
    cur_x = px + 44 + len('echo "open to internships · let\'s build"') * 17 * 0.62 + 6
    body_items.append(f'<g class="{cls}"><rect class="cur" x="{cur_x:.0f}" y="{py2-15}" width="10" height="19" fill="{FG}"/></g>')
    body_items.append(f'<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" stroke="{LINE}" stroke-width="1.5"/>')

    assert t_end2 < T * 0.9, t_end2

    defs = "".join(parts) + f"""
<linearGradient id="artg" gradientUnits="userSpaceOnUse" x1="0" y1="120" x2="0" y2="340">
  <stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{BLUE}"/><stop offset="1" stop-color="{PURPLE}"/>
</linearGradient>
<radialGradient id="core"><stop offset="0" stop-color="{BLUE}" stop-opacity=".28"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<filter id="aglow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
"""
    style = f"""
.m{{font-family:{MONO}}}
.fg{{fill:{FG}}}
.art{{fill:url(#artg);filter:url(#aglow)}}
.cur{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
{''.join(nonlocal_css)}
"""
    write("terminal.svg", svg(W, H, "\n".join(body_items), style, defs))


# ---------------------------------------------------------------- PROJECT CARDS
def card(slug, title, tagline, status, status_col, bullets, chips, accent1, accent2):
    W, H = 590, 330
    defs = f"""
<linearGradient id="bd" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="{accent1}"/><stop offset=".35" stop-color="{LINE}"/>
  <stop offset=".65" stop-color="{LINE}"/><stop offset="1" stop-color="{accent2}"/>
  <animateTransform attributeName="gradientTransform" type="rotate" from="0 .5 .5" to="360 .5 .5" dur="7s" repeatCount="indefinite"/>
</linearGradient>
<radialGradient id="gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{accent1}" stop-opacity=".35"/><stop offset="1" stop-color="{accent1}" stop-opacity="0"/></radialGradient>
<clipPath id="cc"><rect width="{W}" height="{H}" rx="18"/></clipPath>
"""
    style = f"""
.m{{font-family:{MONO}}} .s{{font-family:{SANS}}}
.b{{opacity:0;animation:in .6s cubic-bezier(.2,.8,.2,1) forwards}}
@keyframes in{{from{{opacity:0;transform:translateX(-12px)}}to{{opacity:1;transform:none}}}}
.ring{{transform-origin:{W-92}px 40px;animation:ring 1.8s ease-out infinite}}
@keyframes ring{{from{{transform:scale(1);opacity:.8}}to{{transform:scale(3.2);opacity:0}}}}
.glow{{animation:gl 8s ease-in-out infinite alternate}}
@keyframes gl{{to{{transform:translate(-120px,60px)}}}}
"""
    pw = chip_w(status, 12) + 14
    bx = W - 28 - pw
    items = [
        f'<g clip-path="url(#cc)"><rect width="{W}" height="{H}" fill="{BG}"/>',
        f'<circle class="glow" cx="{W-40}" cy="30" r="170" fill="url(#gl)"/></g>',
        f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="17" stroke="url(#bd)" stroke-width="2"/>',
        f'<rect x="{bx:.0f}" y="26" width="{pw:.0f}" height="28" rx="14" fill="{status_col}" fill-opacity=".12" stroke="{status_col}" stroke-opacity=".5"/>',
        f'<circle class="ring" cx="{bx+16:.0f}" cy="40" r="4" fill="{status_col}"/>',
        f'<circle cx="{bx+16:.0f}" cy="40" r="4" fill="{status_col}"/>',
        f'<text x="{bx+28:.0f}" y="44.5" class="m" font-size="12" font-weight="700" fill="{status_col}">{e(status)}</text>',
        f'<text x="30" y="58" class="s" font-size="34" font-weight="800" fill="{FG}">{e(title)}</text>',
        f'<text x="30" y="86" class="m" font-size="13.5" fill="{DIM}">{e(tagline)}</text>',
    ]
    for i, b in enumerate(bullets):
        y = 128 + i * 32
        items.append(
            f'<g class="b" style="animation-delay:{.25+i*.18:.2f}s"><text x="30" y="{y}" class="m" font-size="15" fill="{accent1}">▹</text>'
            f'<text x="52" y="{y}" class="m" font-size="15" fill="{FG}">{e(b)}</text></g>'
        )
    x = 30
    for c in chips:
        w = chip_w(c, 12)
        items.append(
            f'<rect x="{x:.1f}" y="274" width="{w:.1f}" height="28" rx="8" fill="{BG2}" stroke="{LINE}"/>'
            f'<text x="{x+w/2:.1f}" y="292.5" text-anchor="middle" class="m" font-size="12" fill="{CYAN}">{e(c)}</text>'
        )
        x += w + 8
    assert x < W, (slug, x)
    write(f"card-{slug}.svg", svg(W, H, "\n".join(items), style, defs))


# ---------------------------------------------------------------- JUDGE PIPELINE
def pipeline():
    W, H = 1200, 360
    T = 7.0
    nodes = [
        ("Monaco", "React 18 editor", BLUE),
        ("Spring API", "Boot 3 · Java 21", GREEN),
        ("RabbitMQ", "async job queue", ORANGE),
        ("Warm Pool", "prewarmed containers", CYAN),
        ("Sandbox", "Docker + seccomp BPF", RED),
        ("Checker", "validator · spj", PURPLE),
    ]
    nw, nh, gap = 156, 92, 36
    x0 = (W - (len(nodes) * nw + (len(nodes) - 1) * gap)) / 2
    ny = 104
    cy = ny + nh / 2
    travel = 0.78  # fraction of cycle spent travelling
    css = ""
    items = [
        f'<rect width="{W}" height="{H}" rx="18" fill="{BG}"/>',
        f'<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" stroke="{LINE}" stroke-width="1.5"/>',
        f'<text x="32" y="48" class="m" font-size="15" fill="{DIM}">// life of a submission on <tspan fill="{BLUE}" font-weight="700">ComputeX</tspan></text>',
        f'<text x="{W-32}" y="48" text-anchor="end" class="m" font-size="13" fill="{DIM}">wilbertprojects.me</text>',
    ]
    centers = [x0 + i * (nw + gap) + nw / 2 for i in range(len(nodes))]
    # edges
    for i in range(len(nodes) - 1):
        xa = x0 + i * (nw + gap) + nw
        xb = xa + gap
        items.append(f'<line x1="{xa:.1f}" y1="{cy}" x2="{xb:.1f}" y2="{cy}" class="edge"/>')
        items.append(f'<path d="M{xb-7:.1f} {cy-5} L{xb-1:.1f} {cy} L{xb-7:.1f} {cy+5}" stroke="{DIM}" stroke-width="1.6" fill="none"/>')
    for i, (name, sub, col) in enumerate(nodes):
        x = x0 + i * (nw + gap)
        tc = (i / (len(nodes) - 1)) * travel * T
        css += (
            f"@keyframes n{i}{{0%,{pct(tc-.35,T)},{pct(tc+.7,T)},100%{{stroke:{LINE};stroke-width:1.5}}"
            f"{pct(tc,T)},{pct(tc+.3,T)}{{stroke:{col};stroke-width:2.5}}}}"
            f".n{i}{{animation:n{i} {T}s linear infinite}}"
            f"@keyframes h{i}{{0%,{pct(tc-.35,T)},{pct(tc+.7,T)},100%{{opacity:0}}{pct(tc,T)},{pct(tc+.3,T)}{{opacity:.5}}}}"
            f".h{i}{{animation:h{i} {T}s linear infinite}}"
        )
        items.append(f'<rect class="h{i}" x="{x-4:.1f}" y="{ny-4}" width="{nw+8}" height="{nh+8}" rx="16" fill="{col}" filter="url(#bl)" opacity="0"/>')
        items.append(f'<rect class="n{i}" x="{x:.1f}" y="{ny}" width="{nw}" height="{nh}" rx="13" fill="{BG2}" stroke="{LINE}" stroke-width="1.5"/>')
        items.append(f'<circle cx="{x+18:.1f}" cy="{ny+22}" r="4" fill="{col}"/>')
        items.append(f'<text x="{x+30:.1f}" y="{ny+27}" class="m" font-size="11" fill="{DIM}">0{i+1}</text>')
        items.append(f'<text x="{x+nw/2:.1f}" y="{ny+56}" text-anchor="middle" class="s" font-size="18" font-weight="700" fill="{FG}">{e(name)}</text>')
        items.append(f'<text x="{x+nw/2:.1f}" y="{ny+76}" text-anchor="middle" class="m" font-size="11" fill="{DIM}">{e(sub)}</text>')
    # packet rides a bus line under the nodes
    ty = ny + nh + 22
    items.append(f'<line x1="{centers[0]:.1f}" y1="{ty}" x2="{centers[-1]:.1f}" y2="{ty}" stroke="{LINE}" stroke-width="2" stroke-linecap="round"/>')
    for c_ in centers:
        items.append(f'<line x1="{c_:.1f}" y1="{ny+nh}" x2="{c_:.1f}" y2="{ty}" stroke="{LINE}" stroke-width="2"/>')
    kt = f"0;{travel:.3f};1"
    items.append(
        f'<g><circle r="14" fill="{CYAN}" opacity=".25" filter="url(#bl)"/><circle r="5" fill="#fff"/>'
        f'<animateMotion dur="{T}s" repeatCount="indefinite" keyTimes="{kt}" keyPoints="0;1;1" calcMode="linear" path="M{centers[0]:.1f} {ty} L{centers[-1]:.1f} {ty}"/>'
        f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" keyTimes="0;.03;{travel:.3f};{travel+.04:.3f};1" values="0;1;1;0;0"/></g>'
    )
    # status bar
    sx, sw, sy = 150, W - 300, 262
    items.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="62" rx="12" fill="{BG2}" stroke="{LINE}"/>')
    items.append(f'<text x="{sx+22}" y="{sy+26}" class="m" font-size="13" fill="{DIM}">submission <tspan fill="{FG}">#1337</tspan> · <tspan fill="{FG}">C++17</tspan> · problem <tspan fill="{FG}">B</tspan></text>')
    items.append(f'<rect x="{sx+22}" y="{sy+40}" width="{sw-230}" height="8" rx="4" fill="{BG3}"/>')
    items.append(f'<rect class="prog" x="{sx+22}" y="{sy+40}" width="{sw-230}" height="8" rx="4" fill="{BLUE}"/>')
    css += (
        f".prog{{transform-origin:{sx+22}px 0;animation:prog {T}s linear infinite}}"
        f"@keyframes prog{{0%{{transform:scaleX(0);fill:{BLUE}}}{travel*100:.1f}%{{transform:scaleX(1);fill:{BLUE}}}"
        f"{travel*100+1:.1f}%,97%{{transform:scaleX(1);fill:{GREEN}}}100%{{transform:scaleX(0);fill:{GREEN}}}}}"
    )
    states = [
        (0.0, 0.2, "compiling…", YELLOW),
        (0.2, 0.62, "running tests…", BLUE),
        (0.62, travel, "checking output…", PURPLE),
        (travel, 1.0, "✔ ACCEPTED  0.12s", GREEN),
    ]
    for i, (a, b, txt, col) in enumerate(states):
        a1, b1 = a * 100, b * 100
        css += (
            f"@keyframes v{i}{{0%,{max(a1-0.01,0):.2f}%{{opacity:0}}{a1+1:.2f}%,{b1-1.5:.2f}%{{opacity:1}}{b1:.2f}%,100%{{opacity:0}}}}"
            f".v{i}{{opacity:0;animation:v{i} {T}s linear infinite}}"
        )
        items.append(
            f'<text class="v{i}" x="{sx+sw-22}" y="{sy+38}" text-anchor="end" font-family="{MONO}" font-size="16" font-weight="700" fill="{col}">{e(txt)}</text>'
        )
    style = f"""
.m{{font-family:{MONO}}} .s{{font-family:{SANS}}}
.edge{{stroke:{DIM};stroke-width:1.6;stroke-dasharray:4 5;animation:dash 1s linear infinite}}
@keyframes dash{{to{{stroke-dashoffset:-9}}}}
{css}
"""
    defs = '<filter id="bl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8"/></filter>'
    write("pipeline.svg", svg(W, H, "\n".join(items), style, defs))


# ---------------------------------------------------------------- CP STATS
def cp():
    W, H = 1200, 210
    tiles = [
        ("600+", "problems solved", "LC · CF · CodeChef · AtCoder", GREEN),
        ("#297", "CodeChef global rank", "global leaderboard", RED),
        ("2×", "ICPC regionals", "Chennai 2025 · 2026", BLUE),
        ("600+", "players hosted", "8-week league on ComputeX", PURPLE),
    ]
    tw, gap = 282, 24
    x0 = (W - (4 * tw + 3 * gap)) / 2
    items = []
    defs = ""
    for i, (big, lab, sub, col) in enumerate(tiles):
        x = x0 + i * (tw + gap)
        d = 0.15 + i * 0.18
        defs += (
            f'<linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{FG}"/><stop offset="1" stop-color="{col}"/></linearGradient>'
        )
        items.append(
            f'<g class="tile" style="animation-delay:{d:.2f}s">'
            f'<rect x="{x:.1f}" y="10" width="{tw}" height="{H-20}" rx="16" fill="{BG}" stroke="{LINE}" stroke-width="1.5"/>'
            f'<rect x="{x+24:.1f}" y="10" width="{tw-48}" height="3" rx="1.5" fill="{BG3}"/>'
            f'<rect class="bar" style="animation-delay:{d+.3:.2f}s;transform-origin:{x+24:.1f}px 0" x="{x+24:.1f}" y="10" width="{tw-48}" height="3" rx="1.5" fill="{col}"/>'
            f'<text x="{x+24:.1f}" y="100" class="s big" fill="url(#g{i})">{e(big)}</text>'
            f'<text x="{x+24:.1f}" y="138" class="s" font-size="17" font-weight="700" fill="{FG}">{e(lab)}</text>'
            f'<text x="{x+24:.1f}" y="164" class="m" font-size="12.5" fill="{DIM}">{e(sub)}</text>'
            f'<circle class="blip" style="animation-delay:{i*.4:.1f}s" cx="{x+tw-28:.1f}" cy="40" r="4" fill="{col}"/>'
            f"</g>"
        )
    style = f"""
.m{{font-family:{MONO}}} .s{{font-family:{SANS}}}
.big{{font-size:58px;font-weight:800;letter-spacing:-1px}}
.tile{{opacity:0;animation:up .8s cubic-bezier(.2,.8,.2,1) forwards}}
@keyframes up{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:none}}}}
.bar{{transform:scaleX(0);animation:fill 1.4s cubic-bezier(.2,.8,.2,1) forwards}}
@keyframes fill{{to{{transform:scaleX(1)}}}}
.blip{{animation:blip 1.6s ease-in-out infinite}}
@keyframes blip{{50%{{opacity:.2}}}}
"""
    write("cp.svg", svg(W, H, "\n".join(items), style, defs))


# ---------------------------------------------------------------- FOOTER
def footer():
    W, H = 1200, 190

    def wave(amp, wl, y0):
        d = f"M0 {y0}"
        x = 0
        while x < W * 2:
            d += f" q{wl/4} {-amp} {wl/2} 0 t{wl/2} 0"
            x += wl
        return d + f" V{H} H0 Z"

    style = f"""
.m{{font-family:{MONO}}}
.w1{{animation:mv 9s linear infinite}}
.w2{{animation:mv 14s linear infinite reverse}}
.w3{{animation:mv 20s linear infinite}}
@keyframes mv{{to{{transform:translateX(-600px)}}}}
.cur{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
"""
    defs = f'<clipPath id="fc"><rect width="{W}" height="{H}" rx="18"/></clipPath>'
    body = f"""
<g clip-path="url(#fc)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <path class="w3" d="{wave(10, 300, 120)}" fill="{CYAN}" fill-opacity=".10"/>
  <path class="w2" d="{wave(14, 600, 130)}" fill="{PURPLE}" fill-opacity=".18"/>
  <path class="w1" d="{wave(12, 300, 145)}" fill="{BLUE}" fill-opacity=".26"/>
  <text x="{W/2}" y="62" text-anchor="middle" class="m" font-size="16" fill="{FG}">thanks for scrolling. now go solve a problem<tspan class="cur" fill="{BLUE}">▍</tspan></text>
  <text x="{W/2}" y="92" text-anchor="middle" class="m" font-size="13" fill="{DIM}">verdict: <tspan fill="{GREEN}" font-weight="700">ACCEPTED</tspan>  ·  wilbertprojects.me</text>
</g>
<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" stroke="{LINE}" stroke-width="1.5"/>
"""
    write("footer.svg", svg(W, H, body, style, defs))


if __name__ == "__main__":
    hero()
    terminal()
    header("about", 1, "whoami", "systems · infra · cp", BLUE)
    header("work", 2, "featured work", "things I shipped solo", PURPLE)
    header("stack", 3, "toolbox", "what I reach for", CYAN)
    header("cp", 4, "competitive programming", "handle: wilbert0838n", RED)
    header("stats", 5, "on github", "commits, streaks, snakes", GREEN)
    card(
        "computex", "ComputeX", "competitive programming platform · built solo",
        "LIVE", GREEN,
        ["seccomp-BPF hardened Docker sandboxes",
         "prewarmed container pool, low-latency judging",
         "RabbitMQ async submission queue",
         "ran an 8-week national league, 600+ players"],
        ["Java 21", "Spring Boot 3", "React", "Docker", "RabbitMQ", "Postgres"],
        BLUE, PURPLE,
    )
    card(
        "rooted", "Rooted", "container hosting for Indian engineering students",
        "BUILDING", YELLOW,
        ["a real Linux box for every student",
         "sysbox-runc system containers",
         "Docker-in-container, no --privileged",
         "built on the ComputeX isolation playbook"],
        ["Docker", "sysbox-runc", "Linux", "Nginx"],
        CYAN, BLUE,
    )
    pipeline()
    cp()
    footer()
