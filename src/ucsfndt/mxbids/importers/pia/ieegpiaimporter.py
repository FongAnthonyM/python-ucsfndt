"""ieegpiaimporter.py
A BIDS iEEG PIA Importer.
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
from json import dump, load
from pathlib import Path
from typing import Any

# Third-Party Packages #
from mxbids import ImportFileMap
from mxbids.importers import ModalityImporter
import pandas as pd
from scipy.io import loadmat

# Local Packages #


# Definitions #
# Classes #
class IEEGPiaImporter(ModalityImporter):
    """A BIDS iEEG PIA Importer."""

    coord_info = {"iEEGCoordinateSystem": "ACPC", "iEEGCoordinateUnits": "mm"}
    electrode_columns = [
        "name",
        "x",
        "y",
        "z",
        "size",
        "material",
        "manufacturer",
        "group",
        "hemisphere",
        "type",
        "impedance",
    ]

    # Static Methods #
    @classmethod
    def convert_electrodes(cls, old_path: Path, new_path: Path) -> None:
        """Converts electrode data from a MATLAB file to a BIDS-compliant TSV file.

        Args:
            old_path: The path to the original MATLAB file.
            new_path: The path to the new TSV file.
        """
        original_montage = loadmat(old_path.as_posix(), squeeze_me=True)
        xyz = original_montage["elecmatrix"]
        eleclabels = original_montage["eleclabels"]
        eleclabels = eleclabels[: len(xyz), :]

        bids_montage = pd.DataFrame(columns=cls.electrode_columns)
        bids_montage.loc[:, "x"] = xyz[:, 0]
        bids_montage.loc[:, "y"] = xyz[:, 1]
        bids_montage.loc[:, "z"] = xyz[:, 2]
        bids_montage.loc[:, "name"] = eleclabels[:, 0]
        bids_montage.loc[:, "group"] = eleclabels[:, 2]
        bids_montage.loc[:, "size"] = "n/a"
        bids_montage.loc[:, "material"] = "n/a"
        bids_montage.loc[:, "manufacturer"] = "n/a"
        bids_montage.loc[bids_montage["x"] > 0, "hemisphere"] = "r"
        bids_montage.loc[bids_montage["x"] <= 0, "hemisphere"] = "l"
        bids_montage.loc[:, "type"] = "n/a"
        bids_montage.loc[:, "impedance"] = "n/a"
        bids_montage.name = bids_montage.name.fillna("NaN")

        bids_montage.to_csv(new_path, sep="\t")

    @classmethod
    def create_coodsystem_json(cls, old_path: Path, new_path: Path) -> None:
        """Creates a JSON file for the coordinate system."""
        with open(new_path, "w") as f:
            dump(cls.coord_info, f)

    # Attributes #
    importer_name: str = "Pia"


# Assinments #
IEEGPiaImporter.file_maps = [
    ImportFileMap("coordsystem", ".json", (None,), IEEGPiaImporter.create_coodsystem_json),
    ImportFileMap(
        "electrodes",
        ".tsv",
        (Path("elecs/clinical_elecs_all.mat"), Path("elecs/clinical_TDT_elecs_all.mat"), Path("elecs/clinical_elecs_all1.mat")),
        IEEGPiaImporter.convert_electrodes,
    ),
]
