from tkinter import *
import tkinter
import serial 
import time



window = Tk()
window.geometry('600x500') #tamano de la ventana

serialArduino = serial.Serial("COM4", 9600)
time.sleep(1)


#funcion que se ejecurta al optrimir el boton temperatura
def temperatura ():

    datos_tem =[]
    for i in range(0,10):
        serialArduino.write(b'2')
        val = serialArduino.readline().decode('ascii')
        #print(val)
        val2 = slice(0,2,1)
        datos_tem.append(val[val2])
       
    
    print(datos_tem)
    

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