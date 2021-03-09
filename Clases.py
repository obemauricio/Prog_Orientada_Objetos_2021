class Hotel:
    
    def __init__(self, start, rooms, room_bats):
        self._estrella = start #atributo
        self._cuartos = rooms
        self._cuartos_bano = room_bats
        self._CUARTOS_MAX = rooms #datofijo
        self._CUARTOS_BANO_MAX = room_bats #dato fijo

    def _actualizar_datos(self, accion, cuartos, cuarto_bano): #metodo
        if accion == 'alquilar' or accion == 'reservar': #al alquilar y reservar, restamos y calculamos la disponibilidad
            if self._cuartos - cuartos < 0: #verificamos que el usuario no reserve lo que no se dispone
                print(f'No se dispone de {cuartos} cuartos, solo quedan disponibles {self._cuartos} cuartos')
            else: #si todo es conforme, actualizamos la data
                self._cuartos -= cuartos
            
            if self._cuartos_bano - cuartos_bano < 0:
                print(f'No se dispone de {cuartos_bano} cuartos con baño, solo se dispone de {self._cuartos_bano} cuartos con baño')
            else:
                self._cuartos_bano -= cuarto_bano
        elif accion == 'cancelar reserva': #al cancelar la reserva sumamos y calculamos
            if self._cuartos += cuartos > self._CUARTOS_MAX:
                print(f'No se puede ejecutar la accion, solo se dispone de {self._cuartos} cuartos')
            else: 
                self._cuartos += cuartos
            
            if self._cuartos_bano + cuarto_bano > self._CUARTOS_BANO_MAX:
                print(f'No se puede ejecutar la accion, solo se dispone de {self._CUARTOS_BANO_MAX} cuartos con baño')
            else:
                self._cuartos_bano += cuarto_bano #Actualizamos los atributos

    def alquilar(self, cuartos, cuartos_bano):
        self._actualizar_datos('alquilar', cuartos, cuartos_bano)
        print(f'Quedan {self._cuartos} cuartos y {self._cuarto_bano} cuartos con baño disponibles')
    
    def reservar(self, cuartos, cuartos_bano):
        self._actualizar_datos('reservar', cuartos, cuartos_bano)
        print(f'Quedan {self._cuartos} cuartos y {self._cuarto_bano} cuartos con baño disponible')
    
    def cancelar_reserva(self, cuartos, cuartos_bano):
        self._actualizar_datos('Cancelar_reserva', cuartos, cuarto_bano)
        print(f'Quedan {self._cuartos} cuartos y {self._cuartos_bano}')
    
    def llamar_asistente(self):
        print("""
        --- El asistente esta en camino ---
        """)
    
    def menu(self):
        opcion = int(input(f"""
        ------------------------ WELCOME TO HOTEL ASSISTANT----------------------------
                    Este es el asistente para trabajar con los hoteles
            Diponibilidad de:
            - {self._cuartos} cuartos
            - {self._cuarto_bano} cuartos con baño
            _______________________________________
                ¿que es lo que desea hacer?
                    1.- Alquilar
                    2.- Reservar
                    3.- Cancelar reserva
                    4.- Llamar a asistente
                    5.- Salir del programa 
                Elija una opcion ------> """))
        return opcion

def preguntar():
    cuartos = int(input('Cuantos cuartos: '))
    cuantos_banos =int(input('Cuantos cuartos con baño: '))

    return cuartos, cuantos_banos

def run():
    hotel_cielo = Hotel(3, 20, 15)

    while True:
        opcion = hotel_cielo()
        if opcion == 1:
            cuartos, cuartos baño = preguntar()
            hotel_cielo.alquilar(cuartos, cuartos_bano)
        elif opcion == 2:
            cuartos, cuartos baño = preguntar()
            hotel_cielo.reservar(cuartos, cuartos_bano)     
        elif opcion == 3:
            cuartos, cuartos baño = preguntar()
            hotel_cielo.cancelar_reserva(cuartos, cuartos_bano)
        else:
            break

if __name__ == '__main__':
    run()
            