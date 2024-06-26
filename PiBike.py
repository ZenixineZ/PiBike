#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:11:10 2024

@author: zenix
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow


class DataReader():
    def __init__(self):
        self.count = 0.0
    def get_new_data(self):
        if(self.count == 10.0):
            self.count = 0.0
        self.count += 1
        return [self.count, self.count, self.count, self.count, self.count, self.count]

class PiBike(QMainWindow):
    def __init__(self, data_reader):
        self.data_reader = data_reader
        super(PiBike, self).__init__()
    def setUI(self, ui):
        self.ui = ui
        self.update_timer = QtCore.QTimer(self)
        self.update_timer.timeout.connect(self.update_vals)
        self.update_timer.start(500)
    
    def update_vals(self):
        vals = self.data_reader.get_new_data()
        self.ui.lblDistVal.setText(str(vals[0]) + " Miles")
        self.ui.lblSpeedVal.setText(str(vals[1]) + " MPH")
        self.ui.lblAccVal.setText(str(vals[2]) + " Ft/sec^2")
        self.ui.lblElevVal.setText(str(vals[3]) + " Ft")
        self.ui.lblCadVal.setText(str(vals[4]))
        self.ui.lblAvgSpeedVal.setText(str(vals[5]) + " MPH")
        

class Ui_PiBike(object):
    def setupUi(self, PiBike):
        PiBike.setObjectName("PiBike")
        PiBike.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PiBike)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabData = QtWidgets.QWidget()
        self.tabData.setObjectName("tabData")
        self.gridLayout = QtWidgets.QGridLayout(self.tabData)
        self.gridLayout.setObjectName("gridLayout")
        self.lblDist = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lblDist.setFont(font)
        self.lblDist.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDist.setObjectName("lblDist")
        self.gridLayout.addWidget(self.lblDist, 0, 0, 1, 1)
                                  
        self.lblAvgSpeed = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lblAvgSpeed.setFont(font)
        self.lblAvgSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvgSpeed.setObjectName("lblAvgSpeed")
        self.gridLayout.addWidget(self.lblAvgSpeed, 2, 1, 1, 1)
        self.lblCad = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lblCad.setFont(font)
        self.lblCad.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCad.setObjectName("lblCad")
        self.gridLayout.addWidget(self.lblCad, 4, 1, 1, 1)
        self.lblAcc = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lblAcc.setFont(font)
        self.lblAcc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAcc.setObjectName("lblAcc")
        self.gridLayout.addWidget(self.lblAcc, 4, 0, 1, 1)
        self.lblElev = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lblElev.setFont(font)
        self.lblElev.setAlignment(QtCore.Qt.AlignCenter)
        self.lblElev.setObjectName("lblElev")
        self.gridLayout.addWidget(self.lblElev, 0, 1, 1, 1)
        self.lblSpeed = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lblSpeed.setFont(font)
        self.lblSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSpeed.setObjectName("lblSpeed")
        self.gridLayout.addWidget(self.lblSpeed, 2, 0, 1, 1)
        self.lblElevVal = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblElevVal.setFont(font)
        self.lblElevVal.setText("")
        self.lblElevVal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblElevVal.setObjectName("lblElevVal")
        self.gridLayout.addWidget(self.lblElevVal, 1, 1, 1, 1)
        self.lblDistVal = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblDistVal.setFont(font)
        self.lblDistVal.setText("")
        self.lblDistVal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDistVal.setObjectName("lblDistVal")
        self.gridLayout.addWidget(self.lblDistVal, 1, 0, 1, 1)
        self.lblSpeedVal = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblSpeedVal.setFont(font)
        self.lblSpeedVal.setText("")
        self.lblSpeedVal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSpeedVal.setObjectName("lblSpeedVal")
        self.gridLayout.addWidget(self.lblSpeedVal, 3, 0, 1, 1)
        self.lblAvgSpeedVal = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblAvgSpeedVal.setFont(font)
        self.lblAvgSpeedVal.setText("")
        self.lblAvgSpeedVal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvgSpeedVal.setObjectName("lblAvgSpeedVal")
        self.gridLayout.addWidget(self.lblAvgSpeedVal, 3, 1, 1, 1)
        self.lblAccVal = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblAccVal.setFont(font)
        self.lblAccVal.setText("")
        self.lblAccVal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAccVal.setObjectName("lblAccVal")
        self.gridLayout.addWidget(self.lblAccVal, 6, 0, 1, 1)
        self.lblCadVal = QtWidgets.QLabel(self.tabData)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblCadVal.setFont(font)
        self.lblCadVal.setText("")
        self.lblCadVal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCadVal.setObjectName("lblCadVal")
        self.gridLayout.addWidget(self.lblCadVal, 6, 1, 1, 1)
        self.tabWidget.addTab(self.tabData, "")
        self.tabGraphs = QtWidgets.QWidget()
        self.tabGraphs.setObjectName("tabGraphs")
        self.tabWidget.addTab(self.tabGraphs, "")
        self.tabMao = QtWidgets.QWidget()
        self.tabMao.setObjectName("tabMao")
        self.tabWidget.addTab(self.tabMao, "")
        self.verticalLayout.addWidget(self.tabWidget)
        PiBike.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PiBike)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        PiBike.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PiBike)
        self.statusbar.setObjectName("statusbar")
        PiBike.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(PiBike)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PiBike)

    def retranslateUi(self, PiBike):
        _translate = QtCore.QCoreApplication.translate
        PiBike.setWindowTitle(_translate("PiBike", "MainWindow"))
        self.lblDist.setText(_translate("PiBike", "Distance"))
        self.lblAvgSpeed.setText(_translate("PiBike", "Avg Speed"))
        self.lblCad.setText(_translate("PiBike", "Cadence"))
        self.lblAcc.setText(_translate("PiBike", "Acceleration"))
        self.lblElev.setText(_translate("PiBike", "Elevation Gain"))
        self.lblSpeed.setText(_translate("PiBike", "Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), _translate("PiBike", "Live Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGraphs), _translate("PiBike", "Graphs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMao), _translate("PiBike", "Map"))
        self.menuFile.setTitle(_translate("PiBike", "File"))
        self.menuAbout.setTitle(_translate("PiBike", "About"))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    data_reader = DataReader()
    piBike = PiBike(data_reader)
    ui = Ui_PiBike()
    ui.setupUi(piBike)
    piBike.setUI(ui)
    piBike.show()
    sys.exit(app.exec_())

    
    

    
