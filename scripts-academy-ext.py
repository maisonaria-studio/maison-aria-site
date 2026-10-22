# Génère netlify/lib/academy-ext.mjs à partir de src/academy/*.md
import json, re, pathlib
R = pathlib.Path(__file__).parent
PLAN = [  # (module, insérer après, leçons)
  ("a1", "a1l1", ["a1l4", "a1l5", "a1l6", "a1l7"]),
  ("a4", "a4l1", ["a4l4", "a4l5", "a4l6", "a4l7", "a4l8"]),
  ("a6", "a6l2", ["a6l4"]),
  ("a6", "a6l3", ["a6l5"]),
  ("a7", "a7l1", ["a7l4"]),
]
RES = {
  "a6l4": [{"name": "Modèle n8n · Formulaire → Tableau (.json)", "url": "/formation/modeles/atelier-1-formulaire-vers-tableau.json"}],
  "a6l5": [{"name": "Modèle n8n · Relance hebdo avec condition (.json)", "url": "/formation/modeles/atelier-2-relance-hebdo-conditions.json"}],
  "a7l4": [{"name": "Modèle n8n · Brouillon de réponse par l'IA (.json)", "url": "/formation/modeles/atelier-3-brouillon-reponse-ia.json"}],
}
out = []
for mod, after, ids in PLAN:
  ls = []
  for i in ids:
    t = (R / "src/academy" / f"{i}.md").read_text()
    m = re.match(r"---\ntitle:\s*(.+?)\n---\n", t)
    title = m.group(1).strip().strip('"')
    ls.append({"id": i, "title": title, "video": "", "body": t[m.end():].strip() + "\n", "resources": RES.get(i, []), "published": True})
  out.append({"module": mod, "after": after, "lessons": ls})
js = "// Généré par scripts-academy-ext.py depuis src/academy/*.md : ne pas modifier à la main.\n"
js += "export const EXTRA_LESSONS = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n"
(R / "netlify/lib/academy-ext.mjs").write_text(js)
print(sum(len(x["lessons"]) for x in out), "leçons")
