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
from Bam_QC.tool.bamqc import bamQC


@pytest.mark.bamqc
def test_bamqc():
    """
    Test case to ensure that the testTool works.

    .. code-block:: none

       pytest tests/test_bamqc.py
    """
    resource_path = os.path.join(os.path.dirname(__file__), "data/")
    bam_file = resource_path + "macs2.Human.bam"

    input_files = {
        "bam": bam_file
    }

    output_files = {
        "html": resource_path + "macs2.Human_bamqc.html"
    }

    metadata = {
        "bam": Metadata(
            "data_chip_seq", "bam", bam_file, None,
            {"assembly": "test"}
        )
    }

    bamqc_handle = bamQC()
    bamqc_handle.run(input_files, metadata, output_files)

    assert os.path.isfile(output_files["html"]) is True
    assert os.path.getsize(output_files["html"]) > 0
