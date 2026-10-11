#!/usr/bin/env python3
"""Optimisations SEO de la page d'accueil (idempotent).
- images base64 -> fichiers /img/*.webp (HTML 3x plus léger, images en cache)
- title / meta / H1 / intro orientés recherche locale
- liens vers Aria Academy, guides, zones (maillage interne)
- bloc « Studio créatif dans le Golfe de Saint-Tropez » + plan du site en pied de page
"""
import re, base64, io, sys, json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "public"
sys.path.insert(0, str(Path(__file__).parent))
from content_zones import ZONES
from content_guides import GUIDES

p = PUB / "index.html"
s = p.read_text(encoding="utf-8")

# 1. Images inline -> fichiers
(PUB / "img").mkdir(exist_ok=True)
names = {(360, 204): "logo-maison-aria", (1100, 240): "maison-aria-studio-creatif"}
def extract(m):
    b = base64.b64decode(m.group(2))
    if len(b) < 3000:
        return m.group(0)
    im = Image.open(io.BytesIO(b))
    name = names.get(im.size, f"img-{im.size[0]}x{im.size[1]}")
    out = PUB / "img" / f"{name}.webp"
    if not out.exists():
        im.save(out, "WEBP", quality=90, method=6)
    return f"/img/{name}.webp"
s = re.sub(r"data:image/(png|jpeg);base64,([A-Za-z0-9+/=]+)", extract, s)
s = s.replace('<img src="/img/logo-maison-aria.webp" alt="Maison Aria">', '<img src="/img/logo-maison-aria.webp" alt="Maison Aria" width="360" height="204">')
s = s.replace('<img src="/img/maison-aria-studio-creatif.webp" alt="Maison Aria" width="1100" height="240">',
              '<img src="/img/maison-aria-studio-creatif.webp" alt="Maison Aria, studio créatif" width="1100" height="240" fetchpriority="high">')

# 2. Title, description, H1, intro
T_OLD = "Maison Aria Studio · Studio créatif dans le Golfe de Saint-Tropez"
T_NEW = "Maison Aria · Communication, photo et vidéo à Saint-Tropez"
D_OLD = "Maison Aria Studio, studio créatif dans le Golfe de Saint-Tropez : réseaux sociaux, shooting photo, vidéo, logo et identité visuelle, automatisation IA, 3D et formations. Devis rapide."
D_NEW = "Studio créatif dans le Golfe de Saint-Tropez : community manager, photographe, vidéaste, drone, logo et identité visuelle, automatisation IA. Devis gratuit."
s = s.replace(T_OLD, T_NEW).replace(D_OLD, D_NEW)
s = s.replace('<h1 class="sr">Maison Aria, studio créatif</h1>',
              '<h1 class="sr">Maison Aria, studio créatif dans le Golfe de Saint-Tropez : communication, réseaux sociaux, photo, vidéo et IA</h1>')
s = s.replace('<p class="intro">Nous accompagnons les entreprises, les marques et les particuliers à travers la communication, le design, la photographie et la vidéo.</p>',
              '<p class="intro">Nous accompagnons les entreprises, les marques et les particuliers du Golfe de Saint-Tropez à travers la communication, le design, la photographie et la vidéo.</p>')
if '"@type": "WebSite"' in s and '"inLanguage"' not in s.split('"@type": "WebSite"')[1][:300]:
    s = s.replace('"@type": "WebSite", "name": "Maison Aria Studio", "alternateName": "Maison Aria", "url": "https://maisonaria-studio.com/"',
                  '"@type": "WebSite", "name": "Maison Aria Studio", "alternateName": "Maison Aria", "url": "https://maisonaria-studio.com/", "inLanguage": "fr-FR", "publisher": {"@id": "https://maisonaria-studio.com/#entreprise"}')

# 3. Aria Academy a sa propre page
s = s.replace("https://maisonaria-studio.com/prestations/formation-ia-en-ligne/", "https://maisonaria-studio.com/aria-academy/")
s = s.replace('href="/prestations/formation-ia-en-ligne/"', 'href="/aria-academy/"')
s = s.replace('href="/prestations/${s.slug}/"', 'href="${s.slug === "formation-ia-en-ligne" ? "/aria-academy/" : "/prestations/" + s.slug + "/"}"')

# 4. Navigation
s = s.replace('<a href="#galeries">Galeries</a>\n      <a class="cta" href="#contact">Devis</a>',
              '<a href="#galeries">Galeries</a>\n      <a class="hide-m" href="/aria-academy/">Aria Academy</a>\n      <a class="cta" href="#contact">Devis</a>')
s = s.replace('<a href="/formation/">Espace formation</a>\n    <a class="mcta"',
              '<a href="/aria-academy/">Aria Academy · formation IA</a>\n    <a href="/guides/">Guides</a>\n    <a href="/formation/">Espace formation</a>\n    <a class="mcta"')

# 5. Bloc local + plan du site
if 'id="studio-local"' not in s:
    zones = "".join(f'<a href="/zones/{k}/">{z["ville"]}</a>' for k, z in ZONES.items())
    local = f'''  <section id="studio-local">
    <div class="wrap">
      <h2 class="h-xl">Studio créatif dans le Golfe de Saint-Tropez</h2>
      <div class="loc">
        <div>
          <p>Basée au Plan-de-la-Tour, Maison Aria accompagne les commerces, restaurants, hôtels, artisans, indépendants et marques du Golfe de Saint-Tropez dans toute leur communication : <a href="/expertises/strategie-reseaux-sociaux/">gestion des réseaux sociaux</a>, <a href="/expertises/photographie-creation-de-contenu/">shooting photo</a>, <a href="/expertises/video-montage/">vidéo et Réels</a>, <a href="/expertises/captation-videaste/">captation et drone</a>, <a href="/expertises/identite-visuelle-graphisme/">logo et identité visuelle</a>.</p>
          <p>Le studio aide aussi les entreprises à gagner du temps grâce à l’<a href="/expertises/intelligence-artificielle-automatisation/">intelligence artificielle et à l’automatisation</a>, et forme leurs équipes avec <a href="/aria-academy/">Aria Academy, la formation en ligne pour automatiser son entreprise sans coder</a>. Shootings, tournages et rendez-vous se font sur place ; le graphisme, la stratégie, le montage et l’IA se font aussi à distance, partout en France.</p>
        </div>
        <div>
          <h3>Zones d’intervention</h3>
          <div class="chips">{zones}</div>
          <p class="small-print"><a href="/zones/">Toutes les zones d’intervention</a> · <a href="/prestations/">Toutes les prestations</a> · <a href="/guides/">Guides pratiques</a></p>
        </div>
      </div>
    </div>
  </section>

'''
    s = s.replace('  <section id="contact">', local + '  <section id="contact">', 1)
    css = ('#studio-local .loc{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:32px 48px}'
           '@media(max-width:820px){#studio-local .loc{grid-template-columns:1fr}}'
           '#studio-local p{max-width:68ch}#studio-local p a{color:var(--orange)}#studio-local h3{margin:0 0 12px}'
           '#studio-local .chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}#studio-local .chips a{border:1px solid var(--line);border-radius:99px;padding:6px 14px;font-size:15px;text-decoration:none}#studio-local .chips a:hover{border-color:var(--orange)}'
           'footer .sitemap{flex-basis:100%;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,190px),1fr));gap:24px;padding-bottom:24px;border-bottom:1px solid var(--line)}'
           'footer .sitemap h2{font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin:0 0 10px;color:var(--cream)}'
           'footer .sitemap ul{list-style:none;margin:0;padding:0;display:grid;gap:6px;font-size:14px}footer .sitemap a{color:var(--cream-dim);text-decoration:none}footer .sitemap a:hover{color:var(--cream);text-decoration:underline}\n')
    s = s.replace("footer small{", css + "footer small{", 1)

if 'class="sitemap"' not in s:
    cats = json.loads(re.search(r"const CATS = (\[.*?\]);\n", s, re.S).group(1))
    exp = "".join(f'<li><a href="/expertises/{c["slug"]}/">{c["label"]}</a></li>' for c in cats)
    zon = "".join(f'<li><a href="/zones/{k}/">{z["ville"]}</a></li>' for k, z in ZONES.items())
    gui = "".join(f'<li><a href="/guides/{k}/">{g["h1"]}</a></li>' for k, g in GUIDES.items())
    plan = f'''    <nav class="sitemap" aria-label="Plan du site">
      <div><h2>Expertises</h2><ul>{exp}</ul></div>
      <div><h2>Zones d’intervention</h2><ul>{zon}</ul></div>
      <div><h2>Formation &amp; ressources</h2><ul><li><a href="/aria-academy/">Aria Academy, formation IA en ligne</a></li><li><a href="/formules/essentiel/">Formule Essentiel</a></li><li><a href="/formules/signature/">Formule Signature</a></li><li><a href="/formules/immersion/">Formule Immersion</a></li>{gui}</ul></div>
    </nav>
'''
    s = s.replace('<footer>\n  <div class="wrap">\n', '<footer>\n  <div class="wrap">\n' + plan, 1)

p.write_text(s, encoding="utf-8")
print("accueil :", len(s.encode()) // 1024, "Ko")

# 6. Un seul H1 sur l'accueil : les titres des documents légaux passent en H2 (même style)
s = p.read_text(encoding="utf-8")
for t in ["Mentions légales", "Politique de confidentialité", "Cookies", "Propriété intellectuelle", "Conditions générales de vente"]:
    s = s.replace(f"<h1>{t}</h1>", f'<h2 class="doc-h1">{t}</h2>')
if "h2.doc-h1{" not in s:
    s = s.replace("body h1{", "body h2.doc-h1{font-size:clamp(34px,5vw,54px);font-weight:800;line-height:1.02;margin:0 0 8px}body h1{", 1)
p.write_text(s, encoding="utf-8")
