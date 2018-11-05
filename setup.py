import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="startifiedRS",
    version="0.0.1",
    author="Venkatramireddy Koppula",
    author_email="venkatrami.reddy@latentview.com",
    description="Startied random sample from the dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vrreddy695/startifiedRS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
