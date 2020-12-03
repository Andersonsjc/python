from datetime import datetime
import smtplib
from socket import gethostname
from email.mime.text import MIMEText as text
import pyodbc

host_name = gethostname()
fromaddr = "serverABC"
toaddrs  = [ 'name@email.com' ]


def send_mail(fromaddr, toaddrs, hostname):
    m = text(f'Cannot connect to the database: {datetime.today()}')
    m['Subject'] = f'Database Warning'
    m['From'] = fromaddr
    m['To'] = ", ".join(toaddrs)

    server = smtplib.SMTP('localhost')
    server.set_debuglevel(0)
    server.sendmail(fromaddr, toaddrs, m.as_string())
    server.quit()

datasource = f'DSN=database;Trusted_Connection=True, timeout=5' #timeout in seconds

try:
    con = pyodbc.connect(datasource)
    cursor = con.cursor()
    sql = "SELECT 'PROPERTY ( 'MachineName' )"
    cursor.execute(sql)
    result = cursor.fetchall()

except Exception as e:
    print(f'   ERRO ao consultar a configuracao do HA do servico: {datasource}, mensagem de erro: {str(e)}', 'ERROR', add_msg_mail=True)	


	
send_mail( fromaddr, toaddrs, host_name )