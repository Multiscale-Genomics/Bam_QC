"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from setuptools import setup, find_packages

setup(
    name='Bam_QC',
    url='https://github.com/Multiscale-Genomics/Bam_QC',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy', 'h5py', 'pytest', 'scipy', 'matplotlib', 'pysam', 'mock',
        'bz2file', 'ConfigParser', 'future'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache 2.0",
    ]
)
