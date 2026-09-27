import { files, findLearner } from "../lib/galeries.mjs";

// Téléchargement d'une ressource de cours, réservé aux élèves : POST { email, code, id }
export default async req => {
  if (req.method !== "POST") return new Response("Méthode non autorisée", { status: 405 });
  const body = await req.json().catch(() => ({}));
  const r = await findLearner(body.email, body.code);
  if (r.error) return new Response(r.error, { status: r.status });
  if (!/^[a-z0-9-]+$/.test(body.id || "")) return new Response("Introuvable", { status: 404 });
  const f = await files().getWithMetadata(body.id, { type: "arrayBuffer" });
  if (!f) return new Response("Introuvable", { status: 404 });
  return new Response(f.data, { headers: { "Content-Type": f.metadata?.type || "application/octet-stream", "Cache-Control": "no-store" } });
};
export const config = { path: "/api/course-file" };
