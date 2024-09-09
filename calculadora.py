import tkinter as tk

# Crear la venta principal
ventana = tk.Tk()
ventana.title('Mi Calculadora')

# Cambiar icono de la calculadora
ventana.iconbitmap("calculadora.ico")

# almacenar operacion (expresion matematica)
expresion = ""

# almacenar el estado del visor
resultado = False


# Funcion para actualizar la expresion en el cuadro de texto
def pulsar_tecla(tecla):
    global expresion
    expresion = expresion + str(tecla)
    visor_texto.set(expresion)


# configurar el tamaño dinamico de las columnas y filas
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# cuadro de texto para mostrar las expressiones y resultados
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 24),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=4,
                 justify='right')
visor.grid(row=0,
           column=0,
           columnspan=4)
# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]
# Crear y posicionar los botons (excepto "=")
for (texto, fila, columna) in botones:
    if texto == 'c':
        pass
    else:
        comando = lambda x=texto: pulsar_tecla(x)
    tk.Button(ventana,
              text=texto,
              padx=20,
              pady=20,
              font=('Helvetica', 20),
              command=comando
              ).grid(row=fila,
                     column=columna,
                     sticky='nsew')

# boton "=" ocupa una fila entera
tk.Button(ventana,
          text="=",
          padx=20,
          pady=20,
          font=('Helvetica', 40),
          command=comando
          ).grid(row=5,
                 column=0,
                 columnspan=4,
                 sticky='nsew')
# Ejecutar la aplicacion
ventana.mainloop()
