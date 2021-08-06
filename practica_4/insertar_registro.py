from tkinter import *
from tkinter import ttk

from mysql.connector import cursor
import demo_database

window = Tk()
frame_app = Frame(window, width=800, height=600, )
window.title('REGISTROS')
my_table = ttk.Treeview(window)
frame_app.pack()

nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
correo = StringVar()
direccion = StringVar()

def registro():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    direccion = entry_direcciom.get()
    
    demo_db = demo_database.MyDatabase()
    demo_db.insert_db(nombre, apellido, telefono, correo, direccion)

import mysql.connector
connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_registro")

cursor = connection.cursor()
cursor.execute("SELECT NOMBRE, APELLIDO, TELEFONO, CORREO, DIRECCION FROM TBL_CLIENTE")
   
my_table = ttk.Treeview(window)
    
registro=0
for fila in cursor:
    registro=registro+1
    print(str(registro) + "-"+str(fila))
    nombre = fila[0]  
    apellido = fila[1]
    telefono = fila[2]
    correo = fila[3]
    direccion = fila[4]
    my_table.insert(parent="", index="end", iid=registro, text=str(registro),
        values=(nombre, apellido, telefono, correo, direccion))
connection.close() 
 
my_table['columns'] = ('NOMBRE', 'APELLIDO', 'TELEFONO', 'CORREO', 'DIRECCION')

my_table.column('#0', width=120, minwidth=50)
my_table.column('NOMBRE', anchor=W, width=120)
my_table.column('APELLIDO', anchor=W, width=120)
my_table.column('TELEFONO', anchor=W, width=120)
my_table.column('CORREO', anchor=W, width=120)
my_table.column('DIRECCION', anchor=W, width=120)

my_table.heading('#0', text='ID_CAMPO', anchor=W)
my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
my_table.heading('APELLIDO', text='APELLIDO', anchor=W)
my_table.heading('TELEFONO', text='TELEFONO', anchor=W)
my_table.heading('CORREO', text='CORREO', anchor=W)
my_table.heading('DIRECCION', text='DIRECCION', anchor=W)

my_table.place(x=400, y=350)

frame_navbar = Frame(frame_app, width=900, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=900, height=120)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=900, height=500)
frame_options.grid(row=2, column=0)

title = Label(frame_navbar,
              bg="pink",
              text="BIENVENIDOS A",
              font=("KG What A Time", "16"))
title.place(x=120, y=40)

title1 = Label(frame_title,
               bg="pink",
              text="¡PEDIDOS A DOMICILIO YAISLY!", 
              font=("KG What A Time", "14", "bold"),
              justify=LEFT)
title1.place(x=25, y=0)
title2 = Label(frame_title,
               bg="pink",
              text="REGISTRATE CON NOSOTROS:", 
              font=("KG What A Time", "12"),
              justify=LEFT)
title2.place(x=25, y=50)

frame_form = Frame(frame_options, width=350, height=450, bg="pink")
frame_form.place(x=25, y=5)
label_nombre = Label(frame_form, 
              text="NOMBRE:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="pink")
label_nombre.place(x=30, y=30)
entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
             font=("KG What A Time", "14"))
entry_nombre.place(x=30, y=70)

label_apellido = Label(frame_form, 
              text="APELLIDO:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="pink")
label_apellido.place(x=30, y=100)
entry_apellido = Entry(frame_form, justify=LEFT, width=25, 
                font=("KG What A Time", "14"))
entry_apellido.place(x=30, y=140)

label_telefono = Label(frame_form, 
              text="TELEFONO:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="pink")
label_telefono.place(x=30, y=170)
entry_telefono = Entry(frame_form, justify=LEFT, width=25, 
                font=("KG What A Time", "14"))
entry_telefono.place(x=30, y=210)

label_correo = Label(frame_form, 
              text="CORREO:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="pink")
label_correo.place(x=30, y=240)
entry_correo = Entry(frame_form, justify=LEFT, width=25,
               font=("KG What A Time", "14"))
entry_correo.place(x=30, y=280)
label_direccion = Label(frame_form, 
              text="DIRECCION:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="pink")
label_direccion.place(x=30, y=320)
entry_direccion = Entry(frame_form, justify=LEFT, width=25, 
             font=("KG What A Time", "14"))
entry_direccion.place(x=30, y=360)

button_agregar = Button(frame_form, text="SIGUIENTE>", 
                        font=("KG What A Time", "14", "bold"),
                        command=registro, bg="pink", fg="black")
button_agregar.place(x=30, y=400)

messagebox.showerror("DESEA CREAR EL REGISTRO", "DESEA CREAR EL REGISTRO")


window.mainloop()
