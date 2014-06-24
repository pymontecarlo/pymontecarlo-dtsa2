#!/usr/bin/env python
"""
================================================================================
:mod:`converter` -- PROZA conversion from base options
================================================================================

.. module:: converter
   :synopsis: PROZA conversion from base options

.. inheritance-diagram:: pymontecarlo.program.proza.input.converter

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2011 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.

# Third party modules.

# Local modules.
from pymontecarlo.program._analytical.converter import Converter as _Converter

# Globals and constants variables.

class Converter(_Converter):
    """
    Converter for PROZA simulation.
    """
    pass
