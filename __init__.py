# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NextPrint
                                 A QGIS plugin
 This plugin makes it easy to print using templates and text variables. It provides an easy to use interface/dialog for text input and for rotating and placing your template for printing on map canvas.
version=0.1

 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-10-02
        copyright            : (C) 2019 by Jesper Jøker Eg - GISkonsulenten
        email                : jesper@giskonsulenten.dk

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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load NextPrint class from file NextPrint.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .NextPrint import NextPrint
    return NextPrint(iface)
