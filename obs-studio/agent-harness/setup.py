#!/usr/bin/env python3
"""
setup.py for tarunai-connect-obs-studio

Install with: pip install -e .
Or publish to PyPI: python -m build && twine upload dist/*
"""

from setuptools import setup, find_namespace_packages

with open("tarunai_connect/obs_studio/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-obs-studio",
    version="1.0.0",
    author="tarunai-connect contributors",
    author_email="",
    description="CLI harness for OBS Studio - Create and manage streaming/recording scenes via command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tharunramagiri/tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Video :: Capture",
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
            "tarunai-connect-obs-studio=tarunai_connect.obs_studio.obs_studio_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.obs_studio": ["skills/*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
