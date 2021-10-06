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
    while True:
        serialArduino.write(b'a')
        val = serialArduino.readline().decode('ascii')
        print(val)
        print("*****************")

        if val == 'e':
            break

       
def exit():
    pass



if __name__ == '__main__':
    
    etiqueta = tkinter.Label(window, text='Sistema domotico')
    etiqueta.pack()
    
    bototon1 = tkinter.Button(window, text = 'temperatura', command= temperatura)
    bototon1.pack(side= tkinter.RIGHT)

    window.title("SIS domotico")

    window.mainloop()