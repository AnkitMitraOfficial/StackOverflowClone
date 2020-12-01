import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="StackOverFlowClone",
    version="0.0.1",
    author="Ankit Mitra",
    #author_email="",
    description="StackOverFlowClone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnkitMItraOfficial/StackOverFlow-Clone",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Django>=3.1.4',
        'django-allauth',
        ],
)
