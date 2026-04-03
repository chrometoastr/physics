---
description: Use $/$ $ for math in .ipynb markdown cells.
globs: "**/*.ipynb"
---

When editing Jupyter notebook markdown cells, use `$...$` for inline math and
`$$...$$` for block math. Avoid `\(` `\)` and `\[` `\]` to keep notation
consistent.

## Legacy bracket notation

Some notebooks use display math wrapped in `[` and `]` on their own lines, and
inline math in parentheses like `(\\mathbf E)`. To convert those to `$$` / `$`
in bulk, run from the repo root:

```bash
python tools/notebook_math_delimiters.py path/to/notebook.ipynb
```

Use `--dry-run` to see whether anything would change without writing. Use
`--no-merge-equals` if the notebook should not treat lines of only `====` as
a broken “equals” separator (rare).

To extend inline patterns, edit `INLINE_REPLACEMENTS` in
`tools/notebook_math_delimiters.py`.

**Shortcut phrase for the agent:** “Run the notebook math delimiter script on
this notebook” (or name the file).
