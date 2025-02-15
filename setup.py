from setuptools import setup, find_packages

setup(
    name="username-generator",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    author="sanjeeviraju",
    description="A Python GUI application for generating creative usernames",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sanjeeviraju/username-generator",
)
