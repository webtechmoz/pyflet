from setuptools import setup, find_packages

setup(
    name='pyflet',
    version='0.2.1',
    packages=find_packages(include=['pyflet', 'pyflet.*']),
    install_requires=[
        'typer',
    ],
    entry_points={
        'console_scripts': [
            'pyflet=pyflet.main:app',
        ],
    },
    author='DevPythonMZ',
    author_email='zoidycine@egmail.com',
    description='A CLI tool for generating and managing web projects using Flet.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/webtechmoz/pyflet',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)