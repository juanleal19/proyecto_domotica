from tkinter import *
import tkinter
import serial 
from bokeh.plotting import figure, show
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
        datos_tem = (val[val2])
       
    
    return datos_tem
    

def exit():
    serialArduino.write(b'e')

def grafica():
    i = 0
    x = []
    y = []

    for i in range(200):
        data = temperatura()
        x.append(i)
        y.append(data)

        p = figure(title = "example", x_axis_label="x", y_axis_label="y")
        p.line(x, y, legend_label="Temp.", line_width=2)
        print(data)
        
    show(p)

if __name__ == '__main__':
    
    etiqueta = tkinter.Label(window, text='Sistema domotico')
    etiqueta.pack()
    # boton para la temperatura 
    bototon1 = tkinter.Button(window, text = 'temperatura', command = temperatura)
    bototon1.pack(side= tkinter.RIGHT)

    bototon2 = tkinter.Button(window, text = 'EXIT', command = exit)
    bototon2.pack(side= tkinter.LEFT)

    bototon3 = tkinter.Button(window, text = 'grafica', command = grafica)
    bototon3.pack(side= tkinter.BOTTOM)

    window.title("SIS domotico")

    window.mainloop()