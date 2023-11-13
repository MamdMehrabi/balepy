from setuptools import setup, find_packages

setup(
    name = 'balepy',
    version = '1.1',
    author='Mohammad and Erfan',
    author_email = 'mohammadmehrabi175@gmail.com',
    description = 'balepy a Library Python for create bots API in bale application',
    keywords = ['bot' , 'Bot' , 'bale' , 'robot'],
    long_description = open("README.md", encoding="utf-8").read(),
    python_requires="~=3.6",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/OnlyRad/bale',
    packages = find_packages(),
    install_requires = [],
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
    ]
)
