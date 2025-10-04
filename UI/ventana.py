import tkinter as tk
from tkinter import ttk
from db.db import Conndatabase

ventana = tk.Tk()
ventana.title("Restaurantes")
ventana.config(width=200,height=300)

contenedor_1 = ttk.Frame()
contenedor_1.pack()

titulo = ttk.Label(contenedor_1, text="La nota de los restaurantes")

restaurantes = Conndatabase.mostar_nota_media()

titulo_2 = ttk.Label(contenedor_1, text=restaurantes)

ventana.mainloop()





    

    