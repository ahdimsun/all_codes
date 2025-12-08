# save as render_arabic_dua.py and run with your existing Playwright setup
from playwright.sync_api import sync_playwright
import os
import unicodedata

# 1) The fully-correct dua (NFC-normalized). Prepend ARABIC LETTER MARK to encourage correct shaping.
raw = "أُعِيذُكُمَا بِكَلِمَاتِ اللَّهِ التَّامَّةِ مِنْ كُلِّ شَيْطَانٍ وَهَامَّةٍ وَمِنْ كُلِّ عَيْنٍ لَامَّةٍ"
arabic_text = "\u061C" + unicodedata.normalize("NFC", raw)

# 2) Fonts to try (Google Fonts import styles). Each entry is a dict with name and CSS @import (or direct font stack).
fonts = [
    {
        "tag": "noto_naskh",
        "label": "Noto Naskh Arabic",
        "css_import": "@import url('https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;700&display=swap');",
        "family": "'Noto Naskh Arabic', serif"
    },
    {
        "tag": "amiri",
        "label": "Amiri",
        "css_import": "@import url('https://fonts.googleapis.com/css2?family=Amiri&display=swap');",
        "family": "'Amiri', serif"
    },
    {
        "tag": "fallback",
        "label": "System Arabic Fallback",
        "css_import": "",
        # try common local fonts as fallback (your system may have these)
        "family": "'Noto Naskh Arabic', 'Amiri', 'Scheherazade New', 'Arial', serif"
    }
]

output_files = []
with sync_playwright() as p:
    browser = p.chromium.launch()  # headless by default
    page = browser.new_page()

    for f in fonts:
        output = f"dua_{f['tag']}.png"
        # Build HTML with correct dir and CSS
        html = f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>dua render - {f['label']}</title>
<style>
    {f['css_import']}
    html,body{{height:100%;margin:0;padding:0;background:#000;}}
    .wrap{{display:flex;align-items:center;justify-content:center;height:100%;padding:40px;box-sizing:border-box;}}
    .box {{
        direction: rtl;
        unicode-bidi: isolate-override;
        text-align: center;
        font-family: {f['family']};
        font-size: 72px;            /* adjust size as needed */
        line-height: 1.6;
        color: #ffffff;
        -webkit-font-feature-settings: "rlig" 1, "ccmp" 1;
        font-feature-settings: "rlig" 1, "ccmp" 1;
        text-rendering: optimizeLegibility;
        white-space: pre-wrap;
    }}
    /* limit width to avoid ridiculously long single-line shapes on wide canvases */
    .container {{ max-width: 1400px; }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="container">
      <div class="box">{arabic_text}</div>
    </div>
  </div>
</body>
</html>
"""
        # set content and wait for fonts to load
        page.set_content(html, timeout=60000)
        # give the browser a short moment to fetch fonts and layout (Playwright is fast; increase timeout if needed)
        page.wait_for_timeout(350)  

        # locate and screenshot the element
        elem = page.locator(".box")
        # expand bounding box padding to get neat image
        elem.screenshot(path=output)
        print("Saved:", output, " (font:", f['label'], ")")
        output_files.append(os.path.abspath(output))

    browser.close()

print("\nAll files written:")
for p in output_files:
    print(p)
