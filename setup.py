from setuptools import setup, find_packages


setup(
    name="workshop",
    version="0.0.1",
    author="hnfo",
    author_email="hnfo@equinor.com",
    description="TDD workshop",
    keywords=[
        "tests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Learning :: Software Test",
    ],
    packages=find_packages(where="src", exclude=["tests"]),
    package_dir={"": "src"},
    install_requires=[],
    test_suite="tests",
)
