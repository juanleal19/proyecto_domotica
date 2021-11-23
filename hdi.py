from tkinter import *
import tkinter;import serial ;import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys


window = Tk()
window.geometry('600x500') #tamano de la ventana

serialArduino = serial.Serial("COM4", 9600)
time.sleep(1)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xdat,tdat= [],[]


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
    etiqueta_tem["text"] = (f"temperatura = {datos_tem}C ")
 

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
    etiqueta_hum["text"] = (f"humedad = {datos_hum}%")

def exit():
    ax.clear()
    sys.exit()
    
def animate(i,xdat,tdat):
    data = temperatura()
    xdat.append(i)
    tdat.append(data)
    ax.clear()
    ax.plot(xdat, tdat)
    
def grafica():
    i = 0
    ani = animation.FuncAnimation(fig, animate,fargs=(xdat, tdat))
    plt.show()

def servo():
    serialArduino.write(b's')
    print('entrar de servo')



def angulo_servo():
     serialArduino.write(b'e')
     print('salir de servo')

def on():
    serialArduino.write(b'o')
    bototon8["bg"]="green"
    bototon9["bg"]="red"

def off():
    serialArduino.write(b'f')
    bototon8["bg"]="red"
    bototon9["bg"]="green"



if __name__ == '__main__':
    
    etiqueta_tem = tkinter.Label(window)
    etiqueta_tem.grid(row=1, column=0)

    etiqueta_angulo = tkinter.Label(window)
    etiqueta_angulo.grid(row=5, column=6)  

    etiqueta_hum = tkinter.Label(window)
    etiqueta_hum.grid(row=1, column=3)

    bototon1 = tkinter.Button(window, text = 'Temperatura',width =15 ,height=3 , command = temperaturaPrnt)
    bototon1.grid(row=0, column=0)
    
    bototon2 = tkinter.Button(window, text = 'Humedad',width =15 ,height=3 , command = humedadPrnt)
    bototon2.grid(row=0, column=3)

    bototon3 = tkinter.Button(window, text = 'EXIT',width =10 ,height=3 , bg="red",fg="white", command = exit)
    bototon3.grid(row=0, column=13)

    bototon4 = tkinter.Button(window, text = 'Grafica Temperatura',width =15 ,height=3 , command = grafica)
    bototon4.grid(row=2, column=0)
    
    bototon5 = tkinter.Button(window, text = 'Grafica Humedad',width =15 ,height=3 , command = grafica)
    bototon5.grid(row=2, column=3)
    
    bototon6 = tkinter.Button(window, text = 'off cortina',width =5 ,height=3 , command = angulo_servo)
    bototon6.grid(row=2, column=6)
    
    bototon7 = tkinter.Button(window, text = 'cortina',width =15 ,height=3 , command = servo)
    bototon7.grid(row=0, column=6)

    bototon8 = tkinter.Button(window, text = 'ON',width =5 ,height=2 ,  command =on)
    bototon8.grid(row=0, column=7)

    bototon9 = tkinter.Button(window, text = 'OFF',width =5 ,height=2 , command = off)
    bototon9.grid(row=2, column=7)

    set_servo = tkinter.Entry(window)
    set_servo.grid(row=1, column=6)
    
    window.title("SIS domotico")

    window.mainloop()