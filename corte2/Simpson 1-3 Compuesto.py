import numpy as np
class Simpson13Compuesto:

    def __init__(self, x_inicio, x_fin, funcion, numero_puntos = 2):
        self.h = (x_fin-x_inicio)/(numero_puntos)
        self.x_inicio = x_inicio
        self.x_fin = x_fin
        self.numero_puntos = numero_puntos
        self.funcion = funcion

    def resolver(self):
        sumatoria_par = 0.0
        sumatoria_impar = 0.0
        for i in range(1, self.numero_puntos):
            x_siguiente = self.x_inicio + i*self.h
            if i%2 == 0: #PAR
                sumatoria_par += self.funcion(x_siguiente) + self.funcion(self.x_fin) #Sumatoria descrita en el board
            else:
                sumatoria_impar += self.funcion(x_siguiente) #Sumatoria descrita en el board
        area = (self.h/3)*(self.funcion(self.x_inicio) + 4*sumatoria_impar + 2*sumatoria_par) # Esta parte es la formula que aparece en el board
        return area

#Acá puedo poner cualquiern función que vaya a integrar.
def funcion_a_evaluar(x):
    return np.exp(x)*np.sin(x)

if __name__ == '__main__':
    simpson_1_3_compuesto = Simpson13Compuesto(1.0, 3.0, funcion_a_evaluar, numero_puntos = 8)
    resultado_integracion = simpson_1_3_compuesto.resolver()
    print(resultado_integracion)