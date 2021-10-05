from tkinter import *
import tkinter
  
window = Tk()
window.geometry('600x500')

if __name__ == '__main__':
    
    etiqueta = tkinter.Label(window, text='Sistema domotico')
    etiqueta.pack()
    
    window.title("SIS domotico")

    window.mainloop()