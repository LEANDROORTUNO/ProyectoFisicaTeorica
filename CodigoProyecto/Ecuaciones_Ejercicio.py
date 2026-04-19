from sympy import *
v0b = 70 #km/h
aA = 0 #m/s
aB = 1 #m/s
d0 = 100 #m
dmin = 10 #m
t, vA = symbols('t vA')
#Convertir km/h a m/s
v0b = round(v0b * (1000 / 3600),2)
print('v0b = ',v0b)
#Para hallar la posicion de A y B
xa = vA*t
#B empieza 100m adelante y con aceleracion
#Ec 1
xB = d0 + (v0b*t) + (0.5*aB*t**2)
#Distancia entre autos
#Ec 2
d = xB - xa
print('d =', xB,'-', xa)
#Derivamos Ec 1
deriv = diff(d, t)
print('0 =',deriv)
#Igualamos la derivada a 0 y ya que la distancia minima 
#es 10m y despejamos t
t_ecua = solve(deriv, t)[0]
print('t =',t_ecua)
#Igualamos la distancia minima y sustituimos el valor
#de t por su ecuacion
xB_sus = xB.subs(t, t_ecua)
xa_sus = xa.subs(t, t_ecua)
print(dmin, '=',xB_sus,'-', xa_sus)
ec_2 = xB.subs(t, t_ecua) - xa.subs(t, t_ecua)
ec_2_res = simplify(ec_2)
print(dmin,'=',ec_2_res)
#Multiplicamos todo por '-2' y despejamos
res = Eq(dmin * 2, ec_2_res * 2)
print(dmin * 2,'=', ec_2_res * 2)
print('vA**2 = ',solve(res, vA**2)[0])
#Mediante la formula cuadratica obtenemos los resultados
vA_sol = (solve(ec_2_res - dmin, vA))
sol_redon = [round(float(s), 2) for s in vA_sol]
print(sol_redon)