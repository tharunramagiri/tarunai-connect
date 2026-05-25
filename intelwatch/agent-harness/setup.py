from setuptools import setup, find_namespace_packages

setup(
    name="tarunai-connect-intelwatch",
    version="1.0.0",
    description="CLI harness for Intelwatch - Competitive intelligence and OSINT directly from your terminal",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    install_requires=[
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "tarunai-connect-intelwatch=tarunai_connect.intelwatch.intelwatch_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.intelwatch": ["skills/*.md"],
    },
    include_package_data=True,
    python_requires=">=3.8",
)
