#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="tap-scout",
    version="0.1.0",
    description="Singer.io tap for extracting anesthetic data from Scout",
    author="Modern Animal",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_scout"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-scout=tap_scout:main
    """,
    packages=find_packages(),
    package_data={"schemas": ["tap_scout/schemas/*.json"]},
    include_package_data=True,
)
