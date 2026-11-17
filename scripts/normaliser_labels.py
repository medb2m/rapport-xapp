"""Remplace les ':' des étiquettes (fig:, tab:, ...) par '-' : le ':' est actif sous babel-french et casse cleveref."""
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
MOTIF = re.compile(r"\b(fig|tab|sec|lst|chap):(?=[a-z0-9])")

for fichier in list(RACINE.glob("chapitres/*.tex")) + list(RACINE.glob("annexes/*.tex")) + list(RACINE.glob("frontmatter/*.tex")):
    texte = fichier.read_text(encoding="utf-8")
    nouveau = MOTIF.sub(lambda m: m.group(1) + "-", texte)
    if nouveau != texte:
        fichier.write_text(nouveau, encoding="utf-8", newline="")
        print("modifié :", fichier.name)
