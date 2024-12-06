class ContaBancaria:


    def __init__(self,titular,saldo,limite):
        
        self.titular=str(titular)
        self.saldo=float(saldo)
        self.limite=float(limite)
      

    def depositar(self,value):
        if value> 0:
            self.saldo=self.saldo+value
            print("1")
        else:
            print("0")
       
        
    def levantar(self,value):
        if value <= self.saldo + self.limite:
            self.saldo=self.saldo-value
            print("1")
        else:
            print("0")
        
    def exibir_saldo(self):
        print("{:.2f}".format(self.saldo))

    def exibir_info(self):
        print(f"[{self.titular}] [{self.saldo:.2f}] [{self.limite:.2f}]")



conta = ContaBancaria("João", 1000.00, 500.00)

conta.depositar(-500.00)
conta.depositar(500.00)
conta.levantar(1200.00)
conta.levantar(1200.00)
conta.exibir_info()