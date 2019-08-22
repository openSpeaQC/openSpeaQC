import csv,sqlite3,os.path
from tkinter import filedialog
import tkinter as tk

conn=None
c=None
ordnerpfad="/Users/sebmac/Desktop"
programmname="SMVT_Measure"
datenbankname="DaBa"
csvdata=None
dateipfad=os.path.join(ordnerpfad,datenbankname)
dateipfad+=".db"
root=tk.Tk()
root.withdraw()
csvpfad=filedialog.askopenfilename()


conn=None
c=None
def initDatabase():
    global conn,c
    if(os.path.isfile(dateipfad)):
        print("Datenbank vorhanden, Verbindung wird aufgebaut...")
        conn=sqlite3.connect(dateipfad)
        c=conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS alleartikel (speaker_name text,speaker_id text PRIMARY KEY)''')

def writeIntoDB():
    global csvpfad,csvdata,c
    with open(csvpfad) as csvfile:
        csvdata=csv.reader(csvfile,delimiter=';')
        c.execute('''DELETE FROM lautsprecher''')
        for row in csvdata:
            c.execute('''INSERT INTO lautsprecher (speaker_id,speaker_name,speaker_mode,count_ways,lpf_way1,hpf_way1,lpf_way2,hpf_way2,lpf_way3,hpf_way3) 
            VALUES ("%s","%s",%d,%d,%d,%d,%d,%d,%d,%d,)''' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

initDatabase()
writeIntoDB()
c.execute('''SELECT * FROM alleartikel''')
for elements in c.fetchall():
    print(elements,"\n")
conn.commit()
conn.close()