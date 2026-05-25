"""Setup for tarunai-connect-pm2 — CLI harness for PM2 process management."""

from setuptools import setup, find_namespace_packages

setup(
    name="tarunai-connect-pm2",
    version="1.0.0",
    author="tarunai-connect contributors",
    author_email="",
    description="tarunAI Connect harness for PM2 process management",
    url="https://github.com/tharunramagiri/tarunai-connect",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0.0",
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
            "tarunai-connect-pm2=tarunai_connect.pm2.pm2_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.pm2": ["skills/*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
