# TODO Actualizar la lista del horario Automaticamente (*Poner numeracion a los hroarios y preguntar si es el mismo que hoy*)
# TODO Utilizar websockets para notificar a los usuarios cuando inicia una clase. / Utilizar API de ZOOM

from tkinter import Entry, Button, Tk, Label, LabelFrame, StringVar, Toplevel
from tkinter import ANCHOR, W, E, N, S, LEFT, DISABLED, INSERT
from tkinter import ttk

from modules.mainFunctions import *
import modules.auto as auto
import modules.dataManager as dm

autoOn = False

#--COLORS--#
mainColor = "#14c4ff"
secondaryColor = "#575757"

colorAuto = secondaryColor

def supportWindow(): # Ventana de SOPORTE y CONTACTO
    support = Toplevel(root)
    support.grab_set()
    support.title("Soporte")
    support.iconbitmap('icon.ico')
    support.resizable(height = False, width = False)
    title2 = Label(support, text="Soporte", padx=120, pady=20, font=('Roboto',24))
    title2.grid(row=0,column=0,columnspan=8)
    lbInfo = LabelFrame(support, text="INFO")
    lbInfo.grid(row=1, column=2, columnspan=4, padx=(5,5), pady=(5,5))
    Label(lbInfo, text="Si encontraste algun problema usando ZoomCaller, reportalo a mi correo\nDanielAF07 - daniiel0609@gmail.com").grid(row=0, column=0)
    Button(lbInfo, text="GitHub", padx=8, pady=5, width=11, bg=mainColor, fg='white', relief='flat', command= lambda: webbrowser.open("https://github.com/DanielAF07/ZoomCaller")).grid(row=1, column=0)

def configWindow(): # Ventana para configurar las ID
    window = Toplevel(root)
    window.grab_set()
    window.title("Meetings")
    window.geometry("300x240")
    window.resizable(height = False, width = False)
    window.iconbitmap('icon.ico')

    for i in range(8):
        b = Label(window, text = i+1, padx=8)
        b.grid(row=i+2, column = 0)

    lbName = Label(window, text="Nombre")
    lbName.grid(row=1, column=1, columnspan = 2, sticky=W+E+N+S)
    lbID = Label(window, text="ID de Sala")
    lbID.grid(row=1, column=3, columnspan = 3, sticky=W+E+N+S)
    lbPw = Label(window, text="Password")
    lbPw.grid(row=1, column=6, columnspan = 2, sticky=W+E+N+S)

    entry_class = [0]*8
    for i in range(8):
        entry_class[i] = [ Entry(window, width=16), Entry(window, width=16), Entry(window, width=10) ]
        entry_class[i][0].grid(row=i+2, column=1, columnspan = 2)
        entry_class[i][1].grid(row=i+2, column=3, columnspan = 3)
        entry_class[i][2].grid(row=i+2, column=6, columnspan = 2)

    data = dm.loadMeetings()
    for j in range(8): #Insert
        for i in range(3):
            entry_class[j][i].insert(INSERT, data[j][i])

    def saveInfo():
        data = [0]*8
        for i in range(8):
            data[i] = [""]*3 # Create empty array
        
        for j in range(8): #Save
            for i in range(3):
                data[j][i] = entry_class[j][i].get() # Fill the array
        
        dm.saveMeetings(data)
        auto.reload = True
        window.destroy()
        refresh()
    
    btnConfirmar = Button(window, text="Confirmar", relief='flat', pady=7, bg=mainColor, fg="white", command=saveInfo)
    btnConfirmar.grid(row=10, column=1, columnspan=9, sticky="nsew", pady=(4,4))

def horarioWindow(): # Ventana para configurar el horario
    horarioWindow = Toplevel(root)
    horarioWindow.grab_set()
    horarioWindow.title("Schedule")
    horarioWindow.resizable(height = False, width = False)
    horarioWindow.iconbitmap('icon.ico')
    for i in range(9):
        lblNumber = Label(horarioWindow, text = i+1, padx=5)
        lblNumber.grid(row=i+2, column=0)
    
    Label(horarioWindow, text="12-hour format").grid(row=11, column=1, columnspan=3, sticky="n") 
    lblHora = Label(horarioWindow, text="Hora")
    lblHora.grid(row=1, column=1, columnspan=3)
    lblLunes = Label(horarioWindow, text="Lunes")
    lblLunes.grid(row=1, column=5)
    lblMartes = Label(horarioWindow, text="Martes")
    lblMartes.grid(row=1, column=6)
    lblMiercoles = Label(horarioWindow, text="Miercoles")
    lblMiercoles.grid(row=1, column=7)
    lblJueves = Label(horarioWindow, text="Jueves")
    lblJueves.grid(row=1, column=8)
    lblViernes = Label(horarioWindow, text="Viernes")
    lblViernes.grid(row=1, column=9)
    
    entry_hours = [""]*9
    entry_minutes = [""]*9
    entry_lunes = [""]*9
    entry_martes = [""]*9
    entry_miercoles = [""]*9
    entry_jueves = [""]*9
    entry_viernes = [""]*9
    entry_12h = [""]*9
    
    def hourValidation(S):
        if S.isdigit() == True:
            return True
        return False

    vcmd = (horarioWindow.register(hourValidation), '%S')

    for i in range(9):
        entry_hours[i] = Entry(horarioWindow, width=4, validate='key', vcmd=vcmd)
        entry_hours[i].grid(row=i+2, column=1)
        lblSepar = Label(horarioWindow, text=":")
        lblSepar.grid(row=i+2, column=2)
        entry_minutes[i] = Entry(horarioWindow, width=4, validate='key', vcmd=vcmd)
        entry_minutes[i].grid(row=i+2, column=3)
        
        entry_12h[i] = ttk.Combobox(horarioWindow, state="readonly", width=4)
        entry_12h[i]["values"] = ["AM", "PM"]
        entry_12h[i].set("AM")
        entry_12h[i].grid(row=i+2, column=4, padx=(5,2))
        
        entry_lunes[i] = Entry(horarioWindow)
        entry_lunes[i].grid(row=i+2, column=5, padx=(10,2), pady=(2,2))
        entry_martes[i] = Entry(horarioWindow)
        entry_martes[i].grid(row=i+2, column=6, padx=(2,2))
        entry_miercoles[i] = Entry(horarioWindow)
        entry_miercoles[i].grid(row=i+2, column=7, padx=(2,2))
        entry_jueves[i] = Entry(horarioWindow)
        entry_jueves[i].grid(row=i+2, column=8, padx=(2,2))
        entry_viernes[i] = Entry(horarioWindow)
        entry_viernes[i].grid(row=i+2, column=9, padx=(2,2))
    
    dataHorario = dm.loadSchedule()
    lHours = dataHorario[0]
    lMinutes = dataHorario[1]
    lLunes = dataHorario[2]
    lMartes = dataHorario[3]
    lMiercoles = dataHorario[4]
    lJueves = dataHorario[5]
    lViernes = dataHorario[6]

    for i in range (9):
        if lHours[i] == "":
            entry_12h[i].set("")
        else:
            if int(lHours[i]) > 12:
                entry_hours[i].insert(INSERT, str(int(lHours[i])-12))
                entry_12h[i].set("PM")
            elif 0 <= int(lHours[i]) <= 12:
                entry_hours[i].insert(INSERT, lHours[i])
                entry_12h[i].set("AM")
        entry_minutes[i].insert(INSERT, lMinutes[i])
        entry_lunes[i].insert(INSERT, lLunes[i])
        entry_martes[i].insert(INSERT, lMartes[i])
        entry_miercoles[i].insert(INSERT, lMiercoles[i])
        entry_jueves[i].insert(INSERT, lJueves[i])
        entry_viernes[i].insert(INSERT, lViernes[i])
    
    def deleteHour(ind):
        entry_hours[ind].delete(0,"end")
        entry_minutes[ind].delete(0, "end")
        entry_12h[ind].set('')
        entry_lunes[ind].delete(0, "end")
        entry_martes[ind].delete(0, "end")
        entry_miercoles[ind].delete(0, "end")
        entry_jueves[ind].delete(0, "end")
        entry_viernes[ind].delete(0, "end")

    btnCancel = [0]*9
    for i in range(9):
        index = i
        btnCancel[i] = Button(horarioWindow, text="X", font='Roboto 9 bold', bg="red", fg="white", relief="solid", command=lambda i=i: deleteHour(i))
        btnCancel[i].grid(row=i+2, column=10)

    def saveSchedule():
        sHours = [0]*9
        sMinutes = [0]*9
        sLunes = [0]*9
        sMartes = [0]*9
        sMiercoles = [0]*9
        sJueves = [0]*9
        sViernes = [0]*9
        for i in range (9):
            if entry_12h[i].get() == 'AM':
                sHours[i] = entry_hours[i].get()[0:2]
            elif entry_12h[i].get() == 'PM':
                sHours[i] = str(int(entry_hours[i].get()[0:2]) + 12)
            else:
                sHours[i] = ""
            #print(sHours[i])
            if entry_12h[i].get() != '':
                sMinutes[i] = entry_minutes[i].get()[0:2]
            else:
                sMinutes[i] = ''
            sLunes[i] = entry_lunes[i].get()
            sMartes[i] = entry_martes[i].get()
            sMiercoles[i] = entry_miercoles[i].get()
            sJueves[i] = entry_jueves[i].get()
            sViernes[i] = entry_viernes[i].get()
    
        dataSch = [sHours, sMinutes, sLunes, sMartes, sMiercoles, sJueves, sViernes]
        dm.saveSchedule(dataSch)
        auto.reload = True
        horarioWindow.destroy()
        refresh()
    
    btnConfirm = Button(horarioWindow, text="Confirmar", padx=8, pady=5, width=11, bg=mainColor, fg="white", relief='flat', command=saveSchedule)
    btnConfirm.grid(row=11, column=9, columnspan=2, pady=(3,6))

def start_gui(): # Ventana Principal
    global root
    root = Tk()
    root.title("ZoomCaller v1.2")
    root.resizable(height = False, width = False)
    root.iconbitmap('icon.ico')

    space = Label(root,text=" ", font=('Roboto',4))
    space.grid(row=2,column=0,columnspan=4)
    data = dm.loadMeetings()

    btnClase = [0]*8
    for i in range(8):
        if data[i][0] == "":
            btnClase[i] = Button(root, text="NoClass", width=4, padx=20, pady=8, bg=secondaryColor, fg="white", relief='flat', state=DISABLED)
        else:
            btnClase[i] = Button(root, text=data[i][0], width=4, padx=20, pady=8, bg=mainColor, fg="white", relief='flat', command=lambda i=i: goClass(data[i][1], data[i][2]))

    btnClase[0].grid(row=1, column=0, padx=(10,10), pady=(10,0))
    btnClase[1].grid(row=1, column=1, padx=(0,10), pady=(10,0))
    btnClase[2].grid(row=1, column=2, padx=(0,10), pady=(10,0))
    btnClase[3].grid(row=1, column=3, padx=(0,10), pady=(10,0))
    btnClase[4].grid(row=3, column=0, padx=(10,10), pady=(0,5))
    btnClase[5].grid(row=3, column=1, padx=(0,10), pady=(0,5))
    btnClase[6].grid(row=3, column=2, padx=(0,10), pady=(0,5))
    btnClase[7].grid(row=3, column=3, padx=(0,10), pady=(0,5))

    lbHorario = LabelFrame(root, text="Horario de Hoy")
    lbHorario.grid(row=4, column=0, columnspan=2, rowspan=4, pady=(10,0))
    txtHorario = StringVar()
    txtHorario.set(getHorario())
    lHorario = Label(lbHorario, textvariable=txtHorario, anchor=W, justify=LEFT)
    lHorario.grid(row=0, column=0)

    btnConfig = Button(root, text="Meetings", padx=8, pady=5, width=11, bg=secondaryColor, fg="white", relief='flat', command=configWindow)
    btnConfig.grid(row=5, column=2, columnspan=2, pady=(10,5))
    btnHorario = Button(root, text="Schedule", padx=8, pady=5, width=11, bg=secondaryColor, fg="white", relief='flat', command=horarioWindow)
    btnHorario.grid(row=6, column=2, columnspan=2, pady=(5,5))
    btnSupport = Button(root, text="Support", padx=8, pady=5, width=11, bg=secondaryColor, fg="white", relief='flat', command=supportWindow)
    btnSupport.grid(row=8, column=2, columnspan=2, pady=(5,15))
    
    def toggleButton():
        global autoOn
        if autoOn == False:
            autoOn = True
            initAuto()
            btnAuto.configure(bg=mainColor, text="Auto: ON")
        elif autoOn == True:
            autoOn = False
            stopAuto()
            btnAuto.configure(bg=secondaryColor, text="Auto: OFF")
    
    btnAuto = Button(root, text="Auto: OFF", padx=8, pady=5,width=11, fg="white", relief='flat', command=toggleButton)
    if autoOn == True:
        btnAuto.configure(bg=mainColor, text="Auto: ON")
    else:
        btnAuto.configure(bg=secondaryColor, text="Auto: OFF")
    btnAuto.grid(row=7, column=2, columnspan=2, pady=(5,5))
    
    root.mainloop()

if __name__ == '__main__':
    def refresh():
        root.destroy()
        start_gui()
    start_gui()
