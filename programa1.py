class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        print(self.elementos)


def sumar_colas(cola_a, cola_b):
    resultado = Cola()

    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        numero_a = cola_a.desencolar()
        numero_b = cola_b.desencolar()
        resultado.encolar(numero_a + numero_b)

    return resultado


# Crear las dos colas
cola_a = Cola()
cola_b = Cola()

# Agregar los números de la Cola A
for numero in [3, 4, 2, 8, 12]:
    cola_a.encolar(numero)
# Agregar los números de la Cola B
for numero in [6, 2, 9, 11, 3]:
    cola_b.encolar(numero)

# Sumar las dos colas
resultado = sumar_colas(cola_a, cola_b)

# Mostrar el resultado
print("Cola resultado:")
resultado.mostrar()