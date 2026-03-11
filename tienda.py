class Producto:
    def __init__(self,  nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return self.precio*cantidad
        else:
            print(f"[!] No hay suficiente stock de {self.nombre}.")
            return 0

class Usuario:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

laptop = Producto("Laptop Gamer", 1500, 5)
cliente = Usuario("Ana", 2000)

costo = laptop.vender(1)
if cliente.saldo >= costo and costo > 0:
    cliente.saldo -= costo
    print(f"{cliente.nombre} compró {laptop.nombre}. Saldo restante: ${cliente.saldo}")
