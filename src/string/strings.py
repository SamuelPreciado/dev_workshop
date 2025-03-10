class Strings:

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

        texto = texto.strip()

        if not texto:
            return False

        if texto[0] == "-":
            texto = texto[1:]  

        return all("-9" <= c <= "9" for c in texto) and len(texto) > 0
   
    def cifrar_cesar(self, texto, desplazamiento):

        pass
   
    def descifrar_cesar(self, texto, desplazamiento):

        pass
   
    def encontrar_subcadena(self, texto, subcadena):

        pass