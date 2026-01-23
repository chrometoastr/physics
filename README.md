# physics
This repository contains my notes on Physics and Mathematics. I want to 
understand more about General Relativity and Quantum Field Theory.

## Motivation
My [MOTIVATION](MOTIVATION.md) for studying physics is curiosity.

## Road Map
My [ROADMAP](ROADMAP.md) of concepts needed for a General Relativity and 
Quantum Field Theory. 

## Study Plan
My [STUDYPLAN](STUDYPLAN.md) outlines the subjects that I study in an
order that leads to a better understanding of GR and QFT. Links to notes 
will be added as I work through the plan.

## Progress
See [PROGRESS](PROGRESS.md) for updates on my progress.

### Git Hooks
This repo uses `pre-commit` to enforce a PROGRESS update per commit.

`uv add --dev pre-commit`

`uv run pre-commit install`

## Starting Jupyter Notebook

First checkout the repository and execute:

`uv sync`

and then

`uv run jupyter lab`

## Notebook Math Notation

When writing equations in `.ipynb` markdown cells, use `$...$` for inline math
and `$$...$$` for block math. Avoid `\(` `\)` and `\[` `\]` to keep notation
consistent.

## Export Notebook to PDF

Create the root output directory:

`mkdir -p pdf`

Export a single notebook to the root `pdf/` directory:

`uv run jupyter nbconvert --to pdf "path/to/notebook.ipynb" --output-dir pdf`

Hide all code (show only results, preferred):

`jupyter nbconvert notebook.ipynb --to pdf --no-input`

Hide code for specific cells (tag-based):

1. In Jupyter, enable `View -> Cell Toolbar -> Tags`.
2. Add the tag `hide-input` to any cell where you want to hide code.
3. Export with tag removal enabled:

`uv run jupyter nbconvert --to pdf "path/to/notebook.ipynb" --output-dir pdf --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_input_tags='{"hide-input"}'`

Show both code and results:

`uv run jupyter nbconvert --to pdf "path/to/notebook.ipynb" --output-dir pdf`

### Example: Space and Time Notebook

Show both code and results:

`uv run jupyter nbconvert --to pdf "notebooks/physics/06_relativity/books/Spacetime and Geometry/01_SpecialRelativity/01_02_SpecialRelativity_SpaceAndTime.ipynb" --output-dir pdfs`

Hide all code (show only results):

`uv run jupyter nbconvert "notebooks/physics/06_relativity/books/Spacetime and Geometry/01_SpecialRelativity/01_02_SpecialRelativity_SpaceAndTime.ipynb" --to pdf --no-input --output-dir pdfs`