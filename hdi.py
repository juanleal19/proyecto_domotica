from tkinter import *
import tkinter
  
window = Tk()
window.geometry('600x500')

def temperatura ():
    pass

if __name__ == '__main__':
    
    etiqueta = tkinter.Label(window, text='Sistema domotico')
    etiqueta.pack()
    
    bototon1 = tkinter.Button(window, text = 'temperatura', command= temperatura)
    bototon1.pack(side= tkinter.RIGHT)

    window.title("SIS domotico")

    window.mainloop()