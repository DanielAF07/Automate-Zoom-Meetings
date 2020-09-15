import webbrowser
import time
import datetime
import numpy as np
import threading

from . import auto as auto
from . import dataManager as dm

def getHorario():
    data = dm.loadSchedule()
    lHours = data[0]
    lMinutes = data[1]
    lDias = [data[2], data[3], data[4], data[5], data[6]]
    today = datetime.date.today().weekday()
    count = 0
    horario = ""
    if(today > 4):
        horario = "N/A\n"*5
    else:
        for i in range(len(lHours)):
            if lDias[today][i] != "" and lHours[i] != "":
                if 0 <= int(lHours[i]) <= 12: 
                    horario += lHours[i] + ":" + lMinutes[i] + " AM - " + lDias[today][i]
                else:
                    horario += str((int(lHours[i]) - 12)) + ":" + lMinutes[i] +" PM - " + lDias[today][i]
                horario += "\n"
            else:
                continue
    
    horario = horario[:-1]
    
    return horario

def goClass(id, pw):
    _id = id.replace(" ","")
    a_website = "zoommtg://zoom.us/join?confno=" + _id + "&pwd=" + pw
    webbrowser.open_new_tab(a_website)

def stopAuto():
    auto.autoState = False
    time.sleep(.5)

def initAuto():
    global autoState
    auto.autoState = True
    startThread()

def startThread():
    thread = threading.Thread(target=auto.autoMode)
    thread.daemon = True
    thread.start()