"""ctpiaimporter.py
A BIDS CT Pia Importer.
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
from collections.abc import Callable, Iterable
from pathlib import Path
import shutil
from typing import Any

# Third-Party Packages #
from mxbids import ImportFileMap
from mxbids.importers import ModalityImporter, strip_json_copy, command_copy

# Local Packages #


# Definitions #
# Classes #
class CTPiaImporter(ModalityImporter):
    """A BIDS CT Pia Importer."""

    # Attributes #
    importer_name: str = "Pia"

    strip_fields: set[str] = {
        "InstitutionName",
        "InstitutionalDepartmentName",
        "InstitutionAddress",
        "DeviceSerialNumber",
    }
    file_maps: list[ImportFileMap] = [
        ImportFileMap(
            "CT",
            ".nii",
            (Path("CT/CT.nii"), Path("CT/CT.nii.gz")),
            command_copy,
            kwargs={"command": "mri_convert"},
        ),
        ImportFileMap(
            "CT",
            ".json",
            (Path("CT/CT.json"), Path("CT/CT_orig.json")),
            strip_json_copy,
            kwargs={"strip": strip_fields},
        ),
    ]
