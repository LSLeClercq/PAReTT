import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parett",
    version="2.1.1",
    author="Louis-Stephane Le Clercq",
    author_email="leclercq.l.s@gmail.com",
    description="Python Automated Retrieval of TimeTree data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LSLeClercq/PAReTT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    packages=find_packages(),
    install_requires=[
        'pandas', 'splinter', 'numpy', 'Bio'],
    python_requires=">=3.6",
)