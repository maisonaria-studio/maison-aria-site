# Site Maison Aria

- `public/index.html` : le site
- `public/admin/index.html` : l'espace dédié aux galeries (adresse : ton-domaine.fr/admin)
- `netlify/functions/` : le petit serveur qui stocke les événements et les photos filigranées (Netlify Blobs)

## Réglages Netlify
- Variable d'environnement `ADMIN_PASSWORD` : mot de passe de l'espace dédié.
- Forms : activer la détection des formulaires et les notifications par e-mail (formulaires « contact » et « commande »).
