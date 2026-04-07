import math
class Vehiculo:
	def __init__(self, nombre, x0, v0, aceleracion, color):
		self.nombre = nombre
		self.x0 = x0
		self.v0 = v0
		self.aceleracion = aceleracion
		self.color = color

	def getPosicionFinal(self, tiempo):
		return self.x0 + (self.v0 * tiempo) + (0.5 * self.aceleracion * math.pow(tiempo, 2)) 

	def getVelocidadFinal(self, tiempo):
		return self.v0 + (self.aceleracion * tiempo)

	def getVelocidad(self):
		return self.v0

	def getAceleracion(self):
		return self.aceleracion

	def getPosInicial(self):
		return self.x0