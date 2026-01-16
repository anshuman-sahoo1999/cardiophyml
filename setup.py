# setup.py (updated)
from setuptools import setup, find_packages

setup(
    name="cardiophyml",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "neurokit2",
        "scikit-learn",
        "plotly"
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "cardiophyml=cardiophyml.cli:main",
        ],
    },
)