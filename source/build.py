#!/usr/bin/env python3
"""Génère le site statique Zéro Corvée (pages HTML, sitemap, robots.txt)."""
import json, os, re, shutil, html
from urllib.parse import quote_plus
from content import GUIDES, CATEGORIES, SUBCATS
from pages import STATIC_PAGES

# À remplacer par le vrai nom de domaine une fois acheté.
BASE = "https://jemueldefoi-del.github.io/Zero-corvee"
SITE = "Zéro Corvée"
UPDATED = "2026-10-04"
UPDATED_FR = "4 octobre 2026"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("OUT", os.path.join(HERE, "site"))

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap">')

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="var(--ink)"/>'
        '<path d="M10 10.5h12L10 21.5h12" fill="none" stroke="var(--bg)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="9" fill="#0b0b0b"/>'
           '<path d="M10 10.5h12L10 21.5h12" fill="none" stroke="#f6f6f6" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

e = html.escape

# Une couleur par rubrique (assez foncée pour du texte blanc dessus).
COL = {"menage": "#3355ff", "linge": "#7c3aed", "cuisine": "#ea580c", "jardin": "#16a34a", "animaux": "#e11d63"}


def tint(slug_cat):
    return f' style="--c:{COL.get(slug_cat, "#3355ff")}"'



def url(slug):
    return f"{BASE}/" if slug == "index" else f"{BASE}/{slug}.html"


def href(slug):
    return f"{slug}.html"


def head(title, desc, slug, ld, og_type="article"):
    lds = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url(slug)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{SITE}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(slug)}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#f6f6f6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0b0b0b" media="(prefers-color-scheme: dark)">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="style.css">
{lds}
</head>
<body>
<a class="skip" href="#haut">Aller au contenu</a>
"""


def header(active=None):
    cur = ' aria-current="page"'
    links = ""
    for c in CATEGORIES:
        links += f'<a href="{href(c["key"])}"{cur if c["key"] == active else ""}>{e(c["name"])}</a>'
        for sc in SUBCATS:
            if sc["parent"] == c["key"]:
                links += f'<a class="nav-sub" href="{href(sc["key"])}"{cur if sc["key"] == active else ""}>{e(sc["name"])}</a>'
    return f"""<header class="top">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="{SITE}, accueil">{LOGO}<span translate="no">{SITE}</span></a>
    <button class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="cats">Rubriques</button>
    <nav class="cats" id="cats" aria-label="Rubriques">{links}</nav>
  </div>
</header>
"""


def footer():
    cats = "".join(f'<li><a href="{href(c["key"])}">{e(c["name"])}</a></li>' for c in CATEGORIES)
    cats += "".join(f'<li><a href="{href(sc["key"])}">{e(sc["name"])}</a></li>' for sc in SUBCATS)
    site = "".join(f'<li><a href="{href(p["slug"])}">{e(p["nav"])}</a></li>' for p in STATIC_PAGES)
    return f"""<footer>
  <div class="wrap">
    <div><a class="logo" href="index.html">{LOGO}{SITE}</a><p style="margin-top:8px">Des guides d'achat clairs pour confier les tâches ménagères aux machines et récupérer du temps.</p></div>
    <div><h4>Rubriques</h4><ul>{cats}</ul></div>
    <div><h4>Le site</h4><ul>{site}</ul></div>
    <p class="copy">© 2026 {SITE}. En tant que partenaire de programmes d'affiliation, nous percevons une commission sur certains achats effectués via nos liens, sans surcoût pour vous.</p>
  </div>
</footer>
<script>
(function(){{var b=document.getElementById('menu-btn'),n=document.getElementById('cats');
b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');}});}})();
</script>
</body>
</html>
"""


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url(s)}
                                for i, (n, s) in enumerate(items)]}


def ul(items):
    return "".join(f"<li>{e(x)}</li>" for x in items)


AMAZON_TAG = "zerocorvee-21"
# Recherches Amazon plus précises pour les noms trop génériques.
AMAZON_Q = {"Cosori": "Cosori airfryer", "Lefant": "Lefant robot aspirateur", "Hozelock": "Hozelock programmateur arrosage",
            "Linktap": "Linktap programmateur arrosage", "Rouleau adhésif": "rouleau adhésif anti-poils", "Gant de toilettage": "gant de toilettage chat",
            "Balles anti-poils": "balles anti-poils machine à laver", "Sachets nettoyants pour tambour": "nettoyant tambour poils animaux machine à laver",
            "Robot sans fil fond seul (entrée de gamme)": "robot piscine sans fil", "Lanceur longue portée (plusieurs marques)": "lanceur balle automatique chien",
            "Lanceur mini (plusieurs marques)": "lanceur balle automatique petit chien", "Brosse en caoutchouc pour tissus": "brosse caoutchouc anti-poils",
            "Mijoteuse électrique (slow cooker)": "mijoteuse électrique", "iFetch": "iFetch lanceur balle"}


# Fiches Amazon.fr exactes (ASIN) trouvées pour chaque produit, le 5 octobre 2026.
ASINS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "asins.json")))


def amazon(p):
    """Lien Amazon.fr avec l'identifiant partenaire : fiche exacte si on a l'ASIN, sinon recherche."""
    asin = (ASINS.get(p["name"]) or {}).get("asin")
    if asin:
        return f"https://www.amazon.fr/dp/{asin}?tag={AMAZON_TAG}"
    q = AMAZON_Q.get(p["name"])
    if not q:
        q = p["name"].replace("(", " ").replace(")", " ").replace(" et autres", "").replace("…", "").replace("plusieurs marques", "")
        if p["brand"] not in ("Plusieurs marques",) and p["brand"].split()[0].lower() not in q.lower():
            q = f'{p["brand"]} {q}'
    q = re.sub(r"\s+", " ", q).strip()
    return f"https://www.amazon.fr/s?k={quote_plus(q)}&tag={AMAZON_TAG}"


def buy(p, i, cls="btn btn-main", label="Voir sur Amazon", page=""):
    p = dict(p, link=p.get("link") or amazon(p))
    if p.get("link"):
        return f'<a class="{cls}" href="{e(p["link"])}" rel="sponsored nofollow noopener" target="_blank">{label}</a>'
    return f'<a class="{cls}" href="{page}#p{i+1}">{label}</a>'


BRAND_SITES = {
    "Roborock": "https://www.roborock.com", "Dreame": "https://www.dreametech.com", "Xiaomi": "https://www.mi.com",
    "Ecovacs": "https://www.ecovacs.com", "Husqvarna": "https://www.husqvarna.com", "Gardena": "https://www.gardena.com",
    "Worx": "https://www.worx.com", "Segway": "https://www.segway.com", "Maytronics": "https://www.maytronics.com",
    "Beatbot": "https://www.beatbot.com", "Aiper": "https://www.aiper.com", "Cecotec": "https://www.cecotec.fr",
    "Miele": "https://www.miele.fr", "Bosch": "https://www.bosch-home.fr", "Samsung": "https://www.samsung.com/fr/",
    "Beko": "https://www.beko.fr", "Midea": "https://www.midea.com", "Whisker": "https://www.litter-robot.com",
    "Petkit": "https://www.petkit.com", "PetSafe": "https://www.petsafe.com", "Dyson": "https://www.dyson.fr",
    "Rowenta": "https://www.rowenta.fr", "Tineco": "https://www.tineco.com", "Kärcher": "https://www.kaercher.com",
    "Philips": "https://www.philips.fr", "Cosori": "https://www.cosori.com", "Moulinex": "https://www.moulinex.fr",
    "Vorwerk": "https://www.vorwerk.com", "Kenwood": "https://www.kenwoodworld.com", "LG": "https://www.lg.com/fr/",
    "Catit": "https://www.catit.com", "Nilfisk": "https://www.nilfisk.com", "Rain Bird": "https://www.rainbird.com",
    "Makita": "https://www.makita.fr", "Mammotion": "https://www.mammotion.com", "Sure Petcare": "https://www.surepetcare.com",
    "FURminator": "https://www.furminator.com", "ChomChom": "https://www.chomchomroller.com", "Uproot": "https://uprootclean.com",
    "Oneisall": "https://www.oneisall.com", "Neabot": "https://www.neabot.com", "Eufy": "https://www.eufy.com", "Panasonic": "https://www.panasonic.com/fr/", "Calor": "https://www.calor.fr", "Daan Tech": "https://daan.tech",
}


def sources(g):
    seen = []
    for p in g["products"]:
        b = p["brand"]
        if b in BRAND_SITES and b not in seen:
            seen.append(b)
    if not seen:
        return ""
    items = "".join(f'<li><a href="{BRAND_SITES[b]}" rel="noopener" target="_blank">Site officiel de {e(b)}</a> : fiches techniques et notices</li>' for b in seen)
    return f"""
  <section class="block method" aria-labelledby="h-sources">
    <h2 id="h-sources" class="small-h">Sources ({len(seen)} citées)</h2>
    <ul class="sources">{items}</ul>
  </section>
"""


TOC = [("h-compare", "Le comparatif"), ("h-products", "Les modèles en détail"), ("h-criteria", "Les critères"),
       ("h-mistakes", "Les erreurs à éviter"), ("h-faq", "Questions fréquentes"), ("h-sources", "Sources")]


def toc(g):
    items = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in TOC if a != "h-sources" or sources(g))
    return f'<nav class="toc" aria-label="Sommaire"><span class="eyebrow">Sommaire</span><ol>{items}</ol></nav>'


def guide_page(g):
    cat = next(c for c in CATEGORIES if c["key"] == g["cat"])
    sub = sub_of(g)
    sub_crumb = f' › <a href="{href(sub["key"])}">{e(sub["name"])}</a>' if sub else ""
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"],
         "inLanguage": "fr-FR", "datePublished": UPDATED, "dateModified": UPDATED,
         "author": {"@type": "Organization", "name": SITE, "url": url("index")},
         "publisher": {"@type": "Organization", "name": SITE, "url": url("index")},
         "mainEntityOfPage": url(g["slug"])},
        crumbs_ld([("Accueil", "index"), (cat["name"], cat["key"])] + ([(sub["name"], sub["key"])] if sub else []) + [(g["short"], g["slug"])]),
        {"@context": "https://schema.org", "@type": "ItemList", "name": g["h1"],
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p["name"], "url": f'{url(g["slug"])}#p{i+1}'}
                             for i, p in enumerate(g["products"])]},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                        for q, a in g["faq"]]},
    ]
    n = len(g["products"])
    rows = "".join(
        f'<tr><td><a href="#p{i+1}">{e(p["name"])}</a></td><td>{e(p["badge"])}</td>'
        + "".join(f"<td>{e(v)}</td>" for v in p["table"]) + f'<td class="num">{e(p["price"])}</td><td>{buy(p, i, "btn btn-main btn-sm")}</td></tr>'
        for i, p in enumerate(g["products"]))
    cards = ""
    for i, p in enumerate(g["products"]):
        specs = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in p["specs"])
        cards += f"""
      <article class="card" id="p{i+1}">
        <div class="card-head">
          <span class="rank" aria-label="Rang {i+1}">{i+1:02d}</span>
          <div style="min-width:0"><h3 translate="no">{e(p["name"])}</h3><span class="who">{e(p["brand"])}</span></div>
          <span class="badge">{e(p["badge"])}</span>
        </div>
        <p class="for"><strong>Pour qui :</strong> {e(p["for"])}</p>
        <div class="pc">
          <div class="plus"><h4>Points forts</h4><ul>{ul(p["pros"])}</ul></div>
          <div class="minus"><h4>Points faibles</h4><ul>{ul(p["cons"])}</ul></div>
        </div>
        <dl class="specs">{specs}</dl>
        <div class="card-foot"><small>Caractéristiques issues de la documentation du fabricant, à vérifier sur la fiche produit au moment de l'achat.</small>{buy(p, i)}</div>
      </article>"""
    crit = "".join(f"<tr><td><strong>{e(a)}</strong></td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in g["criteria"])
    tip = "".join(f"<li>{e(x)}</li>" for x in g["tip"]["steps"])
    mistakes = "".join(f"<div><h3>{e(a)}</h3><p>{e(b)}</p></div>" for a, b in g["mistakes"])
    faq = "".join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>'
                  for i, (q, a) in enumerate(g["faq"]))
    same = [x for x in GUIDES if x["cat"] == g["cat"] and x["slug"] != g["slug"]]
    sib = [x for x in GUIDES if x["cat"] == g["cat"]]
    k = sib.index(g)
    prev_g, next_g = sib[k - 1], sib[(k + 1) % len(sib)]
    top = g["products"][0]
    others = same[4:] + [x for x in GUIDES if x["cat"] != g["cat"]]
    rel = "".join(card(x) for x in others[:20])
    cols = "".join(f"<th>{e(c)}</th>" for c in g["table_cols"])
    pick = g["pick"]
    return head(g["title"], g["desc"], g["slug"], ld).replace("<body>", f"<body{tint(g['cat'])}>") + header(g["cat"]).replace('<header class="top">', '<header class="top"><div class="progress" aria-hidden="true"></div>', 1) + f"""
<main class="wrap" id="haut">
  <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> › <a href="{href(cat["key"])}">{e(cat["name"])}</a>{sub_crumb} › {e(g["short"])}</nav>
  <div class="hero">
    <span class="eyebrow">Guide d'achat · {e(cat["name"])}</span>
    <h1>{e(g["h1"])}</h1>
    <p class="lede">{e(g["lede"])}</p>
    <div class="meta"><span>Mis à jour le <time datetime="{UPDATED}">{UPDATED_FR}</time></span><span>Lecture : {g["read"]} min</span><span>{n} modèles comparés</span></div>
    <p class="disclose">Certains liens de cette page sont affiliés : si vous achetez via eux, nous touchons une petite commission, sans surcoût pour vous. Cela ne change ni l'ordre ni l'avis.</p>
  </div>
  {toc(g)}

  <aside class="pick" aria-label="Notre choix rapide">
    <div style="display:grid;gap:8px;min-width:0">
      <span class="eyebrow">Si vous ne lisez qu'une chose</span>
      <h2>{e(g["products"][0]["name"])}</h2>
      <p>{e(pick["why"])}</p>
      <p class="alts">{pick["alts"]}</p>
    </div>
    <div class="pick-cta">{buy(g["products"][0], 0, "btn btn-light")}<a class="btn btn-onc" href="#p1">Lire l'avis</a></div>
  </aside>

  <section class="block" aria-labelledby="h-compare">
    {sec_head(1, "Le comparatif en un coup d'œil", "h-compare")}
    <div class="table-scroll"><table>
      <thead><tr><th>Modèle</th><th>Idéal pour</th>{cols}<th>Prix</th><th><span class="sr">Acheter</span></th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
  </section>

  <section class="block" aria-labelledby="h-products">
    {sec_head(2, f"Les {n} modèles en détail", "h-products")}
    <div class="products">{cards}
    </div>
  </section>

  <section class="block" aria-labelledby="h-same">
    {sec_head(3, f"Les lecteurs de ce guide regardent aussi", "h-same", href(cat["key"]), f"Toute la rubrique {cat['name']}")}
    <div class="related">{"".join(card(x) for x in same[:4])}</div>
  </section>

  <section class="block" aria-labelledby="h-criteria">
    {sec_head(4, g["criteria_title"], "h-criteria")}
    <p class="prose">{e(g["criteria_intro"])}</p>
    <div class="table-scroll"><table>
      <thead><tr><th>Critère</th><th>Ce qu'il faut vérifier</th><th>Pourquoi c'est important</th></tr></thead>
      <tbody>{crit}</tbody>
    </table></div>
    <div class="tip">
      <span class="eyebrow">Le conseil {SITE}</span>
      <h3>{e(g["tip"]["title"])}</h3>
      <ol>{tip}</ol>
    </div>
  </section>

  <section class="block" aria-labelledby="h-mistakes">
    {sec_head(5, "Les erreurs les plus fréquentes", "h-mistakes")}
    <div class="mistakes">{mistakes}</div>
  </section>

  <section class="block" aria-labelledby="h-faq">
    {sec_head(6, "Questions fréquentes", "h-faq")}
    <div class="faq">{faq}</div>
  </section>

  <section class="block method" aria-labelledby="h-method">
    <h2 id="h-method" class="small-h">Comment nous avons choisi</h2>
    <p>Nous comparons les fiches des fabricants, les notices et les retours de propriétaires, en privilégiant ce qui supprime réellement une tâche plutôt que les chiffres marketing. Aucune marque ne paie pour figurer ici. <a href="methode.html">Lire notre méthode</a>.</p>
  </section>
{sources(g)}
  <section class="block" aria-labelledby="h-related">
    {sec_head(7, "À lire aussi", "h-related")}
    <div class="related">{rel}</div>
  </section>
  <nav class="prevnext" aria-label="Guides voisins">
    <a href="{href(prev_g["slug"])}"><span class="eyebrow">← Guide précédent</span><strong>{e(prev_g["short"])}</strong></a>
    <a href="{href(next_g["slug"])}"><span class="eyebrow">Guide suivant →</span><strong>{e(next_g["short"])}</strong></a>
  </nav>
</main>
<aside class="buybar" aria-label="Notre choix">
  <div class="wrap">
    <div class="bb-txt"><span class="eyebrow">Notre choix · {e(top["badge"])}</span><strong translate="no">{e(top["name"])}</strong></div>
    <span class="bb-price">{e(top["price"])}</span>
    {buy(top, 0)}
  </div>
</aside>
""" + footer()


def card(g):
    cat = next(c for c in CATEGORIES if c["key"] == g["cat"])
    return f'<a href="{href(g["slug"])}"{tint(g["cat"])}><span class="tag">{e(cat["name"])}</span><strong>{e(g["short"])}</strong><span>{e(g["teaser"])}</span><small class="cmeta">{len(g["products"])} modèles · {g["read"]} min</small><em>Voir la sélection</em></a>'


def sec_head(n, title, hid, link=None, label=None):
    a = f'<a href="{link}">{e(label)}</a>' if link else ""
    return f'<div class="sec-head"><span class="idx">({n:02d})</span><h2 id="{hid}">{e(title)}</h2>{a}</div>'


def guides_in(key):
    return [g for g in GUIDES if g["cat"] == key]


LOVES = ["robot-aspirateur-laveur", "litiere-autonettoyante", "robot-tondeuse", "airfryer", "rouleau-anti-poils", "seche-linge-pompe-a-chaleur"]
FEATURED = ["robot-aspirateur-laveur", "robot-tondeuse", "litiere-autonettoyante", "seche-linge-pompe-a-chaleur", "airfryer", "robot-piscine", "aspirateur-balai-sans-fil", "fontaine-eau-chat"]


def home_page():
    ld = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": url("index"), "inLanguage": "fr-FR"},
        {"@context": "https://schema.org", "@type": "Organization", "name": SITE, "url": url("index")},
        {"@context": "https://schema.org", "@type": "ItemList", "name": "Guides d'achat",
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": g["h1"], "url": url(g["slug"])}
                             for i, g in enumerate(GUIDES)]},
    ]
    feat = "".join(card(next(g for g in GUIDES if g["slug"] == s)) for s in FEATURED)
    blocks = ""
    loves = ""
    for s_ in LOVES:
        g = next(x for x in GUIDES if x["slug"] == s_)
        p = g["products"][0]
        loves += f"""<article class="love"{tint(g["cat"])}>
  <span class="tag">{e(g["short"])}</span>
  <h3 translate="no">{e(p["name"])}</h3>
  <p>{e(g["pick"]["why"])}</p>
  <ul>{"".join(f"<li>{e(x)}</li>" for x in p["pros"][:2])}</ul>
  <div class="love-foot"><span class="bb-price">{e(p["price"])}</span>{buy(p, 0, page=href(g["slug"]))}<a class="more" href="{href(g["slug"])}">Lire le comparatif</a></div>
</article>"""
    for n, c in enumerate(CATEGORIES, 4):
        gs = guides_in(c["key"])
        blocks += f"""
  <section class="block" aria-labelledby="h-{c["key"]}"{tint(c["key"])}>
    {sec_head(n, c["name"], "h-" + c["key"], href(c["key"]), f"Voir les {len(gs)} guides")}
    <p class="prose muted">{e(c["intro"])}</p>{sub_links(c["key"])}
    <div class="related">{"".join(card(g) for g in gs[:4])}</div>
  </section>"""
    rows = "".join(f"""<a class="row" href="{href(c["key"])}"{tint(c["key"])}>
  <span class="row-n">{i:02d}</span>
  <strong>{e(c["name"])}</strong>
  <span class="row-pain">{e(c["pain"])}</span>
  <span class="row-count">{len(guides_in(c["key"]))} guides</span>
</a>""" + "".join(f"""<a class="row row-sub" href="{href(sc["key"])}"{tint(c["key"])}>
  <span class="row-n">↳</span>
  <strong>{e(sc["name"])}</strong>
  <span class="row-pain">Rouleaux, brosses, aspirateurs de toilettage, linge.</span>
  <span class="row-count">{len(sc["guides"])} guides</span>
</a>""" for sc in SUBCATS if sc["parent"] == c["key"]) for i, c in enumerate(CATEGORIES, 1))
    title = "Zéro Corvée : guides pour automatiser les tâches ménagères"
    desc = "Robots aspirateurs, tondeuses, lave-vitres, litières autonettoyantes… Nos comparatifs indépendants pour confier les corvées aux machines."
    return head(title, desc, "index", ld, "website") + header() + f"""
<main class="wrap" id="haut">
  <div class="hero home-hero">
    <span class="eyebrow"><span class="live" aria-hidden="true"></span>Guides d'achat indépendants · Mis à jour le <time datetime="{UPDATED}">{UPDATED_FR}</time></span>
    <h1>Les corvées, laissez les <span class="hl">machines</span> s'en charger.</h1>
    <div class="hero-foot">
      <p class="lede">Aspirateur, tonte, linge, litière, vaisselle : on compare les appareils qui font le travail à votre place, et on vous dit lesquels valent vraiment leur prix.</p>
      <div class="hero-cta"><a class="btn btn-main go" href="#h-start">Voir les guides</a><a class="btn btn-ghost go" href="methode.html">Notre méthode</a></div>
    </div>
    <dl class="stats">
      <div><dt>Guides d'achat</dt><dd>{len(GUIDES)}</dd></div>
      <div><dt>Rubriques</dt><dd>{len(CATEGORIES)}</dd></div>
      <div><dt>Modèles comparés</dt><dd>{sum(len(g["products"]) for g in GUIDES)}</dd></div>
      <div><dt>Marques qui paient pour apparaître</dt><dd>0</dd></div>
    </dl>
  </div>

  <section class="block" aria-labelledby="h-chores">
    {sec_head(1, "Choisissez votre corvée", "h-chores")}
    <div class="rows">{rows}</div>
  </section>

  <section class="block" aria-labelledby="h-start">
    {sec_head(2, "Pour commencer", "h-start")}
    <div class="related">{feat}</div>
  </section>

  <section class="block" aria-labelledby="h-loves">
    {sec_head(3, "Nos coups de cœur du moment", "h-loves")}
    <p class="prose muted">Le modèle qu'on recommande en premier dans chaque guide, celui qu'on achèterait pour nous.</p>
    <div class="loves">{loves}</div>
  </section>
{blocks}

  <section class="block" aria-labelledby="h-how">
    {sec_head(len(CATEGORIES) + 4, "Comment on choisit", "h-how", "methode.html", "Lire notre méthode")}
    <div class="mistakes how">
      <div><span class="eyebrow">01</span><h3>On part de la corvée</h3><p>La question n'est pas « quel appareil est le plus puissant » mais « qu'est-ce qu'il reste à faire à la main ».</p></div>
      <div><span class="eyebrow">02</span><h3>On compte le coût réel</h3><p>Sacs, filtres, consommables, électricité : on regarde le prix sur plusieurs années, pas seulement à l'achat.</p></div>
      <div><span class="eyebrow">03</span><h3>On dit ce qui coince</h3><p>Chaque modèle a ses points faibles. On les écrit, même pour notre premier choix.</p></div>
    </div>
  </section>
</main>
""" + footer()


def sub_of(g):
    return next((sc for sc in SUBCATS if g["slug"] in sc["guides"] and sc["parent"] == g["cat"]), None)


def sub_links(key):
    links = "".join(f'<a class="chip" href="{href(sc["key"])}">{e(sc["name"])} · {len(sc["guides"])} guides</a>' for sc in SUBCATS if sc["parent"] == key)
    return f'\n    <div class="chips"><span class="eyebrow">Sous-rubrique</span>{links}</div>' if links else ""


def sub_band(key):
    out = ""
    for sc in SUBCATS:
        if sc["parent"] != key:
            continue
        names = [p["name"] for s in sc["guides"] for p in next(g for g in GUIDES if g["slug"] == s)["products"]][:6]
        out += f"""
  <a class="pick sub-band" href="{href(sc["key"])}">
    <div style="display:grid;gap:8px;min-width:0">
      <span class="eyebrow">Sous-rubrique · {len(sc["guides"])} guides</span>
      <h2>{e(sc["name"])}</h2>
      <p>{e(sc["intro"])}</p>
      <p class="alts">{e(", ".join(names))}…</p>
    </div>
    <span class="btn btn-light go">Voir les outils</span>
  </a>"""
    return out


def subcat_page(sc):
    cat = next(c for c in CATEGORIES if c["key"] == sc["parent"])
    gs = [next(g for g in GUIDES if g["slug"] == s) for s in sc["guides"]]
    ld = [crumbs_ld([("Accueil", "index"), (cat["name"], cat["key"]), (sc["name"], sc["key"])]),
          {"@context": "https://schema.org", "@type": "CollectionPage", "name": sc["title"], "description": sc["desc"], "url": url(sc["key"])},
          {"@context": "https://schema.org", "@type": "ItemList",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": g["h1"], "url": url(g["slug"])} for i, g in enumerate(gs)]}]
    where = "".join(f"""<a class="row" href="{href(s)}#p{n}">
  <span class="row-n">{i:02d}</span>
  <strong>{e(w)}</strong>
  <span class="row-pain">{e(t)}</span>
  <span class="row-count">{e(next(g for g in gs if g["slug"] == s)["products"][n - 1]["name"])}</span>
</a>""" for i, (w, t, s, n) in enumerate(sc["where"], 1))
    rows = "".join(
        f'<tr><td><a href="{href(g["slug"])}#p{i+1}">{e(p["name"])}</a></td><td>{e(p["for"][:1].upper() + p["for"][1:])}</td>'
        f'<td class="num">{e(p["price"])}</td><td><a href="{href(g["slug"])}">{e(g["short"])}</a></td></tr>'
        for g in gs for i, p in enumerate(g["products"]))
    n_tools = sum(len(g["products"]) for g in gs)
    return head(f'{sc["title"]} | {SITE}' if len(sc["title"]) < 50 else sc["title"], sc["desc"], sc["key"], ld, "website").replace("<body>", f"<body{tint(cat['key'])}>") + header(sc["key"]) + f"""
<main class="wrap" id="haut">
  <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> › <a href="{href(cat["key"])}">{e(cat["name"])}</a> › {e(sc["name"])}</nav>
  <div class="hero">
    <span class="eyebrow">Sous-rubrique · {len(gs)} guides · {n_tools} outils comparés</span>
    <h1>{e(sc["title"])}</h1>
    <p class="lede">{e(sc["intro"])}</p>
  </div>

  <section class="block" aria-labelledby="h-where">
    {sec_head(1, "Où sont les poils ? Le bon outil pour chaque endroit", "h-where")}
    <div class="rows">{where}</div>
  </section>

  <section class="block" aria-labelledby="h-tools">
    {sec_head(2, f"Les {n_tools} outils comparés", "h-tools")}
    <div class="table-scroll"><table>
      <thead><tr><th>Outil</th><th>Pour qui</th><th>Prix</th><th>Guide complet</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
  </section>

  <section class="block" aria-labelledby="h-guides">
    {sec_head(3, "Les guides de la sous-rubrique", "h-guides", href(cat["key"]), f"Toute la rubrique {cat['name']}")}
    <div class="related">{"".join(card(g) for g in gs)}</div>
  </section>
</main>
""" + footer()


def category_page(c):
    gs = guides_in(c["key"])
    title = f"{c['name']} : nos {len(gs)} guides d'achat | {SITE}"
    desc = c["intro"][:155]
    ld = [crumbs_ld([("Accueil", "index"), (c["name"], c["key"])]),
          {"@context": "https://schema.org", "@type": "CollectionPage", "name": c["name"], "description": c["intro"], "url": url(c["key"])},
          {"@context": "https://schema.org", "@type": "ItemList",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": g["h1"], "url": url(g["slug"])} for i, g in enumerate(gs)]}]
    return head(title, desc, c["key"], ld, "website").replace("<body>", f"<body{tint(c['key'])}>") + header(c["key"]) + f"""
<main class="wrap" id="haut">
  <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> › {e(c["name"])}</nav>
  <div class="hero">
    <span class="eyebrow">Rubrique · {len(gs)} guides</span>
    <h1>{e(c["name"])}</h1>
    <p class="lede">{e(c["intro"])}</p>
  </div>
{sub_band(c["key"])}
  <section class="block" aria-label="Guides">
    <div class="related">{"".join(card(g) for g in gs)}</div>
  </section>
</main>
""" + footer()


def static_page(p):
    ld = [crumbs_ld([("Accueil", "index"), (p["nav"], p["slug"])])]
    return head(p["title"], p["desc"], p["slug"], ld, "website") + header() + f"""
<main class="wrap" id="haut">
  <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> › {e(p["nav"])}</nav>
  <div class="hero"><h1>{e(p["h1"])}</h1></div>
  <div class="prose static">{p["body"]}</div>
</main>
""" + footer()


def not_found():
    return head("Page introuvable | Zéro Corvée", "Cette page n'existe pas ou a été déplacée.", "404", []).replace(
        '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">') + header() + """
<main class="wrap" id="haut">
  <div class="hero"><h1>Cette page a été rangée trop loin.</h1><p class="lede">Elle n'existe pas ou a changé d'adresse. Repartez de l'accueil pour trouver votre guide.</p>
  <p><a class="btn btn-main" href="index.html">Retour à l'accueil</a></p></div>
</main>
""" + footer()


EXTRA_CSS = """
.small-h{font-size:1.2rem;color:var(--ink)}
.nav-sub{font-size:.86rem}
nav.cats a.nav-sub:not([aria-current]){color:#e11d63;box-shadow:inset 0 0 0 1px color-mix(in srgb,#e11d63 35%,transparent)}
nav.cats a.nav-sub[aria-current]{background:#e11d63}
.row-sub strong{font-size:clamp(1.02rem,2vw,1.3rem)}
.row-sub .row-n{background:none}
/* ---------- Envie d'acheter ---------- */
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.btn-sm{padding:7px 14px;font-size:.84rem}
.btn-onc{background:transparent;color:#fff;border-color:rgb(255 255 255 / .5)}
.btn-onc::after{content:"↓"}
.pick-cta .btn-light::after{content:"↗"}
.btn-onc:hover{border-color:#fff}
.pick-cta{display:flex;flex-wrap:wrap;gap:10px}
.cmeta{font-size:.78rem;color:var(--muted);font-variant-numeric:tabular-nums}
.related a{grid-template-rows:auto auto 1fr auto auto}
.loves{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.love{background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:24px;display:grid;gap:10px;align-content:start;position:relative;overflow:hidden}
.love::before{content:"";position:absolute;inset:0 0 auto;height:90px;background:linear-gradient(color-mix(in srgb,var(--c) 12%,transparent),transparent);pointer-events:none}
.love > *{position:relative}
.love h3{font-size:1.35rem;letter-spacing:-.025em}
.love p{color:var(--muted);font-size:.94rem}
.love ul{margin:0;padding:0;list-style:none;display:grid;gap:4px;font-size:.92rem}
.love li::before{content:"✓";color:var(--good);margin-right:8px;font-weight:700}
.love-foot{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin-top:6px;padding-top:14px;border-top:1px solid var(--line)}
.love .more{font-size:.88rem;color:var(--muted)}
.bb-price{font-family:var(--f-mono);font-weight:600;color:var(--c);font-size:.95rem}
.prevnext{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:56px}
.prevnext a{display:grid;gap:6px;padding:22px;border:1px solid var(--line);border-radius:var(--r);background:var(--surface);text-decoration:none;color:var(--ink)}
.prevnext a:last-child{text-align:right}
.prevnext a:hover{border-color:var(--c)}
.prevnext strong{font-size:1.1rem;letter-spacing:-.02em}
@media (max-width:600px){.prevnext{grid-template-columns:1fr}.prevnext a:last-child{text-align:left}}
.buybar{position:sticky;bottom:0;z-index:9;margin-top:40px;background:color-mix(in srgb,var(--surface) 90%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-top:1px solid var(--line);padding-bottom:env(safe-area-inset-bottom,0px)}
.buybar .wrap{display:flex;align-items:center;gap:12px 20px;padding-block:12px}
.bb-txt{display:grid;min-width:0;flex:1}
.bb-txt strong{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
@media (max-width:520px){.buybar .eyebrow{display:none}.bb-price{display:none}}
/* ---------- Couleurs ---------- */
.hl{background:linear-gradient(transparent 62%,color-mix(in srgb,var(--accent) 30%,transparent) 62%);padding-inline:.04em;color:var(--accent)}
.related a{grid-template-rows:auto auto 1fr auto;border-top:4px solid var(--c)}
.related a:hover{background:color-mix(in srgb,var(--c) 7%,var(--surface));border-color:var(--c)}
.tag{display:inline-flex;align-items:center;gap:6px;font-size:.74rem;font-weight:600;color:var(--c);text-transform:uppercase;letter-spacing:.06em}
.tag::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--c)}
.related em{color:var(--c)}
.sec-head .idx{color:var(--c);font-weight:600}
.row-n{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:color-mix(in srgb,var(--c) 14%,transparent);color:var(--c);font-weight:600}
.row:hover strong{color:var(--c)}
.row .row-count{border-color:color-mix(in srgb,var(--c) 40%,transparent);color:var(--c)}
.stats div:nth-child(1) dd{color:#3355ff}.stats div:nth-child(2) dd{color:#7c3aed}.stats div:nth-child(3) dd{color:#ea580c}.stats div:nth-child(4) dd{color:#16a34a}
.toc li::before{color:var(--c);font-weight:600}
.chip{background:var(--c);color:#fff}
.btn-main.go,.hero-cta .btn-main{background:var(--accent)}
.tip{border-left:4px solid var(--c)}
.mistakes{border-top:0;gap:16px 24px}
.mistakes div{border-top:3px solid var(--bad);padding-top:16px}
.how div{border-top:3px solid var(--c)}
.how div:nth-child(2){--c:#7c3aed}.how div:nth-child(3){--c:#16a34a}
.how .eyebrow{color:var(--c);font-weight:600}
.crumbs a:hover{color:var(--c)}
thead th{background:color-mix(in srgb,var(--c) 6%,var(--surface))}
.card-head .rank{border-color:var(--c);color:var(--c)}
.progress{background:var(--c)!important}
.chips{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}
.chip{display:inline-flex;align-items:center;gap:6px;text-decoration:none;font-size:.88rem;font-weight:500;background:var(--accent);color:var(--accent-ink);border-radius:999px;padding:7px 14px;transition:transform var(--t1) var(--ease)}
.chip::after{content:"→"}
.sub-band{text-decoration:none;margin-bottom:8px}
.sub-band .btn{pointer-events:none}
.sub-band h2{color:inherit}
footer .logo rect{fill:var(--accent-ink)}
footer .logo path{stroke:var(--accent)}
.muted{color:var(--muted)}
.home-hero{padding-block:clamp(48px,9vw,112px) 8px;gap:28px}
.home-hero h1{font-size:clamp(2.6rem,8.4vw,6.4rem);letter-spacing:-.05em;line-height:.98;max-width:13ch}
.hero-foot{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:20px 40px;align-items:end}
.hero-cta{display:flex;flex-wrap:wrap;gap:10px}
.go::after{content:"→"}
@media (max-width:760px){.hero-foot{grid-template-columns:1fr}}
.stats{margin:12px 0 0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid var(--line-strong)}
.stats div{padding:18px 16px 0 0;display:grid;gap:4px;align-content:start}
.stats dt{font-size:.8rem;color:var(--muted);order:2}
.stats dd{margin:0;font-size:clamp(1.8rem,4vw,2.6rem);font-weight:600;letter-spacing:-.04em;line-height:1;font-variant-numeric:tabular-nums}
@media (max-width:640px){.stats{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:16px}}
.rows{display:grid;border-top:1px solid var(--line)}
.row{display:grid;grid-template-columns:48px minmax(0,1.1fr) minmax(0,1.6fr) auto 24px;gap:8px 20px;align-items:center;padding:22px 4px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
.row::after{content:"→";justify-self:end;color:var(--muted)}
.row-n{font-family:var(--f-mono);font-size:.78rem;color:var(--muted)}
.row strong{font-size:clamp(1.15rem,2.4vw,1.6rem);font-weight:600;letter-spacing:-.03em;line-height:1.15}
.row-pain{color:var(--muted);font-size:.94rem}
.row-count{font-size:.8rem;border:1px solid var(--line-strong);border-radius:999px;padding:4px 12px;white-space:nowrap}
.row:hover::after{color:var(--ink)}
@media (max-width:760px){.row{grid-template-columns:36px minmax(0,1fr) 20px}.row-pain,.row-count{grid-column:2}.row-count{justify-self:start}.row::after{grid-column:3;grid-row:1}}
.how{border-top:0}
.how div{padding-top:18px}
.toc{border:1px solid var(--line);border-radius:var(--r);padding:20px 24px;margin-bottom:32px;display:grid;gap:10px;background:var(--surface)}
.toc ol{margin:0;padding:0;list-style:none;counter-reset:t;display:grid;gap:6px 24px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.toc li{counter-increment:t}
.toc li::before{content:counter(t,decimal-leading-zero);font-family:var(--f-mono);font-size:.74rem;color:var(--muted);margin-right:10px}
.toc a{text-decoration:none}
.toc a:hover{text-decoration:underline}
.sources{margin:0;padding-left:20px;display:grid;gap:4px}
.sources a{color:var(--muted)}
.related em{font-style:normal;font-weight:500;font-size:.86rem;color:var(--ink);padding-top:12px;border-top:1px solid var(--line)}
.static{display:grid;gap:14px;padding-bottom:24px}
.static h2{font-size:1.35rem;margin-top:12px}
.static ul{margin:0;padding-left:22px;display:grid;gap:6px}
.progress{position:absolute;left:0;right:0;bottom:-1px;height:2px;background:var(--ink);transform-origin:0 50%;transform:scaleX(0)}
/* ---------- Mouvement : personnalité « Corporate / Premium » ----------
   Courbe signature, 3 durées, une seule entrée (montée de 20px) pour tout le site. */
:root{--ease:cubic-bezier(.2,0,0,1);--ease-in:cubic-bezier(.05,.7,.1,1);--ease-out:cubic-bezier(.3,0,1,1);--t1:.15s;--t2:.3s;--t3:.5s}
@media (max-width:700px){:root{--t1:.12s;--t2:.24s;--t3:.4s}}
.live{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--good);margin-right:8px;vertical-align:1px}
.related a,.card{transition:transform var(--t2) var(--ease),border-color var(--t1) var(--ease),box-shadow var(--t2) var(--ease) 50ms}
.btn{transition:transform var(--t1) var(--ease),background-color var(--t1) var(--ease),border-color var(--t1) var(--ease)}
nav.cats a{transition:background-color var(--t1) var(--ease),color var(--t1) var(--ease)}
.related em::after,.row::after,.sec-head a::after,.go::after{display:inline-block;transition:transform var(--t2) var(--ease)}
.related em::after{content:"→";margin-left:6px}
.row{position:relative;isolation:isolate}
.row::before{content:"";position:absolute;inset:0;z-index:-1;background:color-mix(in srgb,var(--c) 7%,var(--surface));transform:scaleY(0);transform-origin:50% 100%;transition:transform var(--t2) var(--ease)}
.row > *{transition:transform var(--t2) var(--ease)}
.stats{position:relative;border-top:0}
.stats::before{content:"";position:absolute;inset:0 0 auto;height:1px;background:var(--line-strong);transform-origin:0 50%}
.sec-head{position:relative;border-top:0}
.sec-head::before{content:"";position:absolute;inset:0 0 auto;height:1px;background:var(--line-strong);transform-origin:0 50%}

@media (prefers-reduced-motion: no-preference){
  /* Entrée de l'en-tête : le titre d'abord, puis le reste (décalage 70 ms, total < 400 ms) */
  .hero > *{animation:rise var(--t3) var(--ease-in) backwards}
  .hero > :nth-child(2){animation-delay:70ms}
  .hero > :nth-child(3){animation-delay:140ms}
  .hero > :nth-child(4){animation-delay:210ms}
  .hero > :nth-child(5){animation-delay:280ms}
  .stats::before{animation:draw .9s var(--ease) .25s backwards}
  .stats > div{animation:rise var(--t3) var(--ease-in) backwards}
  .stats > div:nth-child(2){animation-delay:.33s}
  .stats > div:nth-child(3){animation-delay:.38s}
  .stats > div:nth-child(4){animation-delay:.43s}
  .pick{animation:rise var(--t3) var(--ease-in) .2s backwards}
  .live{animation:breathe 2.6s ease-in-out infinite}
  /* Retours au survol et au clic */
  .related a:hover{transform:translateY(-3px);box-shadow:0 18px 40px -24px rgb(0 0 0 / .35)}
  .related a:hover em::after,.sec-head a:hover::after,.go:hover::after{transform:translateX(4px)}
  .row:hover::before{transform:scaleY(1)}
  .row:hover > *{transform:translateX(10px)}
  .row:hover::after{transform:translateX(-4px)}
  .btn:hover,.chip:hover{transform:translateY(-1px)}
  .love{transition:transform var(--t2) var(--ease),box-shadow var(--t2) var(--ease) 50ms}
  .love:hover{transform:translateY(-3px);box-shadow:0 18px 40px -24px rgb(0 0 0 / .35)}
  .prevnext a{transition:border-color var(--t1) var(--ease)}
  .sub-band:hover .go::after{transform:translateX(4px)}
  .btn:active{transform:scale(.97);transition-duration:80ms}
  summary::after{transition:transform var(--t1) var(--ease)}
  /* Apparition au défilement : même montée partout, freinée en fin de course */
  @supports (animation-timeline: view()){
    .card,.related a,.mistakes > div,.tip,details,.row{animation:enter both var(--ease-in);animation-timeline:view();animation-range:entry 0% entry 40%}
    .sec-head::before{animation:draw both var(--ease);animation-timeline:view();animation-range:entry 10% entry 60%}
  }
  @supports (animation-timeline: scroll()){
    .progress{animation:grow linear both;animation-timeline:scroll(root)}
    .buybar{animation:bbin linear both;animation-timeline:scroll(root);animation-range:0 500px}
  }
}
@keyframes rise{from{transform:translateY(20px)}to{transform:none}}
@keyframes enter{from{opacity:.2;transform:translateY(20px)}to{opacity:1;transform:none}}
@keyframes draw{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes grow{to{transform:scaleX(1)}}
@keyframes bbin{from{transform:translateY(100%);opacity:0}to{transform:none;opacity:1}}
@keyframes breathe{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.45;transform:scale(.8)}}
"""


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    css = open(os.path.join(HERE, "base.css")).read()
    css = css.replace("--accent:#1f6b5c", "--accent:#2346a8").replace("--accent:#5cc2a8", "--accent:#8fa8ff")
    open(os.path.join(OUT, "style.css"), "w").write(css + EXTRA_CSS)
    open(os.path.join(OUT, "favicon.svg"), "w").write(FAVICON)
    # Fichier de validation Google Search Console.
    open(os.path.join(OUT, "google3a179b0f6ec352f4.html"), "w").write("google-site-verification: google3a179b0f6ec352f4.html")
    pages = {"index": home_page()}
    for c in CATEGORIES:
        pages[c["key"]] = category_page(c)
    for sc in SUBCATS:
        pages[sc["key"]] = subcat_page(sc)
    for g in GUIDES:
        pages[g["slug"]] = guide_page(g)
    for p in STATIC_PAGES:
        pages[p["slug"]] = static_page(p)
    for slug, content in pages.items():
        open(os.path.join(OUT, f"{slug}.html"), "w").write(content)
    open(os.path.join(OUT, "404.html"), "w").write(not_found())
    sm = "".join(f"  <url><loc>{url(s)}</loc><lastmod>{UPDATED}</lastmod></url>\n" for s in pages)
    open(os.path.join(OUT, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n')
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print(f"{len(pages) + 1} pages générées dans {OUT}")


if __name__ == "__main__":
    main()
