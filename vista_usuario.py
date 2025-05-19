from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
from conexion import Obtener_conexion
from centrar_ventana import Centrar_Ventana
from tkinter import ttk

def Abrir_dashboard_usuario(usuario):

    #funciones necesarias

    def mostrar_programas():
        limpiar_frame()
        Label(contenido, text="Programas disponibles", font=("Arial", 11, "bold")).pack()

        columnas_bd = ["id",  "nombre", "descripcion", "genero", "tema", "conductor", "duracion", "horario", "plataforma"]
        columnas_vista = ["id",  "Nombre", "Descripción", "Género", "Tema", "Conductor", "Duración", "Horario", "Plataforma"]

        #treeview para mostrar los programas
        tabla = ttk.Treeview(contenido, columns=columnas_vista, show="headings")
        tabla.pack(padx=10, pady=10, fill="both", expand=True)

        for col in columnas_vista:
            tabla.heading(col, text=col)
            tabla.column(col, width=100)

        #cargar los datos desde mysql
        try:
            conexion = Obtener_conexion()
            cursor  =conexion.cursor()
            cursor.execute("SELECT id, nombre, descripcion, genero, tema, conductor, duracion, horario, plataforma FROM programas")
            programas = cursor.fetchall()
            conexion.close()

            for programa in programas:
                tabla.insert("", END, values=programa)

        except Exception as e:
            messagebox.showerror("Error...\n", f"No se pudo cargar los programas\n{e}")

    def cerrar_sesion():
        ventana.destroy()

    def limpiar_frame():
        for widget in contenido.winfo_children():
            widget.destroy()

    #creacion de la ventana
    ventana =  Tk()
    ventana.title("Dashboard Usuario")
    ventana.resizable(0,0)
    Centrar_Ventana(ventana, 1120, 450)

    #barra lateral izquierda
    menu_izq  =  Frame(ventana, width=200, height=550, bd=1, relief="solid")
    menu_izq.pack(side=LEFT, fill=Y)
    menu_izq.pack_propagate(False)

    #imagen
    imagen =  Image.open("Imagen/logo.png")
    imagen = imagen.resize((150, 150))
    imagen_tk = ImageTk.PhotoImage(imagen)

    label = Label(menu_izq, image=imagen_tk)
    label.pack(pady=20)
    label.image = imagen_tk

    #iconos
    icono1 = PhotoImage(file="Imagen/ver_programa.png")
    icono2 = PhotoImage(file="Imagen/salir.png")

    #botones

    boton1 = Button(menu_izq, text="Ver Programas", image=icono1, compound="left", command=mostrar_programas, font=("Arial", 11, "bold"), padx=10, pady=10)
    boton1.pack(fill=X, pady=20)

    boton2 = Button(menu_izq, text="Cerrar sesión", image=icono2, compound="left", command=cerrar_sesion, font=("Arial", 11, "bold"), padx=10, pady=10)
    boton2.pack(fill=X, pady=37)

    #frame derecho
    contenido  =  Frame(ventana)
    contenido.pack(side=RIGHT, expand=True, fill=BOTH)

    ventana.mainloop()