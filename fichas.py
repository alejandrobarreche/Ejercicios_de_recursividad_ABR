class OrdenadorFichas:
    def __init__(self, fichas):
        self.fichas = fichas
        self.fichas_rojas = 0
        self.fichas_azules = 0
        self.fichas_verdes = 0
        self.contar_fichas()

    def contar_fichas(self):
        self.lista_fichas_distintas = []
        for ficha in self.fichas:
            if ficha == "roja":
                self.fichas_rojas += 1
            elif ficha == "verde":
                self.fichas_verdes += 1
            elif ficha == "azul":
                self.fichas_azules += 1
            else:
                self.lista_fichas_distintas.append(ficha)

    def ordenar_fichas(self):
        self.fichas_ordenadas = []
        
        for i in range(self.fichas_rojas):
            self.fichas_ordenadas.append("roja")
            
        for i in range(self.fichas_verdes):
            self.fichas_ordenadas.append("verde")

        for ficha in self.lista_fichas_distintas:
            self.fichas_ordenadas.append(ficha)
            
        for i in range(self.fichas_azules):
            self.fichas_ordenadas.append("azul")

        return self.fichas_ordenadas

def ingresar_ficha_valida():
    while True:
        opcion = input("Ingresa el número correspondiente al color de la ficha (1: roja, 2: verde, 3: azul, 4: otro): ")
        if opcion == "1":
            return "roja"
        elif opcion == "2":
            return "verde"
        elif opcion == "3":
            return "azul"
        else:
            ficha = input("Ingresa otro color de ficha diferente a roja, verde y azul: ")
            return ficha.lower()

def main():
    print("Este programa ordena una lista de fichas según su color. El orden de ordenación será: \n1º Rojo\n2º Verde\n3º Otros colores\n4º Azul")
    print()

    longitud = int(input("Ingresa la longitud de la lista de fichas: "))
    fichas = []

    print("Ingresa los colores de las fichas:")
    for i in range(longitud):
        ficha = ingresar_ficha_valida()
        fichas.append(ficha)

    ordenador = OrdenadorFichas(fichas)
    fichas_ordenadas = ordenador.ordenar_fichas()
    
    print("Fichas ordenadas:", fichas_ordenadas)

if __name__ == "__main__":
    main()
