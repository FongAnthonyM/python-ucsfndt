"""ctupennexporter.py
A class for exporting UPENN CT data.
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
from mxbids.exporters import CTBIDSExporter

# Local Packages #


# Definitions #
# Classes #
class CTUPENNExporter(CTBIDSExporter):
    """A class for exporting UPENN CT data."""

    # Attributes #
    exporter_name: str = "UPENN"
