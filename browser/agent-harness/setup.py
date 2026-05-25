#!/usr/bin/env python3
from pathlib import Path
from setuptools import setup, find_namespace_packages

ROOT = Path(__file__).parent
README = ROOT / "tarunai_connect/browser/README.md"

def read_readme():
    try:
        return README.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""

setup(
    name="tarunai-connect-browser",
    version="1.0.0",

    author="tarunAI Connect Contributors",
    description="CLI harness for browser automation via DOMShell MCP server",
    long_description=read_readme(),
    long_description_content_type="text/markdown",

    url="https://github.com/tharunramagiri/tarunai-connect",
    project_urls={
        "Homepage": "https://github.com/tharunramagiri/tarunai-connect",
        "Issues": "https://github.com/tharunramagiri/tarunai-connect/issues",
    },

    license="MIT",

    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    python_requires=">=3.10",

    install_requires=[
        "click>=8.1,<9.0",
        "prompt-toolkit>=3.0,<4.0",
        "mcp>=0.1.0,<1.0.0",
    ],

    extras_require={
        "dev": [
            "pytest>=7",
            "pytest-cov>=4",
            "build",
            "twine",
        ],
    },

    entry_points={
        "console_scripts": [
            "tarunai-connect-browser=tarunai_connect.browser.browser_cli:main",
        ],
    },

    package_data={
        "tarunai_connect.browser": ["skills/*.md"],
    },

    include_package_data=True,
    zip_safe=False,

    keywords="cli browser automation mcp domshell ai-agent",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
