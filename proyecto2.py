import tkinter as tk

from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

from clientes import *
from Conexion import *

class FormularioCliente:

    global base
    base= None

    global texBoxId
    texBoxCodigo= None

    global texBoxNombres
    texBoxNombres= None

    global texBoxApellidos
    texBoxApellidos= None

    global texBoxDni
    texBoxDni= None

    global texBoxFecha
    texBoxFecha= None

    global groupBox
    groupBox= None

    global tree
    tree = None


def Formulario():

        global base
        global texBoxCodigo
        global texBoxNombres
        global texBoxApellidos
        global texBoxDni
        global texBoxFecha
        global groupBox
        global tree

        try:
            base = Tk()
            base.geometry("1415x300")
            base.title("Formulario Python")

            groupBox = LabelFrame(base, text="Datos de los Productos", padx=5, pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelId=Label(groupBox,text="Codigo:", width=13,font=("Verdana", 12)).grid(row=0,column=0)
            texBoxCodigo=Entry(groupBox)
            texBoxCodigo.grid(row=0,column=1)

            labelNombres=Label(groupBox,text="Producto:", width=13,font=("Verdana", 12)).grid(row=1,column=0)
            texBoxNombres=Entry(groupBox)
            texBoxNombres.grid(row=1,column=1)

            labelApellidos=Label(groupBox,text="Stock:", width=13,font=("Verdana", 12)).grid(row=2,column=0)
            texBoxApellidos=Entry(groupBox)
            texBoxApellidos.grid(row=2,column=1)

            labelDNI=Label(groupBox,text="Precio:", width=13,font=("Verdana", 12)).grid(row=3,column=0)
            texBoxDni=Entry(groupBox)
            texBoxDni.grid(row=3,column=1)

            labelFecha=Label(groupBox,text="Fecha:", width=13,font=("Verdana", 12)).grid(row=4,column=0)
            texBoxFecha=Entry(groupBox)
            texBoxFecha.grid(row=4,column=1)


            Button(groupBox,text="Guardar",width=10,command=guardarRegistro).grid(row=5,column=0)
            Button(groupBox,text="Modificar",width=10,command=modificarRegistro).grid(row=5,column=1)
            Button(groupBox,text="Eliminar",width=10, command=eliminarRegistro).grid(row=5,column=2)

            groupBox = LabelFrame(base,text="Lista de los Productos",padx=4,pady=4,)
            groupBox.grid(row=0,column=1,padx=4,pady=4)

            tree = ttk.Treeview(groupBox,columns=("codigo","nombres","apellidos","dni","fecha"),show="headings",height=10,)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="CODIGO")

            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="PRODUCTO")

            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="STOCK")

            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4",text="PRECIO")

            tree.column("# 5",anchor=CENTER)
            tree.heading("# 5",text="FECHA DE PRODUCCION")


            for row in CClientes.mostrarClientes():
                tree.insert("","end",values=row)

            
            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)

            tree.pack()



            base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))


def guardarRegistro():
     global texBoxNombres, texBoxApellidos, texBoxDni, texBoxFecha, groupBox
     try:
          nombres = texBoxNombres.get()
          apellidos = texBoxApellidos.get()
          dni = texBoxDni.get()
          fecha = texBoxFecha.get()

          if nombres and apellidos and dni and fecha: 
               CClientes.ingresarClientes(nombres,apellidos,dni,fecha)
               messagebox.showinfo("Informacion","Los datos fueron agregados")

               actualizarTreeView()
               texBoxCodigo.delete(0,END)
               texBoxNombres.delete(0,END)
               texBoxApellidos.delete(0,END)
               texBoxDni.delete(0,END)
               texBoxFecha.delete(0,END)
          else: 
               messagebox.showinfo("Warning","Ingrese todos los datos")
          

     except ValueError as error:
          print("Error al ingresar Datos {}".format(error))


def actualizarTreeView():
     global tree

     try:
          tree.delete(*tree.get_children())

          datos = CClientes.mostrarClientes()

          for row in CClientes.mostrarClientes():
               tree.insert("","end",values=row)
     except ValueError as error:
          print("Error al actualizar tabla {}".format(error))
        

def seleccionarRegistro(event):
     try:
          itemSeleccionado = tree.focus()

          if itemSeleccionado:
               values = tree.item(itemSeleccionado)['values']

               texBoxCodigo.delete(0,END)
               texBoxCodigo.insert(0,values[0])
               texBoxNombres.delete(0,END)
               texBoxNombres.insert(0,values[1])
               texBoxApellidos.delete(0,END)
               texBoxApellidos.insert(0,values[2])
               texBoxDni.delete(0,END)
               texBoxDni.insert(0,values[3])
               texBoxFecha.delete(0,END)
               texBoxFecha.insert(0,values[4])

     except ValueError as error:
          print("Error al Seleccionar Registro {}".format(error))

def modificarRegistro():
     global texBoxCodigo, texBoxNombres, texBoxApellidos, texBoxDni, texBoxFecha, groupBox
     try:
          codigo = texBoxCodigo.get()
          nombres = texBoxNombres.get()
          apellidos = texBoxApellidos.get()
          dni = texBoxDni.get()
          fecha = texBoxFecha.get()
          if codigo and nombres and apellidos and dni and fecha:
               CClientes.modificarClientes(codigo,nombres,apellidos,dni,fecha)
               messagebox.showinfo("Informacion","Los datos fueron actualizados")

               actualizarTreeView()
               texBoxCodigo.delete(0,END)
               texBoxNombres.delete(0,END)
               texBoxApellidos.delete(0,END)
               texBoxDni.delete(0,END)
               texBoxFecha.delete(0,END)
          
          else: 
               messagebox.showinfo("Warning","Ingrese todos los datos")

     except ValueError as error:
          print("Error al ingresar Datos {}".format(error))
#pruebaeliminar
def eliminarRegistro():
     global texBoxCodigo, groupBox
     try:
          codigo = texBoxCodigo.get()
          if codigo:
               CClientes.eliminarClientes(codigo)
               messagebox.showinfo("Status","Los datos fueron eliminados")

               actualizarTreeView()
               texBoxCodigo.delete(0,END)
               texBoxNombres.delete(0,END)
               texBoxApellidos.delete(0,END)
               texBoxDni.delete(0,END)
               texBoxFecha.delete(0,END)

          else:
               messagebox.showinfo("Warning","Ingrese todos los datos")
          
          
     except ValueError as error:
          print("Error al eliminar Datos {}".format(error))

if __name__ == "__main__":
     Formulario()