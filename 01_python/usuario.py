
class Usuario:

    def __init__(self, nombre, apellido, email):

       self.nombre = nombre

       self.apellido = apellido

       self.email = email

       self.limite_credito = 30000

       self.saldo_pagar = 0

  
    def hacer_compra(self, monto): 
       self.saldo_pagar += monto  
       return(self)

#pagar_tarjeta(self, monto): crea un método que pague un monto de la tarjeta de crédito, haciendo que se reduzca el saldo_pagar   
    def pagar_tarjeta(self, pago):
       self.saldo_pagar -= pago
       return(self)

#mostrar_saldo_usuario(self): crea un método que imprima el nombre completo del usuario y el saldo a pagar de su tarjeta
# .Ejemplo: “Usuario: Nariyoshi Miyagi, Saldo a Pagar: $50”
    def mostrar_saldo_usuario(self):
       print(f"Usuario: {self.nombre} {self.apellido}, Saldo a pagar {self.saldo_pagar}")
       return(self)

#BONUS: transferir_deuda(self, otro_usuario, monto): crea un método que reduzca la deuda (saldo_pagar) del usuario por el monto,
#y agrega esa cantidad al saldo_pagar de otro_usuario
    def transferir_deuda(self, otro_usuario, monto):
       self.saldo_pagar -= monto
       otro_usuario.saldo_pagar += monto
       print(f"Se transfirió ${monto} de deuda a {otro_usuario.nombre}.")
       return(self)

ivanna = Usuario("Ivanna", "Valenzuela", "iva@gmail.com")
maite = Usuario("Maite", "Valenzuela", "maite@gmail.com")

ivanna.hacer_compra(2000).pagar_tarjeta(1000).mostrar_saldo_usuario()
ivanna.transferir_deuda(maite, 1000)
maite.mostrar_saldo_usuario()






############ METODO DE CLASE 
class TarjetaCredito:

   #Atributos de clase

   banco = "Banco Internacional de Programadores"

   #Agregamos un atributo de clase que guarda todas las tarjetas de crédito

   todas_las_tarjetas = []

   def __init__(self, limite_credito, saldo_pagar):

       #Esteblecemos los atributos de instancia

       self.limite_credito = limite_credito

       self.saldo_pagar = saldo_pagar

       #Cada que se cree una nueva instancia de la clase, se agrega a todas_las_tarjetas

       TarjetaCredito.todas_las_tarjetas.append(self)

   #Método de clase que cambia el banco

   @classmethod

   def cambiar_banco(cls, nombre):

       cls.banco = nombre

