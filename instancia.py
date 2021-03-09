class Coordenada:

    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def distancia(self, otra_coordenada):
        x_diff = (self._x - otra_coordenada._x)**2
        y_diff = (self._y - otra_coordenada._y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    #print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))