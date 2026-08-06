#!/usr/bin/env python3
"""Render Mermaid (.mmd) files to PNG using @mermaid-js/mermaid-cli.

Usage:
  python scripts/render_mermaid.py path/to/diagram.mmd
  python scripts/render_mermaid.py path/to/folder/   # all .mmd in folder
  python scripts/render_mermaid.py file.mmd -o out.png -t dark -w 1600

Requires Node.js/npx. Installs mermaid-cli on first run via npx -y.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def find_npx() -> str:
    npx = shutil.which("npx")
    if not npx:
        raise RuntimeError("npx not found. Install Node.js: https://nodejs.org/")
    return npx


def render_one(
    input_path: Path,
    output_path: Path | None = None,
    theme: str = "default",
    width: int | None = None,
    background: str = "white",
) -> Path:
    if not input_path.is_file():
        raise FileNotFoundError(f"Input not found: {input_path}")
    if input_path.suffix.lower() != ".mmd":
        raise ValueError(f"Expected .mmd file, got: {input_path}")

    out = output_path or input_path.with_suffix(".png")
    out.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        find_npx(),
        "-y",
        "@mermaid-js/mermaid-cli",
        "-i",
        str(input_path.resolve()),
        "-o",
        str(out.resolve()),
        "-b",
        background,
        "-t",
        theme,
    ]
    if width:
        cmd.extend(["-w", str(width)])

    print(f"Rendering {input_path.name} -> {out.name}")
    subprocess.run(cmd, check=True)
    return out


def collect_mmd_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        files = sorted(path.glob("*.mmd"))
        if not files:
            raise FileNotFoundError(f"No .mmd files in {path}")
        return files
    raise FileNotFoundError(f"Path not found: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Mermaid .mmd to PNG")
    parser.add_argument("path", type=Path, help=".mmd file or directory containing .mmd files")
    parser.add_argument("-o", "--output", type=Path, help="Output PNG (single file mode only)")
    parser.add_argument("-t", "--theme", default="default", choices=["default", "dark", "forest", "neutral"])
    parser.add_argument("-w", "--width", type=int, help="Output width in pixels")
    parser.add_argument("-b", "--background", default="white", help="Background color")
    args = parser.parse_args()

    try:
        files = collect_mmd_files(args.path)
        for mmd in files:
            out = args.output if len(files) == 1 and args.output else None
            render_one(mmd, out, theme=args.theme, width=args.width, background=args.background)
        print(f"Done: {len(files)} diagram(s) rendered.")
        return 0
    except subprocess.CalledProcessError as exc:
        print(f"mermaid-cli failed (exit {exc.returncode})", file=sys.stderr)
        return exc.returncode or 1
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
