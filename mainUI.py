# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import time
import pandas as pd


class Ui_Dialog_start(object):
    def setupUi(self, Dialog_start):
        if not Dialog_start.objectName():
            Dialog_start.setObjectName(u"Dialog_start")
        Dialog_start.setEnabled(True)
        Dialog_start.resize(500, 380)

        self.label_TimeR = QLabel(Dialog_start)
        self.label_TimeR.setObjectName(u"label_TimeR")
        self.label_TimeR.setGeometry(QRect(285, 30, 51, 31))
        self.calendarWidget = QCalendarWidget(Dialog_start)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 60, 321, 191))
        self.pushButton_Start = QPushButton(Dialog_start)
        self.pushButton_Start.setObjectName(u"pushButton_Start")
        self.pushButton_Start.setEnabled(False)
        self.pushButton_Start.setGeometry(QRect(350, 30, 131, 31))
        self.label_Time = QLabel(Dialog_start)
        self.label_Time.setObjectName(u"label_Time")
        self.label_Time.setGeometry(QRect(10, 30, 51, 31))
        self.pushButton_Login = QPushButton(Dialog_start)
        self.pushButton_Login.setObjectName(u"pushButton_Login")
        self.pushButton_Login.setGeometry(QRect(70, 340, 75, 23))
        self.lineEdit_user_id = QLineEdit(Dialog_start)
        self.lineEdit_user_id.setObjectName(u"lineEdit_user_id")
        self.lineEdit_user_id.setGeometry(QRect(70, 280, 113, 20))
        self.lineEdit_password = QLineEdit(Dialog_start)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(70, 310, 113, 20))
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.label_User_id = QLabel(Dialog_start)
        self.label_User_id.setObjectName(u"label_User_id")
        self.label_User_id.setGeometry(QRect(10, 270, 51, 31))
        self.label_Password = QLabel(Dialog_start)
        self.label_Password.setObjectName(u"label_Password")
        self.label_Password.setGeometry(QRect(10, 300, 51, 31))
        self.line = QFrame(Dialog_start)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-30, 260, 531, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_success = QLabel(Dialog_start)
        self.label_success.setObjectName(u"label_success")
        self.label_success.setGeometry(QRect(200, 280, 80, 13))
        self.label_TimeR_St = QLabel(Dialog_start)
        self.label_TimeR_St.setObjectName(u"label_TimeR_St")
        self.label_TimeR_St.setGeometry(QRect(10, 0, 331, 31))
        self.label_Connection = QLabel(Dialog_start)
        self.label_Connection.setObjectName(u"label_Connection")
        self.label_Connection.setGeometry(QRect(350, 0, 131, 31))
        self.pushButton_Admin = QPushButton(Dialog_start)
        self.pushButton_Admin.setObjectName(u"pushButton_Admin")
        self.pushButton_Admin.setGeometry(QRect(170, 340, 75, 23))
        self.pushButton_Admin.setEnabled(False)
        self.pushButton_Admin.hide()
        self.textBrowser_Error = QTextBrowser(Dialog_start)
        self.textBrowser_Error.setObjectName(u"label_Connection")
        self.textBrowser_Error.setGeometry(QRect(270, 280, 221, 91))
        self.textBrowser_Error.hide()
        self.table = QTableView(Dialog_start)
        self.table.setObjectName(u"table_show")
        self.table.hide()

        self.retranslateUi(Dialog_start)

        QMetaObject.connectSlotsByName(Dialog_start)
    # setupUi
    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.label_TimeR.setText(text)


    def retranslateUi(self, Dialog_start):
        timer = QTimer(Dialog_start)
        timer.connect(timer, SIGNAL('timeout()'), self.showTime)
        timer.start(10)

        time_now = self.showTime()


        Dialog_start.setWindowTitle(QCoreApplication.translate("Dialog_start", u"Dialog", None))
        self.label_TimeR.setText(QCoreApplication.translate("Dialog_start", time_now, None))
        self.pushButton_Start.setText(QCoreApplication.translate("Dialog_start", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438 \u0441\u0442\u0430\u0440\u0442", None))
        self.label_Time.setText(QCoreApplication.translate("Dialog_start", u"\u0427\u0430\u0441:", None))
        self.pushButton_Login.setText(QCoreApplication.translate("Dialog_start", u"\u0412\u0445\u0456\u0434", None))
        self.label_User_id.setText(QCoreApplication.translate("Dialog_start", u"User_id", None))
        self.pushButton_Admin.setText(QCoreApplication.translate("Dialog_start", u"Check",None))
        self.label_Password.setText(QCoreApplication.translate("Dialog_start", u"Password", None))
        self.label_Connection.setText("Conection")
        self.label_success.setText("")
        self.label_TimeR_St.setText("")
        self.textBrowser_Error.setText("")
    # retranslateUi



class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None