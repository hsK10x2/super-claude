"""Command Line Interface for Skill MCP Hub."""

import argparse
import sys
import os
from .server import run_stdio, run_sse, scanner, mcp

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(
        description="Skill MCP Hub: Universal MCP Server for AI Agent Skills"
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
        help="Transport protocol to use: 'stdio' (default) or 'sse'"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host address for SSE transport (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8765,
        help="Port number for SSE transport (default: 8765)"
    )
    parser.add_argument(
        "--skills-dir",
        action="append",
        dest="skills_dirs",
        help="Additional directory path to scan for skills (can be specified multiple times)"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all discovered skills in terminal and exit"
    )

    args = parser.parse_args()

    if args.skills_dirs:
        for p in args.skills_dirs:
            p_abs = os.path.abspath(p)
            if p_abs not in scanner.search_paths:
                scanner.search_paths.insert(0, p_abs)

    skills = scanner.scan()

    if args.list:
        print("=" * 60)
        print(f"Skill MCP Hub — Discovered Skills ({len(skills)})")
        print("=" * 60)
        for name, meta in sorted(skills.items()):
            scripts_str = f" [scripts: {', '.join(meta.scripts)}]" if meta.scripts else ""
            print(f"• {name:<25} ({meta.source}) {scripts_str}")
            desc_preview = meta.description.replace("\n", " ")[:70]
            print(f"    {desc_preview}...")
        print("=" * 60)
        sys.exit(0)

    if args.transport == "stdio":
        run_stdio()
    elif args.transport == "sse":
        print(f"Starting Skill MCP Hub on SSE http://{args.host}:{args.port}/sse ...")
        run_sse(host=args.host, port=args.port)

if __name__ == "__main__":
    main()
