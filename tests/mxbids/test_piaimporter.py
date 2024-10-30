#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" test_piaimporter.py

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
from ucsfndt.mxbids.importers.pia import *


# Definitions #
# Functions #
@pytest.fixture
def tmp_dir(tmpdir):
    """A pytest fixture that turn the tmpdir into a Path object."""
    return pathlib.Path(tmpdir)


# Classes #
class TestPiaImporter(abc.ABC):
    mxbids_path = Path("/Users/changlab/Documents/JasperNAS/root_store/updated_subjects")
    pia_path = Path("/Users/changlab/Documents/ChangServer/data_store2/imaging/subjects")


    def test_instance_creation(self, *args, **kwargs):

        dataset = Dataset(self.mxbids_path, mode="w", load=True)

        subject_maps = [
            ImportInnerMap(s.name, None, "Pia", f"EC{s.name[2:].lstrip('0')}", None) for s in dataset.subjects.values()
        ]

        pia_dataset_importer = dataset.create_importer("Pia")
        pia_dataset_importer.execute_import(path=self.pia_path, inner_maps=subject_maps)



# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
