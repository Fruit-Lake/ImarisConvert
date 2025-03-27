from setuptools import setup, find_packages
import os

setup(
    name="imaris-convert",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "imaris_convert": [
            "*.dll",
            "*.py",
            "*.so",
            "*.dylib",
            "*.*"
        ],
    },
    install_requires=[
        "numpy",
        "tifffile",
        "tqdm",
    ],
    entry_points={
        'console_scripts': [
            'imaris-convert=imaris_convert.imaris_convert:main_cli',
        ],
    },
    author="Guanhao Sun",
    author_email="sgh4132@outlook.com",
    description="A tool for converting images to Imaris format",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        'Topic :: Scientific/Engineering :: Image Processing',
    ],
)