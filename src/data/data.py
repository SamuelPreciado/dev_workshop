class Data:
    
   
    def invertir_lista(self, lista):
        
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
   
    def buscar_elemento(self, lista, elemento):
       
        for i in range(len(lista)):  
            if lista[i] == elemento:  
                return i
        return -1
   
    def eliminar_duplicados(self, lista):

        lista_sin_duplicados = []
        vistos = []  
   
        for elemento in lista:
            if not any(elemento is v for v in vistos):  
                lista_sin_duplicados.append(elemento)
                vistos.append(elemento)
   
        return lista_sin_duplicados
   
    def merge_ordenado(self, lista1, lista2):

        i, j = 0, 0
        resultado = []

       
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1

        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado
   
    def rotar_lista(self, lista, k):

        if not lista:  
            return lista

        k = k % len(lista)  
        return lista[-k:] + lista[:-k]
   
    def encuentra_numero_faltante(self, lista):

        n = len(lista) + 1  
        suma_esperada = n * (n + 1) // 2  
        suma_actual = sum(lista)  
        return suma_esperada - suma_actual
   
    def es_subconjunto(self, conjunto1, conjunto2):

        for elemento in conjunto1:  
            if elemento not in conjunto2:  
                return False
        return True
   
    def implementar_pila(self):

        pila = []

        def push(elemento):
       
            pila.append(elemento)

        def pop():
            return pila.pop() if pila else None

        def peek():
       
            return pila[-1] if pila else None

        def is_empty():
       
            return len(pila) == 0

        return {
        "push": push,
        "pop": pop,
        "peek": peek,
        "is_empty": is_empty
        }
   
    def implementar_cola(self):

        cola = []

        def enqueue(elemento):
           
            cola.append(elemento)

        def dequeue():
       
            return cola.pop(0) if cola else None

        def peek():
       
            return cola[0] if cola else None

        def is_empty():
       
            return len(cola) == 0

        return {
        "enqueue": enqueue,
        "dequeue": dequeue,
        "peek": peek,
        "is_empty": is_empty
        }
   
    def matriz_transpuesta(self, matriz):

        if not matriz or not matriz[0]:  
            return []

        return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]