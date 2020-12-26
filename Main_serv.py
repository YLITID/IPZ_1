from socket import *
import pyodbc as sql



#connection = sql.connect("Driver={SQL Server};""Server=DESKTOP-4MN9DR5\kurma;"
#                    "Database=CheckDotBD;""Trusted_Connection=yes", autocommit=True)

s = socket()

s.bind(('', 9999))

s.listen(5)
Con_num=1
admin_st=1

while True:
    try:
        conn, addr = s.accept()
        print(Con_num,'Connected', addr)
        choise = conn.recv(1).decode()
        print('Choise', choise)
        if choise=='l':
            datal = ''
            datap = ''
            conn.send('1'.encode())
            datal=conn.recv(1024).decode()
            conn.send('1'.encode())
            datap=conn.recv(1024).decode()
            if admin_st == 1:
                conn.send('adm'.encode())
            else:
                conn.send('1'.encode())
            print(datal, datap)
            choise=''
        elif choise=='c':
            conn.send('1'.encode())
            datat=conn.recv(1024).decode()
            conn.send('1'.encode())
            datast=bool(int(conn.recv(1024).decode()))
            conn.send('1'.encode())
            conn.send('1'.encode())
            datat_sec = int(conn.recv(1024).decode())
            conn.send('1'.encode())
            print(datast,datat, datat_sec)
            choise=''
        elif choise=='a':
            conn.send('1'.encode())
            datatadm = conn.recv(1024).decode()
            conn.send('1'.encode())
            print(datatadm)
        Con_num+=1
    except:
        pass

