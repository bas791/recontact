#!/usr/bin/env python3
"""Generate labelled SVG placeholder images for the commercial homepage.

Each placeholder names the exact photo that should replace it, so supplied
photography can be dropped in file-by-file. Re-run after editing PLACEHOLDERS.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "website", "assets", "img")

# name, width, height, label (the shot required)
PLACEHOLDERS = [
    ("hero-multi-storey-building-wash", 1920, 1080, "HERO — Multi-storey commercial building wash in progress (wide shot)"),
    ("capability-ewp-facade-clean", 900, 1100, "Technician cleaning a commercial facade from an elevated work platform"),
    ("capability-team-working-at-heights", 900, 700, "Technicians in harnesses cleaning skylight glazing on a commercial roof"),
    ("industry-commercial-property", 800, 560, "Commercial office building exterior, freshly washed"),
    ("industry-retirement-village", 800, 560, "Retirement village buildings and grounds"),
    ("industry-body-corporate", 800, 560, "Multi-storey apartment building exterior"),
    ("industry-retail-centre", 800, 560, "Retail / shopping centre frontage"),
    ("industry-warehouse-industrial", 800, 560, "Large warehouse or industrial facility exterior"),
    ("industry-school-education", 800, 560, "School buildings / education campus"),
    ("industry-hotel-hospitality", 800, 560, "Hotel or hospitality building exterior"),
    ("industry-multi-site", 800, 560, "Branded Maximum Wash vehicles / multiple sites collage"),
    ("project-retirement-village", 1000, 700, "PROJECT — Retirement village exterior maintenance programme"),
    ("project-apartment-wash", 1000, 700, "PROJECT — Multi-storey apartment building wash (before/after)"),
    ("project-warehouse-facade", 1000, 700, "PROJECT — Warehouse facade clean"),
    ("project-national-programme", 1000, 700, "PROJECT — National multi-site programme (vehicles / sites)"),
    ("project-roof-treatment", 1000, 700, "PROJECT — Commercial roof treatment (before/after)"),
    ("project-rope-access", 1000, 700, "PROJECT — Rope access technicians washing a building"),
    ("safety-working-at-heights", 900, 1100, "Harnessed technician washing a commercial roof (aerial shot)"),
    ("nationwide-branded-fleet", 1200, 700, "Branded Maximum Wash vehicle fleet lined up"),
]

SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Placeholder: {label}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1b2735"/>
      <stop offset="1" stop-color="#2c3e50"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <rect x="12" y="12" width="{w2}" height="{h2}" fill="none" stroke="#8fa6bc" stroke-width="2" stroke-dasharray="10 8" opacity="0.55"/>
  <g fill="#a9bdd1" opacity="0.9">
    <path transform="translate({cx},{cy}) scale(2)" d="M-14,-8 h8 l3,-4 h6 l3,4 h8 a2,2 0 0 1 2,2 v14 a2,2 0 0 1 -2,2 h-28 a2,2 0 0 1 -2,-2 v-14 a2,2 0 0 1 2,-2 z M0,10 a6,6 0 1 0 0,-12 a6,6 0 0 0 0,12 z" fill-rule="evenodd"/>
  </g>
  <text x="50%" y="{ty1}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="{fs}" font-weight="bold" fill="#dfe9f3">PHOTO REQUIRED</text>
  <text x="50%" y="{ty2}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="{fs2}" fill="#a9bdd1">{label_esc}</text>
  <text x="50%" y="{ty3}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="{fs3}" fill="#7d92a8">{name}.jpg — {w}x{h}px</text>
</svg>
"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, w, h, label in PLACEHOLDERS:
        fs = max(18, w // 34)
        svg = SVG.format(
            w=w, h=h, w2=w - 24, h2=h - 24, cx=w // 2, cy=h // 2 - fs * 3,
            ty1=h // 2 + fs, ty2=h // 2 + fs * 2 + 10, ty3=h // 2 + fs * 3 + 16,
            fs=fs, fs2=max(13, fs * 55 // 100), fs3=max(11, fs * 45 // 100),
            label=esc(label), label_esc=esc(label), name=name,
        )
        path = os.path.join(OUT, f"{name}.svg")
        with open(path, "w") as f:
            f.write(svg)
        print("wrote", path)


if __name__ == "__main__":
    main()
