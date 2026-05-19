"""
File Organizer - Core Logic
Automatically sorts files into categorized folders by extension.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# Extension to folder mapping
EXTENSION_MAP = {
    # Images
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff"],
    # Videos
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm", ".m4v"],
    # Audio
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    # Documents
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    # Code
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".ts", ".json", ".xml", ".sql", ".sh", ".rb", ".go", ".rs"],
    # Archives
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    # Executables
    "Executables": [".exe", ".msi", ".deb", ".rpm", ".dmg", ".apk"],
    # Fonts
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
}


def get_category(extension: str) -> str:
    """Returns the folder category for a given file extension."""
    ext = extension.lower()
    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return category
    return "Others"


def organize_folder(source_dir: str, dry_run: bool = False) -> dict:
    """
    Organizes files in the given directory into categorized subfolders.

    Args:
        source_dir: Path to the folder to organize.
        dry_run: If True, only simulate — don't actually move files.

    Returns:
        A summary dict with moved files and counts.
    """
    source_path = Path(source_dir).resolve()

    if not source_path.exists():
        raise FileNotFoundError(f"Directory not found: {source_path}")
    if not source_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {source_path}")

    summary = {
        "source": str(source_path),
        "dry_run": dry_run,
        "moved": [],
        "skipped": [],
        "errors": [],
        "counts": {},
    }

    for file_path in source_path.iterdir():
        # Skip directories and hidden files
        if file_path.is_dir() or file_path.name.startswith("."):
            summary["skipped"].append(file_path.name)
            continue

        category = get_category(file_path.suffix)
        dest_folder = source_path / category

        dest_file = dest_folder / file_path.name

        # Handle filename conflicts
        if dest_file.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            stem = file_path.stem
            suffix = file_path.suffix
            dest_file = dest_folder / f"{stem}_{timestamp}{suffix}"

        try:
            if not dry_run:
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(dest_file))

            summary["moved"].append({
                "file": file_path.name,
                "from": str(file_path),
                "to": str(dest_file),
                "category": category,
            })
            summary["counts"][category] = summary["counts"].get(category, 0) + 1

        except Exception as e:
            summary["errors"].append({"file": file_path.name, "error": str(e)})

    return summary


def print_summary(summary: dict):
    """Prints a formatted summary of the organize operation."""
    print("\n" + "=" * 50)
    print("📁 FILE ORGANIZER SUMMARY")
    print("=" * 50)
    print(f"📂 Source : {summary['source']}")
    print(f"🧪 Dry Run: {'Yes (no files moved)' if summary['dry_run'] else 'No (files moved)'}")
    print("-" * 50)

    if summary["moved"]:
        print(f"\n✅ Moved {len(summary['moved'])} file(s):\n")
        for item in summary["moved"]:
            print(f"  [{item['category']}] {item['file']}")
    else:
        print("\n⚠️  No files were moved.")

    if summary["counts"]:
        print("\n📊 Category Breakdown:")
        for cat, count in sorted(summary["counts"].items()):
            print(f"  {cat:<15} → {count} file(s)")

    if summary["skipped"]:
        print(f"\n⏭️  Skipped {len(summary['skipped'])} item(s) (folders/hidden files)")

    if summary["errors"]:
        print(f"\n❌ Errors ({len(summary['errors'])}):")
        for err in summary["errors"]:
            print(f"  {err['file']}: {err['error']}")

    print("=" * 50 + "\n")
