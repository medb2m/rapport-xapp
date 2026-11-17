"""Génère rapport_xapp.docx à partir des sources LaTeX (après compilation : main.aux et main.bbl requis).
Les repères \todo et \figmanquante restent en rouge dans le DOCX."""
import re, subprocess, shutil
from pathlib import Path
import pypandoc
from docx import Document
from docx.shared import RGBColor, Pt, Cm

R = Path(__file__).resolve().parent.parent
B = R / "build_docx"; shutil.rmtree(B, ignore_errors=True); B.mkdir()

def grp(t, i):
    d = 0
    for j in range(i, len(t)):
        if t[j] == "{": d += 1
        elif t[j] == "}":
            d -= 1
            if d == 0: return t[i+1:j], j+1
    return "", len(t)

def subcmd(t, name, fn, nargs=1, opt=False):
    out, i = [], 0
    pat = re.compile(r"\\" + name + r"(?![A-Za-z])")
    while True:
        m = pat.search(t, i)
        if not m: out.append(t[i:]); break
        out.append(t[i:m.start()]); k = m.end(); o = None
        if opt and k < len(t) and t[k] == "[":
            e = t.index("]", k); o = t[k+1:e]; k = e+1
        args = []
        for _ in range(nargs):
            while t[k] in " \n": k += 1
            a, k = grp(t, k); args.append(a)
        out.append(fn(o, *args)); i = k
    return "".join(out)

aux = (R/"main.aux").read_text(encoding="utf-8", errors="ignore")
labels = {m.group(1): m.group(2) for m in re.finditer(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", aux)}
noms = {"fig": "la figure", "tab": "le tableau", "lst": "le listing", "sec": "la section", "chap": "le chapitre"}
def cref(o, a):
    return ", ".join(f"{noms.get(l.split('-')[0], '')} {labels.get(l.strip(), '??')}".strip() for l in a.split(","))
bbl = (R/"main.bbl").read_text(encoding="utf-8", errors="ignore")
order = re.findall(r"\\entry\{([^}]+)\}", bbl)
num = {k: i+1 for i, k in enumerate(order)}
gl = {m.group(1): m.group(2) for m in re.finditer(r"\\newacronym\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", (R/"config/glossaire.tex").read_text(encoding="utf-8"))}

# Figures TikZ -> PNG
pre = (R/"config/preambule.tex").read_text(encoding="utf-8")
cols = "\n".join(re.findall(r"\\definecolor\{[^\n]*", pre))
tikz_n = [0]
def tikz_png(block):
    tikz_n[0] += 1; n = tikz_n[0]
    src = ("\\documentclass[border=6pt]{standalone}\\usepackage[utf8]{inputenc}\\usepackage[T1]{fontenc}\\usepackage{lmodern}"
           "\\usepackage[french]{babel}\\usepackage[dvipsnames]{xcolor}\\usepackage{tikz}\\usetikzlibrary{positioning,arrows.meta,shapes,calc}"
           + cols + "\\newcommand{\\code}[1]{\\texttt{\\small #1}}\\newcommand{\\todo}[1]{}\\begin{document}" + block + "\\end{document}")
    (B/f"tikz{n}.tex").write_text(src, encoding="utf-8")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"tikz{n}.tex"], cwd=B, capture_output=True)
    subprocess.run(["pdftoppm", "-r", "200", "-png", "-singlefile", f"tikz{n}.pdf", f"tikz{n}"], cwd=B)
    return f"\\includegraphics[width=0.9\\textwidth]{{{B}/tikz{n}.png}}"

def prep(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    t = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", lambda m: tikz_png(m.group(0)), t, flags=re.S)
    t = subcmd(t, "todo", lambda o, a: f"\\textcolor{{red}}{{\\textbf{{[À COMPLÉTER : {a}]}}}}")
    t = subcmd(t, "figmanquante", lambda o, l, c, d: f"\n\n\\textcolor{{red}}{{\\textbf{{[FIGURE À INSÉRER — {c}] }}{d}}}\n\n", 3)
    t = subcmd(t, "fig", lambda o, p, c, l: f"\\begin{{figure}}\\centering\\includegraphics[width={o or '0.9'}\\textwidth]{{{p}}}\\caption{{Figure {labels.get(l,'')} – {c}}}\\end{{figure}}", 3, opt=True)
    t = re.sub(r"\\caption\{(?!Figure )", "\\\\caption{", t)
    t = subcmd(t, "source", lambda o, a: f"\n\n\\emph{{Source : {a}}}\n\n")
    t = subcmd(t, "route", lambda o, a: f"\\texttt{{{a}}}")
    t = subcmd(t, "code", lambda o, a: f"\\texttt{{{a}}}")
    for c in ("cref", "Cref"): t = subcmd(t, c, cref)
    t = subcmd(t, "ref", lambda o, a: labels.get(a, "??"))
    t = subcmd(t, "cite", lambda o, a: "[" + ", ".join(str(num.get(k.strip(), "?")) for k in a.split(",")) + "]")
    t = subcmd(t, "gls", lambda o, a: gl.get(a, a))
    t = subcmd(t, "rotatebox", lambda o, a, b: b, 2)
    t = t.replace("\\ding{51}", "✓").replace("\\xapp{}", "Xapp").replace("\\xapp", "Xapp")
    t = re.sub(r"\\begin\{remarque\}\[([^\]]*)\]", r"\\textbf{\1.} ", t).replace("\\end{remarque}", "")
    t = re.sub(r"\\(begin|end)\{landscape\}", "", t)
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    t = re.sub(r"\\(selectlanguage|markboth|addcontentsline)\{[^}]*\}(\{[^}]*\})*", "", t)
    t = re.sub(r"\\multirow\{[^}]*\}\{[^}]*\}\{([^}]*)\}", r"\1", t)
    return t

infos = (R/"config/infos.tex").read_text(encoding="utf-8")
vals = {}
for m in re.finditer(r"\\newcommand\{\\(\w+)\}", infos):
    v, _ = grp(infos, infos.index("{", m.end())); vals[m.group(1)] = v
def rep_infos(t):
    for k, v in sorted(vals.items(), key=lambda x: -len(x[0])):
        t = re.sub(r"\\" + k + r"(\{\})?(?![A-Za-z])", lambda m: v.replace("\\", "\\\\"), t) if False else re.sub(r"\\" + k + r"(\{\})?(?![A-Za-z])", lambda m, v=v: v, t)
    return t

main = (R/"main.tex").read_text(encoding="utf-8")
parts = re.findall(r"\\input\{((?:frontmatter|chapitres|annexes)/[^}]+)\}", main)
body = []
cover = (f"\\begin{{center}}\\includegraphics[width=0.35\\textwidth]{{figures/logos/logo_esprit.png}}\n\n"
         f"\\textbf{{PROJET DE FIN D'ÉTUDES}}\n\n\\textbf{{{vals['diplome']}}}\n\nSpécialité : {vals['specialite']}\n\n"
         f"\\textbf{{{vals['titrepfe']}}}\n\n\\includegraphics[width=0.3\\textwidth]{{figures/logos/logo_xapp.png}}\n\n"
         f"Réalisé par : {vals['auteur']}\n\nEncadrante ESPRIT : {vals['encadrantacad']}\n\nEncadrant Entreprise : {vals['encadrantent']}\n\n"
         f"Organisme d'accueil : {vals['organisme']}\n\n\\includegraphics[width=0.25\\textwidth]{{figures/logos/logo_xweb.png}}\n\nAnnée universitaire {vals['anneeuniv']}\\end{{center}}")
for p in parts:
    if p.endswith("couverture"): body.append(cover); continue
    if p == "chapitres/introduction":
        rows = "\n".join(f"{m.group(2)} & {m.group(3)}\\\\" for m in re.finditer(r"\\newacronym\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", (R/"config/glossaire.tex").read_text(encoding="utf-8")))
        body.append("\\chapter*{Liste des abréviations}\n\\begin{tabular}{ll}\n" + rows + "\n\\end{tabular}\n")
    if p == "annexes/annexes": body.append("\\appendix")
    body.append((R/(p+".tex")).read_text(encoding="utf-8"))
tex = rep_infos("\n\n".join(body))
tex = prep(tex)
# Bibliographie
bib = (R/"bibliographie.bib").read_text(encoding="utf-8")
ents = {}
for m in re.finditer(r"@\w+\{([^,]+),(.*?)\n\}", bib, re.S):
    f = dict((a.lower(), b.strip("{} ")) for a, b in re.findall(r"(\w+)\s*=\s*(\{.*?\}|\S+?),?\s*\n", m.group(2) + "\n"))
    ents[m.group(1).strip()] = f
refs = []
for k in order:
    f = ents.get(k, {})
    s = f"[{num[k]}] {f.get('author','').replace('{','').replace('}','')}. \\emph{{{f.get('title','').replace('{','').replace('}','')}}}"
    for x in ("booktitle", "school", "publisher", "institution"):
        if f.get(x): s += f", {f[x]}"
    if f.get("year"): s += f", {f['year']}"
    if f.get("url"): s += f". \\url{{{f['url']}}}"
    refs.append(s + ".")
tex += "\n\n\\chapter*{Bibliographie et webographie}\n\n" + "\n\n".join(refs)
doc = "\\documentclass{book}\\begin{document}\n" + tex + "\n\\end{document}"
(B/"rapport_flat.tex").write_text(doc, encoding="utf-8")
lua = B/"todo.lua"
lua.write_text('function Span(el)\n  local s = el.attributes["style"] or ""\n  if s:find("red") then el.attributes["custom-style"] = "Todo" end\n  return el\nend\n', encoding="utf-8")
out = R/"rapport_xapp.docx"
pypandoc.convert_file(str(B/"rapport_flat.tex"), "docx", format="latex", outputfile=str(out),
                      extra_args=["--toc", "--toc-depth=2", f"--resource-path={R}", f"--lua-filter={lua}", "-M", "lang=fr-FR", "-M", f"title=", "--top-level-division=chapter"])
d = Document(str(out))
st = d.styles
if "Todo" in [s.name for s in st]:
    s = st["Todo"]; s.font.color.rgb = RGBColor(0xC0, 0, 0); s.font.bold = True
for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
    if name in [s.name for s in st]: st[name].font.name = "Calibri"; st[name].font.size = Pt(11)
for sec in d.sections:
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.5); sec.top_margin = sec.bottom_margin = Cm(2.5)
for t in d.tables:
    t.style = d.styles["Table Grid"] if "Table Grid" in [s.name for s in st] else t.style
d.save(str(out))
print("OK", out)
