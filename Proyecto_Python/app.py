# Importar la biblioteca tkinter
import tkinter as tk
from tkinter import messagebox

# Función para agregar una tarea
def agregar_tarea():
    titulo = entrada_texto.get()
    descripcion = texto_descripcion.get("1.0", tk.END).strip()
    if titulo:
        lista_tareas.insert(tk.END, titulo)
        tareas[titulo] = descripcion
        entrada_texto.delete(0, tk.END)
        texto_descripcion.delete("1.0", tk.END)

# Función para mostrar la descripción de una tarea al seleccionarla
def mostrar_descripcion(event):
    try:
        indice = lista_tareas.curselection()[0]
        titulo = lista_tareas.get(indice)
        descripcion = tareas[titulo]
        texto_descripcion.delete("1.0", tk.END)
        texto_descripcion.insert("1.0", descripcion)
    except IndexError:
        pass

# Función para eliminar una tarea seleccionada
def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        titulo = lista_tareas.get(indice)
        del tareas[titulo]
        lista_tareas.delete(indice)
    except IndexError:
        pass

# Función para marcar una tarea como completada
def completar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        titulo = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, titulo + " ✔")
        tareas[titulo + " ✔"] = tareas.pop(titulo)
    except IndexError:
        pass

# Función para limpiar el área de descripción
def limpiar_descripcion():
    texto_descripcion.delete("1.0", tk.END)

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Gestor de Tareas")
root.configure(bg='light blue')
root.resizable(False, False)

# Inicializar el diccionario de tareas
tareas = {}


# Crear un frame principal con fondo azul claro
frame = tk.Frame(root, bg='light blue')
frame.pack(pady=10)

# Crear un nuevo frame para el listado de tareas y su título
frame_tareas = tk.Frame(root, bg='light blue')
frame_tareas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

# Título para el listado de tareas
titulo_tareas = tk.Label(frame_tareas, text="Tareas", bg='light blue', fg='black', font=('Arial', 14))
titulo_tareas.pack(pady=(0, 5))

# Configuración del Listbox para moverlo al nuevo frame
lista_tareas = tk.Listbox(frame_tareas, width=50, height=10, font=('Arial', 12))
lista_tareas.pack(pady=(0, 10))
lista_tareas.bind('<<ListboxSelect>>', mostrar_descripcion)

# Crear un campo de entrada para el título de la tarea
entrada_texto = tk.Entry(frame, width=50, font=('Arial', 12))
entrada_texto.pack(side=tk.LEFT, padx=(0, 10))

# Crear un botón para guardar la tarea
boton_agregar = tk.Button(frame, text="Guardar Tarea", command=agregar_tarea, bg='green', fg='white', font=('Arial', 12))
boton_agregar.pack(side=tk.LEFT)

# Título para el listado de descripcion
titulo_descrpcion = tk.Label(root, text="Descripción", bg='light blue', fg='black', font=('Arial', 14))
titulo_descrpcion.pack(pady=(0, 5))

# Crear un área de texto para la descripción de la tarea
texto_descripcion = tk.Text(root, height=10, width=50, font=('Arial', 12))
texto_descripcion.pack(pady=(10, 0))

# Crear un botón para limpiar la descripción
boton_limpiar = tk.Button(root, text="Limpiar Descripción", command=limpiar_descripcion, bg='blue', fg='white', font=('Arial', 12))
boton_limpiar.pack(pady=(5, 10))

# Crear un botón para eliminar una tarea
boton_eliminar = tk.Button(frame_tareas, text="Eliminar Tarea", command=eliminar_tarea, bg='red', fg='white', font=('Arial', 12))
boton_eliminar.pack(side=tk.TOP, fill=tk.X)

# Crear un botón para marcar una tarea como completada
boton_completar = tk.Button(frame_tareas, text="Completar Tarea", command=completar_tarea, bg='gray', fg='white', font=('Arial', 12))
boton_completar.pack(side=tk.TOP, fill=tk.X)

# Iniciar el bucle principal de la aplicación
root.mainloop()