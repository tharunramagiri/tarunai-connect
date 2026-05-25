#!/usr/bin/env python3
"""
setup.py for tarunai-connect-ollama

Install with: pip install -e .
Or publish to PyPI: python -m build && twine upload dist/*
"""

from setuptools import setup, find_namespace_packages

with open("tarunai_connect/ollama/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-ollama",
    version="1.0.1",
    author="tarunai-connect contributors",
    author_email="",
    description="CLI harness for Ollama - Local LLM inference and model management via Ollama REST API. Recommended: Ollama running at http://localhost:11434",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tharunramagiri/tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
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
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-ollama=tarunai_connect.ollama.ollama_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.ollama": ["skills/*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
