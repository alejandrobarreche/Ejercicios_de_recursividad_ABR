class Busqueda:
    
    def __init__(self, tabla, numero):
        self.tabla = tabla
        self.longitud_tabla = len(self.tabla)
        self.inicio = 0
        self.fin_tabla = self.longitud_tabla - 1
        self.numero = numero
        self.resultado = None

    def comprobar_tabla(self, inicio, fin_tabla):
        for i in range(inicio, fin_tabla - 1):
            if self.tabla[i] > self.tabla[i+1]:
                return False
        return True
    
    def comprobar_numero_en_tabla(self):
        return self.tabla[self.inicio] <= self.numero <= self.tabla[self.fin_tabla]
        
    def buscar_posicion_en_tabla(self):
        while self.comprobar_tabla(self.inicio, self.fin_tabla) and self.comprobar_numero_en_tabla():
            self.indice_medio = (self.fin_tabla + self.inicio) // 2
            if self.tabla[self.indice_medio] == self.numero:
                self.resultado = self.indice_medio
                break
            elif self.tabla[self.indice_medio] < self.numero:
                self.inicio = self.indice_medio + 1
            else:
                self.fin_tabla = self.indice_medio - 1

        return self.resultado

def ingresar_numero_mayor_o_igual_que_anterior(anterior):
    while True:
        nuevo_numero = int(input(f"(Tiene que ser mayor que {anterior}): "))
        if nuevo_numero > anterior:
            return nuevo_numero
        else:
            print("El número ingresado es menor o igual que el anterior. Por favor, ingresa un número válido.")

def main():
    print("Ejemplos de listas:")
    print("1, 3, 5, 7, 9, 11, 13, 15, 17, 19")
    print("2, 4, 6, 8, 10, 12, 14, 16, 18, 20")
    print()

    longitud = int(input("Ingresa la longitud de la lista: "))
    lista = []

    for i in range(longitud):
        if i == 0:
            elemento = int(input(">>> Elemento 1: "))
        else:
            print(f">>> Elemento {i+1}")
            elemento = ingresar_numero_mayor_o_igual_que_anterior(lista[-1])
        lista.append(elemento)

    print()
    print(f"La lista de componentes es: {lista}")
    print()
    
    componente_buscado = int(input("Ingresa el componente que deseas buscar: "))

    busqueda = Busqueda(lista, componente_buscado)
    resultado = busqueda.buscar_posicion_en_tabla()

    if resultado is not None:
        print(f"El componente {componente_buscado} se encuentra en la posición {resultado}.")
    else:
        print(f"El componente {componente_buscado} no se encuentra en la lista.")

if __name__ == "__main__":
    main()


    



