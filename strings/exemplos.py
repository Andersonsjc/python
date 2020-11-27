'''
texto = "Izuku Midoriya"
texto[0:10]
texto2 = texto[:4]
print( texto2)
print(texto)
'''

'''
celular = "(41)96574-1728"
indiceInicialCodigoArea = celular.find("(") + 1
indiceFinalCodigoArea   = celular.find(")")

print (celular[indiceInicialCodigoArea:indiceFinalCodigoArea])
'''

'''
#www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar
url = "pagina?argumentos"
indice = url.find("?")
print(url[indice + 1:] )
'''

'''
episodio = "Boku no hero - TEmporada 1, episodio 12"
episodioFormatado = episodio\
.lower()\
.replace("episodio ","ep")\
.upper()\
.replace("temporada ", "s")

print(episodioFormatado)
'''

#expressao regular
import re

#padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
#E possivel simplificar a representacao do padrao utilizando intervalos de caracteres
#padrao = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"
#Podemos simplificar ainda mais utilizando quantificadores para os intervalos.
#padrao = "[0-9]{4}[-][0-9]{4}"
#Para deixar nosso padrao mais simples podemos retirar [-] e deixar somente -, pois essa e a unica opcao para essa posicao.
#padrao = "[0-9]{4}-[0-9]{4}"
#Agora caso o numero de telefone seja de um celular e possua um 9 na frente do numero? Podemos dar opcoes para os quantificadores.
#padrao = "[0-9]{4,5}-[0-9]{4}"
#Mas e se quisermos que o - seja opcional dentro da expressao regular? Uma forma de fazer isso e utilizando o operador ?
padrao = "[0-9]{4,5}-?[0-9]{4}"

# Vamos testar esse padrao.
texto =  "Meu numero para contato e 2633-5723"
retorno = re.search(padrao,texto)
print(retorno.group())
