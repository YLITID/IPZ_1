from mainUI import *
import sys
import time
from socket import *

#Socket client side

s=socket()
#s.connect(('localhost', 9999))

#datatoconnect = s.recv(1024)



#Create UI app
app = QApplication(sys.argv)
Form = QWidget()
ui = Ui_Dialog_start()
ui.setupUi(Form)
Form.show()

#Logic
timenow = ''
startstop = True


def Login():
    global adminemode
    adminemode = False
    if ui.lineEdit_user_id.text()=='admin' and ui.lineEdit_password.text()=='admin':
        adminemode=True
        print(adminemode)
    if True:
        ui.pushButton_Start.setEnabled(True)
        ui.label_success.setText("Success")
    else:
        ui.label_success.setText("Unsuccess")

    if adminemode == True:
        ui.label_success.setText("Admin mode")
ui.pushButton_Login.clicked.connect(Login)

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


#Run main loop
if __name__ == '__main__':
    sys.exit(app.exec_())