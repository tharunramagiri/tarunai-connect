from setuptools import find_namespace_packages, setup

with open("tarunai_connect/mermaid/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-mermaid",
    version="1.0.0",
    description="CLI harness for Mermaid Live Editor state files and renderer URLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tharunramagiri/tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    install_requires=[
        "click>=8.0.0",
        "prompt-toolkit>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=9.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-mermaid=tarunai_connect.mermaid.mermaid_cli:main",
        ]
    },
    package_data={
        "tarunai_connect.mermaid": ["skills/*.md"],
    },
    include_package_data=True,
    python_requires=">=3.10",
)
