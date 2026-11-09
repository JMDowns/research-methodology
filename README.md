# Research methodology

A method for running cited, checked research with Claude Code, plus the studies that tested the method.

Start with `CLAUDE.md`, which is the method itself. Claude Code loads it automatically when you work in this folder.

## Starting a study

```bash
./research.sh "your topic"
```

This creates a folder for the topic and starts a Claude Code session with the method loaded. `scripts/find_prior.py` needs `scikit-learn`.

## What's here

- `CLAUDE.md`: search rules, study format, citation standard, token rules
- `AUTONOMOUS-RESEARCH-STANDARD.md`: running a batch of studies without stopping to ask
- `how-to-write-proposals-and-studies/`: proposal template, proposal levels, review checklist
- `templates/STUDY_TEMPLATE.md`: the study README template
- `studies/`: the evidence behind the method (listed in `INDEX.md`)

## Left out on purpose

This repo was split out of a larger private research repo. Topic studies are not included. In the method studies, project names were anonymized and some raw data was removed, so a few studies mention files such as probe logs or test runs that are not in this repo.
