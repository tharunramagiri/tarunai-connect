from setuptools import find_namespace_packages, setup

with open("tarunai_connect/eth2_quickstart/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-eth2-quickstart",
    version="1.0.0",
    description="CLI harness for eth2-quickstart - hardened Ethereum node deployment and operations",
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
            "pytest>=7.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-eth2-quickstart=tarunai_connect.eth2_quickstart.eth2_quickstart_cli:main",
        ]
    },
    package_data={
        "tarunai_connect.eth2_quickstart": ["skills/*.md"],
    },
    include_package_data=True,
    python_requires=">=3.10",
)
