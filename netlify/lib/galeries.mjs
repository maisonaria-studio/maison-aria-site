import { getStore } from "@netlify/blobs";
import { MODULE_1 } from "./academy-m1.mjs";
import { MODULE_2 } from "./academy-m2.mjs";
import { MODULE_3 } from "./academy-m3.mjs";
import { MODULE_4 } from "./academy-m4.mjs";
import { MODULE_5 } from "./academy-m5.mjs";
import { MODULE_6 } from "./academy-m6.mjs";
import { MODULE_7 } from "./academy-m7.mjs";
import { MODULE_8 } from "./academy-m8.mjs";
import { MODULE_9 } from "./academy-m9.mjs";

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
export const DEFAULT_COURSE = {
  version: 2,
  title: "Aria Academy",
  intro: "Bienvenue dans Aria Academy ! Ici, tu vas identifier les tâches répétitives de ton entreprise, les transformer en processus clairs, puis les automatiser grâce à l'IA, sans coder. Objectif : au moins un processus qui tourne tout seul à la fin de la formation. Une leçon, une action : fais l'exercice de chaque leçon avant de passer à la suivante, et marque-la comme terminée pour suivre ta progression.",
  groupUrl: "https://discord.gg/6TwQaem8M",
  modules: [
    MODULE_1,
    MODULE_2, MODULE_3, MODULE_4, MODULE_5, MODULE_6, MODULE_7, MODULE_8, MODULE_9
  ]
};

// Ancien programme jamais modifié : remplacé automatiquement par le nouveau
const untouchedV1 = c => !c.version && c.modules?.length === 8 && c.modules.every(m => /^m\d$/.test(m.id) && m.lessons.length === 1 && m.lessons[0].title === "Introduction" && m.lessons[0].body === "Contenu à rédiger." && !m.lessons[0].published);

// Contenus rédigés livrés par mise à jour du site : chaque patch est appliqué une seule fois au programme enregistré.
// Ensuite, tout se modifie normalement depuis l'espace dédié (le numéro contentPatch est conservé à l'enregistrement).
function replaceModule(c, mod) {
  const m = structuredClone(mod), i = c.modules.findIndex(x => x.id === m.id);
  if (i >= 0) {
    // On garde une vidéo déjà renseignée depuis l'espace dédié
    for (const l of m.lessons) { const old = c.modules[i].lessons.find(x => x.id === l.id); if (old?.video) l.video = old.video; }
    c.modules[i] = m;
  } else {
    const after = c.modules.findIndex(x => x.id > m.id);
    after < 0 ? c.modules.push(m) : c.modules.splice(after, 0, m);
  }
}
function setVideos(c, map) {
  for (const m of c.modules) for (const l of m.lessons) if (map[l.id] && !l.video) l.video = map[l.id];
}
// Remplace une vidéo muette par sa version avec voix off (seulement si le lien n'a pas été modifié à la main)
function swapVideos(c, map) {
  for (const m of c.modules) for (const l of m.lessons) if (map[l.id] && (!l.video || l.video === map[l.id][0])) l.video = map[l.id][1];
}
const PATCHES = [
  [1, c => { replaceModule(c, MODULE_1); c.intro = DEFAULT_COURSE.intro; }],
  [2, c => setVideos(c, Object.fromEntries(MODULE_1.lessons.map(l => [l.id, l.video])))],
  [3, c => [MODULE_2, MODULE_3, MODULE_4, MODULE_5, MODULE_6, MODULE_7, MODULE_8, MODULE_9].forEach(m => replaceModule(c, m))],
  [4, c => setVideos(c, Object.fromEntries([MODULE_2, MODULE_3, MODULE_4, MODULE_5, MODULE_6, MODULE_7, MODULE_8, MODULE_9].flatMap(m => m.lessons.map(l => [l.id, l.video]))))],
  [5, c => swapVideos(c, { a1l0: ["https://youtu.be/a4Hi01-mDd8", "https://youtu.be/pSF4MpnOnvA"] })],
  [6, c => swapVideos(c, { a1l0: ["https://youtu.be/pSF4MpnOnvA", "https://youtu.be/jPlo5x-L4Zw"] })],
  [7, c => swapVideos(c, { a1l1: ["https://youtu.be/3FuFhbJkNSg", "https://youtu.be/lCH0m43GXkc"], a1l2: ["https://youtu.be/mnRO-VcgFz4", "https://youtu.be/g_wzvHAqoqw"], a1l3: ["https://youtu.be/rH_jsPnpUsI", "https://youtu.be/pJT3cSiGCp8"], a2l1: ["https://youtu.be/N7bdHqCMJEY", "https://youtu.be/JuAb7ypkE5s"], a2l2: ["https://youtu.be/Nzn0WPWroBI", "https://youtu.be/shhtvrdp9MM"], a2l3: ["https://youtu.be/ZvJt-r9TtZk", "https://youtu.be/XLIQJILNin8"], a3l1: ["https://youtu.be/k5wwzxNDGWk", "https://youtu.be/j7lxZ2hlico"] })],
  [8, c => swapVideos(c, { a3l2: ["https://youtu.be/Hm2v1bAXkRA", "https://youtu.be/C-TGFKYpWOE"], a3l3: ["https://youtu.be/1C1uaExyEcE", "https://youtu.be/kroH_xDbxxA"], a4l1: ["https://youtu.be/raKDvJmMaOA", "https://youtu.be/NhFGi7jKgAs"], a4l2: ["https://youtu.be/gumvg04NpdY", "https://youtu.be/Je0ZnDJCy3s"], a4l3: ["https://youtu.be/Ad23bcGZxIA", "https://youtu.be/HSkETcCZIj4"], a5l1: ["https://youtu.be/7qucy56SLuo", "https://youtu.be/e58UwF9PUDM"] })],
  [9, c => swapVideos(c, { a5l2: ["https://youtu.be/ffDGsveMql0", "https://youtu.be/Kd_zoeV-7yU"], a5l3: ["https://youtu.be/7YcYKpLWUec", "https://youtu.be/8YgPFIlCdEw"], a6l1: ["https://youtu.be/GWzv_vP1ntw", "https://youtu.be/aiT3U06BGkI"], a6l2: ["https://youtu.be/YM0Soz0hpuA", "https://youtu.be/v9RwiB9cXJ4"], a6l3: ["https://youtu.be/flfR2xb4cPQ", "https://youtu.be/xs13nT8oMsg"] })],
  [10, c => swapVideos(c, { a7l1: ["https://youtu.be/b1FD4oTv9HE", "https://youtu.be/_yWMeqUl22k"], a7l2: ["https://youtu.be/dgKcq1pExi4", "https://youtu.be/eT5ekplaQW4"], a7l3: ["https://youtu.be/a6Dq1m9OUdo", "https://youtu.be/c_dfp3kZxr4"], a8l1: ["https://youtu.be/byD26146J10", "https://youtu.be/G_0zLn6RrpM"], a8l2: ["https://youtu.be/eW6-XJp9ncQ", "https://youtu.be/wiKYHnOP79Q"], a8l3: ["https://youtu.be/_SkhChSv8Y0", "https://youtu.be/eCv84qUtyB4"] })],
  [11, c => swapVideos(c, { a9l1: ["https://youtu.be/cKaFazcdjyo", "https://youtu.be/3Dm61Zm_hf4"], a9l2: ["https://youtu.be/YesYTXZeMOM", "https://youtu.be/zCW2Kqj-TsE"], a9l3: ["https://youtu.be/075jIuPdHz4", "https://youtu.be/UHnRRN_ONbw"] })],
];
function applyPatches(c) {
  const todo = PATCHES.filter(([v]) => v > (c.contentPatch || 0));
  todo.forEach(([v, fn]) => { fn(c); c.contentPatch = v; });
  return todo.length > 0;
}

export async function loadCourse() {
  let c = await meta().get("course", { type: "json" });
  if (!c) c = structuredClone(DEFAULT_COURSE);
  else if (untouchedV1(c)) c = { ...structuredClone(DEFAULT_COURSE), groupUrl: c.groupUrl || DEFAULT_COURSE.groupUrl };
  if (!c.groupUrl) c.groupUrl = DEFAULT_COURSE.groupUrl;
  if (applyPatches(c)) await saveCourse(c);
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
