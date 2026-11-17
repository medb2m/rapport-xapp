#!/usr/bin/env bash
# Compilation complète : pdflatex -> biber -> makeindex (abréviations) -> pdflatex x2
# Sous Windows (Git Bash), ajouter MiKTeX au PATH si nécessaire :
#   export PATH="$PATH:/c/Users/<vous>/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
set -e
cd "$(dirname "$0")/.."
OPTS="-interaction=nonstopmode -file-line-error"
pdflatex $OPTS main.tex >/dev/null || true
biber main >/dev/null || true
[ -f main.acn ] && makeindex -s main.ist -t main.alg -o main.acr main.acn >/dev/null 2>&1 || true
pdflatex $OPTS main.tex >/dev/null || true
pdflatex $OPTS main.tex | grep -E "^(\./)?.*:[0-9]+:|Overfull \\\\hbox \([0-9]{3,}|LaTeX Warning: (Reference|Citation)" || true
echo "Terminé : main.pdf"
