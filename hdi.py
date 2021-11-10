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
xdat , tdat ,hdat= [],[],[]


#funcion que se ejecurta al optrimir el boton temperatura
def temperatura ():
    for i in range(0,10):
        serialArduino.write(b'2')
        val = serialArduino.readline().decode('ascii')
        val2 = slice(0,2,1)
        datos_tem = (val[val2])
    return datos_tem

def humedad ():
    for i in range(0,10):
        serialArduino.write(b'2')
        val = serialArduino.readline().decode('ascii')
        val2 = slice(0,2,1)
        datos_hum= (val[val2])
    return datos_hum


def exit():
    serialArduino.write(b'e')


def animate(i,xdat,tdat):
    data = temperatura()
    xdat.append(i)
    tdat.append(data)
    ax.clear()
    ax.plot(xdat, tdat)
    
def animate2(i,xdat,hdat):
    data = humedad()
    xdat.append(i)
    tdat.append(data)
    ax.clear()
    ax.plot(xdat, hdat)

def grafica():
    ani = animation.FuncAnimation(fig, animate,fargs=(xdat, tdat))
    plt.show()

def grafica2():
    ani = animation.FuncAnimation(fig, animate2,fargs=(xdat, hdat))
    plt.show()

if __name__ == '__main__':
    
    etiqueta = tkinter.Label(window, text='Sistema domotico')
    etiqueta.pack()
    # boton para la temperatura 
    bototon1 = tkinter.Button(window, text = 'temperatura', command = temperatura)
    bototon1.pack(side= tkinter.RIGHT)

    bototon2 = tkinter.Button(window, text = 'EXIT', command = exit)
    bototon2.pack(side= tkinter.LEFT)

    bototon3 = tkinter.Button(window, text = 'grafica', command = grafica2)
    bototon3.pack(side= tkinter.BOTTOM)

    window.title("SIS domotico")

    window.mainloop()