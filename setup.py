from pathlib import Path
from typing import List

from setuptools import find_packages, setup


PACKAGE_NAME = "calculator-app"
SUMMARY = "Geometry calculator"
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]
AUTHOR = "mtrqq"
COPYRIGHT = "Copyright 2020 {0}".format(AUTHOR)


HERE: Path = Path(__file__).parent
VERSION: str = Path(HERE, "VERSION").read_text()
REQUIREMENTS: List[str] = Path(HERE, "requirements.txt").read_text().splitlines()

if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        author=AUTHOR,
        description=SUMMARY,
        classifiers=CLASSIFIERS,
        version=VERSION,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=REQUIREMENTS,
    )
