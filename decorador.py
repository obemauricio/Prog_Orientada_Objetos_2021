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
""" class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)

#Metodo getter
def obtener_distancia(self):
    return self._distancia 

#Metodo Setter
def definir_distancia(self, valor):
    if valor < 0:
        raise ValueError('No es posible convertir distancias menores a 0')
    self.distancia = valor

 """

class Millas:
    def __init__(self):
        self._distancia = 0
    
    #getter
    @property
    def distancia(self):
        print('Llamando a guetter')
        print(self.distancia)
        return self._distancia

    #setter
    @distancia.setter
    def distancia(self, valor):
        #validacion si no ingresa un numero
        if False is isinstance(valor, (int, float)):
            raise TypeError('Ingrese un numero entero valido')
        if valor < 0:
            raise ValueError('No es posible convertir distancias menores a 0')

        print('Llamada al setter')
        self._distancia = valor

        print(self._distancia)

    #funcion que convierte de km a millas
    def convertir_a_km(self):
        conversion = self.distancia * 1.609344
        print(f'{self._distancia} millas convertidas a km son {conversion} km')

if __name__ == '__main__':
    avion = Millas()
    avion.distancia  #el getter muestra cero ya que no le pasamos ningun dato
    avion.distancia = 45
    
    avion.convertir_a_km() #se transforma la funcion
    