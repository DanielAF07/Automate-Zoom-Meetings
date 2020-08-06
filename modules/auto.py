import time
import datetime
import numpy as np

from . import mainFunctions as mf
from . import dataManager as dm

autoState = False
reload = False

def goClassName(className):
    data = dm.loadMeetings() #Load classes info
    x = np.array(data) #Put info in a numpy array
    classInfo = x[:,:1] #Get only the first row
    index = np.where(classInfo == className)[0][0] #Locate the class and get the index
    mf.goClass(data[index][1], data[index][2])

def reloadData():
        global dataHorario
        global lHours
        global lMinutes
        global lAccessed
        global lDias 
        dataHorario = dm.loadSchedule()
        lHours = dataHorario[0]
        lMinutes = dataHorario[1]
        lAccessed = [False]*9
        lDias = [ dataHorario[2], dataHorario[3], dataHorario[4], dataHorario[5], dataHorario[6] ]

def inTime(classHour, classMinute):
    retrasoMinutos = 15
    currentTime = datetime.datetime.now()
    classTime = currentTime.replace(hour=classHour, minute=classMinute)
    addTime = datetime.timedelta(minutes = retrasoMinutos)
    
    difference = (classTime + addTime) - currentTime
    t = difference.seconds / 60
    
    if 0<=t<=15:
        return True
    else:
        return False

def autoMode():
    reloadData()
    today = datetime.date.today().weekday()
    while True:
        time.sleep(.5)
        global autoState
        if autoState == False:
            break
        
        global reload
        if reload:
            print("Reloading...")
            reload = False
            reloadData()

        for i in range(9):
            try:
                if inTime(int(lHours[i]), int(lMinutes[i])) == True and lAccessed[i] == False:
                        goClassName(lDias[today][i])
                        lAccessed[i] = True
            except:
                continue