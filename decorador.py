""" def funcion_decoradora(funcion):
    def wrapper():
        print('Este es el ultimo mensaje')
        funcion()
        print('Este es el primer mensaje')
    return wrapper()

def zumbido():
    print('buzzzz')

zumbido = funcion_decoradora(zumbido) """

#Clases whitout getters and setters
class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)

avion = Millas()
avion.distancia = 200
print(avion.distancia)

print(avion.convertir_a_kilometros())
