class Palindromo:
    tildes_dic = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"}

    def __init__(self, texto):
        self.texto = texto

    def texto_filtrado(self, tildes=tildes_dic):
        texto_alfanum = "".join(caracter for caracter in self.texto if caracter.isalnum())
        texto_sin_tildes = ''.join(tildes.get(caracter, caracter) for caracter in texto_alfanum)
        texto_final = texto_sin_tildes.lower()
        self.texto_final = texto_final
        return self.texto_final

    def comprobar_texto(self, tildes=tildes_dic):
        return self.texto_filtrado(tildes) == self.texto_filtrado(tildes)[::-1]

def main():
    # Ejemplos de frases palindrómicas
    frases_ejemplo = [
        "Dábale arroz a la zorra el abad",
        "Logré ver gol",
        "Salas",
        "1754571",
        "10000000000000000001",
        "Oso"
    ]

    # Mostrar ejemplos
    print("Ejemplos de frases palindrómicas:")
    for frase in frases_ejemplo:
        pal = Palindromo(frase)
        print(f"Texto original: {pal.texto}")
        print(f"Texto filtrado: {pal.texto_filtrado()}")
        print(f"¿Es un palíndromo?: {pal.comprobar_texto()}")
        print()

    # Pedir entrada al usuario
    print("Ahora, ingresa tu propia palabra o frase para verificar si es un palíndromo:")
    entrada_usuario = input("> ")

    # Verificar si la entrada del usuario es un palíndromo
    palabra_usuario = Palindromo(entrada_usuario)
    print(f"Texto original: {palabra_usuario.texto}")
    print(f"Texto filtrado: {palabra_usuario.texto_filtrado()}")
    print(f"¿Es un palíndromo?: {palabra_usuario.comprobar_texto()}")

if __name__ == "__main__":
    main()
