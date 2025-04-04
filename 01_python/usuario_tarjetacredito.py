from tarjetacredito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email, tarjeta):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = tarjeta 

    def hacer_compra(self, monto):
        self.tarjeta.compra(monto)
        return self

    def pagar_tarjeta(self, monto):
        self.tarjeta.pago(monto)
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a pagar: ${self.tarjeta.saldo_pagar}")
        return self





###Bonus
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = []  

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)

    def hacer_compra(self, monto, tarjeta):
        if tarjeta in self.tarjetas:
            tarjeta.compra(monto)
        else:
            print("Tarjeta no asociada al usuario.")
        return self

    def pagar_tarjeta(self, monto, tarjeta):
        if tarjeta in self.tarjetas:
            tarjeta.pago(monto)
        else:
            print("Tarjeta no asociada al usuario.")
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}")
        for i, tarjeta in enumerate(self.tarjetas, 1):
            print(f"Tarjeta {i}: Saldo a pagar ${tarjeta.saldo_pagar}")
        return self


#Ejemplo
usuario1 = Usuario("Agustin", "Valenzuela", "agustin@gmail.com")
usuario2 = Usuario("Ivanna", "Loiza", "maria@gmail.com")

#Creacion de tarjetas
tarjeta1 = TarjetaCredito(5000, 1, 1000)
tarjeta2 = TarjetaCredito(8000, 1, 2000)
tarjeta3 = TarjetaCredito(6000, 1, 1500)


#Asignar tarjetas a usuarios
usuario1.agregar_tarjeta(tarjeta1)
usuario1.agregar_tarjeta(tarjeta2)
usuario2.agregar_tarjeta(tarjeta3)

#Probar
usuario1.hacer_compra(500, tarjeta1)
usuario1.pagar_tarjeta(200, tarjeta1)
usuario2.hacer_compra(700, tarjeta3)

#
usuario1.mostrar_saldo_usuario()
usuario2.mostrar_saldo_usuario()

