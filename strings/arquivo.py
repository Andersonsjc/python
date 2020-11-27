from ExtratorArgumentosURL import ExtratorArgumentoURL

url ="https://www.bytebank.com.br/cambio?moedaorigem=real&moedadesino=dolar&valor=150"
cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)

#Aqui ta tudo bem, teste agora o caso em que "moedaorigem=moedadestino".
url ="https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadesino=dolar&valor=150"
cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)
