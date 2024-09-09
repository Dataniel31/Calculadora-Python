import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Mi Calculadora')

# Cambiar icono de la calculadora
ventana.iconbitmap("calculadora.ico")

# Almacenar la expresión matemática
expresion = ""

# Variable para verificar si se ha mostrado un resultado
mostrando_resultado = False


# Función para actualizar la expresión en el cuadro de texto
def pulsar_tecla(tecla):
    global expresion, mostrando_resultado

    if mostrando_resultado:
        if tecla.isdigit() or tecla == '.':
            expresion = str(tecla)  # Inicia una nueva expresión si se presiona un número o punto
        else:
            expresion += str(tecla)  # Continúa la expresión si es un operador
        mostrando_resultado = False
    else:
        expresion += str(tecla)

    visor_texto.set(expresion)


# Función para limpiar la entrada (botón C)
def limpiar():
    global expresion, mostrando_resultado
    expresion = ""
    visor_texto.set(expresion)
    mostrando_resultado = False


# Función para realizar una operación según la expresión
def evaluar():
    global expresion, mostrando_resultado
    try:
        resultado = eval(expresion)
        # Verificar si el resultado es un entero
        if resultado == int(resultado):
            resultado = int(resultado)
        visor_texto.set(str(resultado))
        expresion = str(resultado)
        mostrando_resultado = True
    except:
        visor_texto.set("ERROR")
        expresion = ""
        mostrando_resultado = False


# Configurar el tamaño dinámico de las columnas y filas
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Cuadro de texto para mostrar las expresiones y resultados
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 24),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=4,
                 justify='right')
visor.grid(row=0, column=0, columnspan=4)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

# Crear y posicionar los botones (excepto "=")
for (texto, fila, columna) in botones:
    if texto == 'C':
        comando = limpiar
    else:
        comando = lambda x=texto: pulsar_tecla(x)
    tk.Button(ventana,
              text=texto,
              padx=20,
              pady=20,
              font=('Helvetica', 20),
              command=comando
              ).grid(row=fila, column=columna, sticky='nsew')

# Botón "=" que ocupa una fila entera
tk.Button(ventana,
          text="=",
          padx=20,
          pady=20,
          font=('Helvetica', 40),
          command=evaluar
          ).grid(row=5, column=0, columnspan=4, sticky='nsew')

# Ejecutar la aplicación
ventana.mainloop()
