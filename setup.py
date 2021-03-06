import setuptools
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="slackbuilder",
    version="0.0.1",
    author="Kyle Beauregard",
    author_email="kylembeauregard@gmail.com",
    description="Builder and templates for creating slack messages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kbeauregard/slackbuilder",
    license="MIT",
    packages=setuptools.find_packages(
        include=["slackbuilder*"], exclude=["slackbuilder/tests"]
    ),
    py_modules=["slackbuilder.__init__"],
    keywords=["slack"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
