#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" test_up.py

"""
# Package Header #
from ucsfndt.header import *

# Header #
__author__ = __author__
__credits__ = __credits__
__maintainer__ = __maintainer__
__email__ = __email__


# Imports #
# Standard Libraries #
import abc
from pathlib import Path
import pathlib

# Third-Party Packages #
import pytest
from mxbids import Dataset, ImportInnerMap

# Local Packages #
from ucsfndt.mxbids.exporters.upenn import *


# Definitions #
# Functions #
@pytest.fixture
def tmp_dir(tmpdir):
    """A pytest fixture that turn the tmpdir into a Path object."""
    return pathlib.Path(tmpdir)


# Classes #
class TestUPennExporter(abc.ABC):
    mxbids_path = Path("/Users/changlab/Documents/JasperNAS/root_store/updated_subjects")
    export_path = Path("/Users/changlab/Documents/test")

    def test_instance_creation(self, *args, **kwargs):

        dataset = Dataset(self.mxbids_path, mode="r", load=True)

        name_map = {
            "EC0210": "UPenn0004",
        }

        upenn_dataset_exporter = dataset.create_exporter("UPENN")
        upenn_dataset_exporter.execute_export(path=self.export_path, name_map=name_map)



# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
