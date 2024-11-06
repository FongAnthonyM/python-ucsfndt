"""anatomypiaimporter.py
A BIDS Anatomy Pia Importer.
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
from typing import Any

# Third-Party Packages #
from mxbids import ImportFileMap
from mxbids.importers import ModalityImporter, command_copy, strip_json_copy

# Local Packages #


# Definitions #
# Classes #
class AnatomyPiaImporter(ModalityImporter):
    """A BIDS Anatomy Pia Importer."""

    # Attributes #
    importer_name: str = "Pia"

    strip_fields: set[str] = {
        "InstitutionName",
        "InstitutionalDepartmentName",
        "InstitutionAddress",
        "DeviceSerialNumber",
    }
    file_maps: list[tuple[str, str, Iterable[Path], Callable, dict[str, Any]]] = [
        ImportFileMap(
            "T1w",
            ".nii.gz",
            (Path("mri/brain.mgz"),),
            command_copy,
            kwargs={"command": "mri_convert"},
        ),
        ImportFileMap(
            "T1w",
            ".json",
            (Path("acpc/T1.json"), Path("acpc/T1_orig.json")),
            strip_json_copy,
            kwargs={"strip": strip_fields},
        ),
    ]
