class CasillaVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, reg):
        if reg in self._pais:
            self._region = reg
        else:
            raise ValueError(f'La region {reg} no es valida en {self._pais}')
    
casilla = CasillaVotacion(123, ['Bogota', 'Medellin'])
print(casilla.region)
casilla.region = 'Bogota'
print(casilla.region)