#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Calculate telecomunication cost"""

import sys
from mainwindow import *


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        """Initializing GUI from mainwindow module"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # call a method 'selectfile_Dialog' if one of QLineEdit
        # object's is clicked
        self.ui.lista_lineEdit.clicked.connect(self.selectfile_Dialog)
        self.ui.specif_lineEdit.clicked.connect(self.selectfile_Dialog)
        self.ui.lista_lineEdit_2.clicked.connect(self.selectfile_Dialog)


    def write_to_browser(self, text):
        self.ui.textBrowser.setText(text)


    def selectfile_Dialog(self, event=None):
        """
        Opens a dialog for choosing a file. Takes two positionals arguments
        'self' and 'event' because 'mouseReleaseEvent' sends two. When
        subclassing QLineEdit as ClickableLineEdit 'event' is None"
        """
        # sender is object that sends the signal
        sender = self.sender()
        self.write_to_browser(sender.objectName())
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "/home")
        if fname:
            sender.setText(fname)


    def openfile(self, file_path):
            """Opens a file as 'read-only' and reads it"""
            f = open(file_path, 'r')
            with f:
                data = f.read()
                return data


    def closeEvent(self, event):
        """Ask for closing confirmation"""
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def keyPressEvent(self, e):
        """Action when return or escape is pressed"""
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    instance = Main()
    instance.show()
    sys.exit(app.exec_())
