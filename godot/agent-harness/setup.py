#!/usr/bin/env python3
"""
setup.py for tarunai-connect-godot

Install with: pip install -e .
Or publish to PyPI: python -m build && twine upload dist/*
"""

from setuptools import setup, find_namespace_packages

with open("tarunai_connect/godot/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-godot",
    version="1.0.0",
    author="tarunai-connect contributors",
    author_email="",
    description="CLI harness for Godot Engine - Game project management, scene editing, export and GDScript execution. Recommended: Godot 4.x on PATH",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tharunramagiri/tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0.0",
        "prompt-toolkit>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-godot=tarunai_connect.godot.godot_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.godot": ["skills/*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
