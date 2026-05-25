from __future__ import annotations

import sys


PACKAGE_NAME = "tarunai-connect-mubu"
PACKAGE_VERSION = "0.1.1"


def _handle_metadata_query(argv: list[str]) -> bool:
    if len(argv) != 2:
        return False
    if argv[1] == "--name":
        print(PACKAGE_NAME)
        return True
    if argv[1] == "--version":
        print(PACKAGE_VERSION)
        return True
    return False


if __name__ == "__main__" and _handle_metadata_query(sys.argv):
    raise SystemExit(0)

try:
    from setuptools import find_namespace_packages, setup
except ModuleNotFoundError as exc:
    raise SystemExit("setuptools is required for packaging commands; use `pip install setuptools`.") from exc


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description="Agent-oriented CLI bridge for the Mubu desktop app",
    py_modules=["mubu_probe"],
    install_requires=["click>=8.0"],
    packages=find_namespace_packages(include=["tarunai_connect.*"]),
    include_package_data=True,
    package_data={
        "tarunai_connect.mubu": ["README.md"],
        "tarunai_connect.mubu.skills": ["SKILL.md"],
        "tarunai_connect.mubu.tests": ["TEST.md"],
    },
    entry_points={
        "console_scripts": [
            "tarunai-connect-mubu=tarunai_connect.mubu.mubu_cli:entrypoint",
        ]
    },
)
