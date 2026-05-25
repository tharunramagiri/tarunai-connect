#!/usr/bin/env python3
"""Setup for tarunai-connect-quietshrink agent harness."""

from setuptools import setup, find_namespace_packages
from pathlib import Path

readme = Path(__file__).parent / "QUIETSHRINK.md"
long_description = readme.read_text(encoding="utf-8") if readme.exists() else ""

setup(
    name="tarunai-connect-quietshrink",
    version="1.0.0",
    author="quietshrink contributors",
    description=(
        "Agent-native CLI harness for quietshrink — compress screen recordings "
        "with zero CPU stress on Apple Silicon. JSON output, structured probes, "
        "skill-aware help."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/achiya-automation/quietshrink",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0.0"],
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-quietshrink=tarunai_connect.quietshrink.quietshrink_cli:cli",
        ],
    },
    package_data={
        "tarunai_connect.quietshrink": ["skills/*.md"],
    },
    exclude_package_data={
        "tarunai_connect.quietshrink": ["tests/*"],
    },
    include_package_data=True,
    zip_safe=False,
)
