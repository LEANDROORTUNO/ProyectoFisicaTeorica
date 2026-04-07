from manim import *
from Resolucion import Resolucion

class ProyectoPersecucion(Scene):
    def construct(self):
        # Creamos un ValueTracker para el tiempo (esto es muy pro)(preguntar)
        reloj = ValueTracker(0)
        res = Resolucion()

        va, tiempo, v0b = res.getDatosImportantes()
    
        vehiculo1 = res.getVehiculo1()
        vehiculo2 = res.getVehiculo2()

        #obejtos visuales(preguntar como se usa label, carro, ejes)
        ejes = NumberLine(x_range=[0, 380, 100], length=10).shift(DOWN * 2)

        #Imagenes de los moviles:
        carroA, carroB = self.imagenes()

        #FLECHA DE DISTTANCIA:
        flecha = DoubleArrow(color = WHITE, stroke_width = 1, tip_length = 0.2)

        #POSICIONAMIENTO INCICIAL
        labelA, labelB = self.posicionesIniciales(carroA, carroB, ejes, vehiculo1, vehiculo2, reloj)


        #Metodo interaccion
        self.interaccion(reloj, carroA, carroB, labelA, labelB,flecha, ejes, vehiculo1, vehiculo2)

        #agregamos todo a la escena
        self.add(ejes, carroA, carroB, labelA, labelB, flecha)

        # Busca los add_updater dentro de construct()        # Animación: el reloj corre hasta que las velocidades se igualan (preguntar)
        self.play(reloj.animate.set_value(tiempo), run_time=5, rate_func=linear)
        self.wait()

    def imagenes(self):
        try:
            carroA = ImageMobject("../ImagenesProyecto/AutoAzul.png")
            carroA.scale(0.3)
            carroB = ImageMobject("../ImagenesProyecto/AutoRojo.png")
            carroB.scale(0.3)

        except FileNotFoundError:
            print("Error: No se encontraron las imágenes PNG. Usando puntos de respaldo.")
            carroA = Dot(color = BLUE)
            carroB = Dot(color = RED)
        return carroA, carroB


    def posicionesIniciales(self, carroA, carroB, ejes, vehiculo1, vehiculo2, reloj):
        carroA.add_updater(lambda m: m.move_to(ejes.n2p(vehiculo1.getPosicionFinal(reloj.get_value()))).shift(UP*0.7))
        carroB.add_updater(lambda m: m.move_to(ejes.n2p(vehiculo2.getPosicionFinal(reloj.get_value()))).shift(UP*0.7))
        labelA = Text("Auto A", font_size=24).next_to(carroA, UP)
        labelB = Text("Auto B", font_size=24).next_to(carroB, UP) 

        return labelA, labelB

    #Metodo interaccion
    def interaccion(self, reloj, carroA, carroB, labelA, labelB,
            flecha, ejes, vehiculo1, vehiculo2):

        carroA.add_updater(lambda m: m.move_to(ejes.n2p(min(vehiculo1.getPosicionFinal(reloj.get_value()),vehiculo2.getPosicionFinal(reloj.get_value()) - 20))).shift(UP*0.7))
        carroB.add_updater(lambda m: m.move_to(ejes.n2p(vehiculo2.getPosicionFinal(reloj.get_value()))).shift(UP*0.7))
        
        def actualizacion(flecha, dt=0):
            tiempo = reloj.get_value()
        
            pA = carroA.get_critical_point(RIGHT) 
            pB = carroB.get_critical_point(LEFT)

            distancia = abs(vehiculo1.getPosicionFinal(tiempo) - vehiculo2.getPosicionFinal(tiempo))
            colorActual = colorCarro(distancia)
            
            flecha.set_color(colorActual)
            labelA.set_color(colorActual)
            labelB.set_color(colorActual)

            flecha.put_start_and_end_on(pA, pB)
            
        flecha.add_updater(actualizacion)

        def colorCarro(distancia):
            if distancia > 60: 
                color =  WHITE
            elif 45 < distancia <= 60: 
                color = PINK
            else: 
                color = RED
            return color
