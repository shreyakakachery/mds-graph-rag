# MDS Knowledge Map: GraphRAG Edition 

An automated system to map the MDS curriculum using a local GraphRAG pipeline.

## Project Overview
This project builds upon my previous [MDS Knowledge Map](https://github.com/shreyakakachery/mds-knowledge-map) by replacing manual concept tagging with an automated AI pipeline. I extract technical concepts from course descriptions, with the use of a local LLM, to visualize the hidden prerequisites and knowledge flow across the program.

## Project Roadmap

### Phase 1: Setup & Extraction (current)

- [x] Conda environment and Git structure initialized.
- [x] Raw MDS block 1 course metadata compiled in `data/raw/courses.json`.
- [x] Structured system prompts defined in `prompts/`.
- [x] Modular utility functions for normalization and I/O created.
- [ ] Run LLM pipeline to generate `concepts.json`.

### Phase 2: GraphRAG & Visualization

- [ ] Map course-to-concept relationships using NetworkX.
- [ ] Render the knowledge map using Pyvis and Quarto.

## Tech Stack

TODO

## Project Structure

TODO

## Setup & Installation

TODO