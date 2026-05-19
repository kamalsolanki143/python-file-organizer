# 🗂️ Python File Organizer

A beginner-friendly Python automation project that automatically organizes files into categorized folders based on file type.

---

## ✨ Features

- 📁 Organizes files into folders like Images, Videos, Documents, Audio, Code, and Others
- ⚡ Automatically moves files to their correct folders
- 🧹 Helps keep folders clean and organized
- 🐍 Built using Python file handling modules

---

## 📦 Technologies Used

- Python
- `os` module
- `shutil` module

---

## 🚀 How It Works

The script scans files in a selected folder and moves them into separate folders according to their extensions.

**Example:**

| File | Goes To |
|------|---------|
| `.jpg` | 📷 Images |
| `.pdf` | 📄 Documents |
| `.mp4` | 🎬 Videos |
| `.mp3` | 🎵 Audio |
| `.py`  | 💻 Code |
| `.zip` | 🗜️ Archives |

---

## 📂 Supported File Types

- 🖼️ Images
- 🎬 Videos
- 🎵 Audio
- 📄 Documents
- 💻 Code Files
- 🗜️ Archives
- 📦 Others

---

## 🛠️ Usage

```bash
# Organize current directory
python -m file_organizer

# Organize a specific folder
python -m file_organizer /path/to/folder

# Preview without moving files (dry run)
python -m file_organizer /path/to/folder --dry-run
```

---

## 🎯 Purpose

This project was created to practice Python automation, file handling, and scripting concepts.

---

## 👨‍💻 Author

**Kamal Solanki**  
[GitHub]((https://github.com/kamalsolanki143))
