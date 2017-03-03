#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculate telecomunication cost

author: Hrvoje T
last edited: February 2017
"""

import sys
from mainwindow import *
import datetime


# File for saving the result. Default 'output_pipni2.csv' if not explicitly named
OUTPUT_FILE = "output_pipni.csv"

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        """Initializing GUI from mainwindow module"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # disable 'Spremi' button if there is no data in textBrowser
        self.spremi_button_disabled()

        # call a method 'selectfile_Dialog' if one of QLineEdit objects is clicked
        self.ui.lista_lineEdit.clicked.connect(self.selectfile_Dialog)
        self.ui.specif_lineEdit.clicked.connect(self.selectfile_Dialog)
        self.ui.lista_lineEdit_2.clicked.connect(self.selectfile_Dialog)
        # Close the main windows when 'Exit' menu is triggered
        self.ui.actionExit.triggered.connect(self.close)
        # When 'Prikaži' button is clicked, connect 'accepted' signal to method
        self.ui.prikazi_button.clicked.connect(self.prikazi_button_clicked)
        # When 'Spremi' button is clicked, connect 'accepted' signal to method
        self.ui.spremi_button.clicked.connect(self.spremi_button_clicked)
        # When 'Otkazi' button is clicked, connect 'accepted' signal to method
        self.ui.otkazi_button.clicked.connect(self.otkazi_button_clicked)
        # When 'Reset' menu is triggered
        self.ui.actionReset.triggered.connect(self.otkazi_button_clicked)


    def selectfile_Dialog(self, event=None):
        """
        Opens a dialog for choosing a file. Takes two positionals arguments
        'self' and 'event' because 'mouseReleaseEvent' sends two, when creating
        new method eg. 'label1.mouseReleaseEvent = self.showText1'. When
        subclassing QLineEdit as ClickableLineEdit 'event' is None"
        """
        # QFileDialog doesn't use native OS dialog like this one:
        # 'fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')'
        # to remember last opening path
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
                   self, 'Open File', '', 'Text file (*.csv)',
                   None, QtWidgets.QFileDialog.DontUseNativeDialog)
        # sender is object that sends the signal
        sender = self.sender()
        # write selected file name into that QLineEdit widget 'lista_lineEdit'
        sender.setText(fname)
        # set options for combobox only from 'lista_lineEdit' QLineEdit widget
        if sender.objectName() == "lista_lineEdit":
            # cals a method fill_combobox
            self.fill_combobox(fname)


    def open_file(self, filename):
        """Reads a file and returns a data. Every line is an item in a list"""
        try:
            with open(filename, "r") as fh:
                # read from a file line by line. Every line is a item in a list
                data = fh.readlines()
                # removes escape charachters from items in list 'data'
                data = [x.strip() for x in data]
            return data
        except FileNotFoundError as e:
            self.ui.textBrowser.setText(str("Greška {}; popuni podatke".format(e)))


    def fill_combobox(self, filename):
        """
        Set combobox options from lista.csv header. This method is called
        when first QLineEdit widget is clicked
        """
        # to not allow filename of type Nonetype eg. filename=""
        if filename != "":
            # removes all previous combobox options
            self.ui.zeljeni_comboBox.clear()
            data = self.open_file(filename)
            # from 0-th item in list 'data' and split where is ';' sign
            first_row_words = data[0].split(";")
            index = 0
            # removes first default combobox option
            self.ui.zeljeni_comboBox.removeItem(index)
            # for every item in first row add it as an combobox option
            for item in first_row_words:
                self.ui.zeljeni_comboBox.addItem("")
                self.ui.zeljeni_comboBox.setItemText(index, first_row_words[index])
                index += 1


    def write_outputfile(self):
        """Write everything from textBrowser to a output file"""
        # reads from adresar QLineEdit to see for output file name
        self.adresar_changed()
        # Writes to a global variable defined at the begining of a module
        global OUTPUT_FILE
        data = self.ui.textBrowser.toPlainText()
        with open(OUTPUT_FILE, "w") as f:
            f.write(data)


    def display_in_textbox(self):
        """Display calculation result in QtextBox widget"""
        self.ui.textBrowser.clear()
        self.calculations_lista()


    def cancel_settings(self):
        """Reset all app settings"""
        # remove all QLineEdit widgets text
        self.ui.lista_lineEdit.setText("")
        self.ui.specif_lineEdit.setText("")
        self.ui.lista_lineEdit_2.setText("")
        self.ui.izlazna_lineEdit.setText("")
        self.ui.broj_lineEdit.setText("")
        # radio button reset to 'Svi'
        self.ui.svi_radioButton.setChecked(True)
        # remove all combobox options
        self.ui.zeljeni_comboBox.clear()
        # clear textBrowser text
        self.ui.textBrowser.setText("")


    def adresar_changed(self):
        """Change global OUTPUT_FILE to QLineEdit widget adresar text"""
        global OUTPUT_FILE
        # add time in a file name
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        save_to = self.ui.izlazna_lineEdit.text()
        if save_to != "":
            OUTPUT_FILE = date_string + "-" + save_to
        else:
            OUTPUT_FILE = date_string + "-output_pipni.csv"


    def calculations_lista(self):
        """Method for calculation a logic of a program with lista.csv"""
        # create empty string for storing information to display
        display = []
        file_name = self.ui.lista_lineEdit.text()
        # open a file that is listed in lista QLineEdit widget and
        # put every line as a item in working_data list
        working_data = self.open_file(file_name)
        index = self.ui.zeljeni_comboBox.currentIndex()
        self.ui.textBrowser.setFontFamily("monospace")
        for line in working_data:
            word = line.split(";")
            display.append((word[1], word[index]))
            self.ui.textBrowser.append("{:20}{:.>30}".format(word[1], word[index]))


    def sort_tup_from_list(self, input_list):
        """Sorts tuples in a list by value"""
        tmp = []
        for tup in input_list:
            for key, val in tup:
                tmp.append((val, key))
                tmp.sort(reverse=True)
        return tmp


    def spremi_button_disabled(self):
        """Disables 'Spremi' button until textBrowser if filled"""
        data = self.ui.textBrowser.toPlainText()
        if data == "":
            self.ui.spremi_button.setDisabled(True)
        else:
            self.ui.spremi_button.setDisabled(False)


    def prikazi_button_clicked(self):
        """Actions that hapen when OK button is clicked"""
        self.display_in_textbox()
        self.spremi_button_disabled()


    def spremi_button_clicked(self):
        """Calls a method for saving a result in a file"""
        self.write_outputfile()


    def otkazi_button_clicked(self):
        """Calls a method for canceling app settings"""
        self.cancel_settings()
        self.spremi_button_disabled()


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
