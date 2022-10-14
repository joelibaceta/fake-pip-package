import sys
from setuptools import setup, find_packages

print("Rlly?, do you want to install this?")

setup(
    name="requirements.txt",
    version="1.0.0",
    author="Joel Ibaceta",
    author_email="mail@joelibaceta.com",
    license='MIT',
    description="A joke for developers who forget the -r argument in pip install command",
    long_description="A joke for developers who forget the -r argument in pip install command",
    url="https://github.com/joelibaceta/fake-pip-package",
    project_urls={
        'Source': 'https://github.com/joelibaceta/fake-pip-package',
        'Tracker': 'https://github.com/joelibaceta/fake-pip-package/issues'
    },
    packages=find_packages(),
    include_package_data=True,  
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='Joke, pip, requirements.txt',
)

print("LOL, have you installed a package named 'requirements.txt'...")
