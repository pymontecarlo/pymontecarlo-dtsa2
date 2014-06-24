#!/usr/bin/env python
"""
================================================================================
:mod:`worker` -- XPP worker
================================================================================

.. module:: worker
   :synopsis: XPP worker

.. inheritance-diagram:: pymontecarlo.program.xpp.runner.worker

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2012 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.

# Third party modules.

# Local modules.
from pymontecarlo.settings import get_settings
from pymontecarlo.program._dtsa2.worker import Worker as _Worker

# Globals and constants variables.

class Worker(_Worker):

    def __init__(self, program):
        """
        Runner to run XPP simulation(s).
        """
        _Worker.__init__(self, program, 
                         java_exec=get_settings().xpp.java,
                         jar_path=get_settings().xpp.jar)
