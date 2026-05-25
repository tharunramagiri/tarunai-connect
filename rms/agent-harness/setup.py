#!/usr/bin/env python3
"""setup.py for tarunai-connect-rms"""

from setuptools import setup, find_namespace_packages

with open("tarunai_connect/rms/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-rms",
    version="1.0.0",
    author="tarunai-connect contributors",
    author_email="",
    description="CLI harness for Teltonika RMS — device management, monitoring, and more. Requires: RMS_API_TOKEN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tharunramagiri/tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
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
            "tarunai-connect-rms=tarunai_connect.rms.rms_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.rms": ["skills/*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
