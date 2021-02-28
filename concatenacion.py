import tkinter as tk
from tkinter.ttk import Style
from PIL import Image, ImageTk
import configuracion
ncara=configuracion.nombre_caras()
class Imagenes:
    def __init__(self, master):
        self.master=master
        self.inicializar_gui()

    def inicializar_gui(self):
        Style().configure('Tframe', background='#FFF')
        #ubicar la cara top
        img_face_top=Image.open('Caras digitalizadas\Cara_top.jpg')
        img_face_top=ImageTk.PhotoImage(img_face_top)
        lbl_face_top=tk.Label(self.master, image=img_face_top)
        lbl_face_top.image=img_face_top
        lbl_face_top.place(x=175,y=175)
        #ubicar la cara bottom
        img_face_bottom=Image.open('Caras digitalizadas\Cara_bottom.jpg')
        img_face_bottom=ImageTk.PhotoImage(img_face_bottom)
        lbl_face_bottom=tk.Label(self.master, image=img_face_bottom)
        lbl_face_bottom.image=img_face_bottom
        lbl_face_bottom.place(x=479,y=175)
        #ubicar la cara back
        img_face_back=Image.open('Caras digitalizadas\Cara_back.jpg')
        img_face_back=ImageTk.PhotoImage(img_face_back)
        lbl_face_back=tk.Label(self.master, image=img_face_back)
        lbl_face_back.image=img_face_back
        lbl_face_back.place(x=175,y=23)
        #ubicar la cara front
        img_face_front=Image.open('Caras digitalizadas\Cara_front.jpg')
        img_face_front=ImageTk.PhotoImage(img_face_front)
        lbl_face_front=tk.Label(self.master, image=img_face_front)
        lbl_face_front.image=img_face_front
        lbl_face_front.place(x=175,y=327)
        #ubicar la cara left
        img_face_left=Image.open('Caras digitalizadas\Cara_left.jpg')
        img_face_left=ImageTk.PhotoImage(img_face_left)
        lbl_face_left=tk.Label(self.master, image=img_face_left)
        lbl_face_left.image=img_face_left
        lbl_face_left.place(x=23,y=175)
        #ubicar la cara right
        img_face_right=Image.open('Caras digitalizadas\Cara_right.jpg')
        img_face_right=ImageTk.PhotoImage(img_face_right)
        lbl_face_right=tk.Label(self.master, image=img_face_right)
        lbl_face_right.image=img_face_right
        lbl_face_right.place(x=327,y=175)

def main():
    master=tk.Tk()
    master.title('Ventana nueva')
    master.geometry('650x500')
    ventana=Imagenes(master)
    master.mainloop()


if __name__=="__main__":
    main()
    