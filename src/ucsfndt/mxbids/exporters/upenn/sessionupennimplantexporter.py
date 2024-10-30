"""sessionupennimplantexporter.py
A class for exporting UPENN implant sessions.
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
from mxbids import CT
from mxbids.exporters import SessionBIDSExporter
from xltektools.xltekmxbids import IEEGXLTEK

# Local Packages #
from .ctupennexporter import CTUPENNExporter
from .ieegupennexporter import IEEGUPENNExporter


# Definitions #
# Classes #
class SessionUPENNImplantExporter(SessionBIDSExporter):
    """A class for exporting UPENN implant sessions."""

    # Attributes #
    exporter_name: str = "UPENN"
    type_map: dict[type, (type, dict[str, Any])] = {
        IEEGXLTEK: (IEEGUPENNExporter, {}),
        CT: (CTUPENNExporter, {}),
    }
