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

export const DEFAULT_COURSE = {
  title: "Aria Academy",
  intro: "Bienvenue dans Aria Academy ! Avance à ton rythme, module par module. Marque chaque leçon comme terminée pour suivre ta progression.",
  groupUrl: "",
  modules: [
    ["m1", "Les fondamentaux de l'IA"],
    ["m2", "Prendre en main ChatGPT"],
    ["m3", "Rédiger de bons prompts"],
    ["m4", "Recherche et synthèse"],
    ["m5", "Créer des contenus avec l'IA"],
    ["m6", "Organisation et productivité"],
    ["m7", "Introduction à l'automatisation"],
    ["m8", "Cas pratiques et exercices"]
  ].map(([id, title]) => ({ id, title, lessons: [{ id: id + "l1", title: "Introduction", video: "", body: "Contenu à rédiger.", resources: [], published: false }] }))
};

export async function loadCourse() {
  return (await meta().get("course", { type: "json" })) || structuredClone(DEFAULT_COURSE);
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
