from setuptools import setup, find_namespace_packages

with open("tarunai_connect/krita/README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarunai-connect-krita",
    version="1.0.0",
    description="CLI harness for Krita digital painting application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tarunai-connect contributors",
    url="https://github.com/tharunramagiri/tarunai-connect",
    license="MIT",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Editors",
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
            "tarunai-connect-krita=tarunai_connect.krita.krita_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.krita": ["skills/*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
