#!/usr/bin/env python3
"""Générateur des pages SEO statiques de maisonaria-studio.com.

Usage :  python3 tools/seo/build.py
Lit le catalogue (CATS, PLANS) directement dans public/index.html, puis les contenus
rédigés dans tools/seo/content_*.py, et (ré)écrit :
  /prestations/<slug>/  /prestations/  /expertises/<slug>/  /formules/<code>/
  /zones/<ville>/  /zones/  /guides/<slug>/  /guides/  /aria-academy/  sitemap.xml
Pour modifier un texte : éditer le fichier content_*.py correspondant, relancer le script.
Pour ajouter une prestation : l'ajouter dans CATS (index.html) + une entrée dans content_prestations_*.py.
"""
import json, re, os, sys, datetime, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "public"
sys.path.insert(0, str(Path(__file__).parent))
from content_prestations_1 import P1, P2
from content_prestations_2 import P3, P4
from content_prestations_3 import P5, P6, P7, P8, P9
from content_expertises import EXPERTISES
from content_zones import ZONES
from content_guides import GUIDES

SITE = "https://maisonaria-studio.com"
TODAY = datetime.date.today().isoformat()
PRESTA = {**P1, **P2, **P3, **P4, **P5, **P6, **P7, **P8, **P9}
ACADEMY_SLUG = "formation-ia-en-ligne"   # cette prestation a sa propre page : /aria-academy/
e = lambda s: html.escape(str(s), quote=True)

# ---------- Catalogue lu dans la page d'accueil ----------
INDEX = (PUB / "index.html").read_text(encoding="utf-8")
CATS = json.loads(re.search(r"const CATS = (\[.*?\]);\n", INDEX, re.S).group(1))

def js_plans():
    src = re.search(r"const PLANS = \[(.*?)\n\];", INDEX, re.S).group(1)
    plans = []
    for blk in re.findall(r"\{code:.*?res:\"[^\"]*\"\}", src, re.S):
        g = lambda k: re.search(k + r':"((?:[^"\\]|\\.)*)"', blk).group(1)
        vol = re.findall(r'\["(\d+)","([^"]+)"\]', re.search(r"vol:\[(.*?)\]\]?,", blk, re.S).group(0))
        incl = re.findall(r'"([^"]+)"', re.search(r"incl:\[(.*?)\]", blk, re.S).group(1))
        plans.append(dict(code=g("code"), sub=g("sub"), price=g("price"), desc=g("desc"), concret=g("concret"), res=g("res"), vol=vol, incl=incl))
    return plans
PLANS = js_plans()

ITEMS = {}
for c in CATS:
    for it in c["items"]:
        it["cat"] = c
        ITEMS[it["slug"]] = it
missing = [s for s in ITEMS if s not in PRESTA and s != ACADEMY_SLUG]
if missing:
    sys.exit("Contenu SEO manquant pour : " + ", ".join(missing))

def price_num(p):
    m = re.search(r"\d+", p.replace(" ", ""))
    return m.group(0) if m else None

def url_of(slug):
    return "/aria-academy/" if slug == ACADEMY_SLUG else f"/prestations/{slug}/"

AREA = ["Saint-Tropez", "Sainte-Maxime", "Grimaud", "Port Grimaud", "Cogolin", "Gassin", "Ramatuelle",
        "La Croix-Valmer", "Le Plan-de-la-Tour", "Cavalaire-sur-Mer", "Fréjus", "Saint-Raphaël"]
AREA_LD = [{"@type": "Place", "name": "Golfe de Saint-Tropez"}] + [{"@type": "City", "name": a} for a in AREA]
ORG = {"@type": "ProfessionalService", "@id": SITE + "/#entreprise", "name": "Maison Aria Studio", "url": SITE + "/"}

# ---------- Gabarit commun ----------
CSS = (PUB / "prestations/flyer/index.html").read_text(encoding="utf-8")
CSS = re.search(r"<style>([\s\S]*?)</style>", CSS).group(1)
if "/*seo-v2*/" not in CSS:
    CSS = CSS.split("footer{")[0]
CSS += """/*seo-v2*/
header nav a.on{text-decoration:underline;text-underline-offset:6px}
.ctas{display:flex;flex-wrap:wrap;gap:10px}.ctas .btn{margin-top:28px}.ctas .btn.alt{margin-left:0}
.prose{max-width:72ch}.prose p,.prose li{font-size:18px}.prose h2{margin-top:36px}.prose a{color:var(--orange)}
.prose ol,.prose ul{padding-left:1.2em;display:grid;gap:8px}
ul.list{padding-left:1.2em;margin:0;display:grid;gap:8px}
.faq details{border-bottom:1px solid var(--line);padding:16px 0}.faq summary{cursor:pointer;font:700 19px var(--display);list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}.faq summary::after{content:"+";color:var(--orange);font-size:24px;line-height:1}.faq details[open] summary::after{content:"−"}
.faq details p{margin:10px 0 0;color:var(--cream-dim);max-width:70ch}
.chips{display:flex;flex-wrap:wrap;gap:8px}.chips a{border:1px solid var(--line);border-radius:99px;padding:6px 14px;font-size:15px;text-decoration:none}.chips a:hover{border-color:var(--orange)}
.band{background:var(--cream);color:var(--blue);border-radius:12px;padding:clamp(24px,4vw,40px);margin:48px 0;display:flex;flex-wrap:wrap;gap:16px 32px;align-items:center;justify-content:space-between}
.band h2{font-size:clamp(24px,3vw,34px);margin:0}.band p{margin:6px 0 0}.band .btn{margin:0;background:var(--blue);color:var(--cream)}
.mod{border:1px solid var(--line);border-radius:10px;padding:18px 20px}.mod h3{font-size:20px;margin-bottom:8px}.mod ol{margin:0;padding-left:1.2em;color:var(--cream-dim);font-size:16px}
.mods{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,320px),1fr));gap:14px}
.meta{font-size:14px;color:var(--cream-dim);margin-top:14px}
footer{border-top:1px solid var(--line);padding-block:44px 32px;font-size:15px;color:var(--cream-dim);margin-top:24px}
footer .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:28px}
footer h2{font:700 15px var(--text);letter-spacing:.06em;text-transform:uppercase;color:var(--cream);margin:0 0 12px}
footer ul{list-style:none;margin:0;padding:0;display:grid;gap:6px}footer a{text-decoration:none}footer a:hover{text-decoration:underline;color:var(--cream)}
footer .legal{margin-top:32px;padding-top:20px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px 24px;justify-content:space-between;font-size:14px}
"""

def head(title, desc, path, ld=(), robots=None, og_type="website"):
    url = SITE + path
    if len(title) > 66:   # au-delà, Google tronque : on garde le mot-clé, on retire la marque
        title = re.sub(r" \| Maison Aria( Studio| Visuals)?$", "", title)
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    rob = f'<meta name="robots" content="{robots}">' if robots else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">{rob}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="Maison Aria Studio"><meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png"><link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png"><link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#0A22AE"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Wix+Madefor+Display:wght@700;800&family=Wix+Madefor+Text:wght@400;600;700&display=swap"><style>{CSS}</style>{lds}</head>
"""

def header(on=""):
    links = [("/prestations/", "Prestations"), ("/aria-academy/", "Aria Academy"), ("/guides/", "Guides")]
    nav = "".join(f'<a href="{h}"{" class=on" if on == h else ""}>{t}</a>' for h, t in links)
    return f"""<body><header><div class="wrap"><a href="/" aria-label="Maison Aria Studio, accueil"><img src="/logo.png" alt="Maison Aria Studio" width="120" height="68"></a>
<nav aria-label="Navigation principale">{nav}<a class="cta" href="/#contact">Devis</a></nav></div></header>
"""

def footer():
    exp = "".join(f'<li><a href="/expertises/{c["slug"]}/">{e(c["label"])}</a></li>' for c in CATS)
    zon = "".join(f'<li><a href="/zones/{s}/">{e(z["ville"])}</a></li>' for s, z in ZONES.items())
    gui = "".join(f'<li><a href="/guides/{s}/">{e(g["h1"])}</a></li>' for s, g in list(GUIDES.items())[:4])
    return f"""<footer><div class="wrap"><div class="cols">
<div><h2>Expertises</h2><ul>{exp}</ul></div>
<div><h2>Zones d'intervention</h2><ul>{zon}<li><a href="/zones/">Toutes les zones</a></li></ul></div>
<div><h2>Ressources</h2><ul><li><a href="/aria-academy/">Aria Academy, formation IA</a></li><li><a href="/#formules">Formules mensuelles</a></li>{gui}<li><a href="/formation/">Espace élève</a></li></ul></div>
<div><h2>Maison Aria</h2><ul><li>Studio créatif · Le Plan-de-la-Tour (83120)</li><li><a href="tel:+33609482058">06 09 48 20 58</a></li><li><a href="mailto:maisonaria.contact@gmail.com">maisonaria.contact@gmail.com</a></li><li><a href="https://www.instagram.com/maisonaria_studio/" rel="noopener">Instagram Studio</a></li><li><a href="https://www.instagram.com/maisonaria_visuals/" rel="noopener">Instagram Visuals</a></li></ul></div>
</div><div class="legal"><span>© {datetime.date.today().year} Maison Aria · Studio créatif dans le Golfe de Saint-Tropez</span><span><a href="/#mentions-legales">Mentions légales</a> · <a href="/#confidentialite">Confidentialité</a> · <a href="/#cgv">CGV</a></span></div></div></footer></body></html>
"""

def crumbs(items):
    vis = " › ".join(f'<a href="{u}">{e(n)}</a>' if u else e(n) for n, u in items)
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": SITE + u} if u else {})} for i, (n, u) in enumerate(items)]}
    return f'<p class="crumbs">{vis}</p>', ld

def faq_block(faq, title="Questions fréquentes"):
    if not faq: return "", None
    items = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faq)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    return f'<section class="faq"><h2>{e(title)}</h2>{items}</section>', ld

STEPS = '<ol class="steps"><li><b>On échange</b> sur votre activité et votre projet, sur place ou en visio.</li><li><b>Vous recevez un devis</b> gratuit, clair et adapté.</li><li><b>Maison Aria réalise</b> la prestation.</li><li><b>Vous recevez vos fichiers</b>, prêts à être utilisés.</li></ol>'

def zones_chips():
    return '<div class="chips">' + "".join(f'<a href="/zones/{s}/">{e(z["ville"])}</a>' for s, z in ZONES.items()) + '</div>'

def band(title="Un projet ? Parlons-en.", text="Devis gratuit et sur mesure, réponse rapide.", href="/#contact", cta="Demander un devis ↗"):
    return f'<div class="band"><div><h2>{e(title)}</h2><p>{e(text)}</p></div><a class="btn" href="{href}">{e(cta)}</a></div>'

def card(it):
    return f'<a class="card" href="{url_of(it["slug"])}"><b>{e(it["sub"])}</b><span>{e(short(it["desc"]))}</span><em>dès {e(it["price"])}</em></a>'

def short(t, n=110):
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"

def write(path, content):
    p = PUB / path.strip("/") / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    PAGES.append(path)

PAGES = []

# ---------- Prestations ----------
def title_for(kw, price):
    t = f"{kw} · dès {price}"
    if len(t) > 62: t = kw
    return t + (" | Maison Aria" if len(t) <= 56 else "")

for slug, it in ITEMS.items():
    if slug == ACADEMY_SLUG: continue
    c, d = it["cat"], PRESTA[slug]
    path = f"/prestations/{slug}/"
    cr, cr_ld = crumbs([("Accueil", "/"), ("Prestations", "/prestations/"), (c["label"], f"/expertises/{c['slug']}/"), (it["sub"], None)])
    fq, fq_ld = faq_block(d["faq"], f"Questions fréquentes · {it['sub']}")
    num = price_num(it["price"])
    svc = {"@context": "https://schema.org", "@type": "Service", "name": d["kw"], "alternateName": it["sub"], "description": it["desc"],
           "serviceType": c["label"], "provider": ORG, "areaServed": AREA_LD, "url": SITE + path}
    if num: svc["offers"] = {"@type": "Offer", "priceCurrency": "EUR", "price": num, "priceSpecification": {"@type": "PriceSpecification", "minPrice": num, "priceCurrency": "EUR"}, "url": SITE + path}
    others = [x for x in c["items"] if x["slug"] != slug]
    body = f"""<main class="wrap">{cr}<article><p class="eyebrow">{e(c["label"])} · {e(it["code"])}</p><h1>{e(d["kw"])}</h1>
<p class="lead">{e(it["desc"])}</p><div class="price"><small>À partir de</small><b>{e(it["price"])}</b></div><div class="ctas"><a class="btn" href="/?prestation={it["n"]}#contact">Demander un devis gratuit ↗</a></div></article>
<section><h2>{e(it["sub"])} : en quelques mots</h2><div class="prose"><p>{e(d["txt"])}</p></div></section>
<section class="grid2"><div><h2>Ce que comprend la prestation</h2><ul class="tags">{"".join(f"<li>{e(x[:1].upper() + x[1:])}</li>" for x in it["prog"])}</ul></div>
<div class="box"><h3>Le résultat</h3><p>{e(it["res"][:1].upper() + it["res"][1:])}</p></div></section>
<section class="grid2"><div><h2>Pour qui ?</h2><ul class="list">{"".join(f"<li>{e(x)}</li>" for x in d["qui"])}</ul></div><div><h2>Comment ça se passe ?</h2>{STEPS}</div></section>
{fq}
<section><h2>Où intervient Maison Aria ?</h2><p>Dans tout le Golfe de Saint-Tropez et ses alentours, de Saint-Tropez à Fréjus et Saint-Raphaël. Les prestations réalisables à distance (graphisme, stratégie, montage, IA) sont proposées partout en France.</p>{zones_chips()}</section>
{f'<section><h2>Autres prestations · {e(c["label"])}</h2><div class="cards">{"".join(card(x) for x in others)}</div><p class="meta"><a href="/expertises/{c["slug"]}/">Voir toute l’expertise {e(c["label"])} →</a></p></section>' if others else ''}
{band()}</main>
"""
    ld = [svc, cr_ld] + ([fq_ld] if fq_ld else [])
    write(path, head(title_for(d["kw"], it["price"]), d["meta"], path, ld) + header("/prestations/") + body + footer())

# ---------- Expertises ----------
GUIDE_LINKS = {
    "strategie-reseaux-sociaux": ["tarif-community-manager", "idees-reels-restaurant-commerce"],
    "video-montage": ["idees-reels-restaurant-commerce"],
    "photographie-creation-de-contenu": ["prix-shooting-photo-professionnel"],
    "intelligence-artificielle-automatisation": ["automatiser-son-entreprise-avec-l-ia"],
    "formations-ia": ["automatiser-son-entreprise-avec-l-ia"],
}
for c in CATS:
    d = EXPERTISES[c["slug"]]
    path = f"/expertises/{c['slug']}/"
    cr, cr_ld = crumbs([("Accueil", "/"), ("Prestations", "/prestations/"), (c["label"], None)])
    fq, fq_ld = faq_block(d["faq"])
    items = c["items"]
    lst = {"@context": "https://schema.org", "@type": "ItemList", "name": c["label"], "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": SITE + url_of(x["slug"]), "name": x["sub"]} for i, x in enumerate(items)]}
    svc = {"@context": "https://schema.org", "@type": "Service", "name": d["h1"], "serviceType": c["label"], "provider": ORG, "areaServed": AREA_LD, "url": SITE + path}
    guides = "".join(f'<a class="card" href="/guides/{g}/"><b>{e(GUIDES[g]["h1"])}</b><span>{e(short(GUIDES[g]["lead"]))}</span><em>Lire le guide</em></a>' for g in GUIDE_LINKS.get(c["slug"], []))
    extra = '<p class="meta"><a href="/aria-academy/">Découvrir le programme complet d’Aria Academy →</a></p>' if c["slug"] in ("formations-ia", "intelligence-artificielle-automatisation") else ""
    body = f"""<main class="wrap">{cr}<p class="eyebrow">Maison Aria {"Visuals" if c["u"] == "visuals" else "Studio"}</p><h1>{e(d["h1"])}</h1>
<div class="prose">{"".join(f'<p class="lead">{e(p)}</p>' if i == 0 else f"<p>{e(p)}</p>" for i, p in enumerate(d["intro"]))}</div>
<div class="ctas"><a class="btn" href="/#contact">Demander un devis gratuit ↗</a></div>
<section><h2>{len(items)} prestation{"s" if len(items) > 1 else ""} {e(c["label"].lower())}</h2><div class="cards">{"".join(card(x) for x in items)}</div>{extra}</section>
<section class="grid2"><div><h2>Pourquoi Maison Aria ?</h2><ul class="list">{"".join(f"<li>{e(x)}</li>" for x in d["points"])}</ul></div><div><h2>Comment ça se passe ?</h2>{STEPS}</div></section>
{fq}
{f'<section><h2>Pour aller plus loin</h2><div class="cards">{guides}</div></section>' if guides else ''}
<section><h2>Zones d’intervention</h2><p>Saint-Tropez, Sainte-Maxime, Grimaud, Port Grimaud, Cogolin, Gassin, Ramatuelle, La Croix-Valmer, Cavalaire-sur-Mer, Le Plan-de-la-Tour, Fréjus, Saint-Raphaël et alentours.</p>{zones_chips()}</section>
{band()}</main>
"""
    write(path, head(d["title"], d["meta"], path, [svc, lst, cr_ld] + ([fq_ld] if fq_ld else [])) + header("/prestations/") + body + footer())

# ---------- Index des prestations ----------
path = "/prestations/"
cr, cr_ld = crumbs([("Accueil", "/"), ("Prestations", None)])
secs = "".join(f'<section><h2><a href="/expertises/{c["slug"]}/">{e(c["label"])}</a></h2><div class="cards">{"".join(card(x) for x in c["items"])}</div></section>' for c in CATS)
n = sum(len(c["items"]) for c in CATS)
body = f"""<main class="wrap">{cr}<p class="eyebrow">Catalogue</p><h1>Toutes les prestations Maison Aria</h1>
<p class="lead">{n} prestations de communication, photo, vidéo, graphisme, intelligence artificielle et 3D, pour les entreprises du Golfe de Saint-Tropez et d’ailleurs. Tarifs « à partir de », devis gratuit et sur mesure.</p>
<section><h2>Formules mensuelles de création de contenu</h2><div class="cards">{"".join(f'<a class="card" href="/formules/{p["code"].lower()}/"><b>{e(p["code"].title())} · {e(p["sub"])}</b><span>{e(", ".join(f"{a} {b}" for a, b in p["vol"]))} par mois</span><em>dès {p["price"]} € / mois</em></a>' for p in PLANS)}</div></section>
{secs}{band()}</main>
"""
write(path, head("Prestations : réseaux sociaux, photo, vidéo, logo, IA | Maison Aria", "Les 54 prestations de Maison Aria dans le Golfe de Saint-Tropez : réseaux sociaux, shooting photo, vidéo, logo, identité visuelle, automatisation IA, 3D et formations.", path, [cr_ld]) + header("/prestations/") + body + footer())

# ---------- Formules ----------
FORMULE_FAQ = [("Les formules sont-elles sans engagement ?", "Les formules se renouvellent chaque mois ; les conditions (préavis notamment) sont détaillées dans les CGV."),
               ("Peut-on adapter le contenu de la formule ?", "Oui. Les formules sont une base, ajustable selon votre rythme de publication, vos objectifs et votre budget."),
               ("Qui publie les contenus ?", "Les contenus sont livrés prêts à publier ; les modalités de publication sont définies avec vous.")]
for p in PLANS:
    code = p["code"]; nm = code.title()
    path = f"/formules/{code.lower()}/"
    cr, cr_ld = crumbs([("Accueil", "/"), ("Prestations", "/prestations/"), (f"Formule {nm}", None)])
    fq, fq_ld = faq_block(FORMULE_FAQ)
    vol = ", ".join(f"{a} {b}" for a, b in p["vol"])
    others = "".join(f'<a class="card" href="/formules/{q["code"].lower()}/"><b>{e(q["code"].title())} · {e(q["sub"])}</b><span>{e(", ".join(f"{a} {b}" for a, b in q["vol"]))} par mois</span><em>dès {q["price"]} € / mois</em></a>' for q in PLANS if q is not p)
    svc = {"@context": "https://schema.org", "@type": "Service", "name": f"Formule {nm} · création de contenu réseaux sociaux", "description": p["desc"], "provider": ORG, "areaServed": AREA_LD,
           "offers": {"@type": "Offer", "price": p["price"], "priceCurrency": "EUR", "priceSpecification": {"@type": "UnitPriceSpecification", "price": p["price"], "priceCurrency": "EUR", "unitText": "MONTH"}, "url": SITE + path}}
    body = f"""<main class="wrap">{cr}<article><p class="eyebrow">Formule mensuelle de création de contenu</p><h1>Formule {e(nm)} : {e(vol)} par mois</h1><p class="lead">{e(p["desc"])}</p>
<div class="price"><small>À partir de</small><b>{p["price"]} €</b><small>/ mois</small></div><div class="ctas"><a class="btn" href="/?formule={code}#contact">Choisir la formule {e(nm)} ↗</a></div></article>
<section class="grid2"><div><h2>Inclus chaque mois</h2><ul class="tags">{"".join(f"<li>{e(x[:1].upper() + x[1:])}</li>" for x in p["incl"])}</ul><p>{e(p["concret"])}</p></div><div class="box"><h3>Le résultat</h3><p>{e(p["res"])}</p></div></section>
<section class="grid2"><div><h2>Pour qui ?</h2><p>Commerces, restaurants, établissements touristiques, prestataires et marques du Golfe de Saint-Tropez qui veulent une communication régulière sans y consacrer leurs soirées. Les formules peuvent être ajustées selon vos besoins et votre budget.</p></div><div><h2>Comment ça se passe ?</h2>{STEPS}</div></section>
{fq}<section><h2>Les autres formules</h2><div class="cards">{others}</div><p class="meta"><a href="/expertises/strategie-reseaux-sociaux/">Community manager dans le Golfe de Saint-Tropez →</a></p></section>{band()}</main>
"""
    write(path, head(f"Formule {nm} · {vol} par mois · {p['price']} € | Maison Aria", f"Formule {nm} de création de contenu pour les réseaux sociaux : {vol} chaque mois, dès {p['price']} €/mois. Maison Aria, Golfe de Saint-Tropez.", path, [svc, cr_ld, fq_ld]) + header("/prestations/") + body + footer())

# ---------- Zones ----------
for s, z in ZONES.items():
    path = f"/zones/{s}/"
    cr, cr_ld = crumbs([("Accueil", "/"), ("Zones d’intervention", "/zones/"), (z["ville"], None)])
    fq, fq_ld = faq_block(z["faq"])
    svc = {"@context": "https://schema.org", "@type": "Service", "name": f"Communication, photo et vidéo à {z['ville']}", "provider": ORG,
           "areaServed": [{"@type": "City", "name": v.strip()} for v in re.split(r" et |, ", z["ville"])], "url": SITE + path}
    exp = "".join(f'<a href="/expertises/{c["slug"]}/">{e(c["label"])}</a>' for c in CATS)
    body = f"""<main class="wrap">{cr}<p class="eyebrow">Zone d’intervention</p><h1>Communication, photo et vidéo à {e(z["ville"])}</h1>
<div class="prose">{"".join(f'<p class="lead">{e(p)}</p>' if i == 0 else f"<p>{e(p)}</p>" for i, p in enumerate(z["intro"]))}</div>
<div class="ctas"><a class="btn" href="/#contact">Demander un devis gratuit ↗</a></div>
<section class="grid2"><div><h2>Les entreprises accompagnées</h2><ul class="list">{"".join(f"<li>{e(x)}</li>" for x in z["secteurs"])}</ul></div><div><h2>Comment ça se passe ?</h2>{STEPS}</div></section>
<section><h2>Prestations les plus demandées à {e(z["ville"])}</h2><div class="cards">{"".join(card(ITEMS[x]) for x in z["services"])}</div></section>
<section><h2>Toutes les expertises</h2><div class="chips">{exp}</div></section>
{fq}<section><h2>Autres communes</h2><div class="chips">{"".join(f'<a href="/zones/{t}/">{e(y["ville"])}</a>' for t, y in ZONES.items() if t != s)}</div></section>{band()}</main>
"""
    write(path, head(z["title"], z["meta"], path, [svc, cr_ld, fq_ld]) + header() + body + footer())

path = "/zones/"
cr, cr_ld = crumbs([("Accueil", "/"), ("Zones d’intervention", None)])
body = f"""<main class="wrap">{cr}<p class="eyebrow">Golfe de Saint-Tropez et alentours</p><h1>Zones d’intervention de Maison Aria</h1>
<p class="lead">Basée au Plan-de-la-Tour, Maison Aria se déplace dans tout le Golfe de Saint-Tropez, ainsi qu’à Fréjus et Saint-Raphaël, pour les shootings, tournages et rendez-vous. Graphisme, stratégie, montage et automatisation se font aussi à distance, partout en France.</p>
<section><div class="cards">{"".join(f'<a class="card" href="/zones/{s}/"><b>{e(z["ville"])}</b><span>{e(short(z["intro"][0]))}</span><em>Voir la page</em></a>' for s, z in ZONES.items())}</div></section>{band()}</main>
"""
write(path, head("Zones d'intervention : Golfe de Saint-Tropez, Fréjus, Saint-Raphaël | Maison Aria", "Maison Aria intervient à Saint-Tropez, Sainte-Maxime, Grimaud, Cogolin, Ramatuelle, Gassin, Cavalaire, La Croix-Valmer, Le Plan-de-la-Tour, Fréjus et Saint-Raphaël.", path, [cr_ld]) + header() + body + footer())

# ---------- Guides ----------
PERSON = {"@type": "Person", "name": "Leïssa Vedel", "jobTitle": "Fondatrice de Maison Aria", "url": SITE + "/"}
for s, g in GUIDES.items():
    path = f"/guides/{s}/"
    cr, cr_ld = crumbs([("Accueil", "/"), ("Guides", "/guides/"), (g["h1"], None)])
    fq, fq_ld = faq_block(g["faq"])
    art = {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["meta"], "author": PERSON,
           "publisher": {"@type": "Organization", "name": "Maison Aria Studio", "logo": {"@type": "ImageObject", "url": SITE + "/logo-square.png"}},
           "datePublished": g.get("date", "2026-10-10"), "dateModified": g.get("date", "2026-10-10"), "image": SITE + "/og-image.png", "mainEntityOfPage": SITE + path, "inLanguage": "fr-FR"}
    body = f"""<main class="wrap">{cr}<article class="prose"><p class="eyebrow">Guide</p><h1>{e(g["h1"])}</h1><p class="lead">{e(g["lead"])}</p>
<p class="meta">Par Leïssa Vedel, fondatrice de Maison Aria · mis à jour le {datetime.date.fromisoformat(g.get("date", "2026-10-10")).strftime("%d/%m/%Y")}</p>
{g["body"]}</article>{fq}{band()}</main>
"""
    write(path, head(g["title"] + " | Maison Aria", g["meta"], path, [art, cr_ld, fq_ld], og_type="article") + header("/guides/") + body + footer())

path = "/guides/"
cr, cr_ld = crumbs([("Accueil", "/"), ("Guides", None)])
body = f"""<main class="wrap">{cr}<p class="eyebrow">Ressources</p><h1>Guides pratiques : communication, contenu et IA</h1>
<p class="lead">Des conseils concrets pour les dirigeants de petites entreprises : réseaux sociaux, photo, vidéo, budget et automatisation grâce à l’intelligence artificielle.</p>
<section><div class="cards">{"".join(f'<a class="card" href="/guides/{s}/"><b>{e(g["h1"])}</b><span>{e(short(g["lead"], 140))}</span><em>Lire le guide</em></a>' for s, g in GUIDES.items())}</div></section>{band()}</main>
"""
write(path, head("Guides : réseaux sociaux, photo, vidéo et IA pour TPE | Maison Aria", "Guides pratiques pour les TPE et commerces : prix d'un shooting photo, tarif d'un community manager, idées de Réels, automatiser son entreprise avec l'IA.", path, [cr_ld]) + header("/guides/") + body + footer())

# ---------- Aria Academy ----------
from content_academy import ACADEMY
MODS = json.loads((Path(__file__).parent / "academy_outline.json").read_text(encoding="utf-8"))
A = ACADEMY; it = ITEMS[ACADEMY_SLUG]
path = "/aria-academy/"
cr, cr_ld = crumbs([("Accueil", "/"), ("Formations IA", "/expertises/formations-ia/"), ("Aria Academy", None)])
fq, fq_ld = faq_block(A["faq"])
nb_l = sum(len(m["lessons"]) for m in MODS)
course = {"@context": "https://schema.org", "@type": "Course", "name": "Aria Academy · Automatiser son entreprise grâce à l'IA, sans coder", "description": A["meta"],
          "provider": {"@type": "Organization", "name": "Maison Aria Studio", "sameAs": SITE + "/"}, "inLanguage": "fr", "url": SITE + path,
          "teaches": A["teaches"], "educationalLevel": "Débutant", "numberOfCredits": None,
          "syllabusSections": [{"@type": "Syllabus", "name": m["title"], "description": " · ".join(l["title"] for l in m["lessons"])} for m in MODS],
          "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Online", "courseWorkload": "PT12H", "instructor": PERSON},
          "offers": {"@type": "Offer", "category": "Paid", "price": price_num(it["price"]), "priceCurrency": "EUR", "url": SITE + path, "availability": "https://schema.org/InStock"}}
course = {k: v for k, v in course.items() if v is not None}
mods = "".join(f'<div class="mod"><h3>Module {i + 1} · {e(m["title"])}</h3><ol>{"".join(f"<li>{e(l["title"])}</li>" for l in m["lessons"])}</ol></div>' for i, m in enumerate(MODS))
body = f"""<main class="wrap">{cr}<article><p class="eyebrow">Formation en ligne · Aria Academy</p><h1>{e(A["h1"])}</h1>
<p class="lead">{e(A["lead"])}</p><div class="price"><small>À partir de</small><b>{e(it["price"])}</b></div>
<div class="ctas"><a class="btn" href="/?acces=1#cat-formations-ia">Demander mon accès ↗</a><a class="btn alt" href="/formation/">Espace élève</a></div>
<p class="meta">{len(MODS)} modules · {nb_l} leçons écrites et vidéo · {A["fiches"]} fiches pratiques à télécharger · communauté Discord</p></article>
<section class="grid2"><div><h2>À qui s’adresse la formation ?</h2><ul class="list">{"".join(f"<li>{e(x)}</li>" for x in A["qui"])}</ul></div>
<div><h2>Ce que vous saurez faire</h2><ul class="list">{"".join(f"<li>{e(x)}</li>" for x in A["resultats"])}</ul></div></section>
<section><h2>Le programme en {len(MODS)} modules</h2><div class="mods">{mods}</div></section>
<section class="grid2"><div><h2>Comment se déroule la formation ?</h2><ul class="list">{"".join(f"<li>{e(x)}</li>" for x in A["format"])}</ul></div>
<div><h2>Qui anime la formation ?</h2><div class="prose"><p>{e(A["formatrice"])}</p></div></div></section>
<section><h2>Pourquoi apprendre à automatiser ?</h2><div class="prose">{"".join(f"<p>{e(p)}</p>" for p in A["pourquoi"])}<p>Pour un premier aperçu de la méthode, lisez le guide <a href="/guides/automatiser-son-entreprise-avec-l-ia/">Automatiser son entreprise avec l’IA sans coder</a>.</p></div></section>
{fq}
<section><h2>Préférez-vous être accompagné en présentiel ?</h2><div class="cards">{card(ITEMS["formation-personnalisee"])}{card(ITEMS["audit-ia"])}{card(ITEMS["workflow-ia"])}</div></section>
{band("Prêt à automatiser votre entreprise ?", "Demandez votre accès à Aria Academy : vous recevez vos identifiants par e-mail.", "/?acces=1#cat-formations-ia", "Demander mon accès ↗")}</main>
"""
write(path, head(A["title"], A["meta"], path, [course, cr_ld, fq_ld]) + header("/aria-academy/") + body + footer())

# ---------- Sitemap ----------
old = PUB / "prestations" / ACADEMY_SLUG
if old.exists():
    for f in old.iterdir(): f.unlink()
    old.rmdir()
prio = lambda p: "1.0" if p == "/" else "0.9" if p in ("/aria-academy/", "/prestations/") or p.startswith("/expertises/") else "0.8" if p.startswith(("/zones/", "/formules/", "/guides/")) else "0.7"
urls = ["/"] + sorted(set(PAGES), key=lambda p: (p.count("/"), p))
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{prio(u)}</priority></url>\n" for u in urls) + "</urlset>\n"
(PUB / "sitemap.xml").write_text(sm, encoding="utf-8")
print(f"{len(PAGES)} pages générées, sitemap : {len(urls)} URL")
