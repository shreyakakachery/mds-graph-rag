# MDS Knowledge Map: GraphRAG Edition 

An automated system to map the MDS curriculum using a local GraphRAG pipeline.

## Project Overview

This project builds upon my previous [MDS Knowledge Map](https://github.com/shreyakakachery/mds-knowledge-map) by replacing manual concept tagging with an automated AI pipeline. I extract technical concepts from course descriptions, with the use of a local LLM, to visualize the hidden prerequisites and knowledge flow across the program.

## Project Roadmap

### Phase 1: Knowledge Extraction

- [x] Initial local LLM pipeline for concept extraction
- [x] Process full MDS curriculum (24 courses) into structured concepts.json

### Phase 2: Graph Construction & Interactive UI

- [x] Build similarity-based adjacency matrix using NetworkX
- [x] Implement edge-weighting logic based on shared concept density
- [x] Render interactive map via Pyvis
- [x] Automate deployment via GitHub Actions & Quarto

### TODO

- [ ] GitHub Scraper to fetch public course READMEs for better concept extraction
- [ ] Louvain Community Detection for automated topic clustering
- [ ] Visualize prerequisites for specific advanced topics
- [ ] Integrate RAG interface to query the graph

## Tech Stack

- Python 3.10
- Ollama (Llama 3)
- NetworkX
- Pyvis
- Quarto

## Project Structure

- `scripts/`: Python scripts for extraction and graph building
- `prompts/`: System prompts for the LLM
- `data/processed`: Course concepts
- `.github/workflows/`: CI/CD automation logic
- `index.qmd`: The Quarto homepage

## Setup & Installation

TODO