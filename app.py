from tkinter import *
import time
import tkinter as tk
from tkinter import ttk,font
import TraductorTypes

class Aplicacion():
    def __init__(self):

        #La ventana normal

        self.raiz = Tk()
        self.raiz.title("Traductor-Compiladores2018")
        self.raiz.resizable(False,False)
        self.raiz.geometry("1200x400+50+50")

        #El lugar donde estaran donde estan las letras
        self.miFrame = Frame(self.raiz, width=1200, height=80)
        self.miFrame.config(bg="#00FFFF")
        self.miFrame.pack()
        self.miFrame.config(bd=2)
        #miFrame.config(relief="groove")
        self.miFrame.config(relief="sunken")

        #lugar donde estara la imagen logo
        self.miFrame1 = Frame(self.raiz, width=1200, height=10, pady=4, padx=4)
        self.miFrame1.config(bg="white")
        self.miFrame1.pack()
        


        #El lugar donde estara la imagen
        self.miimagen = Frame(self.raiz, width=1200, height=550)
        self.miimagen.config(bg="white")
        self.miimagen.pack()


        #Tipos de fuentes
        self.fuentenegrita0 =font.Font(family="Helvetica", size=16, weight="bold")
        self.fuentenegrita = font.Font(weight='bold')

        #Variables de los text
        self.texto = StringVar()
        self.texto1 = StringVar()
        self.texto.trace("w",self.traduce)

        #mis widgets para la ventana
        #self.photo = PhotoImage('swap.png')
        self.titulo=Label(self.miFrame,text="ESPAÑOL",bg="red",fg="yellow",font=("chiller",50)).place(x=200,y=10)
        self.imgp2 = Label(self.miimagen,height=8)


        #self.photo = PhotoImage('swap.png')
        self.titulo=Label(self.miFrame,text="INGLES",bg="#08088A",fg="white",font=("chiller",50)).place(x=800,y=10)
        self.imgp2 = Label(self.miimagen,height=8)


        


        #self.savetxt = Button(self.miimagen, text="guardar traduccion", command=self.guardartraduccion)
        #self.savetxt.config(bg="#2C9CF5",fg="white")


        self.etiq1 = Entry(self.miimagen, font=self.fuentenegrita,textvariable=self.texto,width=62,bd=5)
        self.scroll=Scrollbar(self.miimagen,orient="vertical",command=self.etiq1.xview)
        self.etiq1.config(xscrollcommand=self.scroll.set)


        self.etiq2 = Entry(self.miimagen,textvariable=self.texto1, font=self.fuentenegrita,width=62,state=DISABLED,bd=5)
        self.scroll2=Scrollbar(self.miimagen,orient="vertical",command=self.etiq2.xview)
        self.etiq2.config(xscrollcommand=self.scroll2.set)

        self.photo=PhotoImage(file='carlos.gif')
        img=self.labell=Label(self.miFrame1,image=self.photo, width=300, height=120)
        img.grid(row=0, column=2)

        

        #grid
        self.imgp2.grid(row=1,column=0,sticky="nswe",padx=10,pady=10)
        self.etiq1.grid(row=1,column=1,sticky="nswe",pady=10)
        self.scroll.grid(row=1,column=2,sticky="nswe",pady=10)
        self.etiq2.grid(row=1,column=4,sticky="nswe",pady=10)
        

        #self.scroll2.grid(row=1,column=5,sticky="nswe",pady=10)
        #self.imagenindice.grid(row=1,column=6,pady=20)
        #self.savetxt.grid(row=2,column=0,columnspan=2,sticky="nswe",pady=10)



        self.raiz.mainloop()




    def traduce(self,a=0,b=0,c=0):
        print(self.texto.get())
        la_traduccion=TraductorTypes.mein(self.texto.get())
        self.texto1.set(la_traduccion)

    def guardartraduccion(self):
        try:
            f=open('Traduccion_log.txt','a')
        except:
            print("Error")
            return 0
        ahora = time.strftime("%c")
        ## representacion de fecha y hora
        fecha =time.strftime("%c")
        f.write("-------------------------------------")
        f.write("\n")
        f.write(fecha)
        f.write("\n")
        f.write(self.texto.get())
        f.write("\n")
        f.write(self.texto1.get())
        f.write("\n")
        f.write("-------------------------------------")
        f.close()

        
        
        


def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
