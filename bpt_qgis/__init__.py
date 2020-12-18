# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BPTQGIS
                                 A QGIS plugin
 QGIS plugin to determine the near-optimal locations for buildings in a map.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-12-17
        copyright            : (C) 2020 by Sean Francis N. Ballais
        email                : snballais@up.edu.ph
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
import os
import sys


curr_dir_path = os.path.dirname(os.path.realpath(__file__))
lib_dir = os.path.join(curr_dir_path, 'libs')
sys.path.insert(0, lib_dir)


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BPTQGIS class from file BPTQGIS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .bpt_qgis import BPTQGIS
    return BPTQGIS(iface)
