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
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import qgis, platform
from qgis.core import *
from qgis.gui import *
from qgis.PyQt.QtWidgets import *

import os, sys

# Initialize Qt resources from file resources.py
#import resources
# Import the code for the dialog
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
        self.dlg.spinBoxScale.setValue(1000)
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
        scales = self.preferences("scale", False)
        paperformats = self.preferences("format", True)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass


    def preferences(self, pref, text):
        prefs = []
        preffilename = ":/plugins/NextPrint/preferences/preferences.xml"

        try:
            preffile = open(preffilename, "r")
            prefxml = preffile.read()

            doc = QtXml.QDomDocument()
            doc.setContent(prefxml, True)

            root = doc.documentElement()
            if root.tagName() != "preferences":
                return

            n = root.firstChild()
            while not n.isNull():
                e = n.toElement()
                sube = e.firstChild()
                while not sube.isNull():
                    if sube.toElement().tagName() == pref:
                        try:
                            if not text:
                                float(sube.toElement().text())
                            prefs.append(sube.toElement().text())
                        except ValueError:
                            print("float error: reading scales")
                    sube = sube.nextSibling()
                n = n.nextSibling()
        except IOError:

            print("error opening preferences.xml")

        return prefs
