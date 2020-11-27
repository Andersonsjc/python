# -*- coding: latin-1 -*-
class Perfil():
    'Classe para moldar perfis de usuarios'
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprime(self):
        print('nome: {} telefone: {} empresa: {}'.format(self.nome, self.telefone, self.empresa))

class Data(object):
   def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano

   #def imprime(self):
      #print '%s/%s/%s' % (self.dia, self.mes, self.ano)


class Imc(object):
   def __init__(self, peso, altura):
      self.peso = peso
      self.altura = altura

   #def imprime(self):
   #   imc = self.peso / (self.altura * self.altura) 
   #   print '%s' % (imc)
   def imprime(self):
      imc = self.peso / (self.altura * self.altura) 
      print (f'{imc}')

peso = Imc(100,2)

peso.imprime()

'''

perfil1 = Perfil('Flavio', 'nao informado', 'Caelum')

perfil2 = Perfil('Steve', '2121-2121', 'Minecraft')
perfil3 = Perfil('Peter', '3333-4444', 'Minecraft')

perfil1.imprime()
perfil2.imprime()

outro = perfil1

outro.imprime()


perfil4 = Perfil(empresa='Caelum', telefone='não informado', nome='Fulaninho Ciclano')
perfil4.imprime()
'''
