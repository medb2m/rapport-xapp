# À compléter dans le rapport

Fichier généré par `scripts/lister_a_completer.py` (ne pas éditer à la main).

## Figures à capturer ou à créer (8)

| Fichier | Label | Légende | Que capturer |
|---|---|---|---|
| ch1_contexte.tex | `fig-gantt` | Diagramme de Gantt du projet | Insérer une capture du fichier Xapp\_Gantt\_PFE\_2026.xlsx (généré par tools/generate\_xapp\_gantt.py) montrant les 4 phases sur 24 semaines. |
| ch1_contexte.tex | `fig-git-commits` | Extrait de l'historique des commits du dépôt sur GitHub | Capturer la page « Commits » du dépôt xweb-tn/xapp sur GitHub (ou le graphe « Insights > Contributors »). |
| ch4_sprint1_comptes.tex | `fig-login` | Page de connexion | Capturer la page /login (version française et, si possible, version arabe en RTL), avec le formulaire e-mail et mot de passe et le lien « Mot de passe oublié ». |
| ch4_sprint1_comptes.tex | `fig-inscription` | Page d'inscription et saisie du code de vérification | Capturer /register avec le reCAPTCHA visible, puis /verify-email où l'on saisit le code à six chiffres. |
| ch5_sprint2_audit_seo.tex | `fig-comparateur` | Comparateur de concurrents | Capturer /dashboard/comparateur avec le site et deux ou trois concurrents comparés. |
| ch6_sprint3_visibilite_ia.tex | `fig-plan-genere` | Plan d'action généré | Capturer un plan d'action généré (calendrier jour par jour avec contenus prêts à copier) et, si possible, la première page du PDF exporté. |
| ch6_sprint3_visibilite_ia.tex | `fig-corrections` | Page de suivi des corrections | Capturer /dashboard/corrections avec plusieurs éléments de catégories et de gravités différentes, un élément vérifié (fixed) et le bouton « Vérifier ». |
| ch7_sprint4_jannet_collaboration.tex | `fig-upgrade` | Page d'achat de packs | Capturer /dashboard/upgrade avec les packs proposés et, si possible, la page de paiement Flouci en mode test. |

## Informations et vérifications à compléter (65)

| Fichier | À faire |
|---|---|
| annexes.tex | vérifier les préfixes exacts de chaque routeur dans main.py (export, voice, payments, notifications) |
| annexes.tex | vérifier que l'extrait correspond fidèlement au code de audit\_runner.py |
| annexes.tex | rédiger ici, en une page, le scénario de démonstration suivi lors de la soutenance (tableau de bord et support, audit SEO, visibilité IA, plan d'action et corrections, réunion vocale avec Jannet, actions d'administration de Jannet, Kanban et messagerie), avec les comptes de test utilisés et la durée de chaque étape |
| annexes.tex | si l'encadrant demande un manuel utilisateur (client, manager), l'insérer ici sous forme de quelques pages illustrées de captures, ou le fournir comme livrable séparé et y renvoyer |
| ch1_contexte.tex | année de création, forme juridique, adresse, effectif, à confirmer auprès de l'encadrant |
| ch1_contexte.tex | vérifier avec l'agence la répartition réelle des activités et l'autorisation de publier les logos clients visibles sur la capture |
| ch1_contexte.tex | insérer l'organigramme de l'agence (direction, développement, design, SEO, commercial) ou le décrire en quelques lignes, après validation par l'encadrant ; si l'agence ne souhaite pas le publier, supprimer cette sous-section |
| ch1_contexte.tex | préciser la fréquence réelle des points de suivi |
| ch1_contexte.tex | citer un tarif public vérifié de Semrush et d'Ahrefs, consulté à une date précise |
| ch1_contexte.tex | vérifier cette affirmation à la date de la soutenance : certains éditeurs ont commencé à proposer des modules de suivi IA |
| ch1_contexte.tex | à vérifier |
| ch1_contexte.tex | faire valider ces objectifs par l'encadrant |
| ch1_contexte.tex | confirmer les dates réelles de début et de fin du stage ; le dépôt contient des commits dès novembre 2025, préciser si une partie du socle a été réalisée avant le stage |
| ch1_contexte.tex | vérifier ce chiffre sur le dépôt final et l'expliquer par rapport aux dates du stage |
| ch2_analyse.tex | faire valider l'état de chaque module par l'encadrant, en particulier M5 (paiement réel en production ou non) |
| ch2_analyse.tex | confirmer que tous les comptes visibles sur les captures (noms, e-mails, sites) sont bien des comptes de test ou sont autorisés ; flouter sinon |
| ch2_analyse.tex | faire valider par l'agence le contenu juridique des trois pages légales ; mentionner une éventuelle déclaration auprès de l'INPDP si l'agence l'a effectuée |
| ch2_analyse.tex | vérifier que le diagramme de cas d'utilisation reste lisible à l'impression ; sinon le passer sur une page à l'italienne ou le découper par acteur |
| ch2_analyse.tex | si des maquettes Figma ou papier existent, ajouter ici 2 ou 3 figures (landing, tableau de bord, audit) ; sinon conserver ce paragraphe et le mentionner honnêtement au jury |
| ch3_conception.tex | indiquer les caractéristiques du VPS (processeur, mémoire, disque), la version d'Ubuntu et de PostgreSQL |
| ch3_conception.tex | le diagramme de classes ne montre que 9 entités sur 18 ; ajouter les tables de collaboration (tickets, messages, notifications, chat, agent, exports) ou préciser dans la légende qu'il s'agit du cœur métier |
| ch4_sprint1_comptes.tex | indiquer la longueur minimale de mot de passe effectivement imposée côté client et côté serveur |
| ch4_sprint1_comptes.tex | préciser si la connexion est refusée tant que l'adresse n'est pas vérifiée, ou si seules certaines fonctions sont bloquées |
| ch4_sprint1_comptes.tex | vérifier que la demande répond par le même message que l'adresse existe ou non (anti-énumération) |
| ch4_sprint1_comptes.tex | vérifier chaque case du tableau en testant avec un compte de chaque rôle ; ne pas publier le chemin exact de la console super admin |
| ch4_sprint1_comptes.tex | confirmer |
| ch4_sprint1_comptes.tex | confirmer ce récit à partir de l'historique Git et de votre souvenir |
| ch5_sprint2_audit_seo.tex | confirmer la limite de pages réellement appliquée par plan (40, 100 ou par tranche) et la mettre en cohérence avec la présentation |
| ch5_sprint2_audit_seo.tex | vérifier la répartition exacte 60/40 et la formule finale dans scoring.py et full\_site.py avant la soutenance |
| ch5_sprint2_audit_seo.tex | ajouter une capture de la connexion GSC ou de l'état d'indexation, si la fonctionnalité est active en production |
| ch5_sprint2_audit_seo.tex | préciser le nombre maximal de concurrents réellement accepté (la documentation indique 3) |
| ch5_sprint2_audit_seo.tex | reformuler la mention « certifié par signature électronique » imprimée sur les PDF, qui peut prêter à confusion |
| ch6_sprint3_visibilite_ia.tex | faire relire le barème par l'encadrant : il est construit empiriquement et doit être présenté comme tel au jury |
| ch6_sprint3_visibilite_ia.tex | vérifier que l'interface affiche bien cet avertissement ; sinon l'ajouter ou supprimer la phrase |
| ch6_sprint3_visibilite_ia.tex | la documentation et la présentation parlent d'un plan sur 14 jours et de GPT-4o, alors que la consigne actuelle du code demande un plan sur 7 jours au modèle GPT-4o-mini : vérifier et harmoniser le texte |
| ch7_sprint4_jannet_collaboration.tex | préciser si le paiement Flouci est actif en production avec de vrais paiements, et indiquer les prix des packs validés par l'agence |
| ch7_sprint4_jannet_collaboration.tex | ajouter une capture de la page d'accueil ou du tableau de bord en arabe (RTL) |
| ch8_deploiement_tests.tex | vérifier qu'aucun secret ni mot de passe par défaut ne figure dans le dépôt (README, scripts, fichiers de test) ; les renouveler si c'est le cas avant de rendre le dépôt accessible au jury |
| ch8_deploiement_tests.tex | vérifier si Cloudflare ou Nginx appliquent une limitation ; sinon conserver ce point |
| ch8_deploiement_tests.tex | vérifier si les adresses privées et localhost sont filtrées par le contrôle d'éligibilité |
| ch8_deploiement_tests.tex | décrire précisément les tests réellement effectués : le dépôt contient-il des tests automatisés (pytest, tests front) ? sinon le reconnaître ici comme dans la suite du paragraphe |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | à rejouer |
| ch8_deploiement_tests.tex | rejouer chaque scénario sur la plateforme déployée, remplacer « à rejouer » par OK ou KO, et joindre une capture ou une trace pour les cas les plus parlants (T4, T8, T11) |
| ch8_deploiement_tests.tex | mesurer sur la plateforme déployée la durée d'un audit de la page d'accueil et d'un audit Pro de 100 pages sur deux ou trois sites, le temps de réponse de trois routes représentatives (connexion, historique, statut de job) et faire un audit Lighthouse de la page d'accueil de Xapp ; ne reporter que des valeurs réellement mesurées |
| ch8_deploiement_tests.tex | indiquer la politique de sauvegarde de la base PostgreSQL et des fichiers téléversés (fréquence, emplacement), ou reconnaître son absence |
| conclusion.tex | vérifier les chiffres clés avant la version finale |
| conclusion.tex | relire cette section et la réécrire avec vos propres mots et votre vécu réel du stage : les ressentis décrits ci-dessous sont déduits de l'historique du projet et doivent être confirmés ou corrigés par vous |
| introduction.tex | ajouter une statistique sourcée et datée sur la part des recherches passant par les assistants IA, ou supprimer cette phrase |
| infos.tex | spécialité |
| infos.tex | intitulé exact du diplôme |
| infos.tex | date de soutenance |
| dedicace.tex | personnaliser la dédicace : nommer les personnes concernées, ajouter une dédicace à titre personnel si souhaité |
| remerciements.tex | citer nommément les collègues de Xweb à remercier, si souhaité |
| resume.tex | vérifier les chiffres clés repris dans le résumé et la durée exacte du stage |
