from Vehiculo import Vehiculo 
from manim import BLUE, RED

class Resolucion:

	def __init__(self):
		#Resultado obtenido despues de los calculos
		self.va = 31
		self.vehiculo1 = Vehiculo("A", 0, self.va, 0, BLUE)
		self.v0b = 73 / 3.6
		self.vehiculo2 = Vehiculo("B", 100, self.v0b, 1, RED)
		
	def getDatosImportantes(self):
		tiempoEncuentro = (self.va - self.v0b) / self.vehiculo2.getAceleracion()
		return self.va, tiempoEncuentro, self.vehiculo2.getVelocidad()

	def getVehiculo1(self):
		return self.vehiculo1

	def getVehiculo2(self):
		return self.vehiculo2

	 
