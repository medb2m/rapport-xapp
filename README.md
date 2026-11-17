# Rapport PFE — Xapp

Rapport de projet de fin d'études (LaTeX, en français) sur la plateforme **Xapp** (dépôt applicatif : `xapp`), réalisée pour Xweb.

## Structure

```
main.tex                  point d'entrée
config/                   préambule, informations administratives (infos.tex), abréviations
frontmatter/              couverture, dédicaces, remerciements, résumé / abstract
chapitres/                introduction, chapitres 1 à 8, conclusion
annexes/                  compléments techniques
figures/                  logos, architecture, UML, captures d'écran
diagrammes/               sources PlantUML des diagrammes régénérés
scripts/                  build.sh, liste des points à compléter, outils de contrôle
bibliographie.bib         références (BibLaTeX / biber)
A_COMPLETER.md            généré : figures à capturer et informations manquantes
```

## Compiler

Prérequis : une distribution LaTeX (MiKTeX ou TeX Live) avec `pdflatex`, `biber` et `makeindex`.

```bash
bash scripts/build.sh      # pdflatex -> biber -> makeindex -> pdflatex x2
```

Sur Overleaf : choisir `main.tex` comme document principal, compilateur pdfLaTeX, bibliographie biber.

## Terminer le rapport

* Les passages encore à renseigner sont marqués en rouge dans le PDF par `[À COMPLÉTER : …]`, les figures manquantes par un cadre `FIGURE À INSÉRER` qui décrit précisément la capture attendue.
* `python scripts/lister_a_completer.py` régénère `A_COMPLETER.md` avec la liste complète.
* Pour déposer une capture : copier le fichier dans `figures/captures/`, puis remplacer la commande `\figmanquante{label}{légende}{description}` par `\fig[largeur]{figures/captures/fichier.png}{légende}{label}`.
* Pour masquer les repères rouges dans la version finale : `\afficheratodofalse` dans `config/preambule.tex`.
* Informations administratives (diplôme, spécialité, date de soutenance) : `config/infos.tex`.

## Principes de rédaction

* Le texte décrit **ce projet** : les affirmations techniques ont été vérifiées dans le code de `xapp` (modèles, routes, événements Socket.IO, configuration). Rien n'est repris d'un autre rapport ; le rapport B2M-Support n'a servi que de modèle de structure.
* Les sources externes citées sont des documents officiels ou de référence (RFC, W3C, WHATWG, OWASP, documentation des outils, textes de loi). Aucune statistique de marché n'est avancée sans source ; ce qui doit être sourcé est signalé par un `\todo`.
* Les limites du projet (sécurité, passage à l'échelle, tests) sont écrites explicitement : c'est ce qui rend le rapport crédible face à un jury.
* Avant de rendre le rapport : relire chaque chapitre à voix haute, reformuler avec vos propres mots les passages qui ne sonnent pas comme vous, et passer le PDF dans l'outil anti-plagiat exigé par l'établissement.

## Copie DOCX

`python scripts/vers_docx.py` (après `bash scripts/build.sh`) génère `rapport_xapp.docx` ; les parties à revoir y restent en rouge.
Prérequis : `pip install pypandoc_binary python-docx`.
