"""Setup for tarunai-connect-lldb package."""

from pathlib import Path

from setuptools import find_namespace_packages, setup

_README = Path(__file__).parent / "tarunai_connect" / "lldb" / "README.md"
_long_desc = _README.read_text(encoding="utf-8") if _README.is_file() else ""

setup(
    name="tarunai-connect-lldb",
    version="1.0.0",
    description="CLI harness for LLDB debugger via Python API",
    long_description=_long_desc,
    long_description_content_type="text/markdown",
    author="tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0",
        "prompt-toolkit>=3.0",
    ],
    extras_require={
        "test": ["pytest>=7.0"],
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-lldb=tarunai_connect.lldb.lldb_cli:main",
            "tarunai-connect-lldb-dap=tarunai_connect.lldb.dap:main",
        ],
    },
    package_data={
        "tarunai_connect.lldb": ["skills/*.md", "README.md"],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Debuggers",
    ],
)
