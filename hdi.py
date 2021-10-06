from tkinter import *
import tkinter
import serial 
import time



window = Tk()
window.geometry('600x500') #tamano de la ventana

serialArduino = serial.Serial("COM6", 9600)
time.sleep(1)


#funcion que se ejecurta al optrimir el boton temperatura
def temperatura ():

    datos_tem =[]

    #while True:
    for i in range(0,10):
        serialArduino.write(b'a')
        val = serialArduino.readline().decode('ascii')
        print(val)
        dat = (val)
        slc = slice(13,17,1)
        datos_tem.append(val[slc])
        print("*****************")
    
    print(datos_tem)
    serialArduino.write(b'e')
    val = serialArduino.readline().decode('ascii')
    print(val)


def exit():
    serialArduino.write(b'e')


if __name__ == '__main__':
    
    etiqueta = tkinter.Label(window, text='Sistema domotico')
    etiqueta.pack()
    # boton para la temperatura 
    bototon1 = tkinter.Button(window, text = 'temperatura', command = temperatura)
    bototon1.pack(side= tkinter.RIGHT)

    bototon2 = tkinter.Button(window, text = 'EXIT', command = exit)
    bototon2.pack(side= tkinter.LEFT)

    window.title("SIS domotico")

    window.mainloop()