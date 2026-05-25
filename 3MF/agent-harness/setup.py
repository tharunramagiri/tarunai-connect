#!/usr/bin/env python3
"""
setup.py for tarunai-connect-3mf

Install with: pip install -e .
Or publish to PyPI: python -m build && twine upload dist/*
"""

from setuptools import setup, find_namespace_packages

with open("tarunai_connect/threemf/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-3mf",
    version="1.0.0",
    author="tarunai-connect contributors",
    author_email="",
    description="CLI harness for 3MF — Detect and resize cylindrical holes, repair meshes, compare 3D printing files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tharunramagiri/tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "click>=8.0.0",
        "prompt-toolkit>=3.0.0",
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "trimesh>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-3mf=tarunai_connect.threemf.threemf_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.threemf": ["skills/*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
