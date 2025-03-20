class Strings:
    #hola
    def es_palindromo(self, texto):

        palabra="".join(texto.lower().split(" "))
   
        return palabra==palabra[::-1]
   
    def invertir_cadena(self, texto):

        resultado = ""
        for caracter in texto:
            resultado = caracter + resultado  
        return resultado
   
    def contar_vocales(self, texto):

        vocales = "aeiouAEIOU"
        contador = 0
   
        for caracter in texto:
            if caracter in vocales:
                contador += 1
           
        return contador
   
    def contar_consonantes(self, texto):

        vocales = "aeiouyAEIOUY"
        contador = 0
   
        for caracter in texto:
            if caracter not in vocales:
                contador += 1
           
        return contador
   
    def es_anagrama(self, texto1, texto2):

        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
   
    def contar_palabras(self, texto):

        return len(texto.split())
   
    def palabras_mayus(self, texto):

        return texto.title()
   
    def eliminar_espacios_duplicados(self, texto):

        return " ".join(texto.split())
       
   
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] in ('-', '+'):
            texto = texto[1:]
        return all(c in '0123456789' for c in texto) and bool(texto)
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                inicio = ord('A') if char.isupper() else ord('a')
                resultado += chr(inicio + (ord(char) - inicio + desplazamiento) % 26)
            else:
                resultado += char
        return resultado
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        len_sub = len(subcadena)
        for i in range(len(texto) - len_sub + 1):
            if texto[i:i + len_sub] == subcadena:
                posiciones.append(i)
        return posiciones
        pass