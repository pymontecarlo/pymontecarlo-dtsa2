#!/usr/bin/env python
"""
================================================================================
:mod:`config` -- NISTMonte Monte Carlo program configuration
================================================================================

.. module:: config
   :synopsis: NISTMonte Monte Carlo program configuration

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2012 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.
import os
import sys
import subprocess

# Third party modules.

# Local modules.
from pymontecarlo.settings import get_settings
from pymontecarlo.program.config import Program
from pymontecarlo.program.nistmonte.exporter import Exporter
from pymontecarlo.program.nistmonte.importer import Importer
from pymontecarlo.program.nistmonte.converter import Converter
from pymontecarlo.program.nistmonte.worker import Worker

# Globals and constants variables.

class _NISTMonteProgram(Program):

    def __init__(self):
        Program.__init__(self, 'NISTMonte', 'nistmonte',
                         Converter, Worker, Exporter, Importer)

    def validate(self):
        settings = get_settings()

        if 'nistmonte' not in settings:
            raise AssertionError("Missing 'nistmonte' section in settings")

        if 'java' not in settings.nistmonte:
            raise AssertionError("Missing 'java' option in 'nistmonte' section of settings")

        java = settings.nistmonte.java
        if not os.path.isfile(java):
            raise AssertionError("Specified Java executable (%s) does not exist" % java)
        if not os.access(java, os.X_OK):
            raise AssertionError("Specified Java executable (%s) is not executable" % java)

        if 'jar' not in settings.nistmonte:
            raise AssertionError("Missing 'jar' option in 'nistmonte' section of settings")

        jar = settings.nistmonte.jar
        if not os.path.isfile(jar):
            raise AssertionError("Specified jar path (%s) does not exist" % jar)
        if os.path.splitext(jar)[1] != '.jar':
            raise AssertionError("Specified jar path (%s) is not a jar" % jar)

    def autoconfig(self, programs_path):
        settings = get_settings()

        # Java
        try:
            if os.name == 'posix':
                java_path = subprocess.check_output(['which', 'java'])
            else:
                java_path = subprocess.check_output('for %i in (java.exe) do @echo.   %~$PATH:i', shell=True)
            java_path = java_path.decode('ascii').strip()
        except subprocess.CalledProcessError:
            return False
        settings.add_section('nistmonte').java = java_path

        # jar
        if sys.platform == 'linux':
            jar_path = '/usr/share/libpymontecarlo-java/lib/pymontecarlo-dtsa.jar'
            if not os.path.exists(jar_path):
                return False
        else:
            jar_path = os.path.join(programs_path, self.alias, 'pymontecarlo-nistmonte.jar')
            if not os.path.exists(jar_path):
                return False
        settings.add_section('nistmonte').jar = jar_path

        return True

program = _NISTMonteProgram()
