"""subjectpiaimporter.py
A BIDS Subject Pia Importer.
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
from mxbids import Session, Subject, ImportInnerMap
from mxbids.importers import SubjectImporter

# Local Packages #
from .sessionpiaimporter import SessionPiaImporter


# Definitions #
# Classes #
class SubjectPiaImporter(SubjectImporter):
    """A BIDS Subject Pia Importer."""

    # Attributes #
    importer_name: str = "Pia"

    default_inner_importer = (SessionPiaImporter, {})
    inner_maps: list[ImportInnerMap, ...] = [
        ImportInnerMap("clinicalintracranial", Session, "Pia", "", SessionPiaImporter),
    ]


# Assign Importer
Subject.importers["Pia"] = (SubjectPiaImporter, {})
