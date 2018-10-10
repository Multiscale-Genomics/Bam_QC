# Bam_QC

[![Documentation Status](https://readthedocs.org/projects/Bam_QC/badge/?version=latest)](http://Bam_QC.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/Multiscale-Genomics/Bam_QC.svg?branch=master)](https://travis-ci.org/Multiscale-Genomics/Bam_QC) [![Code Health](https://landscape.io/github/Multiscale-Genomics/Bam_QC/master/landscape.svg?style=flat)](https://landscape.io/github/Multiscale-Genomics/Bam_QC/master)


This repository wraps BamQC as tool and pipeline. BamQC gives a summary statistic report of different aspects of a bam file. It generates an html file with the reports on the passed bam file, both summarized, and graphs.

# Requirements
- pyenv and pyenv-virtualenv
- Python 2.7.12
- Python Modules:
  - pylint
  - pytest
  - mg-tool-api

Installation
------------

Directly from GitHub:

```
cd ${HOME}/code

git clone https://github.com/rehamFatima/Bam_QC.git

cd Bam_QC
```

Create the Python environment

```
pyenv-virtualenv 2.7.12 mg-process-test
pyenv activate mg-process-test
pip install -e .
pip install -r requirements.txt
```
