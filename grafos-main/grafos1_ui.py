# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafos1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 798)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 50, 421, 151))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.btnPintarGrafo = QtWidgets.QPushButton(self.centralwidget)
        self.btnPintarGrafo.setGeometry(QtCore.QRect(380, 210, 101, 31))
        self.btnPintarGrafo.setObjectName("btnPintarGrafo")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(70, 260, 751, 491))
        self.graphicsView.setObjectName("graphicsView")
        self.lblTtitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo.setGeometry(QtCore.QRect(370, 0, 301, 31))
        self.lblTtitulo.setStyleSheet(
            'font: 75 14pt "MS Shell Dlg 2";\n' "color:rgb(0, 85, 255);"
        )
        self.lblTtitulo.setObjectName("lblTtitulo")
        self.lblTtitulo_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo_3.setGeometry(QtCore.QRect(170, 10, 161, 31))
        self.lblTtitulo_3.setStyleSheet(
            'font: 75 14pt "MS Shell Dlg 2";\n' "color:rgb(0, 85, 255);"
        )
        self.lblTtitulo_3.setObjectName("lblTtitulo_3")
        self.lblTtitulo2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo2.setGeometry(QtCore.QRect(80, 270, 181, 71))
        self.lblTtitulo2.setStyleSheet(
            'font: 75 14pt "MS Shell Dlg 2";\n' "color:rgb(0, 85, 255);"
        )
        self.lblTtitulo2.setText("")
        self.lblTtitulo2.setPixmap(QtGui.QPixmap("logo_eafit_blanco.png"))
        self.lblTtitulo2.setObjectName("lblTtitulo2")
        self.lblTtitulo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo_2.setGeometry(QtCore.QRect(690, 10, 131, 31))
        self.lblTtitulo_2.setStyleSheet(
            'font: 75 14pt "MS Shell Dlg 2";\n' "color:rgb(0, 85, 255);"
        )
        self.lblTtitulo_2.setObjectName("lblTtitulo_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(520, 50, 421, 151))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.K = QtWidgets.QSpinBox(self.centralwidget)
        self.K.setGeometry(QtCore.QRect(730, 220, 42, 22))
        self.K.setObjectName("K")
        self.lblTtitulo_4 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo_4.setGeometry(QtCore.QRect(700, 210, 31, 31))
        self.lblTtitulo_4.setStyleSheet(
            'font: 75 14pt "MS Shell Dlg 2";\n' "color:rgb(0, 85, 255);"
        )
        self.lblTtitulo_4.setObjectName("lblTtitulo_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 212, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 212, 91, 31))
        self.pushButton.setObjectName("calcula_A_k")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setToolTip(
            _translate(
                "MainWindow",
                "Haga doble clic en el cabaezado de un vértice para generar una matriz de pesos",
            )
        )
        self.btnPintarGrafo.setText(_translate("MainWindow", "Dibujar Grafo"))
        self.lblTtitulo.setText(
            _translate("MainWindow", "Grafos por Alexander Narváez")
        )
        self.lblTtitulo_3.setText(_translate("MainWindow", "Matriz de Pesos"))
        self.lblTtitulo_2.setText(_translate("MainWindow", "K-Trayectorias"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        self.lblTtitulo_4.setText(_translate("MainWindow", "K="))
        self.pushButton.setText(_translate("MainWindow", "Calcula A^k"))
