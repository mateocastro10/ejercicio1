class ViajeroFrecuente
    def __init__(self, nv, d, n, a , ma):
        self.__num_viajero = nv
        self.__dni = d
        self.__nombre = n
        self.__apellido = a
        self.__millas_acum = ma
class Menu:
    __op=None
    def __init__(self):
        self.__op = { '1':self.cantidadTotalMillas,
                            '2':self.acumularmillas,
                            '3':self.canjear,
                            '4':self.salir
                          }
    def cantidadTotalMillas(self, objeto):
        cant1 = objeto.cantidadTotalMillas()
        print('La cantidad total de millas acumuladas es de: %d', cant1)
    def acumularmillas(self, objeto):
        cant2 = int(input('Ingrese la cantidad de millas recorridas: '))
        valor1 = objeto.acumularmillas(cant2)
        print('Valor actualizado de las millas acumuladas: %d', valor1)
    def canjear(self, mac):
        cant3 = int(input('Ingrese la cantidad de millas a canjear: '))
        valor2 = objeto.acumularmillas(cant3)
        print('Valor actualizado de las millas acumuladas: %d', valor2)
    def salir(self):
        print('Usted salio del programa')
