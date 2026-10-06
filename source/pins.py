# Épingles Pinterest (1000×1500) pour chaque guide, + textes prêts à copier.
import os, subprocess, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import GUIDES, CATEGORIES
from icons import art
from build import COL, url

OUT = sys.argv[1] if len(sys.argv) > 1 else "pins"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
e = html.escape
UTM = "?utm_source=pinterest"

PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:G;src:local("DejaVu Sans")}}
*{{margin:0;box-sizing:border-box}}
html,body{{width:1000px;height:1500px;overflow:hidden}}
body{{background:{c};font-family:"Geist","DejaVu Sans",sans-serif;color:#0b0b0b;padding:70px;display:flex;flex-direction:column;gap:40px}}
.top{{display:flex;justify-content:space-between;align-items:center;color:#fff;font-size:30px;font-weight:700;letter-spacing:.02em}}
.logo{{display:flex;align-items:center;gap:16px}}
.logo b{{display:grid;place-items:center;width:56px;height:56px;border-radius:14px;background:#fff;color:{c};font-size:34px}}
.cat{{font-size:24px;text-transform:uppercase;letter-spacing:.12em;opacity:.9;font-weight:600}}
.card{{flex:1;background:#fff;border-radius:48px;padding:70px 64px;display:flex;flex-direction:column;gap:34px}}
.ill{{display:grid;place-items:center;height:400px;border-radius:32px;background:color-mix(in srgb,{c} 10%,#fff);color:{c}}}
.ill svg{{width:300px;height:300px}}
.ill .f{{fill:color-mix(in srgb,currentColor 16%,transparent);stroke:none}}
.short{{font-size:30px;font-weight:600;color:{c};text-transform:uppercase;letter-spacing:.06em}}
h1{{font-size:{fs}px;line-height:1.08;letter-spacing:-.03em;font-weight:800}}
p{{font-size:32px;line-height:1.4;color:#555}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:600}}
.btn{{background:{c};color:#fff;border-radius:999px;padding:20px 36px}}
</style></head><body>
<div class="top"><span class="logo"><b>Z</b>Zéro Corvée</span><span class="cat">{cat}</span></div>
<div class="card">
<div class="ill">{art}</div>
<div class="short">{short}</div>
<h1>{head}</h1>
<p>{sub}</p>
<div class="foot"><span>{n} modèles comparés</span><span class="btn">Voir le guide →</span></div>
</div></body></html>"""


def main():
    os.makedirs(OUT, exist_ok=True)
    md = ["# Épingles Pinterest Zéro Corvée", "",
          "Pour chaque épingle : image, titre, description et lien à coller dans Pinterest.", ""]
    for i, g in enumerate(GUIDES, 1):
        cat = next(c for c in CATEGORIES if c["key"] == g["cat"])
        head = g["teaser"].rstrip(".")
        fs = 84 if len(head) < 34 else 72 if len(head) < 52 else 62
        page = PAGE.format(c=COL[g["cat"]], cat=e(cat["name"]), art=art(g["slug"]), short=e(g["short"]),
                           head=e(head), sub=e(g["lede"][:150].rsplit(" ", 1)[0] + "…" if len(g["lede"]) > 150 else g["lede"]),
                           n=len(g["products"]), fs=fs)
        name = f"{i:02d}-{g['slug']}"
        hp = os.path.abspath(os.path.join(OUT, name + ".html"))
        open(hp, "w").write(page)
        subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=1000,1500", f"--screenshot={os.path.join(OUT, name + '.png')}", hp],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        os.remove(hp)
        title = g["title"].split(" 2026")[0].split(" : ")[0]
        md += [f"## {i}. {g['short']}", "",
               f"- **Image** : {name}.png",
               f"- **Tableau** : {cat['name']}",
               f"- **Titre** : {title} : {head.lower() if head[:1].isupper() and head[1:2].islower() else head}"[:100],
               f"- **Description** : {g['desc']} Comparatif de {len(g['products'])} modèles.",
               f"- **Lien** : {url(g['slug'])}{UTM}", ""]
    open(os.path.join(OUT, "epingles.md"), "w").write("\n".join(md))
    print(len(GUIDES), "épingles dans", OUT)


if __name__ == "__main__":
    main()
