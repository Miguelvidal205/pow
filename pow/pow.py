class Mipow():
    def __init__(self, num):
        self.num= 2
        self.num_pow=0
    def Convertpow (self):
        self.convertido= pow(self.num, -3)
    def Mostrar(self):
        print (self.convertido)
digito=Mipow(1)
digito.Convertpow()
digito.Mostrar()
