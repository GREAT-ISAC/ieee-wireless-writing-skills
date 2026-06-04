#!/usr/bin/env bash
set -euo pipefail

paper_dir="${1:-paper}"

if [ ! -d "$paper_dir" ]; then
  echo "Paper directory not found: $paper_dir" >&2
  exit 1
fi

if [ ! -f "$paper_dir/main.tex" ]; then
  echo "main.tex not found in: $paper_dir" >&2
  exit 1
fi

if ! command -v latexmk >/dev/null 2>&1; then
  echo "latexmk is required to build the IEEE PDF." >&2
  exit 1
fi

mkdir -p "$paper_dir/build"
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir="$paper_dir/build" "$paper_dir/main.tex"

echo "Built: $paper_dir/build/main.pdf"
