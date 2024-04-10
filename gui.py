import tkinter as tk
import ttkbootstrap as ttk
from functional import get_status


def update_status():
    try:
        id = int(id_entry.get())
        estado = get_status(id)

        if estado is not None:
            if estado == 'bueno':
                estado_label.config(text="Estado: " + estado, background='green', font=("Helvetica", 13))
                style.configure('TLabel', foreground='black')
                id_entry.delete(0, 'end')  # limpia el entry field
            elif estado == 'malo':
                estado_label.config(text="Estado: " + estado, background='red', font=("Helvetica", 13))
                style.configure('TLabel', foreground='black')
                id_entry.delete(0, 'end')
            elif estado == 'revision':
                estado_label.config(text="Estado: " + estado, background='yellow', font=("Helvetica", 13))
                style.configure('TLabel', foreground='black')
                id_entry.delete(0, 'end')
            else:
                estado_label.config(text="Codigo no encontrado", background='white', font=("Helvetica", 13))
                style.configure('TLabel', foreground='black')
        else:
            estado_label.config(text="Codigo no encontrado", background='white', font=("Helvetica", 13))
            style.configure('TLabel', foreground='black')
            id_entry.delete(0, 'end')      
    except ValueError:
        estado_label.config(text="Inserte codigo de cliente", background='white', font=("Helvetica", 12))
        style.configure('TLabel', foreground='black')
        id_entry.delete(0, 'end')

# Movimiento con el arrastre del mouse
def start_move(event):
    window.x = event.x
    window.y = event.y

def stop_move(event):
    window.x = None
    window.y = None

def do_move(event):
    dx = event.x - window.x
    dy = event.y - window.y
    x = window.winfo_x() + dx
    y = window.winfo_y() + dy
    window.geometry(f"+{x}+{y}")
    
#Window
window = ttk.Window(themename = 'minty')
window.title("Demo Credito")
window.geometry('290x450')
window.overrideredirect(1) # Quita el control de windows de la barra de titulo

style = ttk.Style()
style.theme_use('minty')
style.configure('TButton', foreground='black')
style.configure('TLabel', foreground='black')
window.bind("<ButtonPress-1>", start_move)
window.bind("<ButtonRelease-1>", stop_move)
window.bind("<B1-Motion>", do_move)
style = ttk.Style()
style.configure('TButton', foreground='black')

style.configure('TButton', 
                foreground='black', 
                relief="sunken",  
                highlightthickness=0) # Segun quita los dash en el selector pero... ?


original_size = None
title_frame = None

# Funcion rollup window para "minimizar" hacia arriba el app
def rollup_window():
    global original_size, title_frame
    if window.winfo_height() > 28:  # If la ventana no esta rollup
        # almacenar tamano original
        original_size = window.winfo_height()
        # Reduce la ventana hasta el tamano de la barra de titulo
        window.geometry(f"{window.winfo_width()}x28")
        # Nuevo frame para el titulo
        title_frame = tk.Frame(window)
        title_frame.place(relx=0.4, rely=0.5, anchor='center')
        # Nuevo label dentro del frame para el titulo
        title_label = tk.Label(title_frame, text="Credito Cliente", bg="white", fg="black", font=("Helvetica 13", 13))
        title_label.pack()
    else:  # If la ventana esta rollup
        # Restaurar el tamano original
        window.geometry(f"{window.winfo_width()}x{original_size}")
        # Destruye el title frame
        if title_frame is not None:
            title_frame.destroy()

def close_window():
    window.destroy()

# Espacio flexible en el top
top_space = ttk.Frame(master = window)
top_space.pack(side='top', fill='both', expand=True)

# El boton X para cerrar por que windows para simular la barra de titulo
style.configure('Close.TButton', borderwidth=0, highlightthickness=0, font=('Helvetica 13', 10))  # Create a new style for the close button
close_button = ttk.Button(window, text="X", command=close_window, style='Close.TButton')  # Apply the new style to the close button
close_button.place(relx=0.95, rely=0.04, anchor='ne')

# Boton para la funcion rollup_window
style.configure('Rollup.TButton', borderwidth=0, highlightthickness=0,  font=('Helvetica 13', 10))  # Create a new style for the rollup button
rollup_button = ttk.Button(window, text="^", command=rollup_window, style='Rollup.TButton')  # Apply the new style to the rollup button
rollup_button.place(relx=0.85, rely=0.04, anchor='ne')

# Label Codigo de cliente
id_label = ttk.Label(master = window, text="Codigo Cliente", font = 'Helvetica 23 bold')
id_label.pack(padx=10, pady=20)

# Frame de entrada
input_frame = ttk.Frame(master = window)
id_entry = ttk.Entry(master = input_frame, width=26)
id_entry.pack()
input_frame.pack(side='top', anchor='center')
style.configure('Submit.TButton', font=('Helvetica', 13))
submit_button = ttk.Button(master = input_frame, text="Enviar", command=update_status, style='Submit.TButton', width=16)
submit_button.pack(padx=10, pady=15)

# Espacio flexible bottom
bottom_space = ttk.Frame(master = window)
bottom_space.pack(side='bottom', fill='both', expand=True)

id_entry.bind('<Return>', lambda event: update_status())

# Mensaje Output
estado_label = ttk.Label(master = window, text="Estado: ", font = 'Helvetica 13')
estado_label.pack(padx=10, pady=20)

# Run
window.mainloop()