import os
from setuptools import setup, find_namespace_packages

_here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_here, "tarunai_connect/mailchimp/README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-mailchimp",
    version="0.1.0",
    description="tarunai-connect harness for the Mailchimp Marketing API v3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tarunai-connect contributors",
    license="Apache-2.0",
    python_requires=">=3.10",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    package_data={"tarunai_connect.mailchimp": ["skills/SKILL.md", "README.md"]},
    install_requires=[
        "click>=8.0",
        "requests>=2.28",
        "prompt-toolkit>=3.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "pytest-cov", "responses>=0.23"],
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-mailchimp=tarunai_connect.mailchimp.mailchimp_cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
