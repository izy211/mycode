#!/usr/bin/env python3
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name = "example-pkg-joshgantt",
        version = "0.0.1",
        author = "Josh Gantt",
        author_email = "yossarian@cheerful.com",
        description = "A test upload, you know, to learn and stuff.",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/pypa/sampleproject",
        packages = setuptools.find_packages(),
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        )

