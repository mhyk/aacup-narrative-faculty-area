# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an academic documentation project for creating narrative profiles for institutional accreditation (AACUP - Association of Accrediting Agencies of the Philippines). The repository contains Markdown files that document faculty development programs and institutional parameters for the MSU-IIT College of Computer Studies.

## Document Processing Commands

### PDF Generation
Use Pandoc with the Eisvogel template to generate PDFs from Markdown files:

```bash
# Generate Area A instruction document
pandoc narrative-profile-area-A-instruction.md -N -V papersize:a4paper --from markdown --top-level-division="chapter" --template "eisvogel.tex" -o narrative-profile-area-A-instruction.pdf

# Generate main narrative profile
pandoc narrative_profile.md -N -V papersize:a4paper --from markdown --top-level-division="chapter" --template "eisvogel.tex" -o narrative_profile.pdf
```

**Required Dependencies:**
- Pandoc (document converter)
- LaTeX distribution (for PDF generation)
- Eisvogel template (eisvogel.tex)

## File Structure and Purpose

### Core Documents
- `narrative_profile.md` - Main faculty development narrative profile (Area A)
- `narrative-profile-area-A-instruction.md` - Instructions for Area A documentation
- `narrative_profile_reference.md` - Reference materials and guidelines
- `eisvogel.tex` - LaTeX template for PDF generation
- `pandoc-command.txt` - Command reference for document processing

### Generated Files
- `*.pdf` - Generated PDF documents (do not edit directly)

## Content Architecture

The narrative profile follows a structured format for academic accreditation:

1. **Well-Defined Objectives** - Faculty development goals and strategic alignment
2. **Projects/Activities** - Specific programs and initiatives
3. **Systematic Procedures** - Implementation frameworks and quality assurance
4. **Reasonable Budgets** - Financial planning and resource allocation
5. **Materials and Resources** - Infrastructure and support systems
6. **Faculty Participation** - Engagement metrics and activities
7. **Distinctions and Achievements** - Recognition and outcomes
8. **Best Practices** - Innovative approaches and proven methodologies

## Document Conventions

### Update Markers
Files contain `[UPDATE NEEDED: 2021-2025 Data]` markers indicating sections requiring current information. When updating:
- Replace placeholder text with actual data
- Remove UPDATE NEEDED markers after completion
- Maintain academic tone and formal documentation style

### Reference System
Documents use PPP (Program Profile Pages) and AACUP Parameter folder references:
- PPP Pages X-Y: Specific page references in supporting documentation
- AACUP Parameter folders: Organized evidence documentation
- Cross-references should be maintained when editing

### Academic Style Guidelines
- Use formal academic writing tone
- Include quantitative data and metrics where possible
- Maintain consistency with institutional terminology
- Follow accreditation documentation standards

## Common Tasks

### Updating Content
When updating narrative sections:
1. Locate UPDATE NEEDED markers
2. Replace with current, accurate data
3. Verify references and citations
4. Regenerate PDF after changes

### Adding New Sections
Follow existing structure:
- Use consistent heading hierarchy
- Include reference citations
- Add appropriate UPDATE NEEDED markers for future maintenance
- Maintain alignment with accreditation parameters