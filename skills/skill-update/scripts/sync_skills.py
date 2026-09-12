"""
Skill & Command Synchronizer for SuperClaude
Audits and synchronizes commands, agents, and skills between the workspace repository and ~/.claude.
"""

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


def get_claude_dir() -> Path:
    return Path.home() / ".claude"


def sync_directory(src: Path, dest: Path, dry_run: bool = False) -> tuple[int, int]:
    """Sync files from src to dest. Returns (updated_count, new_count)."""
    if not src.exists():
        return 0, 0

    dest.mkdir(parents=True, exist_ok=True)
    updated = 0
    created = 0

    for src_file in src.rglob("*"):
        if src_file.is_dir() or ".git" in src_file.parts:
            continue

        rel_path = src_file.relative_to(src)
        dest_file = dest / rel_path

        if not dest_file.exists():
            created += 1
            if not dry_run:
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dest_file)
        elif not filecmp.cmp(src_file, dest_file, shallow=False):
            updated += 1
            if not dry_run:
                shutil.copy2(src_file, dest_file)

    return updated, created


def audit_and_sync(repo_root: Path, dry_run: bool = False, clean: bool = False) -> None:
    claude_dir = get_claude_dir()
    print(f"Target directory: {claude_dir}")
    print(f"Source repository: {repo_root}")
    if dry_run:
        print("[DRY RUN] No files will be modified.\n")

    components = [
        ("Commands", repo_root / "commands", claude_dir / "commands"),
        ("Agents", repo_root / "agents", claude_dir / "agents"),
        ("Skills", repo_root / "skills", claude_dir / "skills"),
    ]

    total_upd = 0
    total_new = 0

    for name, src, dest in components:
        if not src.exists():
            continue
        upd, new = sync_directory(src, dest, dry_run=dry_run)
        total_upd += upd
        total_new += new
        status = "preview" if dry_run else "applied"
        print(f"{name:<10}: {new} new, {upd} updated ({status})")

    # Clean legacy sc directory if requested
    if clean:
        legacy_sc = claude_dir / "commands" / "sc"
        if legacy_sc.exists():
            if not dry_run:
                shutil.rmtree(legacy_sc)
            print("Cleanup   : Removed legacy 'commands/sc' directory")

    print("\nSynchronization complete.")


def main():
    parser = argparse.ArgumentParser(description="Synchronize SuperClaude skills and commands")
    parser.add_argument("--repo", type=str, default=str(Path(__file__).resolve().parents[3]), help="Path to super-claude repository")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--clean", action="store_true", help="Remove legacy/deprecated commands")
    args = parser.parse_args()

    repo_path = Path(args.repo)
    if not repo_path.exists():
        print(f"Error: Repository path not found: {repo_path}", file=sys.stderr)
        sys.exit(1)

    audit_and_sync(repo_path, dry_run=args.dry_run, clean=args.clean)


if __name__ == "__main__":
    main()
