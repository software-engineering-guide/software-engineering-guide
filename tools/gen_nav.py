#!/usr/bin/env python3
import os, re, glob
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH=f"{ROOT}/chapters"
def read(p): return open(p).read()
def write(p,t): open(p,"w").write(t)

PART_TITLES={1:"People",2:"Software Programming",3:"Systems",4:"Security",5:"UI/UX Design",
6:"Artificial Intelligence",7:"Data, Analytics, and Insight",8:"Automation",
9:"Operations, Reliability, and Observability",10:"Project/Product/Program Management",
11:"Flow: Discovery and Delivery Pipelines",12:"Appendices"}

def dec(fp):
    m=re.match(r'(\d+)\.(\d+)-', os.path.basename(fp)); return (int(m.group(1)),int(m.group(2)))
def h1title(fp):
    for ln in read(fp).splitlines():
        if ln.startswith("# "): return ln[2:].strip()
    return os.path.basename(fp)

files=sorted(glob.glob(f"{CH}/*.md"), key=dec)
byp={}
for f in files: byp.setdefault(dec(f)[0],[]).append(f)

# ---- TOC body (shared by README + TOC file) ----
def toc_body(pathprefix):
    out=[]
    for p in sorted(byp):
        out.append(f"### Part {p}: {PART_TITLES[p]}")
        for f in sorted(byp[p], key=dec):
            t=h1title(f); rel=f"{pathprefix}{os.path.basename(f)}"
            # strip redundant "Introduction to Part N: " for intro rows -> label "N.0 Introduction"
            label=t
            m=re.match(r'(\d+\.0)\s+Introduction', t)
            if m: label=f"{m.group(1)} Introduction"
            out.append(f"- [{label}]({rel})")
        out.append("")
    return "\n".join(out)

# ---- README ----
readme=f"""# Software Engineering Recommendations

A comprehensive guidebook of best practices for **large software developer
teams**, including **enterprise and government** organizations. It spans
engineering culture, programming craft, architecture, security, AI, data and
analytics, UI/UX, automation, delivery, operations, flow, management, and the
full breadth of the software engineering body of knowledge, treating
compliance, scale, and long-lived systems as first-class concerns.

- **[What is software engineering?](front-matter/what-is-software-engineering.md):** start here
- **[Introduction](front-matter/introduction.md):** what this book is and how to read it
- **[Table of contents](front-matter/table-of-contents.md):** the full chapter list
- **[Specification (spec/index.md)](spec/index.md):** outline, principles, backlog, and checklists

## How to read this guidebook

Parts are whole numbers; chapters are decimals. Chapter **N.0** introduces each
part; **N.1, N.2, …** are its chapters. Part 12 collects the appendices
(glossary, checklists, templates, maturity self-assessment, references,
adoption roadmap, and index). Each chapter states principles, recommendations,
trade-offs, examples (enterprise and government), a business case (ROI/TCO),
anti-patterns, a maturity model, discussion questions, and references. Adopt
incrementally; do not big-bang.

## Table of contents

{toc_body("chapters/")}
## Cross-cutting themes

Security, privacy, and accessibility appear in every part, not once. Automation
and "everything as code" underpin repeatability and audit. Measurement and
feedback loops turn practices into learning systems. Documentation and
knowledge continuity protect against turnover and scale. Regulatory and
government constraints are treated as design inputs, not afterthoughts.
"""
write(f"{ROOT}/README.md", readme)

# ---- front-matter/table-of-contents.md ----
toc=f"""# Table of contents

Parts are whole numbers; chapters are decimals (chapter **N.0** introduces each
part). See also the [Introduction](introduction.md).

{toc_body("../chapters/")}"""
write(f"{ROOT}/front-matter/table-of-contents.md", toc)

# ---- chapters/12.7-index.md (subject index) ----
idxchap=[f for f in files if dec(f)[1]>=1 and dec(f)[0]<=11]  # substantive chapters, parts 1-11
terms=["accessibility","agile","API","architecture decision record","A/B testing","blameless","blue-green",
 "bounded context","canary","capacity planning","chaos engineering","CI/CD","circuit breaker","code review",
 "compliance","configuration management","containers","continuous delivery","Conway's Law","CQRS","data governance",
 "data mesh","dependency","design system","DevSecOps","Diátaxis","Domain-Driven Design","DORA","encryption",
 "error budget","estimation","event sourcing","experimentation","feature flag","FedRAMP","FinOps","fitness function",
 "formal methods","GDPR","GitOps","hallucination","incident","InnerSource","Kanban","Kubernetes","Little's Law",
 "maintenance","maturity model","microservices","MLOps","monorepo","north star","observability","OKR",
 "OpenTelemetry","OWASP","pair programming","plain language","policy as code","postmortem","privacy",
 "progressive delivery","prompt engineering","quality attributes","queueing theory","RAG","refactoring",
 "reliability","requirements","retrospective","reuse","RFC","risk register","RTO","SBOM","Scrum",
 "secrets management","service level objective","shift-left","SLSA","SMART","SOLID","STRIDE","supply chain",
 "technical debt","test automation","threat modeling","toil","total cost of ownership","traceability",
 "trunk-based development","UML","utilization","value stream","vector database","velocity","WCAG","zero-trust"]
entries={}
for term in terms:
    pat=re.compile(r'(?i)(?<![A-Za-z])'+re.escape(term)+r'(?![A-Za-z])')
    hits=[f"{dec(f)[0]}.{dec(f)[1]}" for f in idxchap if pat.search(read(f))]
    if hits: entries[term]=hits
out=["# 12.7 Index","","A subject index of key concepts and the chapters that cover them.",
 "Terms are defined in the Glossary (chapter 12.1).",""]
byl={}
for term in sorted(entries,key=lambda s:s.lower()):
    L=term[0].upper() if term[0].isalpha() else "#"; byl.setdefault(L,[]).append(term)
for L in sorted(byl):
    out+=[f"## {L}",""]+[f"- **{t}**: {', '.join(entries[t])}" for t in byl[L]]+[""]
write(f"{CH}/12.7-index.md","\n".join(out))

# spec/index.md and spec/structure.md are hand-authored source-of-truth (not generated here).

print("nav generated. parts:", {p:len(byp[p]) for p in sorted(byp)})
print("index terms:", len(entries))
