from pathlib import Path
from setuptools import setup, find_namespace_packages

_readme = Path("tarunai_connect/cloudanalyzer/README.md")
_long_description = _readme.read_text(encoding="utf-8") if _readme.is_file() else ""

setup(
    name="tarunai-connect-cloudanalyzer",
    version="1.0.0",
    description="Agent-friendly CLI harness for CloudAnalyzer point cloud QA platform",
    long_description=_long_description,
    long_description_content_type="text/markdown",
    author="tarunai-connect",
    python_requires=">=3.10",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    package_data={
        "tarunai_connect.cloudanalyzer": ["skills/*.md"],
    },
    install_requires=[
        "click>=8.0.0",
        "prompt-toolkit>=3.0.0",
        "cloudanalyzer",
    ],
    entry_points={
        "console_scripts": [
            "tarunai-connect-cloudanalyzer=tarunai_connect.cloudanalyzer.cloudanalyzer_cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
