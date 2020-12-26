from mainUI import *
import sys
import time
from socket import *


#Create UI app
app = QApplication(sys.argv)
Form = QWidget()
ui = Ui_Dialog_start()
ui.setupUi(Form)
Form.show()

#Logic
timenow = ''
startstop = True

def ErrorShow(error_type, error_code):
    print(error_type,error_code)
    ui.textBrowser_Error.show()
    ui.textBrowser_Error.setText(error_type+str(error_code))

def Login():
    global adminemode
    adminemode = False
    #s.send(ui.lineEdit_user_id.text())
    #s.send(ui.lineEdit_password.text())
    if ui.lineEdit_user_id.text()=='admin' and ui.lineEdit_password.text()=='admin':
        adminemode=True

        ui.label_success.setText("Admin mode")
        ui.pushButton_Admin.show()
        ui.pushButton_Admin.setEnabled(True)

        return adminemode
    if True:
        ui.pushButton_Start.setEnabled(True)
        ui.label_success.setText("Success")
    else:
        ui.label_success.setText("Unsuccess")

    return adminemode
def Admin_checkDate():
    adminmode
    if adminmode != True:
        return
    QDate = ui.calendarWidget.selectedDate.text()
    Date = "{0}.{1}.{2}".format(QDate.day(), QDate.month(), QDate.year())
    print("{0}.{1}.{2}".format(QDate.day(), QDate.month(), QDate.year()))
    return Date.getDate()
adminmode = ui.pushButton_Login.clicked.connect(Login)
Date = ui.pushButton_Admin.clicked.connect(Admin_checkDate)


def ComeTW():
    global startstop
    timenow = time.asctime()
    print(timenow)
    if startstop == True:
        ui.pushButton_Start.setText(QCoreApplication.translate("Dialog_start", u"Завершення роботи", None))
        ui.label_TimeR_St.setText("Розпочато роботу о " + timenow)
    else:
        ui.pushButton_Start.setText(QCoreApplication.translate("Dialog_start", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438 \u0441\u0442\u0430\u0440\u0442", None))
        ui.label_TimeR_St.setText("Завершено роботу о " + timenow)
    startstop = not startstop
ui.pushButton_Start.clicked.connect(ComeTW)

#Socket client side

s=socket()

try:
    s.connect(('localhost', 9999))
except ConnectionRefusedError:
    print(ValueError.__context__)
    ErrorShow('Conection Eror:\n',ValueError)
    ui.label_Connection.setText('Conection Error')
    s.close()
else:
    ui.label_Connection.setText('Conected')





#Run main loop
if __name__ == '__main__':
    sys.exit(app.exec_())