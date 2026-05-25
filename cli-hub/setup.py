"""tarunai-connect — package manager for TarunAI Connect harnesses."""

from setuptools import setup, find_packages

setup(
    name="tarunai-connect",
    version="0.3.0",
    description="Package manager for TarunAI Connect — browse, install, and manage 40+ agent-native CLI interfaces for GUI applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="tharunramagiri",
    author_email="tharun@tarunai.dev",
    url="https://github.com/tharunramagiri/tarunai-connect",
    project_urls={
        "Homepage": "https://tarunai.dev",
        "Repository": "https://github.com/tharunramagiri/tarunai-connect",
        "Bug Tracker": "https://github.com/tharunramagiri/tarunai-connect/issues",
        "Catalog": "https://tarunai.dev/catalog",
    },
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0",
        "requests>=2.28",
    ],
    entry_points={
        "console_scripts": [
            "tarunai-connect=tarunai_connect.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: System :: Installation/Setup",
        "Topic :: Utilities",
    ],
    keywords="cli, agent, gui, automation, package-manager, tarunai-connect",
)
