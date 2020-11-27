class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def like(self):
        return self._like

    def dar_likes(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    #def imprime(self):
    #    print(f'Nome: {self._nome} - Ano: {self.ano} - Like: {self._like}')
    #Ao inves de usar imprime(), usar a representacao textual
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Like: {self._like}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    #def imprime(self):
    #    print(f'Nome: {self.nome} - Detalhe: {self.duracao} min - Ano: {self.ano} - Like: {self.like}')
    #Ao inves de usar imprime(), usar a representacao textual
    def __str__(self):
        return f'Nome: {self.nome} - Detalhe: {self.duracao} min - Ano: {self.ano} - Like: {self.like}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    #def imprime(self):
    #    print(f'Nome: {self.nome} - Detalhe: {self.temporadas} temporadas - Ano: {self.ano} - Like: {self.like}')
    #Ao inves de usar imprime(), usar a representacao textual
    def __str__(self):
        return f'Nome: {self.nome} - Detalhe: {self.temporadas} temporadas - Ano: {self.ano} - Like: {self.like}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

'''
#com heranca de list
class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)        
'''

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()


listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist)}')

'''
#Se fiser com heranca de list
for programa in minha_playlist:
    print(programa)
'''


#print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Like:{atlanta.like}')
#print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Like: {vingadores.like}')

#filmes_e_series = [vingadores, atlanta]

#for programa in filmes_e_series:
    #detalhe = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #print(f'Nome: {programa.nome} - Detalhes: {detalhe} - Ano: {programa.ano}')
    #programa.imprime()
    #print(programa)
