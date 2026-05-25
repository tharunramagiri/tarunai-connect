#!/usr/bin/env python3
"""
setup.py for tarunai-connect-comfyui

Install with: pip install -e .
Or publish to PyPI: python -m build && twine upload dist/*
"""

from setuptools import setup, find_namespace_packages

setup(
    name="tarunai-connect-comfyui",
    version="1.0.0",
    author="tarunai-connect contributors",
    author_email="",
    description="CLI harness for ComfyUI - AI image generation workflow management via ComfyUI REST API. Requires: ComfyUI running at http://localhost:8188",
    long_description=open("tarunai_connect/comfyui/README.md", "r", encoding="utf-8").read()
    if __import__("os").path.exists("tarunai_connect/comfyui/README.md")
    else "CLI harness for ComfyUI AI image generation.",
    long_description_content_type="text/markdown",
    url="https://github.com/tharunramagiri/tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0.0",
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
            "tarunai-connect-comfyui=tarunai_connect.comfyui.comfyui_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.comfyui": ["skills/*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
