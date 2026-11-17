# Guides ajoutés en novembre 2026.
# cat : "ia" (intelligence artificielle & automatisation) ou "com" (communication & contenus)
# related : slugs des guides proposés en « À lire aussi »

GUIDES2 = {
"chatgpt-entreprise-usages-concrets": dict(
 cat="ia", date="2026-11-17",
 title="ChatGPT en entreprise : 20 usages concrets pour TPE et PME",
 h1="ChatGPT en entreprise : 20 usages concrets pour gagner du temps",
 meta="20 usages concrets de ChatGPT, Claude ou Mistral pour une TPE ou PME : exemples de demandes à copier, limites à connaître et précautions pour vos données.",
 lead="Beaucoup de dirigeants ont ouvert ChatGPT une fois, posé une question, obtenu une réponse banale… et refermé l'onglet. Pourtant, bien utilisé, un assistant IA fait gagner du temps chaque jour sur des tâches très concrètes. Voici 20 usages éprouvés dans les petites entreprises, avec des exemples de demandes à copier.",
 body="""
<h2>Trois règles avant de commencer</h2>
<ol>
<li><b>Vous restez le pilote.</b> L'IA produit un brouillon ; vous relisez, corrigez et validez avant tout envoi.</li>
<li><b>Pas de données sensibles</b> dans un outil grand public : pas de coordonnées complètes de clients, de données bancaires ou de santé. Remplacez les noms par [CLIENT] ou [SALARIÉ]. Voir notre guide <a href="/guides/ia-rgpd-entreprise/">IA et RGPD</a>.</li>
<li><b>Donnez du contexte.</b> Plus vous expliquez qui vous êtes, à qui vous vous adressez et ce que vous attendez, meilleure est la réponse. C'est tout l'objet de notre guide <a href="/guides/comment-ecrire-un-bon-prompt/">Comment écrire un bon prompt</a>.</li>
</ol>
<p>Ces usages fonctionnent avec ChatGPT, mais aussi avec Claude, Le Chat de Mistral, Gemini ou Copilot : le principe est le même.</p>

<h2>Relation client</h2>
<ol>
<li><b>Répondre aux avis Google</b>, positifs comme négatifs, avec un ton juste. <i>« Voici un avis client sur mon restaurant. Propose une réponse courte, chaleureuse, qui remercie sans être servile et qui répond calmement à la critique sur l'attente. »</i></li>
<li><b>Préparer les réponses aux questions fréquentes</b> (horaires, tarifs, délais) et les enregistrer comme modèles dans votre messagerie.</li>
<li><b>Désamorcer un message délicat</b> : retard, refus, erreur de facturation. <i>« Reformule ce message pour qu'il soit ferme mais bienveillant. »</i></li>
<li><b>Traduire</b> une réponse ou une page de présentation pour une clientèle étrangère, puis faire relire les points importants.</li>
<li><b>Rédiger une FAQ</b> pour votre site à partir des questions que vous recevez le plus souvent.</li>
</ol>

<h2>Commercial</h2>
<ol start="6">
<li><b>Transformer des notes de rendez-vous en devis structuré</b> : <i>« Voici mes notes en vrac. Organise-les en lignes de devis claires, sans inventer de prix. »</i></li>
<li><b>Relancer un devis sans réponse</b>, en trois versions plus ou moins directes.</li>
<li><b>Rédiger une proposition commerciale</b> à partir d'un brief et de vos offres.</li>
<li><b>Préparer un rendez-vous</b> : liste des questions à poser à un prospect selon son secteur.</li>
</ol>

<h2>Communication</h2>
<ol start="10">
<li><b>Trouver des idées de publications</b> à partir de votre calendrier (saison, événements, nouveautés). Notre guide <a href="/guides/idees-reels-restaurant-commerce/">15 idées de Réels</a> donne aussi des pistes.</li>
<li><b>Écrire des légendes Instagram</b> dans votre ton, en lui donnant trois exemples de vos anciennes publications.</li>
<li><b>Écrire le script d'un Réel</b> : accroche des trois premières secondes, déroulé, texte à l'écran.</li>
<li><b>Préparer une newsletter</b> à partir de vos actualités du mois.</li>
</ol>

<h2>Organisation et administratif</h2>
<ol start="14">
<li><b>Faire un compte rendu</b> à partir de notes ou d'une transcription de réunion : décisions, actions, responsables, échéances.</li>
<li><b>Écrire une procédure</b> pour qu'un collaborateur puisse réaliser une tâche sans vous. <i>« Pose-moi des questions sur cette tâche, puis rédige une fiche procédure étape par étape. »</i></li>
<li><b>Construire un planning</b> (équipe, production, publication) à partir de contraintes données.</li>
<li><b>Écrire une formule de tableur</b> : <i>« Dans Excel, je veux additionner la colonne C seulement quand la colonne B contient “payé”. »</i></li>
</ol>

<h2>Analyse et réflexion</h2>
<ol start="18">
<li><b>Résumer un document long</b> (conditions générales, cahier des charges, compte rendu) et lister les points d'attention. Pour un contrat, la lecture d'un professionnel reste indispensable.</li>
<li><b>Comparer des offres fournisseurs</b> à partir de leurs caractéristiques, dans un tableau.</li>
<li><b>Réfléchir à voix haute</b> : nom d'une nouvelle offre, prix, objections possibles. L'IA est un excellent partenaire de brainstorming, à condition de garder l'esprit critique.</li>
</ol>

<h2>Ce que l'IA fait mal (et comment s'en protéger)</h2>
<ul>
<li><b>Elle peut inventer</b> des chiffres, des sources ou des références avec beaucoup d'assurance : vérifiez tout ce qui est factuel.</li>
<li><b>Elle ne connaît pas forcément l'actualité</b> ni vos tarifs : donnez-lui les informations, ne les lui demandez pas.</li>
<li><b>Ses textes peuvent sonner génériques</b> : fournissez des exemples de votre style et demandez plusieurs versions.</li>
</ul>

<h2>Passer à la vitesse supérieure : automatiser</h2>
<p>Ces usages font gagner du temps à chaque fois que vous ouvrez l'outil. L'étape suivante consiste à relier l'IA à vos outils pour que certaines tâches se fassent <b>sans vous</b> : une demande de devis qui arrive dans un tableau, un brouillon de réponse préparé automatiquement, un récapitulatif hebdomadaire envoyé chaque lundi. C'est ce que détaille notre guide <a href="/guides/automatiser-son-entreprise-avec-l-ia/">Automatiser son entreprise avec l'IA sans coder</a>, et notre comparatif <a href="/guides/zapier-make-n8n-comparatif/">Zapier, Make ou n8n</a>.</p>
<p>Pour apprendre la méthode pas à pas, <a href="/aria-academy/">Aria Academy</a> propose une formation en ligne en 9 modules : panorama des assistants IA, méthode pour écrire des prompts efficaces, bibliothèque de prompts métier, puis automatisations sans code. Elle est accessible dès 390 €.</p>
""",
 faq=[("ChatGPT gratuit suffit-il pour une entreprise ?","Pour découvrir et pour des usages ponctuels, la version gratuite suffit souvent. Pour un usage quotidien en équipe, les offres professionnelles apportent plus de capacité et de meilleures garanties sur les données."),
      ("Quel assistant IA choisir : ChatGPT, Claude, Mistral ou Gemini ?","Ils se valent sur la plupart des usages courants. Le meilleur choix dépend de vos outils (Google, Microsoft), de vos exigences sur les données et de votre préférence de style. L'essentiel est d'apprendre à bien formuler ses demandes."),
      ("Peut-on mettre des informations clients dans ChatGPT ?","Évitez d'y mettre des données personnelles identifiantes dans un outil grand public. Anonymisez les informations et privilégiez une offre professionnelle si vous traitez des données clients.")],
 related=["comment-ecrire-un-bon-prompt", "ia-rgpd-entreprise", "automatiser-son-entreprise-avec-l-ia"]),

"comment-ecrire-un-bon-prompt": dict(
 cat="ia", date="2026-11-17",
 title="Comment écrire un bon prompt : méthode et exemples",
 h1="Comment écrire un bon prompt : la méthode en 6 éléments, avec exemples",
 meta="Écrire un bon prompt pour ChatGPT ou Claude : la méthode en 6 éléments, des exemples avant/après et des modèles prêts à l'emploi pour les pros.",
 lead="Si les réponses de l'IA vous paraissent fades ou à côté de la plaque, le problème vient rarement de l'outil : il vient de la demande. Un bon prompt, c'est un brief clair, comme celui que vous donneriez à un nouveau collaborateur. Voici une méthode simple en six éléments, des exemples concrets et des modèles à réutiliser.",
 body="""
<h2>Pourquoi les réponses sont souvent génériques</h2>
<p>Quand on écrit « écris un post sur mon restaurant », l'IA ne sait ni où vous êtes, ni qui sont vos clients, ni quel ton vous employez, ni où le texte sera publié. Elle comble donc les trous avec la réponse la plus probable… c'est-à-dire la plus banale. Plus vous lui donnez d'éléments, plus la réponse vous ressemble.</p>

<h2>La méthode en 6 éléments</h2>
<ol>
<li><b>Le rôle</b> : qui doit répondre ? <i>« Tu es community manager pour des restaurants de bord de mer. »</i></li>
<li><b>Le contexte</b> : votre activité, votre cible, la situation. <i>« Mon restaurant est à Sainte-Maxime, clientèle familiale et touristique, on rouvre le 1er avril. »</i></li>
<li><b>La tâche</b> : ce que vous voulez précisément, avec un verbe d'action. <i>« Rédige la légende Instagram annonçant la réouverture. »</i></li>
<li><b>Le format</b> : longueur, structure, support. <i>« 80 mots maximum, une accroche sur la première ligne, 3 emojis, 5 hashtags locaux. »</i></li>
<li><b>Les exemples</b> : un ou deux textes que vous aimez, pour caler le ton.</li>
<li><b>Les contraintes</b> : ce qu'il ne faut pas faire. <i>« Pas de superlatifs, pas de “incontournable”, tutoiement interdit. »</i></li>
</ol>
<p>Pas besoin de tout mettre à chaque fois : pour une tâche simple, contexte + tâche + format suffisent souvent. Mais plus l'enjeu est important, plus le brief doit être complet.</p>

<h2>Exemple avant / après</h2>
<p><b>Avant :</b> <i>« Écris une relance pour un devis. »</i> Résultat : un texte passe-partout, trop formel, qui ne mentionne rien de précis.</p>
<p><b>Après :</b> <i>« Tu es l'assistante d'une photographe indépendante. J'ai envoyé il y a 10 jours un devis de 390 € pour une demi-journée de shooting à un hôtel de Grimaud, sans réponse. Rédige un e-mail de relance de 5 lignes maximum, cordial et direct, qui rappelle la date proposée et propose un court appel. Pas de formule du type “je me permets de revenir vers vous”. Donne-moi 3 versions : douce, neutre, plus directe. »</i></p>
<p>Le second prompt prend 30 secondes de plus à écrire et fait gagner dix minutes de corrections.</p>

<h2>Trois réflexes qui changent tout</h2>
<ul>
<li><b>Demandez-lui de vous poser des questions</b> avant de répondre : <i>« Avant de rédiger, pose-moi les questions dont tu as besoin. »</i> L'IA identifie elle-même les informations manquantes.</li>
<li><b>Itérez</b> au lieu de tout recommencer : « plus court », « plus chaleureux », « supprime la deuxième phrase », « garde la version 2 mais avec l'accroche de la 3 ».</li>
<li><b>Demandez plusieurs versions</b> : il est plus facile de choisir et d'assembler que de corriger un texte unique.</li>
</ul>

<h2>Les 5 erreurs les plus fréquentes</h2>
<ol>
<li>Une demande trop vague (« fais-moi un truc sur… »).</li>
<li>Plusieurs tâches mélangées dans un seul message : découpez en étapes.</li>
<li>Croire l'IA sur parole pour les chiffres, les dates ou les règles juridiques.</li>
<li>Recommencer de zéro à chaque fois au lieu de garder ses meilleurs prompts.</li>
<li>Coller des données personnelles de clients dans un outil grand public (voir <a href="/guides/ia-rgpd-entreprise/">IA et RGPD</a>).</li>
</ol>

<h2>Créez votre bibliothèque de prompts</h2>
<p>Les tâches qui reviennent chaque semaine méritent un prompt « modèle », avec des cases à remplir entre accolades. Par exemple :</p>
<p><i>« Tu es [RÔLE]. Voici l'avis laissé par un client sur [ÉTABLISSEMENT] : [AVIS]. Rédige une réponse de [LONGUEUR] mots, au ton [TON], qui remercie, répond au point soulevé et invite à revenir. Ne promets aucune remise. »</i></p>
<p>Rangez ces modèles dans un document partagé ou dans les fonctions « projets » et « instructions personnalisées » de votre assistant. En quelques semaines, vous disposez d'une boîte à outils qui fait gagner du temps à toute l'équipe.</p>

<h2>Trois modèles prêts à l'emploi</h2>
<ul>
<li><b>Compte rendu</b> : <i>« Voici mes notes de réunion. Rédige un compte rendu avec : décisions prises, actions (qui, quoi, pour quand), points en suspens. Style télégraphique, une page maximum. »</i></li>
<li><b>Post réseaux sociaux</b> : <i>« Voici 3 de mes anciennes publications [EXEMPLES]. Dans le même ton, écris une publication sur [SUJET] pour [RÉSEAU], avec une accroche forte en première ligne et un appel à l'action à la fin. »</i></li>
<li><b>Procédure</b> : <i>« Je veux déléguer la tâche suivante : [TÂCHE]. Pose-moi des questions une par une jusqu'à pouvoir écrire une procédure que quelqu'un d'autre pourra suivre sans moi. »</i></li>
</ul>
<p>La méthode pour écrire des prompts efficaces et la construction d'une bibliothèque de prompts métier font partie du module 4 d'<a href="/aria-academy/">Aria Academy</a>, la formation en ligne pour utiliser l'IA dans son entreprise sans coder. Pour une équipe, Maison Aria propose aussi des <a href="/prestations/pack-de-prompts-personnalises/">packs de prompts personnalisés</a>.</p>
""",
 faq=[("Qu'est-ce qu'un prompt ?","C'est la consigne que vous donnez à un assistant IA comme ChatGPT, Claude ou Mistral. Sa qualité détermine en grande partie la qualité de la réponse."),
      ("Faut-il écrire des prompts très longs ?","Non : il faut écrire des prompts complets. Pour une tâche simple, deux ou trois phrases avec le contexte, la tâche et le format suffisent."),
      ("Un bon prompt fonctionne-t-il avec tous les assistants IA ?","Oui, la méthode est la même pour ChatGPT, Claude, Gemini, Mistral ou Copilot. Les réponses varient un peu d'un outil à l'autre, d'où l'intérêt de tester et d'itérer.")],
 related=["chatgpt-entreprise-usages-concrets", "automatiser-son-entreprise-avec-l-ia", "zapier-make-n8n-comparatif"]),

"zapier-make-n8n-comparatif": dict(
 cat="ia", date="2026-11-17",
 title="Zapier, Make ou n8n : quel outil d'automatisation choisir ?",
 h1="Zapier, Make ou n8n : quel outil d'automatisation choisir pour une TPE ?",
 meta="Zapier, Make ou n8n : comparatif pour automatiser une TPE sans coder. Fonctionnement, facturation, simplicité, IA et données : lequel choisir ?",
 lead="Zapier, Make et n8n permettent tous les trois de relier vos applications pour que les tâches répétitives se fassent toutes seules. Ils reposent sur le même principe, mais ne s'adressent pas tout à fait aux mêmes besoins. Voici comment les départager sans se perdre dans les détails techniques.",
 body="""
<h2>Le principe commun : un déclencheur, puis des actions</h2>
<p>Une automatisation commence par un <b>déclencheur</b> (un formulaire est rempli, un e-mail arrive, c'est lundi 8 h), suivi d'<b>actions</b> (ajouter une ligne dans un tableau, créer une fiche client, envoyer un message, demander à l'IA de résumer). Les trois outils fonctionnent ainsi ; ce qui change, c'est la façon de construire, le prix et le niveau de contrôle.</p>

<h2>Zapier : le plus simple pour démarrer</h2>
<ul>
<li><b>Pour qui :</b> les dirigeants non techniques qui veulent des automatisations simples, en quelques étapes.</li>
<li><b>Points forts :</b> l'interface la plus accessible, guidée pas à pas, et le plus grand catalogue d'applications compatibles (plusieurs milliers).</li>
<li><b>À savoir :</b> la facturation se fait à la « tâche » (chaque action exécutée). Le coût peut grimper vite si vos automatisations tournent souvent ou comptent beaucoup d'étapes.</li>
</ul>

<h2>Make : le plus visuel pour des scénarios plus riches</h2>
<ul>
<li><b>Pour qui :</b> ceux qui veulent aller plus loin sans coder : conditions, plusieurs branches, traitement de listes.</li>
<li><b>Points forts :</b> un canevas visuel où l'on voit tout le scénario d'un coup d'œil, et un rapport fonctionnalités/prix souvent intéressant pour les volumes moyens.</li>
<li><b>À savoir :</b> chaque module exécuté consomme des « opérations » ; la prise en main demande un peu plus de temps que Zapier.</li>
</ul>

<h2>n8n : le plus puissant et le plus maîtrisé</h2>
<ul>
<li><b>Pour qui :</b> les entreprises qui veulent garder la main sur leurs données, automatiser beaucoup ou construire des agents IA.</li>
<li><b>Points forts :</b> on peut l'installer sur son propre serveur (y compris en Europe), avec un nombre d'exécutions illimité ; la version en ligne est facturée par exécution de workflow, quelle que soit sa longueur. Très complet pour l'IA.</li>
<li><b>À savoir :</b> l'interface est plus technique, et l'auto-hébergement demande un minimum de maintenance (ou un prestataire).</li>
</ul>

<h2>Cinq questions pour choisir</h2>
<ol>
<li><b>Qui va construire et maintenir les automatisations ?</b> Vous seul·e, sans appétence technique : Zapier ou Make. Quelqu'un d'à l'aise avec les outils : n8n devient intéressant.</li>
<li><b>Combien de fois par mois vont-elles tourner ?</b> Quelques dizaines : tous conviennent. Des milliers : comparez attentivement les modèles de facturation.</li>
<li><b>Vos applications sont-elles compatibles ?</b> Vérifiez que vos outils (agenda, CRM, facturation, boîte mail) sont disponibles dans le catalogue.</li>
<li><b>Où doivent être traitées vos données ?</b> Si vous manipulez des données clients sensibles, la possibilité d'héberger n8n en Europe est un vrai argument (voir <a href="/guides/ia-rgpd-entreprise/">IA et RGPD</a>).</li>
<li><b>Quelle place pour l'IA ?</b> Les trois intègrent l'IA ; n8n va le plus loin pour construire des agents qui enchaînent plusieurs décisions.</li>
</ol>
<p>Les offres gratuites et les tarifs évoluent régulièrement : vérifiez-les sur le site de chaque éditeur au moment de choisir.</p>

<h2>Notre conseil : commencez petit</h2>
<p>Le meilleur outil est celui que vous utiliserez vraiment. Choisissez <b>une seule</b> tâche répétitive, construisez-la, laissez-la tourner deux semaines, mesurez le temps gagné, puis passez à la suivante. Et surtout, décrivez d'abord la tâche étape par étape : une automatisation ne fait qu'exécuter un processus clair (c'est la méthode détaillée dans <a href="/guides/automatiser-son-entreprise-avec-l-ia/">Automatiser son entreprise avec l'IA sans coder</a>).</p>
<p>Dans <a href="/aria-academy/">Aria Academy</a>, les ateliers sont réalisés pas à pas dans n8n, avec un tableau de correspondance pour retrouver chaque bouton dans Make et Zapier : vous apprenez la logique, pas un seul logiciel. Si vous préférez déléguer, Maison Aria réalise aussi des <a href="/prestations/automatisation-simple/">automatisations</a> et des <a href="/prestations/workflow-ia/">workflows IA</a> sur mesure.</p>
""",
 faq=[("Quel est l'outil d'automatisation le plus simple ?","Zapier est généralement le plus simple pour un premier pas : interface guidée et très large catalogue d'applications."),
      ("Faut-il savoir coder pour utiliser n8n ?","Non, n8n se construit aussi par blocs visuels. Il est simplement plus technique que Zapier, surtout si vous l'installez sur votre propre serveur."),
      ("Peut-on changer d'outil plus tard ?","Oui. Si vos processus sont bien décrits, reconstruire une automatisation dans un autre outil est rapide : la logique reste la même.")],
 related=["automatiser-son-entreprise-avec-l-ia", "chatgpt-entreprise-usages-concrets", "ia-rgpd-entreprise"]),

"ai-act-formation-ia-obligatoire": dict(
 cat="ia", date="2026-11-17",
 title="AI Act : la formation IA est-elle obligatoire en entreprise ?",
 h1="AI Act : la formation à l'IA est-elle obligatoire pour votre entreprise ?",
 meta="Article 4 de l'AI Act : ce que les entreprises doivent faire pour la maîtrise de l'IA, ce qu'a changé la réforme de 2026 et un plan d'action pour TPE.",
 lead="Depuis février 2025, le règlement européen sur l'intelligence artificielle (AI Act) contient une obligation qui concerne presque toutes les entreprises : la « maîtrise de l'IA » des personnes qui utilisent ces outils. Elle a été réécrite en 2026. Que faut-il retenir, et que faire concrètement quand on est une petite entreprise ?",
 body="""
<h2>Ce que dit l'article 4 de l'AI Act</h2>
<p>L'article 4 du règlement (UE) 2024/1689, applicable depuis le <b>2 février 2025</b>, porte sur la <b>maîtrise de l'IA</b> (« AI literacy ») : les fournisseurs et les utilisateurs professionnels de systèmes d'IA (les « déployeurs ») doivent prendre des mesures pour que leur personnel, et les personnes qui utilisent ces systèmes pour leur compte, comprennent ce qu'ils utilisent : fonctionnement, possibilités, limites et risques.</p>
<p><b>Êtes-vous concerné ?</b> Très probablement : dès que vos salariés ou vous-même utilisez un outil d'IA dans un cadre professionnel (assistant conversationnel, génération d'images, tri automatique de candidatures, chatbot sur votre site…), votre entreprise est « déployeur » au sens du texte. La taille de l'entreprise n'entre pas en ligne de compte.</p>

<h2>Ce qui a changé en 2026</h2>
<p>Dans sa version de 2025, l'article demandait de « garantir un niveau suffisant » de maîtrise de l'IA. La réforme dite « Digital Omnibus » (règlement (UE) 2026/1744, entré en vigueur fin juillet 2026) a réécrit l'article : les entreprises doivent désormais <b>favoriser le développement</b> de la maîtrise de l'IA de leurs équipes, en tenant compte de leurs connaissances, de leur expérience et du contexte d'utilisation. Le texte précise qu'il n'impose pas de garantir un niveau précis pour chaque personne.</p>
<p>Concrètement, on passe d'une logique de résultat à une <b>obligation de moyens</b> : l'obligation n'a pas disparu, mais ce qui compte est de pouvoir montrer que vous avez agi de façon adaptée. Les contrôles relèvent des autorités nationales, et le régime de sanctions applicable à cet article dépend de chaque État membre.</p>

<h2>Le plan d'action en 6 étapes pour une TPE ou PME</h2>
<ol>
<li><b>Faites l'inventaire des usages.</b> Quels outils d'IA sont utilisés, par qui, pour quoi ? N'oubliez pas les usages « cachés » (un salarié qui utilise ChatGPT sur son téléphone).</li>
<li><b>Fixez des règles simples</b> dans une charte d'usage : outils autorisés, données interdites, validation humaine obligatoire avant envoi. Notre guide <a href="/guides/ia-rgpd-entreprise/">IA et RGPD</a> vous aide à la rédiger.</li>
<li><b>Formez de façon adaptée.</b> Un commercial, une assistante administrative et un dirigeant n'ont pas les mêmes besoins. L'essentiel : comprendre comment fonctionne l'IA, savoir l'utiliser efficacement, repérer ses erreurs et protéger les données.</li>
<li><b>Désignez un référent</b>, même informel, à qui poser ses questions et qui suit l'évolution des outils.</li>
<li><b>Gardez des traces</b> : charte, programme suivi, attestations, date des formations. Avec une obligation de moyens, ces preuves sont précieuses.</li>
<li><b>Mettez à jour</b> chaque année ou à chaque nouvel outil important.</li>
</ol>

<h2>Former sans y passer des semaines</h2>
<p>Pour une petite structure, la formation la plus utile est concrète : elle doit faire gagner du temps tout de suite, tout en donnant les bons réflexes de sécurité. C'est l'approche d'<a href="/aria-academy/">Aria Academy</a>, la formation en ligne de Maison Aria : 9 modules à suivre à son rythme, dont une leçon consacrée à l'automatisation en toute sécurité (RGPD, AI Act et bons réflexes), des quiz à la fin de chaque module et une <b>attestation de réussite nominative</b>, vérifiable en ligne, que vous pouvez conserver dans vos traces de formation. Pour une équipe, une <a href="/prestations/formation-personnalisee/">formation personnalisée</a> sur place est aussi possible.</p>
<p><i>Ce guide donne des repères généraux et ne constitue pas un avis juridique. Pour une situation particulière (IA utilisée dans le recrutement, la santé, le crédit…), d'autres obligations de l'AI Act peuvent s'appliquer : faites-vous accompagner par un professionnel du droit.</i></p>
""",
 faq=[("La formation à l'IA est-elle obligatoire pour les salariés ?","L'article 4 de l'AI Act impose aux entreprises qui utilisent l'IA de favoriser la maîtrise de l'IA de leurs équipes. Ce n'est pas une formation précise imposée à chaque salarié, mais une obligation de prendre des mesures adaptées, dont la formation fait naturellement partie."),
      ("Depuis quand cette obligation s'applique-t-elle ?","Depuis le 2 février 2025. Sa rédaction a été modifiée par le règlement (UE) 2026/1744, entré en vigueur fin juillet 2026, qui en fait une obligation de moyens."),
      ("Une entreprise qui utilise seulement ChatGPT est-elle concernée ?","Oui, dès lors que l'outil est utilisé dans un cadre professionnel, l'entreprise est considérée comme utilisatrice (déployeur) d'un système d'IA."),
      ("Comment prouver que l'on a agi ?","En conservant une charte d'usage, le programme des formations suivies, les dates et les attestations. Ces éléments montrent que des mesures adaptées ont été prises.")],
 related=["ia-rgpd-entreprise", "chatgpt-entreprise-usages-concrets", "comment-ecrire-un-bon-prompt"]),

"ia-rgpd-entreprise": dict(
 cat="ia", date="2026-11-17",
 title="IA et RGPD : utiliser ChatGPT en entreprise sans risque",
 h1="IA et RGPD : utiliser ChatGPT en entreprise sans mettre vos données en danger",
 meta="Utiliser ChatGPT en entreprise en respectant le RGPD : données à ne jamais partager, anonymisation, réglages, offres pro et charte IA.",
 lead="Copier-coller un e-mail client dans ChatGPT pour préparer une réponse : le geste est devenu banal. Il n'est pourtant pas anodin si l'e-mail contient des données personnelles. Bonne nouvelle : quelques règles simples suffisent pour profiter de l'IA sans exposer vos clients ni votre entreprise.",
 body="""
<h2>Où sont les risques ?</h2>
<ul>
<li><b>La réutilisation des données</b> : selon les outils et les réglages, les conversations des versions grand public peuvent servir à améliorer les modèles. Les offres destinées aux entreprises excluent généralement cette utilisation, mais il faut le vérifier.</li>
<li><b>Le lieu de traitement</b> : certaines données sont hébergées hors de l'Union européenne, ce qui impose des garanties particulières au titre du RGPD.</li>
<li><b>Les usages invisibles</b> : un salarié qui utilise son compte personnel pour traiter des documents de l'entreprise, sans règle ni contrôle.</li>
<li><b>Les erreurs</b> : une réponse inventée envoyée à un client sans relecture.</li>
</ul>

<h2>La règle du feu tricolore</h2>
<p>Avant de coller un contenu dans un assistant IA, classez-le :</p>
<ul>
<li><b>Vert, sans souci :</b> textes publics, contenus marketing, idées, informations générales sur votre activité, données anonymisées.</li>
<li><b>Orange, avec précaution :</b> documents internes non sensibles, échanges professionnels, à condition de retirer les noms et coordonnées et d'utiliser un compte professionnel.</li>
<li><b>Rouge, jamais dans un outil grand public :</b> données personnelles identifiantes de clients ou de salariés, données de santé, informations bancaires, mots de passe, secrets d'affaires, documents confidentiels.</li>
</ul>

<h2>Anonymiser : le réflexe qui règle 80 % des cas</h2>
<p>L'IA n'a presque jamais besoin de savoir <i>qui</i> est la personne pour vous aider. Remplacez les noms par [CLIENT], les adresses par [ADRESSE], les montants exacts par des ordres de grandeur si possible. La réponse sera tout aussi utile, et vous n'aurez transmis aucune donnée personnelle.</p>

<h2>Choisir et régler ses outils</h2>
<ul>
<li><b>Vérifiez les paramètres de confidentialité</b> de votre compte : la plupart des assistants permettent de refuser que vos conversations servent à l'entraînement.</li>
<li><b>Privilégiez une offre professionnelle</b> dès que l'IA fait partie du quotidien de l'équipe : comptes gérés par l'entreprise, engagements contractuels sur les données, contrat de sous-traitance conforme au RGPD.</li>
<li><b>Regardez où sont traitées les données</b> : certains fournisseurs proposent un hébergement en Europe. Pour les automatisations, un outil comme n8n peut être installé sur un serveur européen (voir notre <a href="/guides/zapier-make-n8n-comparatif/">comparatif Zapier, Make, n8n</a>).</li>
<li><b>Mettez à jour votre registre des traitements</b> si l'IA est utilisée pour traiter des données personnelles, et informez les personnes concernées dans votre politique de confidentialité.</li>
</ul>

<h2>Que mettre dans une charte IA ?</h2>
<p>Une page suffit. Elle précise :</p>
<ol>
<li>les outils autorisés et les comptes à utiliser (professionnels, pas personnels) ;</li>
<li>les données interdites (la liste rouge ci-dessus) ;</li>
<li>la règle de validation humaine avant tout envoi à un client ou toute publication ;</li>
<li>la transparence quand un contenu est généré par l'IA, si nécessaire ;</li>
<li>la personne à contacter en cas de doute ou d'erreur.</li>
</ol>
<p>Cette charte fait aussi partie des mesures attendues au titre de la maîtrise de l'IA : voir notre guide <a href="/guides/ai-act-formation-ia-obligatoire/">AI Act : la formation à l'IA est-elle obligatoire ?</a></p>

<h2>Se former aux bons réflexes</h2>
<p>La sécurité n'est pas un frein : c'est ce qui permet d'utiliser l'IA sereinement, à grande échelle. Dans <a href="/aria-academy/">Aria Academy</a>, une leçon est consacrée à l'automatisation en toute sécurité (RGPD, AI Act et bons réflexes), avec une check-list à télécharger, avant de passer aux ateliers pratiques. <i>Ce guide donne des repères généraux et ne remplace pas un conseil juridique adapté à votre situation.</i></p>
""",
 faq=[("Peut-on utiliser ChatGPT en respectant le RGPD ?","Oui, à condition de ne pas y transmettre de données personnelles identifiantes sans garanties, d'anonymiser les contenus, de régler la confidentialité du compte et, pour un usage d'équipe, de privilégier une offre professionnelle avec engagements contractuels."),
      ("Mes conversations servent-elles à entraîner l'IA ?","Cela dépend de l'outil, de l'offre et de vos réglages. Les versions grand public le permettent souvent par défaut, avec une option pour le refuser ; les offres entreprises l'excluent généralement. Vérifiez les paramètres de votre compte."),
      ("Faut-il une charte IA dans une petite entreprise ?","C'est fortement recommandé dès qu'une personne utilise l'IA au travail. Une page claire suffit : outils autorisés, données interdites, validation humaine et contact en cas de doute.")],
 related=["ai-act-formation-ia-obligatoire", "chatgpt-entreprise-usages-concrets", "zapier-make-n8n-comparatif"]),

"prix-video-professionnelle-entreprise": dict(
 cat="com", date="2026-11-17",
 title="Prix d'une vidéo professionnelle : Réel, film, drone",
 h1="Combien coûte une vidéo professionnelle pour une entreprise ?",
 meta="Prix d'une vidéo pro pour une entreprise : Réel, film promotionnel, interview, drone. Ce qui fait le tarif et des repères dans le Golfe de Saint-Tropez.",
 lead="Un Réel tourné en une heure et un film de présentation tourné sur une journée n'ont pas le même prix, et c'est normal. Pour comparer des devis et choisir le bon format, voici ce qui fait réellement le tarif d'une vidéo professionnelle et des repères concrets.",
 body="""
<h2>Ce qui fait le prix d'une vidéo</h2>
<ol>
<li><b>La préparation</b> : idée, script, liste des plans, repérage. C'est elle qui fait la différence entre une vidéo « jolie » et une vidéo qui atteint son objectif.</li>
<li><b>Le tournage</b> : durée sur place, nombre de lieux, personnes à filmer, prise de son (interview), lumière.</li>
<li><b>Le montage</b> : sélection des rushs, rythme, étalonnage des couleurs, habillage graphique, sous-titres.</li>
<li><b>La musique</b> : elle doit être libre de droits ou sous licence, surtout si la vidéo est utilisée en publicité. Un titre connu de la radio ne peut pas être utilisé librement dans une vidéo d'entreprise.</li>
<li><b>Les déclinaisons</b> : un même tournage peut donner une version horizontale pour le site, des formats verticaux pour les Réels et stories, et des extraits courts.</li>
<li><b>Les options</b> : prises de vue aériennes, sous-titrage, voix off, plusieurs langues.</li>
</ol>

<h2>Quel format pour quel objectif ?</h2>
<ul>
<li><b>Le Réel</b> (15 à 60 secondes, vertical) : pour être vu sur Instagram, Facebook et TikTok, montrer les coulisses, une nouveauté, une ambiance. C'est le format qui touche le plus de monde, à condition d'en publier régulièrement.</li>
<li><b>Le film promotionnel</b> (1 à 2 minutes) : pour présenter votre établissement ou votre savoir-faire sur votre site, en salon ou en publicité.</li>
<li><b>L'interview</b> : pour donner la parole au dirigeant, à l'équipe ou à des clients satisfaits. Idéal pour créer la confiance.</li>
<li><b>L'aftermovie</b> : pour faire revivre un événement et donner envie de venir à la prochaine édition.</li>
<li><b>Les images de drone</b> : pour révéler un lieu (villa, domaine, hôtel, plage) dans son environnement.</li>
</ul>

<h2>Repères de prix chez Maison Aria</h2>
<p>Voici les prix de départ pratiqués par Maison Aria dans le Golfe de Saint-Tropez (tarifs « à partir de », devis gratuit et sur mesure) :</p>
<ul>
<li><a href="/prestations/reel-tourne-monte/">Réel tourné et monté</a> : dès 70 €.</li>
<li><a href="/prestations/reel-a-partir-de-vos-images/">Réel monté à partir de vos images</a> : dès 60 €.</li>
<li><a href="/prestations/pack-4-reels/">Pack de 4 Réels</a> : dès 200 € ; <a href="/prestations/pack-8-reels/">pack de 8 Réels</a> : dès 390 €.</li>
<li><a href="/prestations/interview-video/">Interview vidéo</a> : dès 190 €.</li>
<li><a href="/prestations/film-promotionnel/">Film promotionnel</a> et <a href="/prestations/aftermovie/">aftermovie</a> : dès 230 €.</li>
<li><a href="/prestations/captation-video/">Captation vidéo</a> : dès 120 € ; <a href="/prestations/tournage-video/">tournage vidéo</a> : dès 220 €.</li>
<li><a href="/prestations/prises-de-vue-aeriennes/">Prises de vue aériennes par drone</a> : dès 150 €.</li>
<li><a href="/prestations/montage-video/">Montage vidéo</a> de vos rushs : dès 160 € ; <a href="/prestations/sous-titrage-video/">sous-titrage</a> : dès 25 €.</li>
<li><a href="/prestations/content-day-journee-creation-contenu/">Content Day</a>, demi-journée photo et vidéo : dès 390 €.</li>
</ul>

<h2>Le drone : ce qu'il faut savoir</h2>
<p>Un vol de drone professionnel se prépare : le télépilote vérifie la réglementation de la zone, les autorisations nécessaires et la météo. Le Golfe de Saint-Tropez compte de nombreuses zones réglementées ; la faisabilité est donc vérifiée avant chaque prestation, et le vol est reporté si les conditions ne le permettent pas.</p>

<h2>Rentabiliser un tournage</h2>
<ul>
<li><b>Tournez une fois, déclinez plusieurs fois</b> : prévoyez dès le départ les formats horizontal et vertical, et des extraits courts.</li>
<li><b>Pensez saison</b> : dans le Golfe, des images tournées au printemps sont prêtes pour la haute saison, quand vous n'aurez plus le temps.</li>
<li><b>Sous-titrez</b> : une grande partie des vidéos est regardée sans le son sur les réseaux sociaux.</li>
<li><b>Accrochez dès les premières secondes</b> : sur les réseaux, c'est là que tout se joue. Notre guide <a href="/guides/idees-reels-restaurant-commerce/">15 idées de Réels</a> donne des pistes concrètes.</li>
</ul>

<h2>Les questions à poser avant de signer</h2>
<ul>
<li>Combien de versions et de formats seront livrés ?</li>
<li>Combien d'allers-retours de corrections sont prévus ?</li>
<li>La musique est-elle utilisable en publicité ?</li>
<li>Quels usages de la vidéo sont autorisés (site, réseaux, publicité, salon) ?</li>
<li>Que se passe-t-il en cas de mauvais temps pour un tournage en extérieur ?</li>
</ul>
<p>Un projet de vidéo à Saint-Tropez, Sainte-Maxime, Grimaud ou ailleurs dans le Golfe ? Découvrez l'<a href="/expertises/video-montage/">offre vidéo et montage</a> de Maison Aria ou <a href="/#contact">demandez un devis gratuit</a>.</p>
""",
 faq=[("Combien coûte un Réel professionnel ?","Chez Maison Aria, un Réel tourné et monté démarre à 70 €, et un pack de 4 Réels à 200 €. Le prix dépend de la préparation, du temps de tournage et du montage."),
      ("Combien coûte un film de présentation d'entreprise ?","Un film promotionnel démarre à 230 € chez Maison Aria. Le devis s'adapte à la durée du tournage, au nombre de lieux et aux options (drone, interview, sous-titres)."),
      ("Peut-on mettre une musique connue dans une vidéo d'entreprise ?","Non, pas librement : une musique commerciale nécessite des droits. Pour une vidéo d'entreprise, et surtout pour la publicité, on utilise une musique libre de droits ou sous licence."),
      ("Peut-on filmer au drone partout dans le Golfe de Saint-Tropez ?","Non, certaines zones sont réglementées ou interdites. La faisabilité est vérifiée avant chaque prestation.")],
 related=["idees-reels-restaurant-commerce", "prix-shooting-photo-professionnel", "tarif-community-manager"]),

"prix-logo-identite-visuelle": dict(
 cat="com", date="2026-11-17",
 title="Prix d'un logo et d'une identité visuelle pour une TPE",
 h1="Combien coûtent un logo et une identité visuelle pour une petite entreprise ?",
 meta="Prix d'un logo et d'une identité visuelle pour une TPE : ce qui est inclus, les fichiers à exiger, les droits d'auteur et des repères de tarifs.",
 lead="Un logo à 20 € sur une plateforme en ligne, un autre à plusieurs milliers d'euros en agence : difficile de s'y retrouver. Voici ce que recouvrent vraiment un logo, une identité visuelle et une charte graphique, ce qui fait leur prix et ce qu'il faut exiger avant de payer.",
 body="""
<h2>Logo, identité visuelle, charte graphique : quelles différences ?</h2>
<ul>
<li><b>Le logo</b> est le signe qui représente votre entreprise : un nom stylisé, un symbole, ou les deux.</li>
<li><b>L'identité visuelle</b> est l'ensemble cohérent qui entoure le logo : couleurs, typographies, éléments graphiques, style des photos. C'est elle qui rend votre entreprise reconnaissable sur une affiche comme sur Instagram.</li>
<li><b>La charte graphique</b> est le document qui explique comment utiliser cette identité : tailles, espaces de protection, couleurs exactes, exemples à suivre et à éviter. Indispensable dès que plusieurs personnes ou prestataires communiquent pour vous.</li>
</ul>

<h2>Ce qui fait le prix</h2>
<ol>
<li><b>La phase de découverte</b> : comprendre votre activité, vos clients, vos concurrents et vos valeurs.</li>
<li><b>Le nombre de pistes</b> explorées et d'allers-retours de corrections.</li>
<li><b>Les déclinaisons</b> : version couleur, monochrome, sur fond clair et foncé, format carré pour les réseaux, icône.</li>
<li><b>Les éléments livrés en plus du logo</b> : palette, typographies, motifs, modèles pour les réseaux sociaux, papeterie.</li>
<li><b>Les droits</b> : la cession des droits d'auteur et son étendue.</li>
</ol>

<h2>Repères de prix chez Maison Aria</h2>
<p>Prix de départ pratiqués par Maison Aria (tarifs « à partir de », devis gratuit et sur mesure) :</p>
<ul>
<li><a href="/prestations/creation-de-logo/">Création de logo</a> : dès 90 €.</li>
<li><a href="/prestations/refonte-de-logo/">Refonte de logo</a> : dès 70 €.</li>
<li><a href="/prestations/identite-visuelle-essentielle/">Identité visuelle essentielle</a> : dès 160 €.</li>
<li><a href="/prestations/identite-visuelle-complete/">Identité visuelle complète</a> : dès 240 €.</li>
<li><a href="/prestations/charte-graphique/">Charte graphique</a> : dès 70 €.</li>
<li><a href="/prestations/templates-reseaux-sociaux/">Templates pour les réseaux sociaux</a> : dès 80 €.</li>
<li>Supports imprimés : <a href="/prestations/carte-de-visite/">carte de visite</a> dès 60 €, <a href="/prestations/flyer/">flyer</a> dès 70 €, <a href="/prestations/menu-grille-tarifaire/">menu ou grille tarifaire</a> dès 90 €.</li>
</ul>

<h2>Les fichiers à exiger</h2>
<ul>
<li><b>SVG ou PDF vectoriel</b> : agrandissable à l'infini, indispensable pour une enseigne, un véhicule ou un textile.</li>
<li><b>PNG à fond transparent</b> : pour le web, les documents et les réseaux.</li>
<li><b>Versions couleur, noir et blanc</b>, sur fond clair et sur fond foncé.</li>
<li><b>Les références de couleurs</b> : codes pour l'écran (RVB, hexadécimal) et pour l'impression (CMJN).</li>
<li><b>Le nom des typographies</b> utilisées et leurs conditions de licence.</li>
</ul>

<h2>Les droits d'auteur : le point à ne pas oublier</h2>
<p>En France, le logo est une création protégée par le droit d'auteur. Pour pouvoir l'exploiter librement (enseigne, publicité, produits), la cession des droits doit être prévue par écrit et préciser l'étendue des droits cédés : usages, supports, territoire et durée (article L131-3 du Code de la propriété intellectuelle). Vérifiez que votre devis ou vos conditions générales en parlent. Si vous souhaitez aussi déposer votre marque, c'est une démarche distincte auprès de l'INPI.</p>

<h2>Et les logos générés par l'IA ?</h2>
<p>Les générateurs d'images permettent d'explorer des idées rapidement, et c'est un bon point de départ pour une réflexion. Mais un logo doit aussi être simple, lisible en petit, déclinable, cohérent avec votre activité… et vraiment à vous. Un visuel généré automatiquement peut ressembler à d'autres, et sa protection par le droit d'auteur est incertaine. Le plus sûr : s'en servir comme inspiration, puis faire concevoir un logo original.</p>

<h2>Les questions à poser avant de commander</h2>
<ul>
<li>Combien de pistes et d'allers-retours de corrections sont inclus ?</li>
<li>Quels fichiers et quelles déclinaisons seront livrés ?</li>
<li>La cession des droits est-elle prévue, et pour quels usages ?</li>
<li>Une mini-charte est-elle fournie pour utiliser le logo correctement ?</li>
</ul>
<p>Vous lancez votre activité ou souhaitez moderniser votre image dans le Golfe de Saint-Tropez ? Découvrez l'offre <a href="/expertises/identite-visuelle-graphisme/">identité visuelle et graphisme</a> de Maison Aria ou <a href="/#contact">demandez un devis gratuit</a>.</p>
""",
 faq=[("Combien coûte un logo professionnel ?","Chez Maison Aria, la création d'un logo démarre à 90 € et une identité visuelle complète à 240 €. Le prix dépend du nombre de pistes, des déclinaisons et des éléments livrés."),
      ("Quels formats de fichiers doit-on recevoir pour un logo ?","Au minimum un fichier vectoriel (SVG ou PDF), des PNG à fond transparent, des versions couleur et monochrome, et les codes couleurs pour l'écran et l'impression."),
      ("Est-ce que je suis propriétaire de mon logo ?","Vous pouvez l'exploiter librement si une cession des droits d'auteur écrite le prévoit, avec les usages, supports, territoire et durée. Vérifiez-le dans votre devis ou vos conditions générales.")],
 related=["optimiser-fiche-google-business-profile", "prix-shooting-photo-professionnel", "tarif-community-manager"]),

"optimiser-fiche-google-business-profile": dict(
 cat="com", date="2026-11-17",
 title="Optimiser sa fiche Google Business Profile : 10 actions",
 h1="Fiche Google Business Profile : 10 actions pour attirer plus de clients locaux",
 meta="Optimiser sa fiche Google Business Profile : catégories, horaires de saison, photos, avis, publications. 10 actions pour les commerces du Golfe.",
 lead="Quand un touriste cherche « restaurant Sainte-Maxime » ou « fleuriste Cogolin », c'est souvent votre fiche Google qu'il voit en premier, avant votre site ou vos réseaux. Une fiche complète et vivante peut faire la différence entre vous et le voisin. Voici 10 actions concrètes, faciles à mettre en place.",
 body="""
<h2>Pourquoi votre fiche Google compte autant</h2>
<p>Pour une recherche locale, Google affiche une carte avec quelques établissements mis en avant. Pour choisir, l'internaute regarde les photos, la note, les avis récents et les horaires, puis appelle, demande l'itinéraire ou réserve, souvent sans jamais visiter votre site. Votre fiche est donc une vitrine à part entière.</p>

<h2>Les 10 actions</h2>
<ol>
<li><b>Revendiquez et validez votre fiche.</b> Sans validation, vous ne contrôlez pas les informations affichées, et n'importe qui peut suggérer des modifications.</li>
<li><b>Choisissez la bonne catégorie principale</b>, la plus précise possible (« Restaurant de fruits de mer » plutôt que « Restaurant »), puis ajoutez quelques catégories secondaires pertinentes.</li>
<li><b>Soignez la cohérence de vos coordonnées</b> : nom, adresse et téléphone identiques sur votre fiche, votre site, vos réseaux et les annuaires.</li>
<li><b>Tenez vos horaires à jour</b>, y compris les horaires exceptionnels (jours fériés, événements). Dans le Golfe, indiquez clairement vos horaires d'hiver et une fermeture saisonnière comme une fermeture temporaire, jamais définitive.</li>
<li><b>Rédigez une description utile</b> : ce que vous proposez, pour qui, où, ce qui vous distingue. Mentionnez naturellement votre ville et vos spécialités, sans accumuler les mots-clés.</li>
<li><b>Publiez de vraies photos, souvent</b> : devanture (pour être reconnu dans la rue), intérieur, équipe, produits, plats, terrasse. Des photos professionnelles récentes inspirent confiance ; un <a href="/prestations/photographie-commerce-etablissement/">shooting d'établissement</a> au printemps peut nourrir votre fiche toute l'année.</li>
<li><b>Renseignez vos produits et services</b>, avec des prix quand c'est possible. Ils apparaissent directement sur la fiche.</li>
<li><b>Publiez des actualités</b> : réouverture, menu de saison, événement, offre. Une publication par semaine ou tous les quinze jours montre que l'établissement est actif.</li>
<li><b>Demandez des avis et répondez à tous.</b> Demandez au bon moment (fin de repas réussi, livraison terminée), avec un lien direct ou un QR code. Répondez à chaque avis, positif comme négatif, avec calme et personnalisation. Acheter ou inventer des avis est interdit et sanctionné.</li>
<li><b>Ajoutez les bons liens et suivez les statistiques</b> : site, réservation, menu, prise de rendez-vous. Consultez régulièrement les performances de la fiche (recherches, appels, itinéraires) pour voir ce qui fonctionne.</li>
</ol>

<h2>Spécial Golfe de Saint-Tropez : penser saison</h2>
<ul>
<li><b>Avant la saison</b> (mars-avril) : nouvelles photos, horaires d'été, menu ou tarifs à jour, publication de réouverture.</li>
<li><b>Pendant la saison</b> : publications régulières, réponses rapides aux avis, notamment en anglais pour la clientèle étrangère.</li>
<li><b>Après la saison</b> : horaires d'hiver ou fermeture temporaire bien indiqués, remerciements aux clients, annonce de la date de retour.</li>
</ul>

<h2>Gagner du temps avec l'IA, sans perdre votre ton</h2>
<p>Un assistant IA peut vous aider à rédiger la description de la fiche, des idées de publications ou des brouillons de réponses aux avis, que vous relisez et personnalisez avant de les publier. Notre guide <a href="/guides/chatgpt-entreprise-usages-concrets/">ChatGPT en entreprise : 20 usages concrets</a> donne des exemples de demandes à copier, et <a href="/guides/comment-ecrire-un-bon-prompt/">Comment écrire un bon prompt</a> explique comment obtenir des réponses qui vous ressemblent.</p>
<p>Besoin de photos qui donnent envie ou d'un accompagnement pour votre présence en ligne ? Maison Aria accompagne les commerces, restaurants et hôtels du Golfe de Saint-Tropez en <a href="/expertises/photographie-creation-de-contenu/">photographie</a> et en <a href="/expertises/strategie-reseaux-sociaux/">stratégie réseaux sociaux</a>. <a href="/#contact">Demandez un devis gratuit</a>.</p>
""",
 faq=[("La fiche Google Business Profile est-elle gratuite ?","Oui, créer et gérer une fiche d'établissement Google est gratuit."),
      ("Combien de photos faut-il mettre sur sa fiche Google ?","Il n'y a pas de nombre magique : l'important est d'avoir des photos récentes et variées (devanture, intérieur, équipe, produits) et d'en ajouter régulièrement."),
      ("Faut-il répondre aux avis négatifs ?","Oui, toujours, calmement et de façon personnalisée. Une réponse professionnelle rassure les futurs clients qui lisent l'échange."),
      ("Comment indiquer une fermeture pour l'hiver ?","Utilisez la fermeture temporaire ou des horaires spéciaux, jamais la fermeture définitive, qui ferait disparaître votre établissement des recherches.")],
 related=["prix-shooting-photo-professionnel", "tarif-community-manager", "chatgpt-entreprise-usages-concrets"]),
}
