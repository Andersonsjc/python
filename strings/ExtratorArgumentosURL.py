class ExtratorArgumentoURL:
    def __init__(self,url):
        if self.stringEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url invalida")

    @staticmethod
    def stringEhValida(url):
        if url:
            return True
        else:
            return False

    def __str__(self):
        moedaOrigem,moedaDestino = self.extraiArgumentos()
        representacaoString2 = "Valor:" + self.extraiValor() + " " + moedaOrigem + " " + moedaDestino
        representacaoString  = "Valor: {}\n Moeda Origem: {} \n Moeda Destino: {} \n".format(self.extraiValor(),moedaOrigem,moedaDestino)
        return representacaoString

    def __str__(self):
        moedaOrigem,moedaDestino = self.extraiArgumentos()
        representacaoString2 = "Valor:" + self.extraiValor() + " " + moedaOrigem + " " + moedaDestino
        representacaoString  = "Valor: {}\n Moeda Origem: {} \n Moeda Destino: {} \n".format(self.extraiValor(),moedaOrigem,moedaDestino)
        return representacaoString

    def __eq__(self,outraInstancia):
      return self.url == outraInstancia.url

    def retornaMoedas(self):
        buscaMoedaOrigem = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]

        inicioSubstringMoedaDestino = self.encontraIndiceInicioSubstring(buscaMoedaDestino)
        finalSubstringMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[inicioSubstringMoedaDestino:finalSubstringMoedaDestino]

        if moedaOrigem == "moedadestino":
            moedaOrigem = self.verificaMoedaOrigem(buscaMoedaOrigem)
        return moedaOrigem, moedaDestino
       
    def encontraIndiceInicioSubstring(self, moedaOuValor):
        return self.url.find(moedaOuValor) + len(moedaOuValor) + 1

    def verificaMoedaOrigem(self, buscaMoedaOrigem):
        self.url = self.url.replace("moedadestino", "real", 1)  # primeiro vou fazer sem o 1 e depois vou usa-lo
        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        return self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]

    def retornaValor(self):
        buscaValor = "Valor".lower()
        inicioSubstringValor = self.encontraIndiceInicioSubstring(buscaValor)
        valor = self.url[inicioSubstringValor:]
        return valor

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino=","real",1)
        print(self.url)

    def extraiValor(self):
        buscaValor = "Valor="
        indeceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indeceInicialValor:]
