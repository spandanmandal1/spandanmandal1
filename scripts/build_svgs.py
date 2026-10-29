"""Builds the risograph-style SVGs in assets/.

Style adapted from "Risograph Poster" in beydemirfurkan/awesome-github-profile (CC0):
two spot inks screened 60 degrees apart, misregistered headlines, paper grain.
Run from the repo root: python3 scripts/build_svgs.py
"""

W = 1200
PINK, BLUE, STOCK, INK, MUTED = "#f0338c", "#1257a8", "#f4efe3", "#101a2c", "#5c6474"
SANS = "'Helvetica Neue', Helvetica, Arial, system-ui, sans-serif"
MONO = "ui-monospace, Menlo, Consolas, monospace"


def defs():
    pats = ""
    for name, color, angle, r in [
        ("pink-12", PINK, 15, 1.5), ("pink-20", PINK, 15, 2.1), ("pink-55", PINK, 15, 3.6),
        ("blue-12", BLUE, 75, 1.5), ("blue-20", BLUE, 75, 2.1), ("blue-40", BLUE, 75, 3.0), ("blue-90", BLUE, 75, 4.9),
    ]:
        pats += (f'    <pattern id="rp-{name}" width="11" height="11" patternUnits="userSpaceOnUse" '
                 f'patternTransform="rotate({angle})"><circle cx="5.5" cy="5.5" r="{r}" fill="{color}"/></pattern>\n')
    return f"""  <defs>
{pats}    <filter id="rp-grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.62" numOctaves="4" seed="19" result="n"/>
      <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.10  0 0 0 0 0.09  0 0 0 0 0.07  0 0 0 0.55 0"/>
    </filter>
  </defs>
"""


def reg_marks(h):
    one = '<line x1="-11" y1="0" x2="11" y2="0"/><line x1="0" y1="-11" x2="0" y2="11"/><circle cx="0" cy="0" r="6.5" fill="none"/>'
    pts = [(36, 36), (W - 36, 36), (36, h - 36), (W - 36, h - 36)]
    g = "".join(f'    <g transform="translate({x},{y})">{one}</g>\n' for x, y in pts)
    return f'  <g stroke="#16233a" stroke-width="1" opacity="0.65">\n{g}  </g>\n'


def misreg(x, y, text, size, anchor="start", top=PINK, under=BLUE, spacing=-3):
    return (f'  <text x="{x - 4}" y="{y + 3}" text-anchor="{anchor}" font-family="{SANS}" font-size="{size}" font-weight="800" '
            f'fill="{under}" letter-spacing="{spacing}" opacity="0.85">{text}</text>\n'
            f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{SANS}" font-size="{size}" font-weight="800" '
            f'fill="{top}" letter-spacing="{spacing}">{text}</text>\n')


def mono(x, y, text, color=BLUE, size=12, spacing=6, anchor="start", weight="400"):
    return (f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{MONO}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" letter-spacing="{spacing}">{text}</text>\n')


def disc(cx, cy, r):
    return (f'  <clipPath id="d{cx}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>\n'
            f'  <g clip-path="url(#d{cx})"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="url(#rp-blue-90)"/>'
            f'<rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{r}" fill="url(#rp-blue-40)"/></g>\n')


def wrap(h, label, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{label}">\n'
            f'  <title>{label}</title>\n{defs()}  <rect width="{W}" height="{h}" fill="{STOCK}"/>\n{body}{reg_marks(h)}'
            f'  <rect width="{W}" height="{h}" filter="url(#rp-grain)" opacity="0.6"/>\n</svg>\n')


def header():
    h = 250
    body = disc(1032, 118, 84)
    body += misreg(72, 128, "SPANDAN MANDAL", 84)
    body += mono(76, 162, "DEVOPS ENGINEER · AWS EKS · KOLKATA, INDIA")
    body += f'  <rect x="72" y="184" width="640" height="34" fill="url(#rp-pink-20)"/>\n'
    body += (f'  <text x="88" y="207" font-family="{SANS}" font-size="16" font-weight="700" fill="{INK}">'
             f'2+ years running production on AWS EKS · open to DevOps, Platform &amp; SRE roles</text>\n')
    return wrap(h, "Spandan Mandal, DevOps Engineer. 2+ years running production on AWS EKS. Open to DevOps, Platform and SRE roles. Kolkata, India.", body)


def what_i_build():
    h, bw, bh, gap, x0 = 450, 228, 60, 40, 72
    xs = [x0 + i * (bw + gap) for i in range(4)]
    row1, row2 = 196, 318
    ship = [("git push", "CODE"), ("GitHub Actions", "TRIVY CVE GATE"), ("Argo CD", "GITOPS SYNC"), ("AWS EKS", "TERRAFORM")]
    watch = [("Prometheus + Loki", "METRICS · LOGS"), ("Alertmanager", "ALERT FIRES"),
             ("Triage bot", "LOKI LOGS + LLM"), ("Slack", "LIKELY CAUSE IN 7–9 S")]

    def station(x, y, title, sub, ink, tint):
        return (f'  <rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="url(#{tint})"/>\n'
                f'  <rect x="{x}" y="{y}" width="6" height="{bh}" fill="{ink}"/>\n'
                f'  <text x="{x + bw / 2 + 3}" y="{y + 27}" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="800" fill="{INK}">{title}</text>\n'
                + mono(x + bw / 2 + 3, y + 46, sub, INK, 10.5, 2, "middle", "700"))

    def arrow(x1, y1, x2, y2, color):
        if y1 == y2:
            d = 1 if x2 > x1 else -1
            return (f'  <line x1="{x1}" y1="{y1}" x2="{x2 - 9 * d}" y2="{y2}" stroke="{color}" stroke-width="3"/>\n'
                    f'  <polygon points="{x2},{y2} {x2 - 10 * d},{y2 - 6} {x2 - 10 * d},{y2 + 6}" fill="{color}"/>\n')
        return (f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2 - 9}" stroke="{color}" stroke-width="3"/>\n'
                f'  <polygon points="{x2},{y2} {x2 - 6},{y2 - 10} {x2 + 6},{y2 - 10}" fill="{color}"/>\n')

    body = disc(1040, 96, 66)
    body += misreg(72, 103, "WHAT I BUILD", 68)
    body += mono(74, 138, "SHIP IT · THEN WATCH IT")
    body += mono(x0, row1 - 14, "01 · SHIP — ECOMMERCE-EKS-GITOPS", PINK, 11, 3)
    body += mono(x0, row2 - 14, "02 · WATCH — ALERT-TRIAGE-BOT", BLUE, 11, 3)
    for i, (t, s) in enumerate(ship):
        body += station(xs[i], row1, t, s, PINK, "rp-pink-12")
        if i < 3:
            body += arrow(xs[i] + bw + 4, row1 + bh / 2, xs[i + 1] - 4, row1 + bh / 2, BLUE)
    for i, (t, s) in enumerate(watch):  # second row runs right to left, starting under EKS
        body += station(xs[3 - i], row2, t, s, BLUE, "rp-blue-12")
        if i < 3:
            body += arrow(xs[3 - i] - 4, row2 + bh / 2, xs[2 - i] + bw + 4, row2 + bh / 2, PINK)
    body += arrow(xs[3] + bw / 2 + 3, row1 + bh + 4, xs[3] + bw / 2 + 3, row2 - 4, BLUE)
    body += f'  <g transform="translate({x0},{h - 50})">'
    for i, f in enumerate([PINK, BLUE, "url(#rp-pink-55)", "url(#rp-blue-40)", "url(#rp-pink-20)"]):
        body += f'<rect x="{i * 30}" y="0" width="26" height="12" fill="{f}"/>'
    body += "</g>\n"
    body += mono(x0 + 168, h - 40, "RISO 2-COLOUR · FLUORO PINK + FEDERAL BLUE", MUTED, 9.5, 2.5)
    body += mono(W - 72, h - 40, "SPANDAN MANDAL · DEVOPS ENGINEER", MUTED, 9.5, 2.5, "end")
    return wrap(h, "What I build: git push, GitHub Actions with a Trivy CVE gate, Argo CD, AWS EKS on Terraform; then Prometheus and Loki, Alertmanager, a triage bot using Loki logs and a self-hosted LLM, and Slack.", body)


def impact():
    h = 260
    stats = [("30→10", "MIN PER DEPLOY", "parallel GitHub Actions"), ("8", "MICROSERVICES", "Prometheus + Grafana"),
             ("99.9%", "UPTIME", "on the services I owned"), ("−60%", "FAILED RELEASES", "DevSecOps gates in CI")]
    body = mono(72, 76, "IMPACT AT QUESTALIOUS · 2024–2026", INK, 12, 6, weight="700")
    col = (W - 144) / 4
    for i, (num, label, note) in enumerate(stats):
        x = 72 + i * col
        top, under = (PINK, BLUE) if i % 2 == 0 else (BLUE, PINK)
        tint = "rp-pink-12" if i % 2 == 0 else "rp-blue-12"
        body += f'  <rect x="{x}" y="96" width="{col - 24}" height="84" fill="url(#{tint})"/>\n'
        body += f'  <rect x="{x}" y="96" width="6" height="84" fill="{top}"/>\n'
        body += misreg(x + 20, 158, num, 56, top=top, under=under, spacing=-2)
        body += mono(x + 2, 204, label, INK, 11, 3, weight="700")
        body += (f'  <text x="{x + 2}" y="222" font-family="{SANS}" font-size="13" fill="{INK}" opacity="0.75">{note}</text>\n')
    return wrap(h, "Impact at Questalious, 2024 to 2026: deploys cut from 30 to 10 minutes, monitoring for 8 microservices, 99.9% uptime on the services I owned, 60% fewer failed releases.", body)


if __name__ == "__main__":
    for name, fn in [("header", header), ("what-i-build", what_i_build), ("impact", impact)]:
        with open(f"assets/{name}.svg", "w") as f:
            f.write(fn())
