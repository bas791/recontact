#!/usr/bin/env python3
"""Crop, resize and compress the supplied project photos into the homepage
image slots. Originals live in website/assets/img/source/; web-ready JPEGs are
written to website/assets/img/ under the slot filenames the page references."""
import os
from PIL import Image, ImageOps

IMG = os.path.join(os.path.dirname(__file__), "..", "website", "assets", "img")
SRC = os.path.join(IMG, "source")

# slot name -> (source file, target w, target h, horizontal focus 0-1, vertical focus 0-1)
# Focus shifts the crop window toward the subject instead of a plain centre crop.
JOBS = {
    "hero-multi-storey-building-wash":  ("IMG_9014.JPG", 1920, 1080, 0.5, 0.42),
    "capability-ewp-facade-clean":      ("IMG_9919 (2).JPG", 900, 1100, 0.42, 0.5),
    "capability-team-working-at-heights": ("Pic11.PNG", 900, 700, 0.6, 0.5),
    "safety-working-at-heights":        ("Pic7.JPG", 900, 1100, 0.58, 0.4),
    "industry-commercial-property":     ("IMG_9919 (2).JPG", 800, 560, 0.5, 0.45),
    "industry-retail-centre":           ("pic2.PNG", 800, 560, 0.5, 0.5),
    "industry-warehouse-industrial":    ("Pic5.jpg", 800, 560, 0.5, 0.55),
    "industry-multi-site":              ("Pic8.JPG", 800, 560, 0.5, 0.5),
    "industry-hotel-hospitality":       ("pic3.JPG", 800, 560, 0.5, 0.5),
    "nationwide-branded-fleet":         ("pic1.JPG", 1200, 700, 0.55, 0.6),
    "project-rope-access":              ("Pic6.jpg", 1000, 700, 0.4, 0.5),
    "project-roof-treatment-before":    ("image_20260714_172411_588.jpg", 600, 700, 0.5, 0.5),
    "project-roof-treatment-after":     ("image_20260714_172411_646.jpg", 600, 700, 0.5, 0.5),
    "team-fleet-auckland":              ("team photo 2023 (4) (1).JPG", 1296, 869, 0.5, 0.5),
}


def process(src_path, out_path, tw, th, fx, fy):
    im = ImageOps.exif_transpose(Image.open(src_path)).convert("RGB")
    w, h = im.size
    target_ratio = tw / th
    if w / h > target_ratio:            # source wider than target: crop width
        cw, ch = int(h * target_ratio), h
        left = min(max(int(w * fx - cw / 2), 0), w - cw)
        box = (left, 0, left + cw, ch)
    else:                               # source taller: crop height
        cw, ch = w, int(w / target_ratio)
        top = min(max(int(h * fy - ch / 2), 0), h - ch)
        box = (0, top, cw, top + ch)
    im = im.crop(box)
    if im.width > tw:
        im = im.resize((tw, th), Image.LANCZOS)
    im.save(out_path, "JPEG", quality=82, optimize=True, progressive=True)


def main():
    for slot, (src, tw, th, fx, fy) in JOBS.items():
        src_path = os.path.join(SRC, src)
        out_path = os.path.join(IMG, f"{slot}.jpg")
        process(src_path, out_path, tw, th, fx, fy)
        print(f"{slot}.jpg  {os.path.getsize(out_path)//1024}KB  <- {src}")


if __name__ == "__main__":
    main()
