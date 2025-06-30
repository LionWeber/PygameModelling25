from distutils.core import setup

from setuptools import find_packages

setup(
    name='PyGame Modelling Workshop 2025',
    description='Workshop material for hands-on demonstration of using pygame in modelling collective behavior using agent-based models.',
    version='1.0.0',
    url='https://github.com/mezdahun/PygameModelling25',
    maintainer='David Mezey @ SCIoI',
    packages=find_packages(exclude=['tests']),
    package_data={'pygmodw25': ['*.txt']},
    python_requires=">=3.7",
    install_requires=[
        'pygame',
        'numpy',
        'scipy',
        'matplotlib',
        'opencv-python',
        'h5py'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Operating System :: Other OS',
        'Programming Language :: Python :: 3.7'
    ],
    zip_safe=False
)
