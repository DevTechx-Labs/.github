# DevTechx Labs Brand Assets

The approved symbol is preserved from the supplied square artwork. The wide
reference informed the graphite planes and restrained architectural composition;
its alternate slogans are not carried into the GitHub banner.

## Exports

| File in `profile/assets/` | Dimensions | Purpose |
| --- | --- | --- |
| `devtechx-logo.png` | 1254 × 1254 | Losslessly optimized source artwork; original pixels preserved |
| `devtechx-logo-small.png` | 512 × 512 | Compact avatar derivative |
| `devtechx-avatar.png` | 1024 × 1024 | Organization avatar master |
| `devtechx-github-banner.png` | 1600 × 480 | Primary profile header |
| `devtechx-github-banner-mobile.png` | 800 × 600 | Stacked header for screens at or below 600 px |
| `devtechx-github-banner.svg` | 1600 × 480 | SVG composition with editable text and embedded approved raster symbol |
| `devtechx-wordmark.svg` | 1000 × 160 | Spaced uppercase wordmark on near black |
| `devtechx-divider.svg` | 1600 × 12 | Decorative silver/graphite rule |
| `social-preview.png` | 1280 × 640 | Repository social preview |
| `manifest.json` | — | Source checksum, visible bounds, font, dimensions, and PNG byte sizes |

The avatar's visible symbol spans approximately 72% of the canvas width. Its
original aspect ratio is unchanged. No new monogram, tracing, or additional glow
is used. The source is opaque; derivatives match only near-black backdrop pixels
to the canvas and feather exterior padding. Metallic pixels retain their color.

The supplied source is retained in [input/devtechx-logo.png](input/devtechx-logo.png).
PNG output is compressed losslessly after high-quality proportional resampling.
No font files are redistributed. The banner SVG embeds a compact raster symbol
so it has no external image dependency; it is not a vector reconstruction of the logo.
For fixed typography across renderers, use the PNG export.

## Palette and typography

| Role | Color |
| --- | --- |
| Near black / primary canvas | `#050505` |
| Black | `#000000` |
| Graphite | `#151515` |
| Dark graphite | `#202124` |
| Steel | `#777C82` |
| Silver / supporting text | `#B8BDC4` |
| Bright silver / display text | `#E4E7EA` |
| Near white | `#F5F6F7` |

The supplied exports use Avenir Next Regular, with generous display tracking.
SVG text falls back through Avenir, Montserrat, Century Gothic, Arial, and
sans-serif. Near-black backing keeps the silver wordmark readable in both themes.
README body typography and colors remain native to GitHub.

## Rebuild assets

Use Python 3 and Pillow 12.2.0 with a locally licensed font. From the repository
root, create an isolated environment and pass the font path explicitly:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install Pillow==12.2.0
printf 'Path to your locally licensed font file: '
IFS= read -r DEVTECHX_FONT
python3 scripts/build_assets.py --font "$DEVTECHX_FONT" --font-index 7
```

Index `7` selects Regular in the Avenir Next collection used for these exports.
Use index `0` for a single-face TTF and check the output if choosing another font.
Rebuilding with a different font changes typography; it must be visually reviewed.
The script expects the approved source at `input/devtechx-logo.png` and does not
access the network. Retain the source checksum in the manifest for provenance.

## README behavior

The hero uses a GitHub-supported `picture` element with the required desktop PNG
as its fallback. All image paths begin with `./assets/`. The mobile source keeps
the name and positioning readable at narrow widths. The body repeats the company
name and positioning so the profile still communicates when images are unavailable.
The divider is decorative and has empty alt text.

Preview the organization Overview after publishing as well as the file in this
repository. Local browser previews approximate GitHub's Markdown presentation;
they do not reproduce its server-side sanitization or asset URL rewriting.

See [BRAND_ASSETS.md](BRAND_ASSETS.md) before reusing the identity.
