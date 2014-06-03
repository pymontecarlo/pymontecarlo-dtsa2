#!/usr/bin/env python
"""
================================================================================
:mod:`importer` -- Importer for NISTMonte simulations
================================================================================

.. module:: importer
   :synopsis: Importer for NISTMonte simulations

.. inheritance-diagram:: pymontecarlo.program.nistmonte.importer

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
from pymontecarlo.program.importer import HDF5Importer as _Importer
from pymontecarlo.program.nistmonte.converter import Converter

# Globals and constants variables.

class Importer(_Importer):

    def __init__(self):
        _Importer.__init__(self, Converter)
