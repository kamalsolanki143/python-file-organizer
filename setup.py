from setuptools import setup, find_packages

setup(
    name="python-file-organizer",
    version="1.0.0",
    author="Kamal Solanki",
   author_email="solankikamal55143@gmail.com",
    description="A CLI tool to automatically organize files into categorized folders.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kamalsolanki143/python-file-organizer",
    packages=find_packages(),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "file-organizer=file_organizer.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
)
