from math import log
import numpy as np
class TrapecioCompuesto:

    def __init__(self, x_inicio, x_fin, funcion, numero_puntos = 2):
        self.h = (x_fin-x_inicio)/(numero_puntos)
        self.x_inicio = x_inicio
        self.x_fin = x_fin
        self.numero_puntos = numero_puntos
        self.funcion = funcion

    def resolver(self):
        sumatoria = 0.0
        area = 0.0
        for i in range(1, self.numero_puntos):
            x_siguiente = self.x_inicio + i*self.h
            sumatoria += self.funcion(x_siguiente) + self.funcion(self.x_fin) #Sumatoria descrita en el board
        area = (self.h/2)*(self.funcion(self.x_inicio) + 2*sumatoria) # Esta parte es la formula que aparece en el board
        return area

#Acá puedes poner cualquiern función que vayas a integrar.
def funcion_a_evaluar(x):
    return np.exp(x)*np.sin(x)

if __name__ == '__main__':
    trapecio_compuesto = TrapecioCompuesto(1.0, 3.0, funcion_a_evaluar, numero_puntos = 100)
    resultado_integracion = trapecio_compuesto.resolver()
    print(resultado_integracion)