# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Tue Apr  5 19:30:24 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ReadCSV import ReadCSV
from Buffer import Buffer
from Fixer import Fixer
import os
from DataLoader import DataLoader
from Plots import Plots
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    plots = Plots()
    data = []
    rfile = []
    csv_loaded = False
    upload_data = []
    wys = kat = dyst = pred = odchyl = 0
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(819, 582)
        self.ladujButton = QtGui.QPushButton(Form)
        self.ladujButton.setGeometry(QtCore.QRect(0, 10, 121, 27))
        self.ladujButton.setObjectName(_fromUtf8("ladujButton"))
        self.ladujButton.clicked.connect(self.connect)
        self.plotWidget = QtGui.QTabWidget(Form)
        self.plotWidget.setGeometry(QtCore.QRect(130, 20, 681, 551))
        self.plotWidget.setDocumentMode(False)
        self.plotWidget.setTabsClosable(False)
        self.plotWidget.setMovable(False)
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.info = QtGui.QLabel(Form)
        self.info.setGeometry(QtCore.QRect(155,360, 600, 377))
        self.info.setText(_fromUtf8("Plik z danymi powinien nazywac sie test.csv i znajdowac sie w tym katalogu"))
        self.info.setObjectName(_fromUtf8("info"))
        self.infocsv = QtGui.QLabel(Form)
        self.infocsv.setGeometry(QtCore.QRect(20,45, 121, 17))
        self.infocsv.setText(_fromUtf8(""))
        self.infocsv.setObjectName(_fromUtf8("infocsv"))
        self.wysokoscButton = QtGui.QPushButton(Form)
        self.wysokoscButton.setGeometry(QtCore.QRect(0, 70, 121, 27))
        self.wysokoscButton.setObjectName(_fromUtf8("wysokoscButton"))
        self.wysokoscButton.clicked.connect(self.plotWys)
        self.katButton = QtGui.QPushButton(Form)
        self.katButton.setGeometry(QtCore.QRect(0, 110, 121, 27))
        self.katButton.setObjectName(_fromUtf8("katButton"))
        self.katButton.clicked.connect(self.plotKat)
        self.dystButton = QtGui.QPushButton(Form)
        self.dystButton.setGeometry(QtCore.QRect(0, 150, 121, 27))
        self.dystButton.setObjectName(_fromUtf8("dystButton"))
        self.dystButton.clicked.connect(self.plotDyst)
        self.predButton = QtGui.QPushButton(Form)
        self.predButton.setGeometry(QtCore.QRect(0, 190, 121, 27))
        self.predButton.setObjectName(_fromUtf8("predButton"))
        self.predButton.clicked.connect(self.plotPred)
        self.odchylButton = QtGui.QPushButton(Form)
        self.odchylButton.setGeometry(QtCore.QRect(0, 230, 121, 27))
        self.odchylButton.setObjectName(_fromUtf8("odchylButton"))
        self.odchylButton.clicked.connect(self.plotOdchyl)

        self.retranslateUi(Form)
        self.plotWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ladujButton.setText(_translate("Form", "Zaladuj csv", None))
        self.wysokoscButton.setText(_translate("Form", "Wysokosc", None))
        self.katButton.setText(_translate("Form", "Kat nachylenia", None))
        self.dystButton.setText(_translate("Form", "Dystans", None))
        self.predButton.setText(_translate("Form", "Predkosc", None))
        self.odchylButton.setText(_translate("Form", "Odchylenie", None))
    def connect(self):
        if (self.csv_loaded == False):
            self.plotWidget.clear()
            line = 1
            rfile = ReadCSV.read("test.csv")
            for row in rfile:
			    if(line == 1):
				    line = line+1
				    continue
			    self.upload_data.append(row)

            Fixer.fixTimeAndAlt(self.upload_data)
            buff = Buffer()
            if os.path.exists('data.txt'):
                 os.remove('data.txt')
            for i in self.upload_data:
	            buff.sendToBuffer(i)
	            buff.sendData()
            self.data = (DataLoader.read('data.txt'))
            self.csv_loaded = True
	    self.infocsv.setText(_fromUtf8("Zaladowano"))
            self.info.setText("")
            self.wys = self.kat = self.dyst = self.pred = self.odchyl = 0
    def plotWys(self):
        if (self.csv_loaded == True and self.wys == 0):
            fig = self.plots.altitude(self.data)
            self.tWys = QtGui.QWidget()
            self.tWys.setObjectName(_fromUtf8("wys"))
            self.plotWidget.addTab(self.tWys, _fromUtf8("Wysokosc"))
            self.plotWidget.setCurrentWidget(self.tWys)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tWys.setLayout(layout)
            self.wys = -1
    def plotKat(self):
        if (self.csv_loaded == True and self.kat == 0):
            fig = self.plots.pitch(self.data)
            self.tKat = QtGui.QWidget()
            self.tKat.setObjectName(_fromUtf8("kat"))
            self.plotWidget.addTab(self.tKat, _fromUtf8("Kat"))
            self.plotWidget.setCurrentWidget(self.tKat)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tKat.setLayout(layout)
            self.kat = -1
    def plotDyst(self):
        if (self.csv_loaded == True and self.dyst == 0):
            fig = self.plots.distance(self.data)
            self.tDyst = QtGui.QWidget()
            self.tDyst.setObjectName(_fromUtf8("dyst"))
            self.plotWidget.addTab(self.tDyst, _fromUtf8("Dystans"))
            self.plotWidget.setCurrentWidget(self.tDyst)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tDyst.setLayout(layout)
            self.dyst = -1
    def plotPred(self):
        if (self.csv_loaded == True and self.pred == 0):
            fig = self.plots.speed(self.data)
            self.tPred = QtGui.QWidget()
            self.tPred.setObjectName(_fromUtf8("pred"))
            self.plotWidget.addTab(self.tPred, _fromUtf8("Predkosc"))
            self.plotWidget.setCurrentWidget(self.tPred)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tPred.setLayout(layout)
            self.pred = -1
    def plotOdchyl(self):
       if (self.csv_loaded == True and self.odchyl == 0):
            fig = self.plots.roll(self.data)
            self.tOdchyl = QtGui.QWidget()
            self.tOdchyl.setObjectName(_fromUtf8("odchyl"))
            self.plotWidget.addTab(self.tOdchyl, _fromUtf8("Odchylenie"))
            self.plotWidget.setCurrentWidget(self.tOdchyl)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tOdchyl.setLayout(layout)
            self.odchyl = -1
            
        
        
