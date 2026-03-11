# Clase padre (superclase)
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario # protegido con guion bajo

    def calcular_pago(self):
        return self._salario

    def __str__(self):
        return f"Empleado: {self.nombre}"

# Clase hija 1 (hereda de empleado)
class Jefe(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario) # Llama al __init__ del padre
        self.bono = bono

    def calcular_pago(self):
        return self._salario + self.bono # Polimorfismo (cambiamos el comportamiento)

    def __str__(self):
        return f"Jefe: {self.nombre}"

# Prueba del sistema
if __name__ == '__main__':
    emp1 = Empleado("Luis", 1000)
    jefe1 = Jefe("Marta", 2000, 500)

    for persona in [emp1, jefe1]:
        print(f"{persona} -> Pago final: ${persona.calcular_pago()}")
