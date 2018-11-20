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

git clone https://github.com/Multiscale-Genomics/Bam_QC.git

cd Bam_QC
```

Install Ant

```
wget http://www.mirrorservice.org/sites/ftp.apache.org//ant/binaries/apache-ant-1.10.5-bin.zip
unzip apache-ant-1.10.5-bin.zip
```

Install Bamqc
```
git clone https://github.com/s-andrews/BamQC.git
cd BamQC
chmod +x bamqc
```

Setup symlinks

```
cd ${HOME}/bin

ln -s ${HOME}/lib/apache-ant-1.10.5/bin/ant ant
ln -s ${HOME}/lib/BamQC/bamqc bamqc

```

Create the Python environment

```
pyenv-virtualenv 2.7.12 mg-bamqc
pyenv activate mg-bamqc
pip install -e .
pip install -r requirements.txt
```
