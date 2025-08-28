#!/usr/bin/env python3
"""
Setup script for txt-to-qti library - Independent QTI Converter for Canvas LMS
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read version from the package
def get_version():
    """Get version from __init__.py"""
    init_path = this_directory / "txttoqti" / "__init__.py"
    if init_path.exists():
        with open(init_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('__version__'):
                    return line.split('=')[1].strip().strip('"').strip("'")
    return "1.0.0"

setup(
    name="txt-to-qti",
    version=get_version(),
    author="Educational Tools Team",
    author_email="dev@example.com",
    description="Universal converter from text-based question banks to Canvas LMS QTI packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/txt-to-qti",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Only standard library dependencies - no external packages needed
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "txt-to-qti=txttoqti.cli:main",
            "txt2qti=txttoqti.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "txttoqti": [
            "templates/*.xml",
            "examples/*.txt",
            "tests/data/*.txt",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/txt-to-qti/issues",
        "Source": "https://github.com/yourusername/txt-to-qti",
        "Documentation": "https://txt-to-qti.readthedocs.io/",
    },
    keywords="education canvas lms qti assessment quiz testing e-learning",
    zip_safe=False,
)