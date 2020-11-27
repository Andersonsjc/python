# -*- coding: latin-1 -*-
import re

resultado = re.match('Py','Python')
print(resultado.group())
['Py']

#Nem sempre queremos levar em considera��o se o padr�o procurado est� em mai�scula ou min�scula, 
# como � o caso da pesquisa por perfis de outras redes sociais. Nossa sorte � que podemos definir uma faixa de caracteres 
# e assim podemos dizer que estamos procurando por p ou P. Vamos testar isso e criar um grupo na express�o regular usando colchetes [..]:
resultado = re.match('[pP]y','Python')
print(resultado.group())
['Py']

resultado = re.match('[pP]y','python')
print(resultado.group())
['py']

#E se a quisermos achar todas as s�labas que come�am com qualquer letra seguida de y? 
# Basta alterar a nossa faixa e deix�-la mais gen�rica. Podemos definir todas as caracteres de A at� Z pela express�o:
resultado = re.match('[A-Za-z]y','Python')
print(resultado.group())
['Py']

#Ah, mas s� temos uma palavra em nossa string, que tal adicionar mais uma e verificar se encontramos nosso padr�o nas duas palavras?
resultado = re.match('[A-Za-z]y','Python ou jython')
print(resultado.group())
['Py']

#Estamos procurando a express�o [A-Za-z]y dentro do texto Python ou jython. As palavras 'Python' e 'jython' atendem nosso crit�rio, 
# no entanto, s� recebemos o Py como resposta. O problema � que a fun��o match() s� encontrou a primeira ocorr�ncia, 
# parando logo em seguida. Nesse exemplo queremos achar Py E jy.
#A fun��o findall()
#Podemos utilizar no lugar da fun��o match() a fun��o findall(), que devolve uma lista de resultados:
resultados = re.findall('([A-Za-z]y)','Python ou jython')
print(resultados)
['Py','jy']
#Repare que ela retorna uma lista com os padr�es encontrados. Diferente da fun��o match() que retornava um objeto.

#Meta caracteres
#Perfeito, mas agora queremos a palavra completa como retorno. Queremos todas as palavras que come�am com express�o [A-Za-z]y. 
# O truque � definirmos uma faixa ainda maior de caracteres, indicado pelo operador +. Este operador significa um ou mais caracteres. 
# Vamos adicionar a express�o [A-Za-z]+ ap�s a j� existente:
resultados = re.findall('([A-Za-z]y[A-Za-z]+)','Python ou jython ou PyPy')
print(resultados)

['Python', 'jython', 'PyPy']

#Caso queiramos buscar qualquer caractere, inclusive considerando n�meros, podemos usar [A-Za-z0-9] como faixa. 
# Por�m, por ser uma necessidade t�o comum, podemos optar pelo atalho \w. Reescrevendo a express�o:
resultados = re.findall('(\wy\w+)','Python ou jython ou PyPy')
print(resultados)
['Python', 'jython', 'PyPy']

#Novamente, o \w tamb�m incorpora n�meros. N�o acredita? Vamos alterar nossa string:
resultados = re.findall('(\wy\w+)','Python3 ou jython2 ou PyPy')
print(resultados)
['Python3', 'jython2', 'PyPy']

#Mas s� uma observa��o: \w n�o leva em considera��o acentos. Infelizmente devemos configurar esses caracteres separadamente, como por exemplo: \w|�|� (\w ou � ou �).
#Existem outros atalhos como o \d que identifica apenas n�meros ou \s para whitespaces como espa�o ou tabula��o. 
# No exemplo a seguir, procuraremos por qualquer palavra que contenha um y como segunda letra, mas agora com um n�mero no final:
resultados = re.findall('(\wy\w+\d)','Python3 ou jython2 ou PyPy')
print(resultados)
['Python3','jython2']

#Tamb�m poder�amos quantificar o n�mero no final. Caso o n�mero seja opcional podemos usar o operador ? 
# que significa zero ou um. Se quisermos zero ou mais n�meros no final podemos usar o asterisco *.
#Por exemplo, a express�o [A-Za-z]+\d? pega qualquer palavra com as letra de A-Z independente de minuscula ou mai�scula contendo opcionalmente um n�mero:
resultados = re.findall('[A-Za-z]+\d?','Python3 ou jython ou PyPy44')
print(resultados)
['Python3', 'ou', 'jython', 'ou', 'PyPy4']

#Raw String
#Repare que usamos muitos caracteres especiais para definir uma express�o regular. 
# Existem v�rios outros como o . (ponto) que indica qualquer caractere, ou () (par�nteses) para definir grupos de express�es. 
# Alguns dos caracteres possuem um significado especial dentro de uma string e pode ocorrer um conflito entre a defini��o da string e a express�o regular. 
# Ou seja, antes que o m�dulo re interprete a express�o a string j� fez uma altera��o da mesma!
#Para fugir desses problemas devemos usar uma string crua, ou em ingl�s raw string. Para definir uma raw string devemos prefixar a string com a letra r, por exemplo r'[A-Z]+'. 
# N�o confunda o r com regex, r significa raw. A partir de agora sempre vamos usar raw strings para declarar express�es regulares!
#Mais quantificadores
#Repare com os regex que vimos aqui j� podemos executar uma busca mais poderosa encontrarmos o nome de um perfil. 
# Tendo quatro nomes, por exemplo: 'Nico Flavio Fabiana Romulo', podemos facilmente buscar todos os nomes que come�am com a letra F:
resultados = re.findall('([fF]\w+)','Nico Flavio Fabiana Romulo')
print(resultados)
['Flavio', 'Fabiana']

#Vamos dificultar um pouco mais. Queremos buscar todos os nomes que come�am com uma determinada letra, mas devem ter uma quantidade m�nima de caracteres. 
# Digamos que todos os nomes que come�am com a letra F t�m pelo menos 6 caracteres! J� vimos os quantificadores como +,? e *, 
# mas existe uma forma exata de dizer quantos caracteres um resultado deveria ter. Para isso usaremos as {} (chaves). 
# Por exemplo, a express�o seguinte pega todos os nomes que come�am com F e possuem mais de 6 caracteres: r'[fF]\w{6}':
resultados = re.findall(r'[fF]\w{6}','Nico Flavio Fabiana Romulo')
print(resultados)
['Fabiana']

#Para buscar nomes entre 6 e 20 caracteres basta colocar: r'[fF]\w{6,20}'.
#Buscar no in�cio e fim da string
#Para terminar, veremos rapidamente como buscar algo pelo in�cio ou pelo fim da string. Quando usarmos as fun��es match() ou findall() vimos que elas 
# procuram alguma ocorr�ncia ou todas as ocorr�ncias da express�o em um texto. Isso nem sempre � suficiente.
#Por exemplo, quando realizamos leitura de um arquivos, muitas vezes queremos uma linha que comece com uma palavra ou s�mbolo especial. 
# Neste caso, faz sentido lermos linha a linha e verificarmos se a linha inicia com aquele s�mbolo ou n�o. N�o queremos saber se a linha cont�m a express�o, 
# e sim se ela come�a com a express�o.
#Com express�es regulares procuramos pelo in�cio atrav�s do caractere ^ (circunflexo). Por exemplo, para pegar um texto que come�a com # (tralha) usaremos a express�o r'^#'.
resultado = re.match(r'^#','#comentarios come�am com tralha')
resultado is None
False

#Analogamente podemos usar o caractere $ para buscar pelo final da string. Para saber se uma string termina com br podemos usar a express�o: r'.*br$'. 
# Repare o $ no final da express�o. br deve estar no final ($) e antes do br podem vir quaisquer caracteres, zero ou mais vezes (.*):
resultado = re.match(r'.*br$','http://alura.com.br')
print(resultado.group())
'http://alura.com.br'


#A resposta certa � r'(\w+\d$)'. Ou seja, qualquer word char (\w) um ou mais vez (+) seguindo pelo n�mero decimal (\d) no fim ($) da palavra!
resultados = re.findall(r'(\w+\d$)', 'rota66 88centavos Peer2Peer Python2')
print(resultados)
['Python2']

#Repare que recebemos apenas uma palavra como resposta j� que o char $ significa no final da string. 
# No entanto podemos definir um novo limite (boundary) para a express�o usando o \b inv�s de $:
resultados = re.findall(r'(\w+\d\b)', 'rota66 88centavos Peer2Peer Python2')
print(resultados)
['rota66', 'Python2']

#Agora procure n�meros no inicio da string atrav�s do char �:
resultados = re.findall(r'(^\d\w+)', '88centavos Peer2Peer Python2 99taxi')
print(resultados)
['88centavos']

#E tamb�m teste o \b:
resultados = re.findall(r'(\b\d\w+)', '88centavos Peer2Peer Python2 99taxi')
print(resultado)
