import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="genetic_algo",
    version="1.1.1",
    author="Stunning Impalas INST326 Final Project Group",
    description="A genetic algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheRun98/genetic-algo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)