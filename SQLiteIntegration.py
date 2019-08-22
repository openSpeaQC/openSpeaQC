import sqlite3
import os.path
import tkinter as tk
from tkinter import filedialog
import mysql.connector as mysqlconn
import csv

root=tk.Tk()
root.withdraw()
#ordnerpfad=filedialog.askdirectory()
#datenbankname=input("Der Name der Datenbank?")
ordnerpfad="/Users/sebmac/Desktop"
programmname="SMVT_Measure"
datenbankname="DaBa"


##VARIABLEN
speaker_id="2788--1"
speaker_name="TX3"
speaker_mode=1
count_ways=1
lpf_way1=None
lpf_way2=None
lpf_way3=None
hpf_way1=None
hpf_way2=None
hpf_way3=None
#ordnerpfad=os.path.join(ordnerpfad,programmname)
dateipfad=os.path.join(ordnerpfad,datenbankname)
dateipfad+=".db"



print(ordnerpfad)
conn=None
c=None
def initDatabase():
    global conn,c
    if(os.path.isfile(dateipfad)):
        print("Datenbank vorhanden, Verbindung wird aufgebaut...")
        conn=sqlite3.connect(dateipfad)
        c=conn.cursor()
    else:
        conn=sqlite3.connect(dateipfad)
        c=conn.cursor()
        print("Neue Datenbank erfolgreich aufgebaut!!")
        c.execute('''CREATE TABLE lautsprecher (speaker_id text PRIMARY KEY,speaker_name text NOT NULL,speaker_mode int NOT NULL,count_ways int NOT NULL,lpf_way1 int,hpf_way1 int,lpf_way2 int,hpf_way2 int,lpf_way3 int,hpf_way3 int)''')
        c.execute('''CREATE TABLE messungen (measure_id int AUTO_INCREMENT, speaker_id int, path_to_data_w1 text, path_to_data_w2 text, path_to_data_w3 text, impedancy_w1 real, impedancy_w2 real, impedancy_w3 real)''')

def loadDataInTemp(dataEntry):
    global speaker_id,speaker_name,speaker_mode,count_ways,lpf_way1,hpf_way1,lpf_way2,hpf_way2,lpf_way3,hpf_way3
    speaker_id=dataEntry[0]
    speaker_name=dataEntry[1]
    speaker_mode=dataEntry[2]
    count_ways=dataEntry[3]
    lpf_way1=dataEntry[4]
    hpf_way1=dataEntry[5]
    lpf_way2=dataEntry[6]
    hpf_way2=dataEntry[7]
    lpf_way3=dataEntry[8]
    hpf_way3=dataEntry[9]
    print("lokale Variablen erfolgreich eingelesen!",speaker_id,speaker_name,speaker_mode)




initDatabase()
speaker_id=input("Scannen Sie bitte den Lautsprecher: ")
befehlAktuellerLautsprecher='''SELECT speaker_id from lautsprecher where speaker_id="%s"'''%(speaker_id)
isLSEntry=c.execute(befehlAktuellerLautsprecher)
c.execute('''SELECT COUNT (*) FROM lautsprecher where speaker_id="%s"''' % (speaker_id))
queryResult=c.fetchone()[0]
print(queryResult)
if(queryResult==1):
    print("gibt schon nen Datensatz!")
    c.execute('''SELECT * FROM lautsprecher where speaker_id="%s"''' % (speaker_id))
    queryResult=c.fetchone()
    loadDataInTemp(queryResult)
else:
    c.execute('''SELECT speaker_name FROM alleartikel where speaker_id="%s"''' % (speaker_id))
    queryResult=c.fetchone()
    speaker_name=queryResult[0]
    c.execute('''INSERT INTO lautsprecher (speaker_id,speaker_name,speaker_mode,count_ways) VALUES ("%s","%s",%d,%d)''' % (speaker_id,speaker_name,speaker_mode,count_ways))
    print("Neuer Datensatz erstellt!")
c.execute('''SELECT * FROM lautsprecher''')
queryResult=c.fetchall()
for element in queryResult:
    print(element[1],"\n")
conn.commit()
conn.close()


