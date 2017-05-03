#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui


class ClickableLineEdit(QtWidgets.QLineEdit):
    """Subclassing QLineEdit class to make it clickable"""
    clicked = QtCore.pyqtSignal() # signal when the text entry is left clicked

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
        else:
            super().mousePressEvent(event)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.zeljeni_groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.zeljeni_groupBox.setGeometry(QtCore.QRect(350, 10, 431, 181))
        self.zeljeni_groupBox.setObjectName("zeljeni_groupBox")
        self.zeljeni_comboBox = QtWidgets.QComboBox(self.zeljeni_groupBox)
        self.zeljeni_comboBox.setGeometry(QtCore.QRect(10, 30, 411, 26))
        self.zeljeni_comboBox.setObjectName("zeljeni_comboBox")
        # Adds first combobox item.
        self.zeljeni_comboBox.addItem("")

        # manualy added 'Prikaži' button
        self.prikazi_button = QtWidgets.QPushButton(self.zeljeni_groupBox)
        self.prikazi_button.setGeometry(170, 145, 80, 26)
        self.prikazi_button.setText("Prikaži")

        # added 'Spremi' button
        self.spremi_button = QtWidgets.QPushButton(self.zeljeni_groupBox)
        self.spremi_button.setGeometry(250, 145, 80, 26)
        self.spremi_button.setText("Spremi")

        # added 'Cancel' button
        self.otkazi_button = QtWidgets.QPushButton(self.zeljeni_groupBox)
        self.otkazi_button.setGeometry(330, 145, 80, 26)
        self.otkazi_button.setText("Otkaži")

        self.jedansvi_groupBox = QtWidgets.QGroupBox(self.zeljeni_groupBox)
        self.jedansvi_groupBox.setGeometry(QtCore.QRect(10, 70, 151, 60))
        self.jedansvi_groupBox.setObjectName("jedansvi_groupBox")
        self.jedan_radioButton = QtWidgets.QRadioButton(self.jedansvi_groupBox)
        self.jedan_radioButton.setGeometry(QtCore.QRect(10, 30, 71, 24))
        self.jedan_radioButton.setObjectName("jedan_radioButton")
        self.svi_radioButton = QtWidgets.QRadioButton(self.jedansvi_groupBox)
        self.svi_radioButton.setGeometry(QtCore.QRect(90, 30, 61, 24))
        self.svi_radioButton.setObjectName("svi_radioButton")
        self.svi_radioButton.setChecked(True)
        self.kojibroj_groupBox = QtWidgets.QGroupBox(self.zeljeni_groupBox)
        self.kojibroj_groupBox.setGeometry(QtCore.QRect(180, 70, 241, 60))
        self.kojibroj_groupBox.setObjectName("kojibroj_groupBox")
        self.broj_lineEdit = QtWidgets.QLineEdit(self.kojibroj_groupBox)
        self.broj_lineEdit.setGeometry(QtCore.QRect(10, 28, 221, 26))
        self.broj_lineEdit.setObjectName("broj_lineEdit")
        self.datoteke_groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.datoteke_groupBox.setGeometry(QtCore.QRect(10, 10, 311, 181))
        self.datoteke_groupBox.setAutoFillBackground(False)
        self.datoteke_groupBox.setStyleSheet("")
        self.datoteke_groupBox.setFlat(False)
        self.datoteke_groupBox.setObjectName("datoteke_groupBox")
        self.listaLabel = QtWidgets.QLabel(self.datoteke_groupBox)
        self.listaLabel.setGeometry(QtCore.QRect(20, 35, 58, 18))
        self.listaLabel.setObjectName("listaLabel")
        self.specifikacijaLabel = QtWidgets.QLabel(self.datoteke_groupBox)
        self.specifikacijaLabel.setGeometry(QtCore.QRect(20, 75, 91, 18))
        self.specifikacijaLabel.setObjectName("specifikacijaLabel")
        self.adresarLabel = QtWidgets.QLabel(self.datoteke_groupBox)
        self.adresarLabel.setGeometry(QtCore.QRect(20, 115, 58, 18))
        self.adresarLabel.setObjectName("adresarLabel")
        self.izlazna_Label = QtWidgets.QLabel(self.datoteke_groupBox)
        self.izlazna_Label.setGeometry(QtCore.QRect(20, 155, 58, 18))
        self.izlazna_Label.setObjectName("izlazna_Label")
        self.izlazna_lineEdit = ClickableLineEdit(self.datoteke_groupBox)
        self.izlazna_lineEdit.setStatusTip("Unesi naziv datoteke za spremanje rezultata")
        self.izlazna_lineEdit.setGeometry(QtCore.QRect(120, 150, 171, 26))
        self.izlazna_lineEdit.setObjectName("izlazna_lineEdit")
        self.lista_lineEdit = ClickableLineEdit(self.datoteke_groupBox)
        self.lista_lineEdit.setStatusTip("Klikni za unos lista.csv datoteke")
        self.lista_lineEdit.setGeometry(QtCore.QRect(120, 30, 171, 26))
        self.lista_lineEdit.setObjectName("lista_lineEdit")
        self.specif_lineEdit = ClickableLineEdit(self.datoteke_groupBox)
        self.specif_lineEdit.setStatusTip("Klikni za unos 'specifikacija.csv' datoteke")
        self.specif_lineEdit.setGeometry(QtCore.QRect(120, 70, 171, 26))
        self.specif_lineEdit.setObjectName("specif_lineEdit")
        self.lista_lineEdit_2 = ClickableLineEdit(self.datoteke_groupBox)
        self.lista_lineEdit_2.setStatusTip("Klikni za unos 'adresar.csv' datoteke")
        self.lista_lineEdit_2.setGeometry(QtCore.QRect(120, 110, 171, 26))
        self.lista_lineEdit_2.setObjectName("lista_lineEdit_2")
        self.izlazni_groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.izlazni_groupBox.setGeometry(QtCore.QRect(10, 210, 771, 521))
        self.izlazni_groupBox.setObjectName("izlazni_groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.izlazni_groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 751, 481))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralWidget)

        # create menu bar
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        # actions
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setShortcut("Ctrl+B")
        self.actionAbout.setStatusTip("O programu")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionReset.setShortcut("Ctrl+R")
        self.actionReset.setStatusTip("Resetiraj postavke")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+E")
        self.actionExit.setStatusTip("Zatvori program")

        # menu actions
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        # added here from QtCreator's translate function
        MainWindow.setWindowTitle("PipNi2")
        self.zeljeni_groupBox.setTitle("Željeni podaci")
        self.zeljeni_comboBox.setItemText(0, "Uvezi 'lista.csv' file za opcije")
        self.jedansvi_groupBox.setTitle("Jedan broj ili svi:")
        self.jedan_radioButton.setText("Jedan")
        self.svi_radioButton.setText("Svi")
        self.kojibroj_groupBox.setTitle("Koji broj:")
        self.broj_lineEdit.setPlaceholderText("npr. 3859Xxxxxxx")
        self.datoteke_groupBox.setTitle("Datoteke csv")
        self.listaLabel.setText("Lista:")
        self.specifikacijaLabel.setText("Specifikacija:")
        self.adresarLabel.setText("Adresar:")
        self.izlazna_Label.setText("Snimi u:")
        self.izlazna_lineEdit.setPlaceholderText("npr. resultat.csv")
        self.lista_lineEdit.setPlaceholderText("npr. lista.csv")
        self.specif_lineEdit.setPlaceholderText("npr. sprecifikacija.csv")
        self.lista_lineEdit_2.setPlaceholderText("npr. adresar.csv")
        self.izlazni_groupBox.setTitle("Izlazni podaci")
        self.menuFile.setTitle("File")
        self.menuHelp.setTitle("Help")
        self.actionAbout.setText("About")
        self.actionReset.setText("Reset")
        self.actionExit.setText("Exit")