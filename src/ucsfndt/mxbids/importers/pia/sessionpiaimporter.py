"""sessionpiaimporter.py
A BIDS Session Pia Importer.
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
from typing import Any

# Third-Party Packages #
from mxbids import Anatomy, CT, IEEG, Session, ImportInnerMap
from mxbids.importers import SessionImporter

# Local Packages #
from .anatomypiaimporter import AnatomyPiaImporter
from .ctpiaimporter import CTPiaImporter
from .ieegpiaimporter import IEEGPiaImporter


# Definitions #
# Classes #
class SessionPiaImporter(SessionImporter):
    """A BIDS Session Pia Importer."""

    # Attributes #
    importer_name: str = "Pia"

    inner_maps: list[ImportInnerMap, ...] = [
        ImportInnerMap("anat", Anatomy, "Pia", "", AnatomyPiaImporter),
        ImportInnerMap("ieeg", IEEG, "Pia", "", IEEGPiaImporter),
        ImportInnerMap("ct", CT, "Pia", "", CTPiaImporter),
    ]


# Assign Importer
Session.importers["Pia"] = (SessionPiaImporter, {})
