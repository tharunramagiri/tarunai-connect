from pathlib import Path

from setuptools import setup, find_namespace_packages

BASE_DIR = Path(__file__).parent
long_description = (BASE_DIR / "tarunai_connect" / "calibre" / "README.md").read_text(
    encoding="utf-8"
)

setup(
    name="tarunai-connect-calibre",
    version="1.0.0",
    description="CLI harness for Calibre e-book manager — part of the tarunai-connect toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    include_package_data=True,
    package_data={"tarunai_connect.calibre": ["skills/*.md", "README.md"]},
    install_requires=[
        "click>=8.0.0",
        "prompt-toolkit>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "tarunai-connect-calibre=tarunai_connect.calibre.calibre_cli:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
)
