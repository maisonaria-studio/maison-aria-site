import { json, loadCourse, findLearner, saveLearners } from "../lib/galeries.mjs";

// Espace élève : POST { email, code, done? } → contenu publié du cours + progression
export default async req => {
  if (req.method !== "POST") return json({ error: "Méthode non autorisée" }, 405);
  const body = await req.json().catch(() => ({}));
  const r = await findLearner(body.email, body.code);
  if (r.error) return json({ error: r.error }, r.status);
  const l = r.learner;
  if (Array.isArray(body.done)) l.done = [...new Set(body.done.map(String))].slice(0, 500);
  l.lastSeen = new Date().toISOString();
  await saveLearners(r.learners);
  const c = await loadCourse();
  const modules = c.modules
    .map(m => ({ id: m.id, title: m.title, lessons: m.lessons.filter(x => x.published).map(({ id, title, video, body, resources }) => ({ id, title, video, body, resources })) }))
    .filter(m => m.lessons.length);
  return json({ learner: { name: l.name, expires: l.expires, done: l.done || [] }, course: { title: c.title, intro: c.intro, groupUrl: c.groupUrl, modules } });
};
export const config = { path: "/api/course" };
