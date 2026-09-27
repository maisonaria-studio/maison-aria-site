import { loadEvents, saveEvents, photos, json, isAdmin, slug, files, loadCourse, saveCourse, loadLearners, saveLearners, newCode } from "../lib/galeries.mjs";

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

  // Envoi d'une ressource de cours (PDF, image…) : corps = fichier brut
  if (url.searchParams.get("action") === "uploadFile") {
    const buf = await req.arrayBuffer();
    if (!buf.byteLength || buf.byteLength > 5_500_000) return json({ error: "Fichier vide ou trop lourd (5 Mo maximum)" }, 400);
    const name = (url.searchParams.get("name") || "fichier").slice(0, 120);
    const id = `f-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
    await files().set(id, buf, { metadata: { name, type: req.headers.get("content-type") || "application/octet-stream" } });
    return json({ ok: true, file: { id, name, size: buf.byteLength } });
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

    // ----- Formation -----
    case "listLearners":
      return json({ learners: await loadLearners() });

    case "saveLearner": {
      const learners = await loadLearners();
      const e = body.learner || {};
      if (!e.email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(e.email)) return json({ error: "Adresse e-mail invalide" }, 400);
      let l = e.code && learners.find(x => x.code === e.code);
      if (!l) {
        if (learners.some(x => x.email.toLowerCase() === e.email.toLowerCase())) return json({ error: "Cet e-mail a déjà un accès" }, 400);
        l = { code: newCode(), created: new Date().toISOString().slice(0, 10), done: [], active: true };
        learners.push(l);
      }
      Object.assign(l, {
        name: String(e.name || "").slice(0, 120),
        email: String(e.email).trim().toLowerCase().slice(0, 160),
        expires: String(e.expires || "").slice(0, 10),
        active: e.active !== false,
        note: String(e.note || "").slice(0, 300)
      });
      await saveLearners(learners);
      return json({ ok: true, learner: l });
    }

    case "deleteLearner": {
      await saveLearners((await loadLearners()).filter(x => x.code !== body.code));
      return json({ ok: true });
    }

    case "getCourse":
      return json({ course: await loadCourse() });

    case "saveCourse": {
      const c = body.course;
      if (!c || !Array.isArray(c.modules)) return json({ error: "Cours invalide" }, 400);
      await saveCourse(c);
      return json({ ok: true });
    }

    case "deleteFile":
      await files().delete(String(body.id || ""));
      return json({ ok: true });

    default:
      return json({ error: "Action inconnue" }, 400);
  }
};
export const config = { path: "/api/admin" };
