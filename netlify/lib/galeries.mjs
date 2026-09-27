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
