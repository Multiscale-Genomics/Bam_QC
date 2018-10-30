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

Pipelines
=========

Bam QC Tool
-----------
.. automodule:: process_bamqc

   This is a pipeline using BamQC for bam file stats.

   Running from the command line
   =============================

   Parameters
   ----------
   config : file
      Location of the config file for the workflow
   in_metadata : file
      Location of the input list of files required by the process
   out_metadata : file
      Location of the output results.json file for returned files

   Returns
   -------
   output : file
      Html file with all the statistics

   Example
   -------
   When using a local verion of the [COMPS virtual machine](http://www.bsc.es/computer-sciences/grid-computing/comp-superscalar/downloads-and-documentation):

   .. code-block:: none
      :linenos:

      cd /home/compss/code/Bam_QC
      runcompss --lang=python Bam_QC/process_bamqc.py --config /home/compss/code/Bam_QC/tool_config/process_bamqc.json --in_metadata /home/compss/code/Bam_QC/tests/json/input_bamqc.json --out_metadata /home/compss/code/Bam_QC/tests/results.json

   Methods
   =======
   .. autoclass:: process_bamqc.process_bamqc
      :members:
