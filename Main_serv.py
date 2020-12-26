from socket import *
import pyodbc as sql



connection = sql.connect("Driver={SQL Server};""Server=DESKTOP-4MN9DR5\kurma;"
                    "Database=CheckDotBD;""Trusted_Connection=yes", autocommit=True)

s = socket()

s.bind(('', 9999))

s.listen(1)

conn, addr = s.accept()

print('Connected', addr)
