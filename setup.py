import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

with open('requirements.txt') as f:
    install_reqs = f.readlines()
    reqs = [str(ir) for ir in install_reqs]

setuptools.setup(
    name="pymaya",
    version="0.1.3",
    author="Ben Sterenson",
    author_email="bensterenson@gmail.com",
    description="Python client to interact with maya.tase.co.il",
    install_requires=reqs,
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenSterenson/pymaya",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    test_suite="tests",
)
