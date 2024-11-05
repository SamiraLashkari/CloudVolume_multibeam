# setup.py
from setuptools import setup, find_packages

setup(
    name="CloudVolume_multibeam",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "open3d==0.17.0",
        "hdbscan==0.8.33",
        "pandas==1.5.3",
        "numpy==1.24.3",
        "scikit-learn==1.3.0",
        "matplotlib==3.7.2",
    ],
     entry_points={
        "console_scripts": [
            "CloudVolume = CloudVolume.CloudVolume:main",  # Points to main() function in app.py
        ]
    },
    description="Visualization and calculation volume of under water installation using processed multibeam data",
    author="Samira Lashkari",
    author_email="samira.lashkari@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.9.20",
)