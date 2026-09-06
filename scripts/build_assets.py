#!/usr/bin/env python3
"""Deterministic derivatives of the approved raster symbol; requires Pillow."""

import argparse
import base64
import hashlib
import io
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "profile" / "assets"
SCALE = 2
BG = (5, 5, 5)
SILVER = (228, 231, 234)
MUTED = (184, 189, 196)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", required=True, help="Path to a locally licensed TTF or TTC")
    parser.add_argument("--font-index", type=int, default=0)
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    source = ROOT / "input" / "devtechx-logo.png"
    original = Image.open(source)
    # Detect the supplied symbol's visible bounds without transforming its geometry.
    rgb = original.convert("RGB")
    box = rgb.convert("L").point(lambda p: 255 if p > 28 else 0).getbbox()
    if box is None:
        raise ValueError("The source contains no visible symbol")
    x0, y0, x1, y1 = box
    pad = 18
    crop_box = (max(0, x0-pad), max(0, y0-pad), min(rgb.width, x1+pad), min(rgb.height, y1+pad))
    symbol_rgb = rgb.crop(crop_box)
    # Match only near-black backdrop pixels to the output canvas; keep metal intact.
    symbol_rgb.putdata([BG if max(pixel) <= 8 else pixel for pixel in symbol_rgb.get_flattened_data()])
    symbol = symbol_rgb.convert("RGBA")
    # Feather only the exterior backdrop padding, never the metallic symbol.
    mask = Image.new("L", symbol.size)
    mask.putdata([round(255 * min(1, min(x, y, symbol.width-1-x, symbol.height-1-y) / 12))
                  for y in range(symbol.height) for x in range(symbol.width)])
    symbol.putalpha(mask)
    original.save(OUT / "devtechx-logo.png", optimize=True)

    def place(canvas, width, center):
        height = round(width * symbol.height / symbol.width)
        resized = symbol.resize((width, height), Image.Resampling.LANCZOS)
        xy = (round(center[0] - width/2), round(center[1] - height/2))
        canvas.paste(resized, xy, resized)

    # The visible symbol, excluding exterior padding, spans exactly 72% of the avatar.
    avatar = Image.new("RGB", (1024, 1024), BG)
    width = round(1024 * .72 * symbol.width / (x1-x0))
    place(avatar, width, (512, 512))
    avatar.save(OUT / "devtechx-avatar.png", optimize=True)
    avatar.resize((512, 512), Image.Resampling.LANCZOS).save(OUT / "devtechx-logo-small.png", optimize=True)

    def font(size):
        return ImageFont.truetype(args.font, round(size*SCALE), index=args.font_index)

    def tracked(draw, xy, text, size, spacing, fill):
        x,y = xy
        ft = font(size)
        for char in text:
            draw.text((round(x*SCALE), round(y*SCALE)), char, font=ft, fill=fill, anchor="ls")
            x += draw.textlength(char, font=ft)/SCALE + spacing

    def make_layout(w, h, mark_width, mark_center, title, tagline, eyebrow):
        return dict(w=w, h=h, mark_width=mark_width, mark_center=mark_center,
                    title=title, tagline=tagline, eyebrow=eyebrow)

    layouts = {
        "devtechx-github-banner": make_layout(1600,480,365,(285,240),
            (550,224,78,4.3),[(550,291,"Building practical technology",31),(550,335,"for modern teams.",31)],
            (553,142,14,3.2)),
        "devtechx-github-banner-mobile": make_layout(800,600,240,(400,151),
            (91,339,57,2.9),[(400,421,"Building practical technology",29),(400,462,"for modern teams.",29)],
            (156,535,12,2.2)),
        "social-preview": make_layout(1280,640,345,(265,320),
            (515,295,56,3),[(515,364,"Building practical technology",29),(515,407,"for modern teams.",29)],
            (518,224,11,2.2)),
    }
    for name, layout in layouts.items():
        w,h = layout["w"],layout["h"]
        canvas = Image.new("RGB",(w*SCALE,h*SCALE),BG)
        draw = ImageDraw.Draw(canvas)
        # Graphite architectural planes echo the supplied wide reference's restraint.
        draw.polygon([(int(w*.79*SCALE),h*SCALE),(w*SCALE,int(h*.28*SCALE)),(w*SCALE,h*SCALE)],fill=(12,12,12))
        draw.line([(int(w*.79*SCALE),h*SCALE),(w*SCALE,int(h*.28*SCALE))], fill=(37,38,40), width=SCALE)
        draw.line([(0,h*SCALE-2),(w*SCALE,h*SCALE-2)],fill=(49,51,53),width=2)
        if name != "devtechx-github-banner-mobile":
            draw.line([(475*SCALE,132*SCALE),(475*SCALE,(h-132)*SCALE)],fill=(47,49,51),width=SCALE)
        place(canvas,layout["mark_width"]*SCALE,tuple(v*SCALE for v in layout["mark_center"]))
        tx,ty,ts,tsp=layout["title"]
        if name.endswith("mobile"):
            copy = "DEVTECHX LABS"
            tx = (w - sum(draw.textlength(c,font=font(ts))/SCALE for c in copy) - tsp*(len(copy)-1))/2
        tracked(draw,(tx,ty),"DEVTECHX LABS",ts,tsp,SILVER)
        for x,y,copy,size in layout["tagline"]:
            draw.text((x*SCALE,y*SCALE),copy,font=font(size),fill=MUTED,
                      anchor="ms" if name.endswith("mobile") else "ls")
        ex,ey,es,esp=layout["eyebrow"]
        if name.endswith("mobile"):
            copy = "SOFTWARE · INFRASTRUCTURE · AUTOMATION"
            ex = (w - sum(draw.textlength(c,font=font(es))/SCALE for c in copy) - esp*(len(copy)-1))/2
        tracked(draw,(ex,ey),"SOFTWARE · INFRASTRUCTURE · AUTOMATION",es,esp,MUTED)
        canvas.resize((w,h),Image.Resampling.LANCZOS).save(OUT/f"{name}.png",optimize=True)

    # Embed only the canonical raster mark. Text and geometry remain native SVG.
    embedded = io.BytesIO()
    symbol.resize((500, round(500*symbol.height/symbol.width)),Image.Resampling.LANCZOS).save(embedded,format="PNG",optimize=True)
    data=base64.b64encode(embedded.getvalue()).decode("ascii")
    mark_h=365*symbol.height/symbol.width
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1600" height="480" viewBox="0 0 1600 480" role="img" aria-labelledby="title desc">
  <title id="title">DEVTECHX LABS</title>
  <desc id="desc">Building practical technology for modern teams. The approved silver DevTechx symbol on near black.</desc>
  <rect width="1600" height="480" fill="#050505"/>
  <path d="M1264 480L1600 134.4V480Z" fill="#0c0c0c"/>
  <path d="M1264 480L1600 134.4" fill="none" stroke="#252628"/>
  <path d="M0 479H1600" stroke="#313335"/>
  <path d="M475 132V348" stroke="#2f3133"/>
  <image x="102.5" y="{240-mark_h/2:.3f}" width="365" height="{mark_h:.3f}" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{data}"/>
  <g font-family="Avenir Next, Avenir, Montserrat, Century Gothic, Arial, sans-serif" font-weight="400">
    <text x="553" y="142" font-size="14" letter-spacing="3.2" fill="#B8BDC4">SOFTWARE · INFRASTRUCTURE · AUTOMATION</text>
    <text x="550" y="224" font-size="78" letter-spacing="4.3" fill="#E4E7EA">DEVTECHX LABS</text>
    <g font-size="31" fill="#B8BDC4">
      <text x="550" y="291">Building practical technology</text>
      <text x="550" y="335">for modern teams.</text>
    </g>
  </g>
</svg>
'''
    (OUT/"devtechx-github-banner.svg").write_text(svg)
    (OUT/"devtechx-wordmark.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="160" viewBox="0 0 1000 160" role="img" aria-labelledby="title">
  <title id="title">DEVTECHX LABS</title>
  <rect width="1000" height="160" fill="#050505"/>
  <text x="500" y="103" text-anchor="middle" font-family="Avenir Next, Avenir, Montserrat, Century Gothic, Arial, sans-serif" font-size="65" font-weight="400" letter-spacing="7" fill="#E4E7EA">DEVTECHX LABS</text>
</svg>
''')
    (OUT/"devtechx-divider.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="12" viewBox="0 0 1600 12" aria-hidden="true">
  <defs><linearGradient id="line"><stop stop-color="#777C82" stop-opacity="0.1"/><stop offset="0.5" stop-color="#B8BDC4"/><stop offset="1" stop-color="#777C82" stop-opacity="0.1"/></linearGradient></defs>
  <path d="M0 6H1600" stroke="url(#line)"/>
</svg>
''')
    manifest={"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
              "visible_bounds":list(box),"avatar_symbol_width_percent":72,
              "font":ImageFont.truetype(args.font,12,index=args.font_index).getname(),
              "assets":{p.name:{"bytes":p.stat().st_size,"dimensions":list(Image.open(p).size)}
                        for p in sorted(OUT.glob("*.png"))}}
    (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(json.dumps(manifest,indent=2))


if __name__ == "__main__":
    main()
