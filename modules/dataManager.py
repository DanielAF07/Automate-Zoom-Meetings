import pickle
import datetime

def saveSchedule(horarioData):
    f = open('schedule.pckl', 'wb')
    pickle.dump(horarioData, f)
    f.close()

def loadSchedule():
    try:
        f = open('schedule.pckl', 'rb')
        data = pickle.load(f)
        f.close()
        return data
    except:
        hours = [""]*9
        minutes = [""]*9
        lunes = [""]*9
        martes = [""]*9
        miercoles = [""]*9
        jueves = [""]*9
        viernes = [""]*9
        info = [hours, minutes, lunes, martes, miercoles, jueves, viernes]
        return info


def loadMeetings():
    try:
        f = open('meetings.pckl', 'rb')
        data = pickle.load(f)
        f.close()
        return data
    except:
        data1 = [""]*3
        data2 = [""]*3
        data3 = [""]*3
        data4 = [""]*3
        data5 = [""]*3
        data6 = [""]*3
        data7 = [""]*3
        data8 = [""]*3
        data = [data1, data2, data3, data4, data5, data6, data7, data8]
        return data

def saveMeetings(arrayData):
    f = open('meetings.pckl', 'wb')    
    pickle.dump(arrayData, f)
    f.close()
