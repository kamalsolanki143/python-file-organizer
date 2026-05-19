"""
Unit Tests for Python File Organizer
Run with: pytest tests/
"""

import os
import shutil
import tempfile
from pathlib import Path

import pytest
from file_organizer.organizer import get_category, organize_folder


# ---------- get_category tests ----------

def test_image_extensions():
    assert get_category(".jpg") == "Images"
    assert get_category(".PNG") == "Images"
    assert get_category(".gif") == "Images"


def test_video_extensions():
    assert get_category(".mp4") == "Videos"
    assert get_category(".MKV") == "Videos"


def test_document_extensions():
    assert get_category(".pdf") == "Documents"
    assert get_category(".docx") == "Documents"


def test_code_extensions():
    assert get_category(".py") == "Code"
    assert get_category(".js") == "Code"


def test_unknown_extension():
    assert get_category(".xyz") == "Others"
    assert get_category("") == "Others"


# ---------- organize_folder tests ----------

@pytest.fixture
def temp_dir():
    """Creates a temporary directory with sample files for testing."""
    d = tempfile.mkdtemp()
    # Create sample files
    Path(d, "photo.jpg").touch()
    Path(d, "video.mp4").touch()
    Path(d, "notes.txt").touch()
    Path(d, "script.py").touch()
    Path(d, "archive.zip").touch()
    Path(d, "unknown.xyz").touch()
    yield d
    shutil.rmtree(d)


def test_organize_moves_files(temp_dir):
    summary = organize_folder(temp_dir, dry_run=False)
    assert len(summary["moved"]) == 6
    assert len(summary["errors"]) == 0

    # Check folders were created
    assert (Path(temp_dir) / "Images").exists()
    assert (Path(temp_dir) / "Videos").exists()
    assert (Path(temp_dir) / "Documents").exists()
    assert (Path(temp_dir) / "Code").exists()
    assert (Path(temp_dir) / "Archives").exists()
    assert (Path(temp_dir) / "Others").exists()


def test_dry_run_does_not_move(temp_dir):
    summary = organize_folder(temp_dir, dry_run=True)
    assert len(summary["moved"]) == 6
    # Files should still be in root (not moved)
    assert (Path(temp_dir) / "photo.jpg").exists()
    assert not (Path(temp_dir) / "Images").exists()


def test_invalid_directory():
    with pytest.raises(FileNotFoundError):
        organize_folder("/nonexistent/path/abc")


def test_counts_summary(temp_dir):
    summary = organize_folder(temp_dir, dry_run=False)
    assert summary["counts"]["Images"] == 1
    assert summary["counts"]["Videos"] == 1
    assert summary["counts"]["Code"] == 1
