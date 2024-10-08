#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    "Rich",
    "pdfrw",
    "PyYAML",
    "Pydantic",
]

test_requirements = []

setup(
    author="Jaideep Sundaram",
    author_email='sundaram.previse@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Collection of Python modules for processing PreviseDx Esopredict PDF final report files.",
    entry_points={
        'console_scripts': [
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='previsedx_esopredict_pdf_file_utils',
    name='previsedx_esopredict_pdf_file_utils',
    packages=find_packages(include=['previsedx_esopredict_pdf_file_utils', 'previsedx_esopredict_pdf_file_utils.*']),
    package_data={"previsedx_esopredict_pdf_file_utils": ["conf/config.yaml"]},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sundaram-previsedx/previsedx-eospredict-pdf-file-utils',
    version='0.1.0',
    zip_safe=False,
)
