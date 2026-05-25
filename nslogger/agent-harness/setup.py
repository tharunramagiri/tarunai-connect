"""PyPI setup for tarunai-connect-nslogger."""
from setuptools import setup, find_namespace_packages

setup(
    name="tarunai-connect-nslogger",
    version="0.1.0",
    description="CLI harness for NSLogger — read, filter, export, and monitor NSLogger log files",
    long_description=open("tarunai_connect/nslogger/README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="tarunai-connect",
    python_requires=">=3.10",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    package_data={
        "tarunai_connect.nslogger": ["helpers/*.swift", "skills/*.md"],
    },
    install_requires=[
        "click>=8.0",
        "rich>=13.0",
        "zeroconf>=0.38.0",
    ],
    entry_points={
        "console_scripts": [
            "tarunai-connect-nslogger=tarunai_connect.nslogger.nslogger_cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    include_package_data=True,
    zip_safe=False,
)
