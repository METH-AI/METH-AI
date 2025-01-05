from setuptools import setup, find_packages

setup(
    name="meth_ai",
    version="0.1.0",
    description="AI-powered trading assistant for the Solana blockchain.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
