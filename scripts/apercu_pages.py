"""Contrôle visuel du PDF.
  python scripts/apercu_pages.py 1 5 20        -> pages individuelles (PNG)
  python scripts/apercu_pages.py --chercher "texte"  -> numéros de pages contenant le texte
"""
import sys
from pathlib import Path

import pymupdf

racine = Path(__file__).resolve().parent.parent
doc = pymupdf.open(racine / "main.pdf")
if sys.argv[1] == "--chercher":
    for i, page in enumerate(doc, 1):
        if page.search_for(sys.argv[2]):
            print(i, end=" ")
    print()
else:
    sortie = racine / "_apercu"
    sortie.mkdir(exist_ok=True)
    for n in map(int, sys.argv[1:]):
        doc[n - 1].get_pixmap(dpi=60).save(sortie / f"page_{n:03d}.png")
    print(len(doc), "pages")
