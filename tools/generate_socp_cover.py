"""Render the SOCP card artwork in the existing HPR covers' neon style.

Requires Pillow and NumPy. Run from any directory with a Python environment
that provides those packages. The existing LP and QP images are untouched.
"""

from pathlib import Path
import math
import random

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "avatars" / "hpr_socp_cover.png"
WIDTH, HEIGHT = 2048, 1152
RNG = random.Random(572)


def render_cover():
    y, x = np.mgrid[:HEIGHT, :WIDTH]
    halo = np.exp(-(((x - 1024) / 440) ** 2 + ((y - 570) / 350) ** 2))
    beam = np.exp(-(((x - 1024) / 780) ** 2 + ((y - 567) / 36) ** 2))
    pixels = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    for channel, (base, light, flare) in enumerate(
        [(1, 0, 0), (4, 17, 9), (9, 31, 18)]
    ):
        pixels[:, :, channel] = base + light * halo + flare * beam
    background = Image.fromarray(np.uint8(np.clip(pixels, 0, 255)))

    network = Image.new("RGB", (WIDTH, HEIGHT))
    network_draw = ImageDraw.Draw(network)
    for left, right in [(0, 590), (1490, WIDTH)]:
        nodes = [(RNG.uniform(left, right), RNG.uniform(250, 965)) for _ in range(38)]
        for index, point in enumerate(nodes):
            for other in sorted(nodes[index + 1 :], key=lambda p: math.dist(point, p))[:2]:
                if math.dist(point, other) < 215:
                    network_draw.line([point, other], fill=(6, 28, 44), width=1)
            radius = RNG.choice([1, 1, 2, 3])
            px, py = point
            network_draw.ellipse((px - radius, py - radius, px + radius, py + radius), fill=(40, 137, 165))
    for _ in range(160):
        px, py = RNG.uniform(50, WIDTH - 50), RNG.uniform(160, HEIGHT - 130)
        radius = RNG.choice([0.7, 0.8, 1, 1.5])
        shade = RNG.randint(32, 115)
        network_draw.ellipse((px - radius, py - radius, px + radius, py + radius), fill=(shade // 3, shade, min(230, shade + 33)))
    background = ImageChops.add(background, network.filter(ImageFilter.GaussianBlur(7)))
    background = ImageChops.add(background, network)

    geometry = Image.new("RGB", (WIDTH, HEIGHT))
    lines = ImageDraw.Draw(geometry)

    # A circular section of the Lorentz cone: (t, x, y) = (t, t cos a, t sin a).
    # Projection makes its circular rim elliptical, with a single lower apex.
    def project(t, angle):
        return (1024 + 425 * t * math.cos(angle), 930 - 575 * t + 135 * t * math.sin(angle))

    for ring in range(1, 13):
        t = ring / 12
        points = [project(t, step * math.tau / 240) for step in range(241)]
        lines.line(points, fill=(16, 86, 116) if ring < 12 else (65, 215, 239), width=1 if ring < 12 else 3)
    for meridian in range(36):
        angle = meridian * math.tau / 36
        shade = 0.4 + 0.6 * (math.sin(angle) + 1) / 2
        color = (int(32 * shade), int(169 * shade), int(205 * shade))
        lines.line([project(step / 90, angle) for step in range(91)], fill=color, width=1)
    for angle in [math.pi, 0]:
        lines.line([project(0, angle), project(1, angle)], fill=(78, 233, 249), width=3)

    # Elliptical light orbits echo the LP and QP artwork.
    for orbit, phase in [(0, 0), (1, 0.9)]:
        points = []
        for step in range(241):
            angle = step * math.tau / 240
            points.append((1024 + (490 + orbit * 35) * math.cos(angle), 586 + 233 * math.sin(angle) + 75 * math.cos(angle + phase)))
        lines.line(points, fill=(12, 55, 82), width=1)
        for angle in [0.45 + phase, 2.2 + phase, 3.8 + phase, 5.4 + phase]:
            px = 1024 + (490 + orbit * 35) * math.cos(angle)
            py = 586 + 233 * math.sin(angle) + 75 * math.cos(angle + phase)
            lines.ellipse((px - 3, py - 3, px + 3, py + 3), fill=(94, 218, 249))

    # Clear a soft pocket behind the type so the mesh cannot obscure the name.
    mask = Image.new("L", (WIDTH, HEIGHT), 255)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((645, 496, 1403, 632), radius=55, fill=30)
    mask = mask.filter(ImageFilter.GaussianBlur(23))
    geometry = Image.composite(geometry, Image.new("RGB", geometry.size), mask)
    for radius, strength in [(27, 0.7), (9, 0.8), (2, 0.8)]:
        glow = geometry.filter(ImageFilter.GaussianBlur(radius)).point(lambda value: int(value * strength))
        background = ImageChops.add(background, glow)
    background = ImageChops.add(background, geometry)

    lights = Image.new("RGB", (WIDTH, HEIGHT))
    light_draw = ImageDraw.Draw(lights)
    for px, py, radius in [(1024, 930, 5), (599, 355, 3), (1449, 355, 3), (1024, 220, 3)]:
        light_draw.ellipse((px - radius, py - radius, px + radius, py + radius), fill=(177, 251, 255))
    background = ImageChops.add(background, lights.filter(ImageFilter.GaussianBlur(20)))
    background = ImageChops.add(background, lights.filter(ImageFilter.GaussianBlur(6)))
    background = ImageChops.add(background, lights)

    font_path = Path("C:/Windows/Fonts/arial.ttf")
    if not font_path.exists():
        font_path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    font = ImageFont.truetype(str(font_path), 119)
    text_mask = Image.new("L", (WIDTH, HEIGHT))
    ImageDraw.Draw(text_mask).text((1024, 568), "HPR-SOCP", font=font, anchor="mm", fill=255, stroke_width=1)
    for radius, opacity in [(24, 0.55), (9, 0.9), (3, 0.6)]:
        glow_mask = text_mask.filter(ImageFilter.GaussianBlur(radius)).point(lambda value: int(value * opacity))
        glow = Image.composite(Image.new("RGB", background.size, (15, 202, 245)), Image.new("RGB", background.size), glow_mask)
        background = ImageChops.add(background, glow)
    background.paste((222, 253, 255), mask=text_mask)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    background.save(OUTPUT, optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    render_cover()
