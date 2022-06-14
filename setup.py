import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PAReTT",
    version="1.0.1",
    author="Louis-Stephane Le Clercq",
    author_email="leclercq.l.s@gmail.com",
    description="Python Automated Retrieval of TimeTree data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LSLeClercq/PAReTT",
    project_urls={
        "https://github.com/LSLeClercq/PAReTT/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["pandas", "numpy", "Bio", "splinter"],
)
