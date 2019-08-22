import tkinter as tk
import os.path
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
openpath=filedialog.askdirectory() #AskForDirectory

import audioSample
import numpy as np
from audioPlayer import audioPlayer
from audioMeasure import audioMeasure
import matplotlib.pyplot as plt
import time
import sqlite3
import pyaudio
import audioop
#import csvImport
#import SQLiteIntegration
#import inputaudioImp



timestamp=time.strftime("%Y%m%d%H%M%S")
dateipfad=os.path.join(openpath,timestamp)# neben Timestamp wird bei Integration der Datenbank hier der Artikelname ausgesucht // Skript dient zur Veranschaulichung der exakten Funktionsweise
dateipfad+=".csv"
messung = audioMeasure(channels=1)
messung.pinkNoiseLoop(samples=44100,repetitions=5,normalize=False)
messung.testAllChannels(hpf=20,lpf=20000)
messung.calcTF()
messung.tf[0].smoothFFT(float(0.2),destructive='y')
print(len(messung.tf))
messung.tf[0].normalize()
f=open(dateipfad,"w")
i=0

#Amplitudenexport
for daten in messung.tf[0].data:
      if(i==0):
          i=1

      else:
         f.write(str(daten.real))
         f.write("\n")
#Frequenzexport nach Amplitudenwerte zu Debugging
for daten in messung.input[0].f():
    if(i==0):
        i=1

    else:
       f.write(str(daten))
       f.write("\n")
f.close()
messung.input[0].toDb()
messung.plotFreqResp()
messung.plotImpulseResp()
