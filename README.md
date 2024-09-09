# Mi Calculadora

Este proyecto es una calculadora desarrollada en Python utilizando la biblioteca **Tkinter** para crear la interfaz gráfica. La calculadora permite realizar operaciones básicas y tiene la funcionalidad de alternar entre **modo claro** y **modo noche**.

## Librerías Utilizadas

- **Tkinter:** Esta biblioteca estándar de Python es usada para crear la interfaz gráfica de usuario (GUI). No necesita instalación adicional, ya que viene preinstalada con Python.

    ```python
    import tkinter as tk
    ```

## Funcionalidades

- **Operaciones básicas:** Suma, resta, multiplicación, y división.
- **Modo Claro/Noche:** Permite cambiar entre los modos visuales claro y oscuro para mejorar la experiencia de usuario.
- **Interfaz amigable:** Botones grandes y fácilmente accesibles, con un diseño adaptado para todos los tamaños de pantalla.
  
### Métodos Principales

1. **pulsar_tecla(tecla):** Actualiza la expresión matemática al pulsar un botón.
2. **limpiar():** Limpia la pantalla y resetea la expresión.
3. **evaluar():** Evalúa la expresión ingresada y muestra el resultado.
4. **cambiar_modo():** Alterna entre modo claro y modo noche.
5. **aplicar_estilos():** Aplica el estilo visual correspondiente según el modo activo (noche o claro).

## Requisitos

Antes de ejecutar la calculadora, asegúrate de tener instalado Python en tu sistema. Si no lo tienes, puedes descargarlo desde [aquí](https://www.python.org/downloads/).

## Instalación

1. Clona este repositorio en tu máquina local.
2. Navega a la carpeta del proyecto y ejecuta el siguiente comando en la terminal para instalar las dependencias necesarias:

    ```bash
    pip install tk
    ```

3. Para ejecutar la calculadora, simplemente usa el siguiente comando:

    ```bash
    python calculadora.py
    ```

## Crear un archivo ejecutable (.exe)

Si deseas convertir este proyecto en un archivo ejecutable para Windows, puedes usar **PyInstaller**:

1. Instala **PyInstaller** ejecutando este comando en tu terminal:

    ```bash
    pip install pyinstaller
    ```

2. Una vez instalado, navega hasta la carpeta del proyecto y ejecuta el siguiente comando para generar el archivo `.exe`:

    ```bash
    pyinstaller --onefile --windowed --icon=calculadora.ico calculadora.py
    ```

3. Esto creará una carpeta `dist` en tu proyecto, donde encontrarás el archivo `calculadora.exe` listo para ser ejecutado sin necesidad de tener Python instalado.

## Personalización

Puedes personalizar el diseño y los estilos de la calculadora modificando los colores y las fuentes en el archivo `calculadora.py`. También es posible cambiar el icono de la aplicación agregando un archivo `.ico` con el nombre **calculadora.ico** en la carpeta raíz del proyecto.
