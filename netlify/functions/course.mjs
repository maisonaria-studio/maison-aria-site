import { json, loadCourse, findLearner, saveLearners } from "../lib/galeries.mjs";
import { QUIZZES, FINAL, QUIZ_PASS, FINAL_PASS, publicQuiz, grade } from "../lib/academy-quiz.mjs";

const newId = () => "AA-" + Array.from(crypto.getRandomValues(new Uint8Array(5)), b => "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"[b % 32]).join("");

// Espace élève : POST { email, code, done? } → contenu publié du cours + progression
// POST { …, action: "quiz", module: "a1" | "final", answers: [index…] } → correction
// POST { …, action: "certificate" } → attestation si toutes les conditions sont remplies
export default async req => {
  if (req.method !== "POST") return json({ error: "Méthode non autorisée" }, 405);
  const body = await req.json().catch(() => ({}));
  const r = await findLearner(body.email, body.code);
  if (r.error) return json({ error: r.error }, r.status);
  const l = r.learner;
  l.quiz = l.quiz || {};
  const c = await loadCourse();
  const modules = c.modules
    .map(m => ({ id: m.id, title: m.title, lessons: m.lessons.filter(x => x.published).map(({ id, title, video, body, resources }) => ({ id, title, video, body, resources })) }))
    .filter(m => m.lessons.length);

  if (body.action === "quiz") {
    const key = String(body.module || "");
    const list = key === "final" ? FINAL : QUIZZES[key];
    if (!list) return json({ error: "Quiz introuvable" }, 404);
    const { score, res } = grade(list, body.answers);
    const pass = key === "final" ? FINAL_PASS : QUIZ_PASS;
    const prev = l.quiz[key] || {};
    l.quiz[key] = { best: Math.max(prev.best || 0, score), last: score, tries: (prev.tries || 0) + 1, passed: !!prev.passed || score >= pass, at: new Date().toISOString() };
    l.lastSeen = new Date().toISOString();
    await saveLearners(r.learners);
    return json({ score, pass, passed: score >= pass, res, quiz: l.quiz });
  }

  if (body.action === "certificate") {
    const done = new Set(l.done || []);
    const missingLessons = modules.flatMap(m => m.lessons).filter(x => !done.has(x.id)).length;
    const missingQuiz = modules.filter(m => QUIZZES[m.id] && !l.quiz[m.id]?.passed).map(m => m.title);
    const finalOk = !!l.quiz.final?.passed;
    if (missingLessons || missingQuiz.length || !finalOk) return json({ error: "Conditions non remplies", missingLessons, missingQuiz, finalOk }, 400);
    if (!l.certificate) {
      const scores = modules.filter(m => QUIZZES[m.id]).map(m => l.quiz[m.id]?.best || 0);
      l.certificate = { id: newId(), date: new Date().toISOString().slice(0, 10), name: l.name, average: Math.round((scores.reduce((a, b) => a + b, 0) + (l.quiz.final.best || 0)) / (scores.length + 1)) };
      await saveLearners(r.learners);
    }
    return json({ certificate: l.certificate });
  }

  if (Array.isArray(body.done)) l.done = [...new Set(body.done.map(String))].slice(0, 500);
  l.lastSeen = new Date().toISOString();
  await saveLearners(r.learners);
  const quizzes = Object.fromEntries(modules.filter(m => QUIZZES[m.id]).map(m => [m.id, publicQuiz(QUIZZES[m.id])]));
  return json({
    learner: { name: l.name, expires: l.expires, done: l.done || [], quiz: l.quiz, certificate: l.certificate || null },
    course: { title: c.title, intro: c.intro, groupUrl: c.groupUrl, modules, quizzes, final: publicQuiz(FINAL), pass: { quiz: QUIZ_PASS, final: FINAL_PASS } },
  });
};
export const config = { path: "/api/course" };
