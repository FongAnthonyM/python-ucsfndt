""""datasetpiaimporter.py
A BIDS Dataset PIA Importer.
"""
# Package Header #
from ....header import *

# Header #
__author__ = __author__
__credits__ = __credits__
__maintainer__ = __maintainer__
__email__ = __email__


# Imports #
# Standard Libraries #

# Third-Party Packages #
from mxbids import Dataset
from mxbids.importers import DatasetImporter

# Local Packages #
from .subjectpiaimporter import SubjectPiaImporter


# Definitions #
# Classes #
class DatasetPiaImporter(DatasetImporter):
    """A BIDS Dataset PIA Importer."""

    # Attributes #
    importer_name: str = "Pia"

    default_inner_importer = (SubjectPiaImporter, {})


# Assign Importer
Dataset.importers["Pia"] = (DatasetPiaImporter, {})
