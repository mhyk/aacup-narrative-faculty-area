# AACUP Narrative Faculty Area Documentation

This repository contains academic documentation for creating narrative profiles for institutional accreditation under the Association of Accrediting Agencies of the Philippines (AACUP). The documentation focuses on faculty development programs and institutional parameters for the MSU-IIT College of Computer Studies.

## Overview

The project generates formal accreditation documentation in PDF format from Markdown source files, specifically focusing on Area A (Faculty Development) of the AACUP accreditation framework.

## Key Files

- `narrative_profile.md` - Main faculty development narrative profile
- `narrative-profile-area-A-instruction.md` - Documentation instructions for Area A
- `narrative_profile_reference.md` - Reference materials and guidelines
- `eisvogel.tex` - LaTeX template for PDF generation

## PDF Generation

Generate PDFs using Pandoc with the Eisvogel template:

```bash
# Generate Area A instruction document
pandoc narrative-profile-area-A-instruction.md -N -V papersize:a4paper --from markdown --top-level-division="chapter" --template "eisvogel.tex" -o narrative-profile-area-A-instruction.pdf

# Generate main narrative profile
pandoc narrative_profile.md -N -V papersize:a4paper --from markdown --top-level-division="chapter" --template "eisvogel.tex" -o narrative_profile.pdf
```

## Requirements

### Windows Users

1. **Install Pandoc**
   - Download from https://pandoc.org/installing.html
   - Or use package manager: `winget install JohnMacFarlane.Pandoc`

2. **Install LaTeX Distribution**
   - **MiKTeX** (recommended): Download from https://miktex.org/download
   - **TeX Live**: Download from https://www.tug.org/texlive/windows.html
   - Ensure LaTeX is added to your system PATH

3. **Eisvogel Template**
   - Template file `eisvogel.tex` is included in this repository
   - Must be in the same directory as your Markdown files

### Verification

Test your installation:
```cmd
pandoc --version
pdflatex --version
```

## Document Structure

The narrative profile follows AACUP accreditation standards with sections covering:

1. Well-Defined Objectives
2. Projects/Activities
3. Systematic Procedures
4. Reasonable Budgets
5. Materials and Resources
6. Faculty Participation
7. Distinctions and Achievements
8. Best Practices

## Updating Content

Look for `[UPDATE NEEDED: 2021-2025 Data]` markers throughout the documents. Replace these with current data and remove the markers when complete.