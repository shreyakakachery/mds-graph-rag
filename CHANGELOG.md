# Changelog

All notable changes to the **MDS Knowledge Map v2** project will be documented in this file.

## 2026-02-17

### Added

- Course descriptions for all 24 MDS courses.
- Created `scripts/build_graph.py` using NetworkX and Pyvis to model course relationships.
- Initialized Quarto site with `_quarto.yml`, `index.qmd`, and custom `styles.css`.
- Created `.github/workflows/publish.yml` to automate the Python graph build and Quarto deployment to GitHub Pages.
- Filled the Tech Stack and Project Structure sections in `README.md`

### Changed

- Expanded `data/processed/concepts.json` from the Block 1 prototype to include all 24 MDS courses.
- Modified `extract_concepts.py` to use a maximalist prompt for higher density concept extraction.
- Modified the Project Roadmap section in `README.md` to include a TODO list.

### Fixed

- Resolved `MissingEnvVarsError` by renaming `.env` files and updating `.gitignore` to prevent environment clashes.
- Added `lib/` and generated HTML files to `.gitignore` to maintain a clean repository state.

### Removed

- Deprecated `data/raw/courses.json` in favor of more detailed course description schemas.

## 2026-01-29

### Added

- Initial project folder structure.
- Basic concept extraction script using local Ollama (Llama 3).
- Block 1 course descriptions in `data/raw/courses.json`.
- Conceptual project roadmap and placeholder sections in README.