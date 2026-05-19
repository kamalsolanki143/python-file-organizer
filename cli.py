"""
CLI Entry Point for Python File Organizer
Usage: python -m file_organizer <path> [--dry-run]
"""

import argparse
import sys
from organizer import organize_folder, print_summary

def main():
    parser = argparse.ArgumentParser(
        prog="file-organizer",
        description="🗂️  Automatically organize files into categorized folders.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the folder you want to organize.\nDefaults to current directory (.).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what will happen without actually moving any files.",
    )

    args = parser.parse_args()

    print(f"\n🗂️  Python File Organizer")
    print(f"   Target: {args.path}")
    if args.dry_run:
        print("   Mode  : DRY RUN (no files will be moved)\n")

    try:
        summary = organize_folder(args.path, dry_run=args.dry_run)
        print_summary(summary)
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
    except NotADirectoryError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
