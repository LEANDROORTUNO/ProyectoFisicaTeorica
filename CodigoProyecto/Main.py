import subprocess
import sys

def ejecutar_manim():
    """
    Lanza el renderizado de Manim usando subprocess para capturar 
    la salida de la terminal de Linux Mint.
    """
    # Configuración del comando:
    # -p: Abrir video al finalizar
    # -ql: Calidad baja (480p) para rapidez
    comando = ["manim", "-pql", "Persecucion.py", "ProyectoPersecucion"]

    try:
        # Ejecutamos el comando como si estuviéramos en la terminal
        subprocess.run(comando, check=True)
    except FileNotFoundError:
        print("Error: No se encontró 'manim'. ¿Instalaste las dependencias?")
    except subprocess.CalledProcessError:
        print("Error: Hubo un problema al renderizar la escena.")

if __name__ == "__main__":
    ejecutar_manim()