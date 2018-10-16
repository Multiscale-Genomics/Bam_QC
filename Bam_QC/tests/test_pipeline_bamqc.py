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

from __future__ import print_function

import os.path
import pytest

from basic_modules.metadata import Metadata
from process_bamqc import process_bamqc

@pytest.mark.bamqc
@pytest.mark.pipeline
def test_pipeline_bamqc():
    """
    Test case to ensure that the Genome indexing pipeline code works.

    Running the pipeline with the test data from the command line:

    .. code-block:: none

       pytest tests/test_pipeline_test.py
    """
    resource_path = os.path.join(os.path.dirname(__file__), "data/")

    input_files = {
        "bam": resource_path + "macs2.Human.bam"
    }

    metadata = {
        "bam": Metadata(
            "data_chip_seq", "bam", input_files["bam"], None,
            {"assembly": "test"}
        )
    }

    files_out = {
        "html": resource_path + 'macs2.Human_bamqc.html',
    }

    bqc_handle = process_bamqc()
    bqc_files, bqc_meta = bqc_handle.run(input_files, metadata, files_out)

    # Add tests for all files created
    for f_out in bqc_files:
        print("BAMQC RESULTS FILE:", f_out)
        assert os.path.isfile(bqc_files[f_out]) is True
        assert os.path.getsize(bqc_files[f_out]) > 0
        assert f_out in bqc_meta
