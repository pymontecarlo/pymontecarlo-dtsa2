#!/usr/bin/env python
"""
================================================================================
:mod:`config_gui` -- PAP program GUI configuration
================================================================================

.. module:: config_gui
   :synopsis: PAP program GUI configuration

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2012 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.
import os

# Third party modules.

# Local modules.
from pymontecarlo.program.config_gui import GUI, _ConfigurePanelWidget
from pymontecarlo.program.pap.config import program

from pymontecarlo.ui.gui.util.widget import FileBrowseWidget

# Globals and constants variables.

class _PAPConfigurePanelWidget(_ConfigurePanelWidget):

    def _initUI(self):
        # Controls
        self._brw_java = FileBrowseWidget()
        if os.name == 'nt':
            self._brw_java.setNameFilter('Application files (*.exe)')
        else:
            self._brw_java.setNameFilter('Application files (*)')

        self._brw_jar = FileBrowseWidget()
        self._brw_jar.setNameFilter('Jar files (*.jar)')

        # Layouts
        layout = _ConfigurePanelWidget._initUI(self)
        layout.addRow('Path to Java executable', self._brw_java)
        layout.addRow('Path to pymontecarlo-dtsa2-pap.jar', self._brw_jar)

        # Signals
        self._brw_java.pathChanged.connect(self._onPathChanged)
        self._brw_jar.pathChanged.connect(self._onPathChanged)

        return layout

    def _onPathChanged(self, path):
        if not path:
            return
        if not self._brw_java.baseDir():
            self._brw_java.setBaseDir(path)
        if not self._brw_jar.baseDir():
            self._brw_jar.setBaseDir(path)

    def hasAcceptableInput(self):
        if not self._brw_java.path():
            return False
        if not os.access(self._brw_java.path(), os.X_OK):
            return False
        if not self._brw_jar.path():
            return False
        return True

    def setSettings(self, settings):
        if 'pap' in settings:
            path = getattr(settings.pap, 'java', None)
            try:
                self._brw_java.setPath(path)
            except ValueError:
                pass

            path = getattr(settings.pap, 'jar', None)
            try:
                self._brw_jar.setPath(path)
            except ValueError:
                pass

    def updateSettings(self, settings):
        section = _ConfigurePanelWidget.updateSettings(self, settings)
        section.java = self._brw_java.path()
        section.jar = self._brw_jar.path()
        return section

class _PAPGUI(GUI):

    def create_configure_panel(self, parent=None):
        """
        Returns the configure panel for this program.

        :arg parent: parent window
        :arg settings: settings object
        """
        return _PAPConfigurePanelWidget(program, parent)

gui = _PAPGUI()
