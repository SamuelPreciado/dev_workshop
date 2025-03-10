class Magic:

    def fibonacci(self, n):

        if n < 0:
            raise ValueError("n debe ser un número entero no negativo")
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
   
        return b
   
    def secuencia_fibonacci(self, n):

        if n < 0:
            raise ValueError("n debe ser un número entero no negativo")
        elif n == 0:
            return []
        elif n == 1:
            return [0]
   
        fibonacci = [0, 1]  
        for _ in range(2, n):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
   
        return fibonacci
   
    def es_primo(self, n):

        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
   
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
   
        return True
   
    def generar_primos(self, n):

        if n < 2:
            return []
   
        primos = [True] * (n + 1)  
        primos[0] = primos[1] = False  

        for i in range(2, int(n ** 0.5) + 1):
            if primos[i]:
                for j in range(i * i, n + 1, i):  
                    primos[j] = False

        return [i for i in range(n + 1) if primos[i]]
   
    def es_numero_perfecto(self, n):

        if n < 2:
            return False
   
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
   
        return suma_divisores == n
   
    def triangulo_pascal(self, filas):

        if filas <= 0:
            return []

        triangulo = [[1]]  

        for i in range(1, filas):
            fila_anterior = triangulo[-1]  
            nueva_fila = [1]

            for j in range(1, len(fila_anterior)):
                nueva_fila.append(fila_anterior[j - 1] + fila_anterior[j])  
            nueva_fila.append(1)  
            triangulo.append(nueva_fila)

        return triangulo
   
    def factorial(self, n):

        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
   
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
   
        return resultado
   
    def mcd(self, a, b):

        while b:
            a, b = b, a % b
        return abs(a)
   
    def mcm(self, a, b):

        def mcd(x, y):
            while y:
                x, y = y, x % y
            return abs(x)
   
        return abs(a * b) // mcd(a, b) if a and b else 0
   
    def suma_digitos(self, n):

        return sum(int(d) for d in str(abs(n)))
   
    def es_numero_armstrong(self, n):

        num_str = str(n)  
        num_digitos = len(num_str)  
        suma_potencias = sum(int(d)**num_digitos for d in num_str)  
        return suma_potencias == n
   
    def es_cuadrado_magico(self, matriz):

        if not matriz or any(len(fila) != len(matriz) for fila in matriz):
            return False  

        n = len(matriz)
        suma_referencia = sum(matriz[0])  

       
        for fila in matriz:
            if sum(fila) != suma_referencia:
                return False

       
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_referencia:
                return False


        if sum(matriz[i][i] for i in range(n)) != suma_referencia:
            return False

       
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_referencia:
            return False

        return True