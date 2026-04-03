#!/usr/bin/env python3
"""
Convert legacy notebook markdown math delimiters to Jupyter/MathJax form:

  - Display: lines containing only '[' ... ']' (block) -> $$ ... $$
  - Optional: merge spurious '====' separator lines into ' = ' (common paste artifact)
  - Fix common LaTeX typos: F^{}*{sub} -> F^{}_{sub}
  - Inline: replace (\\...) and selected (...) math-like fragments with $...$

Run:
  python tools/notebook_math_delimiters.py path/to/notebook.ipynb
  python tools/notebook_math_delimiters.py path/to/notebook.ipynb --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def merge_equals_separator_lines(lines: list[str]) -> list[str]:
    """Turn 'expr' + line of only '=' + blanks + 'rest' into 'expr = rest'."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if (
            i + 1 < len(lines)
            and (lines[i + 1] or "").strip()
            and re.fullmatch(r"=+", (lines[i + 1] or "").strip())
        ):
            j = i + 2
            while j < len(lines) and not (lines[j] or "").strip():
                j += 1
            if j < len(lines):
                merged = line.rstrip() + " = " + lines[j].lstrip()
                out.append(merged)
                i = j + 1
                continue
        out.append(line)
        i += 1
    return out


def strip_markdown_headers_inside_block(lines: list[str]) -> list[str]:
    """Remove accidental '## ' at line start inside what will become math."""
    return [re.sub(r"^##\s+", "", ln) for ln in lines]


def bracket_blocks_to_dollars(text: str, merge_equals: bool) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "[":
            block_lines: list[str] = []
            i += 1
            while i < len(lines) and lines[i].strip() != "]":
                block_lines.append(lines[i])
                i += 1
            if i < len(lines) and lines[i].strip() == "]":
                i += 1
            inner = strip_markdown_headers_inside_block(block_lines)
            if merge_equals:
                inner = merge_equals_separator_lines(inner)
            body = "\n".join(inner).strip("\n")
            out.append("$$")
            if body:
                out.append(body)
            out.append("$$")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def fix_latex_typos(text: str) -> str:
    # Common corruption: * instead of _ for subscripts (narrow replacements)
    text = text.replace("F^\\nu{}*{", "F^\\nu{}_{")
    text = text.replace("F*{\\alpha\\beta}", "F_{\\alpha\\beta}")
    text = text.replace("F*{\\alpha}", "F_{\\alpha}")
    return text


# Longer patterns first. Extend this list as you encounter new notebooks.
INLINE_REPLACEMENTS: list[tuple[str, str]] = [
    ("**products of (F)**", "**products of $F$**"),
    (r"(F^{\mu\alpha}F^\nu{}_{\alpha})", r"$F^{\mu\alpha}F^\nu{}_{\alpha}$"),
    (r"(\frac14 g^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta})", r"$\frac14 g^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}$"),
    (r"(\mathbf E\times \mathbf B=0)", r"$\mathbf E\times \mathbf B=0$"),
    (r"(T^{33}\neq 0)", r"$T^{33}\neq 0$"),
    (r"(T^{30}\neq 0)", r"$T^{30}\neq 0$"),
    (r"(T^{03}\neq 0)", r"$T^{03}\neq 0$"),
    (r"(T^{00}\neq 0)", r"$T^{00}\neq 0$"),
    (r"(g_{\mu\nu})", r"$g_{\mu\nu}$"),
    (r"(T^{\mu\nu})", r"$T^{\mu\nu}$"),
    (r"(F_{\mu\nu})", r"$F_{\mu\nu}$"),
    (r"(\mathbf E)", r"$\mathbf E$"),
    (r"(\mathbf B)", r"$\mathbf B$"),
    (r"* (T^{\mu\nu}) is built from **products of (F)**", r"* $T^{\mu\nu}$ is built from **products of $F$**"),
    (r"* (F) contains", r"* $F$ contains"),
    (r"(+z)", r"$+z$"),
]


def apply_inline_replacements(text: str) -> str:
    for old, new in INLINE_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def process_markdown_cell_source(source: list[str], merge_equals: bool) -> list[str]:
    text = "".join(source)
    text = bracket_blocks_to_dollars(text, merge_equals=merge_equals)
    text = fix_latex_typos(text)
    text = apply_inline_replacements(text)
    # Preserve line-based cell format
    parts = text.split("\n")
    if not parts:
        return []
    return [p + "\n" for p in parts[:-1]] + ([parts[-1] + "\n"] if parts[-1] else [""])


def process_notebook(path: Path, merge_equals: bool, dry_run: bool) -> bool:
    raw = path.read_text(encoding="utf-8")
    nb = json.loads(raw)
    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        old = "".join(cell.get("source", []))
        new_list = process_markdown_cell_source(cell["source"], merge_equals)
        new = "".join(new_list)
        if new != old:
            changed = True
            cell["source"] = new_list
    if not changed:
        print(f"No changes: {path}", file=sys.stderr)
        return True
    if dry_run:
        print(f"Would update: {path}")
        return True
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated: {path}")
    return True


def main() -> int:
    p = argparse.ArgumentParser(description="Convert [ ] / () math delimiters in notebook markdown.")
    p.add_argument("notebook", type=Path, help=".ipynb path")
    p.add_argument(
        "--no-merge-equals",
        action="store_true",
        help="Do not merge lines that are only '====' into ' = '",
    )
    p.add_argument("--dry-run", action="store_true", help="Parse only; do not write")
    args = p.parse_args()
    if not args.notebook.suffix == ".ipynb":
        print("Expected a .ipynb file", file=sys.stderr)
        return 2
    return 0 if process_notebook(args.notebook, merge_equals=not args.no_merge_equals, dry_run=args.dry_run) else 1


if __name__ == "__main__":
    raise SystemExit(main())
