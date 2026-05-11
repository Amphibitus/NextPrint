# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NextPrint
                                 A QGIS plugin
 This plugin makes it easy to print using templates and text variables.
 It provides an easy to use interface/dialog for text input and for 
 rotating and placing your template for printing on map canvas.
                              -------------------
        begin                : 2018-01-08
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Jesper Jøker Eg / GISkonsulenten
        email                : jesper@giskonsulenten.dk
        begin                : 2024-09-05
        git sha              : $Format:%H$
        copyright            : (C) 2024 by g3er@geoplaning.de
        email                : g3er@geoplaning.de
        
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os
import sys
import platform

# Der richtige Weg für QGIS 3 & 4: Nutze qgis.PyQt statt PyQt5
from qgis.PyQt.QtCore import QObject, QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import  QToolButton


from qgis.core import *
from qgis.gui import *


# Lokale Ressourcen und Dialoge
from .NextPrint_dialog import NextPrintDialog
from .InstantPrintTool import InstantPrintTool
from . import resources


class NextPrint(QObject):
    def __init__(self, iface):
        QObject.__init__(self)

        self.iface = iface
        self.pluginDir = os.path.dirname(__file__)
        self.tool = InstantPrintTool(self.iface)
        
        # Localize
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.pluginDir, 'i18n', 'instantprint_{}.qm'.format(locale))

        
        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)
            QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        self.toolButton = QToolButton(self.iface.mapNavToolToolBar())
        self.toolButton.setIcon(QIcon(":/plugins/NextPrint/icon.png"))
        self.toolButton.setText(self.tr("NextPrint"))
        self.toolButton.setToolTip(self.tr("NextPrint"))
        self.toolButton.setCheckable(True)
        self.toolAction = self.iface.pluginToolBar().addWidget(self.toolButton)

        self.toolButton.toggled.connect(self.__enableTool)
        self.iface.mapCanvas().mapToolSet.connect(self.__onToolSet)


        
    def unload(self):
        self.tool.setEnabled(False)
        self.tool = None
        self.iface.pluginToolBar().removeAction(self.toolAction)

    def __enableTool(self, active):
        self.tool.setEnabled(active)

    def __onToolSet(self, tool):
        if tool != self.tool:
            self.toolButton.setChecked(False)

    def exitAll(self):
        self.dlg.comboBox_scale.setValue(1000)
        self.dlg.spinBoxRotation.setValue(0)
        self.dlg.LegendCheckbox.setChecked(False)
        self.dialogui.LegendCheckbox.setEnabled(True)
        self.dlg.close()
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&NextPrint'),
                action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        """Run method that performs all the real work"""

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass



