from math import sqrt
class Motorfisica:
    def velocidad_movil_a():
        vb0 = 70.0 / 3.6
        a_b = 1.0
        sep_ini = 100.0
        sep_fin = 10.0
        
        dfa = sep_ini - sep_fin
        at = a_b / 0.5
        
        vam = sqrt(dfa * at)
        va = vb0 + vam

        return va
res = Motorfisica.velocidad_movil_a()
print("El valor de la velocidad de a: ", res)