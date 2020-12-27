from socket import *
import pyodbc as sql
import pandas as pd
import pickle
from PySide2.QtCore import QDateTime

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=localhost;"
            "Database=CheckDotBD;"
            "Trusted_Connection=yes;")

cnxn = sql.connect(cnxn_str)
cursor = cnxn.cursor()
print(pd.read_sql("SELECT * FROM Employee", cnxn))
s = socket()

s.bind(('', 9999))

s.listen(50)


def Search(df, login, password):
    global admin_st
    reslog = False
    try:
        passcheck = df[df['login'] == login]['password'].iloc[0]
        admin_st = int(df[df['login'] == login]['admin_st'].iloc[0])
        if passcheck == password:
            reslog = True
        print(reslog, passcheck,admin_st)
        return reslog
    except:
        return reslog

Con_num = 1
admin_st = 0

datap = ''

while True:
    try:
        conn, addr = s.accept()
        print(Con_num, 'Connected', addr)
        choise = conn.recv(1).decode()
        print('Choise', choise)
        if choise == 'l':  # Login
            global datal
            data_sql = pd.read_sql("SELECT L.admin_st,L.login,P.password FROM Employee as L INNER JOIN Employee_p as P "
                                   "on L.Employee_id =P.Employee_id ", cnxn)
            conn.send('1'.encode())
            datal = conn.recv(1024).decode()
            conn.send('1'.encode())
            datap = conn.recv(1024).decode()
            log_st = Search(data_sql,datal,datap)
            print(log_st)
            if log_st == True:
                if admin_st == 1:
                    conn.send('adm'.encode())
                else:
                    conn.send('1'.encode())
            else:
                conn.send('2'.encode())
            print( data_sql)
            choise = ''
        elif choise == 'c':  # Coming to work
            qtimenow = QDateTime.currentDateTime()
            timenow = qtimenow.toString('hh:mm:ss')
            datenow = qtimenow.toString('dd.MM.yyyy')
            timenow_s = str(qtimenow.currentSecsSinceEpoch())
            conn.send('1'.encode())
            datat = conn.recv(1024).decode()
            conn.send('1'.encode())
            datast = bool(int(conn.recv(1024).decode()))
            conn.send('1'.encode())
            conn.send('1'.encode())
            datat_sec = int(conn.recv(1024).decode())
            print(datast, datat, datat_sec)
            print(f"SELECT Employee_id from Employee where login = \'{datal}\'")

            Employee_id_sql = pd.read_sql(f"SELECT Employee_id from Employee where login = '{datal}'", cnxn)
            Employee_id = Employee_id_sql['Employee_id'].iloc[0]
            print(Employee_id)
            cursor.execute(f"INSERT INTO Worktime ([Start/Stop],Employee_id, Datetime_sec, [Time] , [Date]) values('{datast}','{Employee_id}','{timenow_s}','{timenow}','{datenow}')")
            cnxn.commit()
            print('Comitted')
            conn.send('1'.encode())


        elif choise == 'a':  # Admin Check
            conn.send('1'.encode())
            datatadm = conn.recv(1024).decode()
            conn.send('1'.encode())

            Employee_data_adm_sql = pd.read_sql(f"SELECT W.Employee_id, E.First_Name, E.Last_Name, W.[Start/Stop],W.[Time], W.[Date] FROM Worktime as W "
                                                f"RIGHT JOIN Employee as E on W.Employee_id=E.Employee_id "
                                                f"WHERE W.[Date]='{datatadm}';", cnxn)
            df_bytes = pickle.dumps(Employee_data_adm_sql)

            conn.send(df_bytes)
        Con_num += 1
    except Exception as ex:
        print(ex)
