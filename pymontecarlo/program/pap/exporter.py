#!/usr/bin/env python
"""
================================================================================
:mod:`exporter` -- Exporter of PAP simulation
================================================================================

.. module:: exporter
   :synopsis: Exporter of PAP simulation

.. inheritance-diagram:: pymontecarlo.program.pap.exporter

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2014 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.

# Third party modules.

# Local modules.
from pymontecarlo.program.exporter import XMLExporter as _Exporter
from pymontecarlo.program.pap.converter import Converter

# Globals and constants variables.

class Exporter(_Exporter):

    def __init__(self):
        _Exporter.__init__(self, Converter)
