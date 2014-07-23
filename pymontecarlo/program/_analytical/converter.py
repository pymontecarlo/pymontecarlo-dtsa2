#!/usr/bin/env python
"""
================================================================================
:mod:`converter` -- Analytical program conversion from base options
================================================================================

.. module:: converter
   :synopsis: Analytical program conversion from base options

.. inheritance-diagram:: pymontecarlo.program._analytical.input.converter

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
from pymontecarlo.program.converter import Converter as _Converter

from pymontecarlo.options.particle import ELECTRON
from pymontecarlo.options.beam import PencilBeam
from pymontecarlo.options.material import Material
from pymontecarlo.options.geometry import Substrate
from pymontecarlo.options.detector import PhotonIntensityDetector, PhiZDetector
from pymontecarlo.options.model import \
    (IONIZATION_CROSS_SECTION, MASS_ABSORPTION_COEFFICIENT,
     UserDefinedMassAbsorptionCoefficientModel)

# Globals and constants variables.

class Converter(_Converter):
    """
    Converter for analytical program simulation.
    """

    PARTICLES = [ELECTRON]
    MATERIALS = [Material]
    BEAMS = [PencilBeam]
    GEOMETRIES = [Substrate]
    DETECTORS = [PhotonIntensityDetector, PhiZDetector]
    LIMITS = []
    MODELS = {IONIZATION_CROSS_SECTION: [IONIZATION_CROSS_SECTION.bote_salvat2008,
                                         IONIZATION_CROSS_SECTION.casnati1982,
                                         IONIZATION_CROSS_SECTION.dijkstra_heijliger1998,
                                         IONIZATION_CROSS_SECTION.pouchou1986],
              MASS_ABSORPTION_COEFFICIENT: [MASS_ABSORPTION_COEFFICIENT.chantler2005,
                                            MASS_ABSORPTION_COEFFICIENT.heinrich_ixcom11,
                                            MASS_ABSORPTION_COEFFICIENT.heinrich_ixcom11_dtsa,
                                            MASS_ABSORPTION_COEFFICIENT.henke1993,
                                            MASS_ABSORPTION_COEFFICIENT.none,
                                            MASS_ABSORPTION_COEFFICIENT.pouchou_pichoir1991,
                                            UserDefinedMassAbsorptionCoefficientModel],
              }
    DEFAULT_MODELS = {IONIZATION_CROSS_SECTION: IONIZATION_CROSS_SECTION.bote_salvat2008,
                      MASS_ABSORPTION_COEFFICIENT: MASS_ABSORPTION_COEFFICIENT.chantler2005}

    def _convert_limits(self, options):
        for limit in list(options.limits):
            clasz = limit.__class__
            if clasz not in self.LIMITS:
                options.limits.discard(limit)

                self._warn("Limit of type '%s' cannot be converted." % clasz.__name__,
                           "It was removed")

        return True
