"""subjectupennexporter.py
A class for exporting UPENN BIDS subjects.
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
from pathlib import Path
from typing import Any

# Third-Party Packages #
from mxbids import Subject
from mxbids.exporters import SubjectBIDSExporter
from xltektools.xltekmxbids import XLTEKMXBIDSSession

# Local Packages #
from .sessionupennimplantexporter import SessionUPENNImplantExporter
from .sessionupennpreimplantexporter import SessionUPENNPreImplantExporter


# Definitions #
# Classes #
class SubjectUPENNExporter(SubjectBIDSExporter):
    """A class for exporting UPENN BIDS subjects."""

    # Attributes #
    exporter_name: str = "UPENN"

    # Instance Methods #
    def export_sessions(
        self,
        path: Path,
        name_map: dict[str, str] | None = None,
        type_map: dict[type, type] | None = None,
        **kwargs: Any,
    ) -> None:
        """Exports sessions from the subject to the specified path.

        Args:
            path: The root path to export the sessions to.
            name_map: A mapping of original session names to new names.
            type_map: A mapping of session types to exporter types.
            **kwargs: Additional keyword arguments.
        """
        session = self.bids_object.sessions["clinicalintracranial"]
        preimplant = session.require_exporter("UPENNPreImplant", SessionUPENNPreImplantExporter)
        preimplant.execute_export(path, name="ses-preimplant01")
        implant = session.require_exporter("UPENNImplant", SessionUPENNImplantExporter)
        implant.execute_export(path, name="ses-implant01")


# Assign Exporter
Subject.exporters["UPENN"] = (SubjectUPENNExporter, {})
