# Copyright 2013 Colin Duquesnoy
#
# This file is part of OpenCobolIDE.
#
# OpenCobolIDE is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# OpenCobolIDE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# OpenCobolIDE. If not, see http://www.gnu.org/licenses/.
"""
Contains the application dialogs
"""
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
from oci.settings import Settings
from oci.ui import loadUi


class DlgNewFile(QtGui.QDialog):

    def path(self):
        return os.path.join(
            self.lineEditPath.text(),
            self.lineEditName.text() + self.comboBoxExtension.currentText())

    def template(self):
        """ Gets the file template"""
        return ""

    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        loadUi("dlg_file_type.ui", self)
        self.enableOkButton()
        completer = QtGui.QCompleter(self)
        completer.setModel(QtGui.QDirModel(completer))
        self.lineEditPath.setCompleter(completer)

    @QtCore.pyqtSlot(unicode)
    def on_lineEditName_textChanged(self, txt):
        self.enableOkButton()

    @QtCore.pyqtSlot(unicode)
    def on_lineEditPath_textChanged(self, txt):
        self.enableOkButton()

    @QtCore.pyqtSlot()
    def on_toolButton_clicked(self):
        ret = QtGui.QFileDialog.getExistingDirectory(
            self, "Choose the program directory",
            Settings().lastFilePath)
        if ret:
            self.lineEditPath.setText(ret)

    def enableOkButton(self):
        pth = self.lineEditPath.text()
        name = self.lineEditName.text()
        enable =  name != "" and os.path.exists(pth) and os.path.isdir(pth)
        bt = self.buttonBox.button(QtGui.QDialogButtonBox.Ok)
        bt.setEnabled(enable)