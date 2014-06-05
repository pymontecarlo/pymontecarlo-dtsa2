#!/usr/bin/env python
"""
================================================================================
:mod:`worker` -- NISTMonte worker
================================================================================

.. module:: worker
   :synopsis: NISTMonte worker

.. inheritance-diagram:: pymontecarlo.program.nistmonte.runner.worker

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2012 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.
import os
import subprocess
import logging

# Third party modules.

# Local modules.
from pymontecarlo.settings import get_settings
from pymontecarlo.program.worker import SubprocessWorker as _Worker

# Globals and constants variables.

class Worker(_Worker):

    def __init__(self, program):
        """
        Runner to run NISTMonte simulation(s).
        """
        _Worker.__init__(self, program)

        self._java_exec = get_settings().nistmonte.java
        logging.debug('Java executable: %s', self._java_exec)

        self._jar_path = get_settings().nistmonte.jar
        logging.debug('pyMonteCarlo jar path: %s', self._jar_path)

    def run(self, options, outputdir, workdir):
        xmlfilepath = self.create(options, workdir)

        args = [self._java_exec]
        args += ['-Djava.library.path=%s' % os.path.dirname(self._jar_path)] # for native libraries
        args += ['-jar', self._jar_path]
        args += ['-o', workdir]
        args += [xmlfilepath]
        logging.debug('Launching %s', ' '.join(args))

        with self._create_process(args, stdout=subprocess.PIPE) as process:
            for line in iter(process.stdout.readline, b""):
                infos = line.decode('ascii').split('\t')
                if len(infos) == 2:
                    self._progress = float(infos[0])
                    self._status = infos[1].strip()

        retcode = self._join_process()

        if retcode != 0:
            raise RuntimeError("An error occurred during the simulation")

        return self._importer.import_(options, workdir)
