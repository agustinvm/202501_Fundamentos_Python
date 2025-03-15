class TarjetaCredito:
   tarjetas_creadas = []

   def __init__(self, limite_credito, intereses, saldo_pagar = 0, ):

        self.limite_credito = limite_credito
        self.intereses = intereses/100
        self.saldo_pagar = saldo_pagar
        TarjetaCredito.tarjetas_creadas.append(self)

   def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return(self)

   def pago(self, monto):
        self.saldo_pagar -= monto
        return(self)

   def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        return(self)

   def cobrar_interes(self):
        self.saldo_pagar += (self.saldo_pagar * self.intereses)
        return(self)
   
   @classmethod
   def mostrar_todo(cls):
       print("\n--- Información de todas las tarjetas ---")
       for tarjeta in cls.tarjetas_creadas:
           print(f"Limite: {tarjeta.limite_credito}, Saldo: {tarjeta.saldo_pagar}")
           
           
       

#Crea 3 tarjetas
uno = TarjetaCredito(1000, 1, 200)
dos = TarjetaCredito(2000, 1)
tres = TarjetaCredito(3000, 2, 1000)

#Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en
#una sola línea a través de la encadenación.

uno.compra(100).compra(200).pago(300).cobrar_interes().mostrar_info_tarjeta()


#Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta; todo esto 
# en una sola línea a través de la encadenación.
dos.compra(1000).compra(1000).pago(500).pago(500).cobrar_interes().mostrar_info_tarjeta()

#Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; 
#todo esto en una sola línea a través de la encadenación.
tres.compra(500).compra(500).compra(250).compra(250).compra(700).mostrar_info_tarjeta()

#BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas. 
#En el capítulo pasado te dimos algunas pistas de cómo realizarlo.
TarjetaCredito.mostrar_todo()