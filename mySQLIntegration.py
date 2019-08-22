import mysql.connector as mysqlconn

epiconnector=mysqlconn.connect(host="192.168.5.229",user="user1",passwd="xxxx",port=55519)
mycursor=epiconnector.cursor()
mycursor.execute("SHOW DATABASES")
databases=mycursor.fetchall()
for x in databases:
    print (x)
epiconnector.disconnect()
