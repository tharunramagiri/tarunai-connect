"""Setup for tarunai-connect-freecad — CLI harness for FreeCAD."""

from setuptools import setup, find_namespace_packages

setup(
    name="tarunai-connect-freecad",
    version="1.0.0",
    description="CLI harness for FreeCAD parametric 3D CAD modeler",
    long_description=open("tarunai_connect/freecad/README.md").read(),
    long_description_content_type="text/markdown",
    author="tarunAI Connect Contributors",
    license="Apache-2.0",
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0.0",
        "prompt-toolkit>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "tarunai-connect-freecad=tarunai_connect.freecad.freecad_cli:main",
        ],
    },
    package_data={
        "tarunai_connect.freecad": ["skills/*.md"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
