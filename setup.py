import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zyplots",  # Replace with your own username
    version="0.0.4",
    author="Vibhatha Abeykoon",
    author_email="vibhatha@gmail.com",
    description="A small plot package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'matplotlib',
        'cloudpickle',
        'numpy',
        'pandas'
    ],
)
