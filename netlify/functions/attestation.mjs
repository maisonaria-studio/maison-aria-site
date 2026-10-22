import { json, loadLearners } from "../lib/galeries.mjs";

// Vérification publique d'une attestation : GET /api/attestation?id=AA-XXXXX
export default async req => {
  const id = new URL(req.url).searchParams.get("id") || "";
  if (!/^AA-[A-Z0-9]{5}$/.test(id)) return json({ valid: false }, 400);
  const l = (await loadLearners()).find(x => x.certificate?.id === id);
  if (!l) return json({ valid: false }, 404);
  return json({ valid: true, name: l.certificate.name, date: l.certificate.date, course: "Aria Academy · Automatiser et processiser son entreprise avec l'IA" });
};
export const config = { path: "/api/attestation" };
