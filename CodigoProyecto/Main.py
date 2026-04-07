import subprocess
import sys

def ejecutar_manim():
    
    comando = ["manim", "-pql", "Persecucion.py", "ProyectoPersecucion"]

    try:
        subprocess.run(comando, check=True)
    except FileNotFoundError:
        print("Error: No se encontró 'manim'. ¿Instalaste las dependencias?")
    except subprocess.CalledProcessError:
        print("Error: Hubo un problema al renderizar la escena.")

if __name__ == "__main__":
    ejecutar_manim()