#!/usr/bin/env python3
"""
Render a Jinja2 template with parameters from a vars file.
Supports:
 - simple key=value lines
 - JSON files (.json)
 - YAML files (.yaml/.yml)
"""
from __future__ import annotations
import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Dict

try:
    import yaml  # optional
except Exception:
    yaml = None

from jinja2 import Environment, FileSystemLoader, select_autoescape, TemplateSyntaxError

LOG = logging.getLogger("injector")


def read_kv_file(path: Path) -> Dict[str, str]:
    params = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            params[k.strip()] = v.strip()
        else:
            LOG.warning("Skipping invalid line in vars file: %r", line)
    return params


def read_vars(path: Path) -> Dict:
    suffix = path.suffix.lower()
    if suffix in (".json",):
        return json.loads(path.read_text(encoding="utf-8"))
    if suffix in (".yaml", ".yml"):
        if yaml is None:
            LOG.error("PyYAML not installed. Install with: pip install pyyaml")
            raise SystemExit(2)
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    # fallback to key=value text
    return read_kv_file(path)


def make_env(template_dir: Path) -> Environment:
    # Use a small, safe environment. You can expand filters here.
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(enabled_extensions=("html", "xml")),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_template(template_path: Path, vars_path: Path, out_path: Path) -> None:
    template_dir = template_path.parent
    env = make_env(template_dir)
    try:
        template = env.get_template(template_path.name)
    except TemplateSyntaxError as e:
        LOG.error("Template syntax error: %s", e)
        raise SystemExit(2)
    params = read_vars(vars_path)
    rendered = template.render(**(params or {}))
    out_path.write_text(rendered, encoding="utf-8")
    LOG.info("Rendered template saved to %s", out_path)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Render Jinja2 templates with vars")
    p.add_argument("template", type=Path, help="Template file (jinja2 template)")
    p.add_argument("output", type=Path, help="Output file to write")
    p.add_argument(
        "-v",
        "--vars",
        type=Path,
        default=Path("vars"),
        help="Vars file (key=value lines) or JSON (.json) or YAML (.yaml/.yml). Default: ./vars",
    )
    p.add_argument("-q", "--quiet", action="store_true", help="Less verbose")
    p.add_argument("-V", "--version", action="version", version="injector 1.0")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO if not args.quiet else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )
    LOG.debug("Args: %r", args)

    if not args.template.exists():
        LOG.error("Template file not found: %s", args.template)
        return 2
    if not args.vars.exists():
        LOG.error("Vars file not found: %s", args.vars)
        return 2

    try:
        render_template(args.template, args.vars, args.output)
    except Exception as e:
        LOG.error("Failed to render: %s", e)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
