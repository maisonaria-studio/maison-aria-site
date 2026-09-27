import { photos } from "../lib/galeries.mjs";

// Sert une photo filigranée : /api/photo/<evenement>/<numero>
export default async (req, context) => {
  const { event, n } = context.params;
  if (!/^[a-z0-9-]+$/.test(event) || !/^\d+$/.test(n)) return new Response("Introuvable", { status: 404 });
  const data = await photos().get(`${event}/${n}`, { type: "arrayBuffer" });
  if (!data) return new Response("Introuvable", { status: 404 });
  return new Response(data, { headers: { "Content-Type": "image/jpeg", "Cache-Control": "public, max-age=604800" } });
};
export const config = { path: "/api/photo/:event/:n" };
