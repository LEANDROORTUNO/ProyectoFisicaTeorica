from manim import *
from Resolucion import Resolucion


class ProyectoPersecucion(Scene):
    def construct(self):
        res = Resolucion()
        #obtencion Calculos
        va, tiempo, v0b = res.getDatosImportantes()
        #objetos fisicos
        vehiculo1 = res.getVehiculo1()
        vehiculo2 = res.getVehiculo2()

        #obejtos visuales(preguntar como se usa label, carro, ejes)
        ejes = NumberLine(x_range=[0, 500, 100], length=10, include_numbers=True).shift(DOWN * 2)
        #imagenes de autos
        try:
            carro_a = ImageMobject("../ImagenesProyecto/AutoAzul.png")
            carro_a.scale(0.7)
            carro_b = ImageMobject("../ImagenesProyecto/AutoRojo.png")
            carro_b.scale(0.7)

        except FileNotFoundError:
            print("Error: No se encontraron las imágenes PNG. Usando puntos de respaldo.")
            carro_a = Dot(color=BLUE)
            carro_b = Dot(color=RED)

        carro_a.move_to(ejes.n2p(vehiculo1.getPosInicial())).shift(UP*0.7)
        carro_b.move_to(ejes.n2p(vehiculo2.getPosInicial())).shift(UP*0.7)

        label_a = Text("Auto A", font_size=24).next_to(carro_a, UP)
        label_b = Text("Auto B", font_size=24).next_to(carro_b, UP) 

        #agregamos todo a la escena
        self.add(ejes, carro_a, carro_b, label_a, label_b)

        # Creamos un ValueTracker para el tiempo (esto es muy pro)(preguntar)
        reloj = ValueTracker(0)


        # Actualizadores (Mantenemos la física unida a lo visual)(preguntar)
        # Busca los add_updater dentro de construct()
        carro_a.add_updater(lambda m: m.move_to(ejes.n2p(vehiculo1.getPosicionFinal(reloj.get_value()))).shift(UP*0.7)) 
        carro_b.add_updater(lambda m: m.move_to(ejes.n2p(vehiculo2.getPosicionFinal(reloj.get_value()))).shift(UP*0.7)) 
        label_a.add_updater(lambda m: m.next_to(carro_a, UP))
        label_b.add_updater(lambda m: m.next_to(carro_b, UP))


        # Animación: el reloj corre hasta que las velocidades se igualan (preguntar)
        self.play(reloj.animate.set_value(tiempo), run_time=5, rate_func=linear)
        self.wait()