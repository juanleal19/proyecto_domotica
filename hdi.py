from tkinter import *
import tkinter
import serial 
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



window = Tk()
window.geometry('600x500') #tamano de la ventana

serialArduino = serial.Serial("COM4", 9600)
time.sleep(1)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xdat,xdat2,tdat ,hdat= [],[],[],[]


#funcion que se ejecurta al optrimir el boton temperatura
def temperatura ():
    serialArduino.write(b'2')
    val = serialArduino.readline().decode('ascii')
    val2 = slice(0,2,1)
    datos_tem = (val[val2])
    return datos_tem

def temperaturaPrnt ():
    serialArduino.write(b'2')
    val = serialArduino.readline().decode('ascii')
    val2 = slice(0,2,1)
    datos_tem = (val[val2])
    print(datos_tem)

def humedad ():
    serialArduino.write(b'1')
    val = serialArduino.readline().decode('ascii')
    val2 = slice(0,2,1)
    datos_hum= (val[val2])
    return datos_hum

def humedadPrnt():
    serialArduino.write(b'1')
    val = serialArduino.readline().decode('ascii')
    val2 = slice(0,2,1)
    datos_hum= (val[val2])
    print( datos_hum)


def exit():
    ax.clear()
    


def animate(i,xdat,tdat, hdat):
    data = temperatura()
    data2 = humedad()
    
    xdat.append(i)
    tdat.append(data)
    hdat.append(data2)
    
    ax.clear()
    ax.plot(xdat, tdat,hdat)
    
def animate2(j,xdat2,hdat):
    data2 = humedad()
    xdat2.append(j)
    tdat.append(data2)
    ax.clear()
    ax.plot(xdat2, hdat)

def grafica():
    i = 0
    ani = animation.FuncAnimation(fig, animate,fargs=(xdat, tdat))
    plt.show()

def grafica2():
    i = 0
    ani = animation.FuncAnimation(fig, animate2,fargs=(xdat2, hdat))
    plt.show()

if __name__ == '__main__':
    
    etiqueta = tkinter.Label(window, text='Sistema domotico')
    etiqueta.pack()
    # boton para la temperatura 
    bototon1 = tkinter.Button(window, text = 'Temperatura', command = temperaturaPrnt)
    bototon1.pack(side= tkinter.RIGHT)
    bototon1 = tkinter.Button(window, text = 'Humedad', command = humedadPrnt)
    bototon1.pack(side= tkinter.RIGHT)

    bototon2 = tkinter.Button(window, text = 'EXIT', command = exit)
    bototon2.pack(side= tkinter.LEFT)

    bototon3 = tkinter.Button(window, text = 'Grafica Temperatura', command = grafica)
    bototon3.pack(side= tkinter.BOTTOM)
    
    bototon3 = tkinter.Button(window, text = 'Grafica Humedad', command = grafica2)
    bototon3.pack(side= tkinter.BOTTOM)
    
    window.title("SIS domotico")

    window.mainloop()