import base64
import re
from pathlib import Path

SVG_PATH = Path("c:/workspace/AI/supervised-systems/architecture.svg")
ASSETS_DIR = SVG_PATH.parent

with open(SVG_PATH, "r", encoding="utf-8") as f:
    svg = f.read()

def embed_png(match):
    img_path = ASSETS_DIR / match.group(1)
    if img_path.exists():
        with open(img_path, "rb") as img_file:
            b64 = base64.b64encode(img_file.read()).decode("ascii")
        return f'<image xlink:href="data:image/png;base64,{b64}"'
    else:
        print(f"Warning: {img_path} not found")
        return match.group(0)

# Replace all xlink:href="*.png" with embedded base64
svg_embedded = re.sub(r'<image xlink:href="([^"]+\.png)"', embed_png, svg)

# Save as a new file
with open(ASSETS_DIR / "architecture_embedded.svg", "w", encoding="utf-8") as f:
    f.write(svg_embedded)

print("Embedded SVG written to architecture_embedded.svg")