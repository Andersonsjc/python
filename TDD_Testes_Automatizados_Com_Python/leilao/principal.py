from dominio import Leilao, Usuario, Lance, Avaliador

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_de_yuri = Lance(yuri, 100.00)
lance_de_gui = Lance(gui, 150.00)

leilao = Leilao("Celular")

leilao.lances.append(lance_de_yuri)
leilao.lances.append(lance_de_gui)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance no valor de {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
