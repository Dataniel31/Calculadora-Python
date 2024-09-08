import tkinter as tk

# Crear la venta principal
ventana = tk.Tk()
ventana.title('Mi Calculadora')

#Cambiar icono de la calculadora
ventana.iconbitmap("calculadora.ico")

#configurar el tamaño dinamico de las columnas y filas
for i in range(5):
    ventana.grid_rowconfigure(i,weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i,weight=1)

#cuadro de texto para mostrar las expressiones y resultados
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica',24),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=4,
                 justify='right')
visor.grid(row=0,
           column=0,
           columnspan=4)
#Ejecutar la aplicacion
ventana.mainloop()
