import { getStore } from "@netlify/blobs";

export const meta = () => getStore({ name: "galeries", consistency: "strong" });
export const photos = () => getStore({ name: "photos", consistency: "strong" });

export async function loadEvents() {
  return (await meta().get("events", { type: "json" })) || [];
}
export async function saveEvents(events) {
  await meta().setJSON("events", events);
}
export const json = (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" } });

export function isAdmin(req) {
  const expected = process.env.ADMIN_PASSWORD || "";
  const got = (req.headers.get("authorization") || "").replace(/^Bearer\s+/i, "");
  if (!expected || got.length !== expected.length) return false;
  let diff = 0;
  for (let i = 0; i < expected.length; i++) diff |= expected.charCodeAt(i) ^ got.charCodeAt(i);
  return diff === 0;
}
export const slug = s => String(s).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 60);

// ---------- Formation en ligne ----------
export const files = () => getStore({ name: "formation-fichiers", consistency: "strong" });

// Programme : automatiser et « processiser » les tâches de l'entreprise grâce à l'IA.
// Chaque leçon est créée en brouillon avec un plan, à compléter et publier depuis l'espace dédié.
const L = (id, title, plan) => ({ id, title, video: "", body: "## Au programme\n" + plan.map(x => "- " + x).join("\n") + "\n\n> Leçon en cours de rédaction.", resources: [], published: false });
export const DEFAULT_COURSE = {
  version: 2,
  title: "Aria Academy",
  intro: "Bienvenue dans Aria Academy ! Cette formation t'accompagne pas à pas pour identifier les tâches répétitives de ton entreprise, les transformer en processus clairs, puis les automatiser grâce à l'IA. Avance à ton rythme et marque chaque leçon comme terminée pour suivre ta progression.",
  groupUrl: "",
  modules: [
    { id: "a1", title: "L'IA au service de l'entreprise", lessons: [
      L("a1l1", "Ce que l'IA peut (et ne peut pas) faire pour ton entreprise", ["IA générative, assistants et automatisations : les différences", "Exemples concrets de gains de temps", "Les limites à connaître"]),
      L("a1l2", "Utiliser l'IA en toute sécurité", ["Données sensibles et confidentialité", "RGPD : les bons réflexes", "Vérifier et relire ce que produit l'IA"]),
      L("a1l3", "Ta feuille de route", ["Fixer ton objectif de temps gagné", "Choisir les premiers processus à traiter", "Organiser ta progression dans la formation"])
    ]},
    { id: "a2", title: "Cartographier ses tâches et ses processus", lessons: [
      L("a2l1", "Faire l'inventaire des tâches répétitives", ["Lister les tâches d'une semaine type", "Mesurer le temps passé", "Repérer les tâches à faible valeur"]),
      L("a2l2", "Choisir quoi automatiser en premier", ["La matrice impact / effort", "Les tâches idéales pour débuter", "Éviter les fausses bonnes idées"]),
      L("a2l3", "Dessiner un processus de A à Z", ["Déclencheur, étapes, décisions, résultat", "Qui fait quoi, avec quel outil", "Exercice : cartographier un processus de ton entreprise"])
    ]},
    { id: "a3", title: "Processiser : documenter pour mieux déléguer", lessons: [
      L("a3l1", "Rédiger une procédure claire", ["Structure d'une fiche procédure", "Checklists et modèles réutilisables", "Rédiger une procédure avec l'aide de l'IA"]),
      L("a3l2", "Créer sa bibliothèque de modèles", ["E-mails types, devis, relances, comptes rendus", "Où et comment les ranger", "Garder une bibliothèque à jour"]),
      L("a3l3", "Standardiser ses données", ["Nommer et ranger ses fichiers", "Structurer un tableur exploitable", "Préparer ses données pour l'automatisation"])
    ]},
    { id: "a4", title: "Les assistants IA au quotidien", lessons: [
      L("a4l1", "Bien choisir son assistant IA", ["ChatGPT, Claude, Copilot, Gemini : lequel pour quoi", "Versions gratuites et payantes", "Paramétrer son assistant"]),
      L("a4l2", "La méthode pour écrire des prompts efficaces", ["Contexte, rôle, tâche, format, exemples", "Améliorer une réponse étape par étape", "Erreurs fréquentes"]),
      L("a4l3", "Ta bibliothèque de prompts métier", ["Prompts pour les e-mails, devis, comptes rendus, synthèses", "Transformer un prompt en modèle réutilisable", "Exercice : 5 prompts pour ton activité"])
    ]},
    { id: "a5", title: "Créer ses propres assistants IA", lessons: [
      L("a5l1", "Assistants personnalisés : le principe", ["GPTs, Projets et assistants sur mesure", "Instructions et base de connaissances", "Cas d'usage en entreprise"]),
      L("a5l2", "Construire un assistant pas à pas", ["Rédiger les instructions", "Ajouter ses documents et procédures", "Tester et améliorer"]),
      L("a5l3", "Partager un assistant avec son équipe", ["Droits d'accès et bonnes pratiques", "Maintenir l'assistant à jour", "Mesurer son utilisation"])
    ]},
    { id: "a6", title: "Automatiser sans coder", lessons: [
      L("a6l1", "Les bases de l'automatisation", ["Déclencheur, actions, conditions", "Zapier, Make, n8n : comparatif", "Coûts et limites des offres gratuites"]),
      L("a6l2", "Ta première automatisation", ["Exemple : formulaire → tableur → e-mail de confirmation", "Tester et corriger", "Surveiller les erreurs"]),
      L("a6l3", "Automatisations avancées", ["Conditions et filtres", "Boucles et traitement de listes", "Organiser et nommer ses scénarios"])
    ]},
    { id: "a7", title: "Connecter l'IA à ses outils", lessons: [
      L("a7l1", "Ajouter l'IA dans une automatisation", ["Appeler une IA dans Zapier, Make ou n8n", "Rédiger, résumer, classer, extraire automatiquement", "Garder un humain dans la boucle"]),
      L("a7l2", "E-mails, agenda et CRM", ["Trier et pré-rédiger les réponses aux e-mails", "Relances clients automatiques", "Mettre à jour son CRM ou son tableur"]),
      L("a7l3", "Documents, devis et facturation", ["Générer des documents à partir de modèles", "Extraire les données de factures et justificatifs", "Suivre les paiements"])
    ]},
    { id: "a8", title: "Déployer, mesurer et faire adopter", lessons: [
      L("a8l1", "Tester avant de généraliser", ["Phase pilote et jeux de test", "Plan B en cas de panne", "Documenter l'automatisation"]),
      L("a8l2", "Mesurer les gains", ["Temps gagné et erreurs évitées", "Tableau de suivi simple", "Calculer le retour sur investissement"]),
      L("a8l3", "Embarquer son équipe", ["Présenter les nouveaux processus", "Former et accompagner", "Faire vivre et améliorer les processus"])
    ]},
    { id: "a9", title: "Cas pratiques", lessons: [
      L("a9l1", "Cas 1 : de la demande de devis à la relance", ["Formulaire, devis généré, envoi et relance automatiques"]),
      L("a9l2", "Cas 2 : la boîte mail sous contrôle", ["Tri, étiquettes, brouillons de réponse et résumé quotidien"]),
      L("a9l3", "Cas 3 : le reporting hebdomadaire automatique", ["Collecte des chiffres, synthèse par l'IA et envoi à l'équipe"]),
      L("a9l4", "Ton projet : automatiser un processus de ton entreprise", ["Choisir le processus", "Le documenter", "L'automatiser et mesurer le résultat", "Le partager sur le Discord pour avoir des retours"])
    ]}
  ]
};

// Ancien programme jamais modifié : remplacé automatiquement par le nouveau
const untouchedV1 = c => !c.version && c.modules?.length === 8 && c.modules.every(m => /^m\d$/.test(m.id) && m.lessons.length === 1 && m.lessons[0].title === "Introduction" && m.lessons[0].body === "Contenu à rédiger." && !m.lessons[0].published);

export async function loadCourse() {
  const c = await meta().get("course", { type: "json" });
  if (!c) return structuredClone(DEFAULT_COURSE);
  if (untouchedV1(c)) return { ...structuredClone(DEFAULT_COURSE), groupUrl: c.groupUrl || "" };
  return c;
}
export async function saveCourse(c) { await meta().setJSON("course", c); }
export async function loadLearners() { return (await meta().get("learners", { type: "json" })) || []; }
export async function saveLearners(l) { await meta().setJSON("learners", l); }

export function newCode() {
  const abc = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  const bytes = crypto.getRandomValues(new Uint8Array(8));
  const s = [...bytes].map(b => abc[b % abc.length]).join("");
  return `ARIA-${s.slice(0, 4)}-${s.slice(4)}`;
}
export const normCode = c => String(c || "").toUpperCase().replace(/[^A-Z0-9]/g, "");

// Retrouve un élève valide à partir de son e-mail et de son code
export async function findLearner(email, code) {
  const learners = await loadLearners();
  const l = learners.find(x => x.email.toLowerCase() === String(email || "").trim().toLowerCase() && normCode(x.code) === normCode(code));
  if (!l) return { error: "E-mail ou code d'accès incorrect.", status: 401 };
  if (!l.active) return { error: "Ton accès est suspendu. Contacte Maison Aria.", status: 403 };
  if (l.expires && new Date(l.expires + "T23:59:59") < new Date()) return { error: "Ton accès a expiré. Contacte Maison Aria pour le prolonger.", status: 403 };
  return { learner: l, learners };
}
