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

import sys
import os
import shlex
import subprocess

from utils import logger

try:
    if hasattr(sys, '_run_from_cmdl') is True:
        raise ImportError
    from pycompss.api.parameter import FILE_IN, FILE_OUT
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on
except ImportError:
    logger.warn("[Warning] Cannot import \"pycompss\" API packages.")
    logger.warn("          Using mock decorators.")

    from utils.dummy_pycompss import FILE_IN, FILE_OUT  # pylint: disable=ungrouped-imports
    from utils.dummy_pycompss import task  # pylint: disable=ungrouped-imports
    from utils.dummy_pycompss import compss_wait_on  # pylint: disable=ungrouped-imports

from basic_modules.tool import Tool
from basic_modules.metadata import Metadata

# ------------------------------------------------------------------------------


class bamQC(Tool):  # pylint: disable=invalid-name
    """
    Tool for statistical and qualitative analysis of a Bam file
    """

    def __init__(self, configuration=None):
        """
        Init function
        """
        logger.info("BamQC - Bam file stats")
        Tool.__init__(self)

        if configuration is None:
            configuration = {}

        self.configuration.update(configuration)

    @task(returns=bool, file_in_loc=FILE_IN, file_out_loc=FILE_OUT, isModifier=False)
    def bamqc(self, bam_file_in, html_file_out, params):  # pylint: disable=no-self-use
        """
        Count the number of characters in a file and return a file with the count

        Parameters
        ----------
        file_in_loc : str
            Location of the input file
        file_out_loc : str
            Location of an output file

        Returns
        -------
        bool
            Writes to the file, which is returned by pyCOMPSs to the defined location
        """
        bqc_tmp_out = os.path.join(html_file_out)
        bqc_tmp_out = bqc_tmp_out.replace(
            "html",
            "tmp.html"
        )

        if os.path.isfile(bam_file_in) is False:
            logger.fatal("FILE NOT FOUND: " + bam_file_in)
            return False

        command_line = "bamqc " + " ".join(params) + " "
        command_line += bam_file_in
        logger.info("BAMQC: command_line: " + command_line)

        try:
            args = shlex.split(command_line)
            process = subprocess.Popen(args)
            process.wait()
        except (OSError, IOError) as msg:
            logger.fatal("I/O error({0}) - bamQC: {1}\n{2}".format(
                msg.errno, msg.strerror, command_line))
            return False

        try:
            with open(html_file_out, "r") as f_in:
                with open(bqc_tmp_out, "w") as file_handle:
                    file_handle.write(f_in.read())
        except IOError as error:
            logger.fatal("I/O error({0}): {1}".format(error.errno, error.strerror))
            return False

        return True

    def run(self, input_files, input_metadata, output_files):
        """
        The main function to run the bamqc tool

        Parameters
        ----------
        input_files : dict
            Input bam file
        input_metadata: dict
            Matching metadata for the file, plus any additional data
        output_files : dict
            html file containing reports.

        Returns
        -------
        output_files : dict
            List of files with a single entry.
        output_metadata : dict
            List of matching metadata for the returned files
        """

        command_params = self.get_bamqc_params(self.configuration)

        results = self.bamqc(
            input_files["bam"],
            output_files["html"],
            command_params
        )
        results = compss_wait_on(results)

        if results is False:
            logger.fatal("Error in bamqc.py: bamQC: run failed with error: {}", results)
            return {}, {}

        output_files_created = {
            "html": output_files["html"]
        }

        output_metadata = {
            "html": Metadata(
                data_type=input_metadata["bam"].data_type,
                file_type="html",
                file_path=output_files["html"],
                sources=[input_metadata["bam"].file_path],
                taxon_id=input_metadata["bam"].taxon_id,
                meta_data={
                    "tool": "bamqc"
                }
            )
        }

        return (output_files_created, output_metadata)

    @staticmethod
    def get_bamqc_params(params):
        """
            Function to handle for extraction of commandline parameters
            Parameters
            ----------
            params : dict
            Returns
            -------
            list
        """
        command_params = []

        command_parameters = {
            # General options
            "bqc_gff": ["--gff", True],
            "bqc_genome": ["--genome", True],
            "bqc_species": ["--species", True],
            "bqc_assembly": ["--assembly", True],
            "bqc_available": ["--available", False],
            "bqc_saved": ["--saved", False],
            "bqc_help": ["--help", False],
            "bqc_version": ["--version", False],
            "bqc_outdir": ["--outdir", True],
            "bqc_extract": ["--extract", False],
            "bqc_java": ["--java", False],
            "bqc_noextract": ["--noextract", False],
            "bqc_nogroup": ["--nogroup", False],
            "bqc_threads": ["--threads", True],
            "bqc_limits": ["--limits", True],
            "bqc_quiet": ["--quiet", False],
            "bqc_dir": ["--dir", True]
        }

        for param in params:
            if param in command_parameters:
                if command_parameters[param][1] and params[param] != "":
                    command_params = command_params + [command_parameters[param][0], params[param]]
                else:
                    if command_parameters[param][0] and params[param] is not False:
                        command_params.append(command_parameters[param][0])


        return command_params
