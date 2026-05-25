from setuptools import setup, find_namespace_packages

setup(
    name="tarunai-connect-adguardhome",
    version="1.0.0",
    description="CLI harness for AdGuardHome - control your ad blocker from the command line",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    install_requires=[
        "click>=8.0.0",
        "prompt-toolkit>=3.0.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "tarunai-connect-adguardhome=tarunai_connect.adguardhome.adguardhome_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.adguardhome": ["skills/*.md"],
    },
    include_package_data=True,
    python_requires=">=3.10",
)
