import { loadEvents, json } from "../lib/galeries.mjs";

// Liste publique des galeries visibles
export default async () => {
  const events = (await loadEvents()).filter(e => !e.hidden && e.photos.length);
  events.sort((a, b) => (b.date || "").localeCompare(a.date || ""));
  return json(events.map(({ id, code, title, lieu, date, cover, photos }) => ({ id, code, title, lieu, date, cover, photos })));
};
export const config = { path: "/api/events" };
