\"\"\"0.13_setup.py — Pip installation for cophenetic package.

Usage:
    pip install -e .
    # or
    python 0.13_setup.py install
\"\"\"

from setuptools import setup, find_packages

setup(
    name='cophenetic',
    version='0.1.0',
    description='Tree Distance Cophenetic — cophenetic distance, ultrametric inequality, triadic rigidity',
    author='Rowan Brad Quni',
    author_email='rowan.quni@qnfo.org',
    url='https://qnfo.org',
    packages=find_packages(),
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
