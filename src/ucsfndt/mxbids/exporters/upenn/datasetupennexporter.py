"""datasetbidsexporter.py
A class for exporting UPENN BIDS datasets.
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
from mxbids.exporters import DatasetExporter

# Local Packages #
from .subjectupennexporter import SubjectUPENNExporter


# Definitions #
# Classes #
class DatasetUPENNExporter(DatasetExporter):
    """A class for exporting UPENN BIDS datasets."""

    # Attributes #
    exporter_name: str = "UPENN"
    default_type: type = (SubjectUPENNExporter, {})


# Assign Exporter
Dataset.exporters["UPENN"] = (DatasetUPENNExporter, {})
