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

# Variable para el estado del modo (True = modo noche, False = modo claro)
modo_noche = False


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


# Función para cambiar entre modo claro y modo noche
def cambiar_modo():
    global modo_noche
    modo_noche = not modo_noche  # Alternar entre modo claro y modo noche
    aplicar_estilos()


# Aplicar los estilos según el modo actual
def aplicar_estilos():
    if modo_noche:
        color_fondo_numero = '#333333'
        color_fondo_operacion = '#444444'
        color_fondo_especial = '#555555'
        color_fondo_calcular = '#888888'
        color_texto_numero = '#ffffff'
        color_texto_especial = '#ffffff'
        ventana.config(bg='#222222')
    else:
        color_fondo_numero = '#b3cde0'
        color_fondo_operacion = '#7A869A'
        color_fondo_especial = '#9B90B6'
        color_fondo_calcular = '#b0e57c'
        color_texto_numero = '#333333'
        color_texto_especial = '#ffffff'
        ventana.config(bg='#f0f0f0')

    # Actualizar los colores de los botones
    for (boton, texto) in zip(lista_botones, lista_textos_botones):
        if texto in ['/', '*', '-', '+']:
            boton.config(bg=color_fondo_operacion, fg=color_texto_especial)
        elif texto == 'C':
            boton.config(bg=color_fondo_especial, fg=color_texto_especial)
        elif texto == '.':
            boton.config(bg=color_fondo_especial, fg=color_texto_especial)
        else:
            boton.config(bg=color_fondo_numero, fg=color_texto_numero)

    boton_igual.config(bg=color_fondo_calcular, fg=color_texto_numero)
    boton_modo.config(bg=color_fondo_especial, fg=color_texto_especial)
    visor.config(bg='#e8f0fe' if not modo_noche else '#333333', fg=color_texto_numero)


# Configurar el tamaño dinámico de las columnas y filas
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Cuadro de texto para mostrar las expresiones y resultados
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 32, 'bold'),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=2,
                 justify='right',
                 relief='sunken')
visor.grid(row=0, column=0, columnspan=4, sticky='ew', padx=10, pady=10)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

lista_botones = []
lista_textos_botones = []

# Crear y posicionar los botones (excepto "=" y el botón de modo)
for (texto, fila, columna) in botones:
    if texto == 'C':
        comando = limpiar
    else:
        comando = lambda x=texto: pulsar_tecla(x)

    boton = tk.Button(ventana,
                      text=texto,
                      padx=20,
                      pady=20,
                      font=('Helvetica', 20, 'bold'),
                      command=comando,
                      bd=1,
                      relief='raised')
    boton.grid(row=fila, column=columna, sticky='nsew', padx=2, pady=2)
    lista_botones.append(boton)
    lista_textos_botones.append(texto)

# Botón "=" que ocupa una fila entera
boton_igual = tk.Button(ventana,
                        text="=",
                        padx=20,
                        pady=20,
                        font=('Helvetica', 40, 'bold'),
                        command=evaluar,
                        bd=1,
                        relief='raised')
boton_igual.grid(row=5, column=0, columnspan=4, sticky='ew', padx=2, pady=2)

# Botón para cambiar de modo (noche/claro)
boton_modo = tk.Button(ventana,
                       text="Modo Noche",
                       padx=20,
                       pady=20,
                       font=('Helvetica', 20, 'bold'),
                       command=cambiar_modo,
                       bd=1,
                       relief='raised')
boton_modo.grid(row=6, column=0, columnspan=4, sticky='ew', padx=2, pady=2)

# Aplicar los estilos iniciales (modo claro por defecto)
aplicar_estilos()

# Ejecutar la aplicación
ventana.mainloop()
