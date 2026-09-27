import { loadEvents, saveEvents, photos, json, isAdmin, slug } from "../lib/galeries.mjs";

// Actions de l'espace dédié (protégées par ADMIN_PASSWORD)
export default async req => {
  if (req.method !== "POST") return json({ error: "Méthode non autorisée" }, 405);
  if (!isAdmin(req)) return json({ error: "Mot de passe incorrect" }, 401);
  const url = new URL(req.url);

  // Envoi d'une photo : corps = image JPEG déjà filigranée par le navigateur
  if (url.searchParams.get("action") === "upload") {
    const id = url.searchParams.get("event");
    const events = await loadEvents();
    const ev = events.find(e => e.id === id);
    if (!ev) return json({ error: "Événement introuvable" }, 404);
    const buf = await req.arrayBuffer();
    if (!buf.byteLength || buf.byteLength > 5_000_000) return json({ error: "Fichier vide ou trop lourd" }, 400);
    const n = (ev.next || 1);
    await photos().set(`${ev.id}/${n}`, buf);
    ev.next = n + 1;
    ev.photos.push(n);
    if (!ev.cover) ev.cover = n;
    await saveEvents(events);
    return json({ ok: true, n });
  }

  const body = await req.json().catch(() => ({}));
  const events = await loadEvents();

  switch (body.action) {
    case "login":
    case "list":
      return json({ events });

    case "saveEvent": {
      const e = body.event || {};
      if (!e.title) return json({ error: "Le titre est obligatoire" }, 400);
      let ev = e.id && events.find(x => x.id === e.id);
      if (!ev) {
        let id = slug(e.title) || "evenement", k = 2;
        while (events.some(x => x.id === id)) id = `${slug(e.title)}-${k++}`;
        ev = { id, photos: [], next: 1, cover: null, hidden: false };
        events.push(ev);
      }
      Object.assign(ev, {
        title: String(e.title).slice(0, 120),
        lieu: String(e.lieu || "").slice(0, 120),
        date: String(e.date || "").slice(0, 10),
        code: String(e.code || "").toUpperCase().replace(/[^A-Z0-9]/g, "").slice(0, 6) || "MA",
        hidden: !!e.hidden
      });
      await saveEvents(events);
      return json({ ok: true, event: ev });
    }

    case "deleteEvent": {
      const ev = events.find(x => x.id === body.id);
      if (!ev) return json({ error: "Événement introuvable" }, 404);
      await Promise.all(ev.photos.map(n => photos().delete(`${ev.id}/${n}`)));
      await saveEvents(events.filter(x => x.id !== ev.id));
      return json({ ok: true });
    }

    case "deletePhoto": {
      const ev = events.find(x => x.id === body.id);
      if (!ev) return json({ error: "Événement introuvable" }, 404);
      const n = Number(body.n);
      await photos().delete(`${ev.id}/${n}`);
      ev.photos = ev.photos.filter(p => p !== n);
      if (ev.cover === n) ev.cover = ev.photos[0] || null;
      await saveEvents(events);
      return json({ ok: true });
    }

    case "setCover": {
      const ev = events.find(x => x.id === body.id);
      if (!ev) return json({ error: "Événement introuvable" }, 404);
      ev.cover = Number(body.n);
      await saveEvents(events);
      return json({ ok: true });
    }

    default:
      return json({ error: "Action inconnue" }, 400);
  }
};
export const config = { path: "/api/admin" };
