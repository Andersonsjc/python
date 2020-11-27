class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} para o titilar {}.".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= (valor_disponivel_a_sacar)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor) 
    
    def get_titular(self):
        return self.__titular

    def set_titular(self, nome):
        self.__titular = nome
    
    def get_saldo(self):
        return self.__saldo

    # Get setter
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    # Metodos staticos
    @staticmethod
    def codigo_banco():
        return "002"

    @staticmethod
    def codigo_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

'''
    >>> from conta import Conta
    >>> conta = Conta(123, "Nico", 55.5, 1000.0)
    Construindo objeto ... <conta.Conta object at 0x7fc4ed132048>
    >>> conta2 = Conta(321, "Marcos", 100.0, 1000.0)
    Construindo objeto ... <conta.Conta object at 0x7fc4ed1324a8>
    >>> conta.titular
    'Nico'
    >>> conta2.titular
    'Marcos'
    >>> conta.deposita(100)
    >>> conta.extrato()
    Saldo de 155.5 para o titilar Nico.
    >>> conta.saca(5)
    >>> conta.extrato()
    Saldo de 150.5 para o titilar Nico.
'''
