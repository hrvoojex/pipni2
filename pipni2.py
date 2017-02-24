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

        # call a method 'selectfile_Dialog' if one of QLineEdit objects is clicked
        self.ui.lista_lineEdit.clicked.connect(self.selectfile_Dialog)
        self.ui.specif_lineEdit.clicked.connect(self.selectfile_Dialog)
        self.ui.lista_lineEdit_2.clicked.connect(self.selectfile_Dialog)

        self.ui.actionExit.triggered.connect(self.close)


    def selectfile_Dialog(self, event=None):
        """
        Opens a dialog for choosing a file. Takes two positionals arguments
        'self' and 'event' because 'mouseReleaseEvent' sends two, when creating
        new method eg. 'label1.mouseReleaseEvent = self.showText1'. When
        subclassing QLineEdit as ClickableLineEdit 'event' is None"
        """
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "/home")
        # sender is object that sends the signal
        sender = self.sender()
        # wite selected file name into that QLineEdit widget 'lista_lineEdit'
        sender.setText(fname)
        # set options for combobox only from 'lista_lineEdit' QLineEdit widget
        if sender.objectName() == "lista_lineEdit":
            # cals a method fill_combobox
            self.fill_combobox(fname)


    def fill_combobox(self, filename):
        """Set combobox options from lista.csv header. This method is called
        when first QLineEdit widget is clicked"""
        with open(filename, "r") as fh:
            # read from a file line by line. Every line is a item in a list
            data = fh.readlines()
            # removes escape charachters from items in list 'data'
            data = [x.strip() for x in data]
            # from 0-th item in list 'data' and split where is ;
            first_row_words = data[0].split(";")
            index = 0
            self.ui.zeljeni_comboBox.removeItem(index)
            for item in first_row_words:
                self.ui.zeljeni_comboBox.addItem("")
                self.ui.zeljeni_comboBox.setItemText(index, first_row_words[index])
                index += 1

            #self.ui.textBrowser.setText(first_row_words[0])


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
