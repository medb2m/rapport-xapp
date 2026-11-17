"""Génère A_COMPLETER.md : liste des \\todo{...} et des \\figmanquante{...} présents dans les sources LaTeX.

Usage : python scripts/lister_a_completer.py
"""
import re
from pathlib import Path

racine = Path(__file__).resolve().parent.parent
fichiers = sorted(
    list(racine.glob("frontmatter/*.tex"))
    + list(racine.glob("chapitres/*.tex"))
    + list(racine.glob("annexes/*.tex"))
    + list(racine.glob("config/infos.tex"))
)


def accolades(texte, debut):
    """Retourne le contenu du groupe { ... } commençant à `debut` (équilibré) et l'indice de fin."""
    profondeur, i = 0, debut
    while i < len(texte):
        if texte[i] == "{":
            profondeur += 1
        elif texte[i] == "}":
            profondeur -= 1
            if profondeur == 0:
                return texte[debut + 1 : i], i + 1
        i += 1
    return "", len(texte)


todos, figures = [], []
for f in fichiers:
    t = f.read_text(encoding="utf-8")
    for m in re.finditer(r"\\todo\{", t):
        contenu, _ = accolades(t, m.end() - 1)
        todos.append((f.name, " ".join(contenu.split())))
    for m in re.finditer(r"\\figmanquante\{", t):
        args, pos = [], m.end() - 1
        for _ in range(3):
            c, pos = accolades(t, pos)
            args.append(" ".join(c.split()))
        figures.append((f.name, *args))

sortie = ["# À compléter dans le rapport", "", "Fichier généré par `scripts/lister_a_completer.py` (ne pas éditer à la main).", ""]
sortie += [f"## Figures à capturer ou à créer ({len(figures)})", "", "| Fichier | Label | Légende | Que capturer |", "|---|---|---|---|"]
for f, label, legende, desc in figures:
    sortie.append(f"| {f} | `{label}` | {legende} | {desc} |")
sortie += ["", f"## Informations et vérifications à compléter ({len(todos)})", "", "| Fichier | À faire |", "|---|---|"]
for f, c in todos:
    sortie.append(f"| {f} | {c} |")
(racine / "A_COMPLETER.md").write_text("\n".join(sortie) + "\n", encoding="utf-8")
print(len(figures), "figures,", len(todos), "points à compléter")
