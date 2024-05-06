print("Hello World!")
#modo  de fazer comentarios por linha

"""
comentário 
em 
várias 
linhas
"""
#Operadores Mateáticos

print(2 + 2) #Soma
print(2 - 2) #Adição
print(2 * 2) #Multiplicação
print(2 / 2) #Divisão
print(10 % 3) #Resto da Divisão
print(2 ** 3) #Exponenciação


#Variáveis e Tipos de dados
#variáveis - são espaços na memoria que são guardadas para serem usadas
mensagem = 'Olá mundo'
print(mensagem)

Calc = 2 + 10 + (5 + 5)
print (Calc)

Calc = 2 + 10 + (5 + 5) / 2 + 5 - 6
print (Calc)

# podemos exibir a variável quantos vezes quiseremos

minha_variavel = 'Hello World'
print(minha_variavel)
print(minha_variavel)
print(minha_variavel)
print(minha_variavel)


#Tipos de Dados

""""
10 (int)
10.1 (float)
texto (String)
true/false (Booleana)
"""

var1 = 1 #Int
var2 = 1.1 #Float
var3 = "Eu sou uma string" #String
var4 = True #Bool

print(f"{var1}\n{var2}\n{var3}\n{var4}") #para printar uma a baixo da outra


#Operadores relacionais
"""
== Igual
!= Diferente
> Maior
< Menor
>= Maior ou igual
<= Menor ou igual
"""
x = 2
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 2
y = 3
soma = x + y
print(soma)


x = 2
y = 3
soma = x + y
print(soma > y)


#Operadores Lógicos

"""
AND - Duas condições seja verdadeiras 
OR- Pelo meno uma condição seja verdadeira
NOT - inverte o valor
"""
x = 2
y = 3
soma = x + y
print(x == y and x == soma)# Duas condições seja verdadeiras 

x = 3
y = 3
z = 3
print(x == y and x == z)# Duas condições seja verdadeiras 

x = 3
y = 3
z = 4
print(x == y or x == z) #Pelo meno uma condição seja verdadeira

#Estrutura Condicinal 
#if
#Elif
#Else


#if
a = 3
b = 5 

if a < b:
    print('OKAY A É MAIOR QUE B')

#Else é executado caso o if nao seja atendido
if a > b:
    print('OKAY A É MENOR QUE B')
else:
    print("A É MENOR QUE B")


#elif
a = 5
b = 5 
if a > b:
    print('OKAY A É MENOR QUE B')
elif a == b:
    print('A é igual a B')
else:
    print("A É MENOR QUE B")


#While (quer dizer, ENQUANTO)
#Enquanto uma condição não for verdadeira ou falsa ele se repete

x = 1
while x < 10:
    print(x)#se caso eu mande imprimir aqui, o looping será infinito pq enquanto xm for menor que 10 ele vai ficar imprimindo x
    x = x + 1 #para que isso não aconteça incrementamos + 1, acontecerá que em cada rodada x receberá mais 1


#comando for
#for percorre um conjunto de dados pre estabelecido

lista1 = [1,2,3,4,56]
lista2 = ['Olá','Mundo']
lista3 = [0,'Olá',1.90,False,]

for i in lista1: #como se lê = para cada execusão do laço for o valor i será atribuido a um dos elementos
    print(i)

#Comando range 
#me retornaa uma lista

for i in range (10):
    print(i)

#nesse caso abaixo ele imprimiu do 50 até o 110

for i in range (50, 110):
    print(i)

##nesse caso abaixo ele imprimiu  de 2 em 2

for i in range (10,22,2):
    print(i)


#comando Imput
#Esse coamdo recebe dados enviados pelo usuários

numero = input("Digite um Numero:24 ")
print(numero)

#Concatenação de Strings

a = "Diego"
b = "Douglas"
concatenar = a + " " + b
print(concatenar) 

a = "Diego"
b = "Douglas"
concatenar = a + " " + b
tamanho = len(concatenar) #a função len conta a string
print(tamanho) 

#Navegação pelo Indice

seq = "cgat gcac tagc tcac tata agtt acga"
letra = seq[1]
print(letra) #Ele retorna g pq o c vale zero

a = "Diego"
b = "Douglas"
concatenar = a + " " + b
print(concatenar[0:4]) #nesse caso ele imprimiu parte da palabra diego da posiçã0 ate 4

#Método na string

# primeiro metodo - alterar a caixa da string

a = "DIEGO"
b = "DOUGLAS"
concatenar = a + " " + b
print(concatenar.lower()) #lower colocou em minusculo


a = "diego@#"
b = "douglas  s"
concatenar = a + " " + b
print(concatenar.upper()) #lower colocou em mmaiusculo


a = "diego"
b = "douglas"
concatenar = a + " " + b + "\n"
print(concatenar.strip()) #lower colocou em mmaiusculo

#Listas
minha_lista1 = ['abacaxi','melancia','abacate']
minha_lista2 = [1,2,3,4,5]
minha_ista3 = ['abacate', 1, 9.0, False]
print(minha_lista1[2])

#Podemos navegar pelo elemento da lista usando um laço
minha_lista1 = ['abacaxi','melancia','abacate']
minha_lista2 = [1,2,3,4,5]
minha_ista3 = ['melao', 1, 9.0, False]

for item in minha_lista1:
    print(item)

    #tamanho da lista

    #Podemos navegar pelo elemento da lista usando um laço
minha_lista1 = ['abacaxi','melancia','abacate']
minha_lista2 = [1,2,3,4,5]
minha_ista3 = ['melao', 1, 9.0, False]

tamanho = len(minha_lista2)
print(tamanho)

#Adicionando elementos a lista
minha_lista1 = ['abacaxi','melancia','abacate']
minha_lista2 = [1,2,3,4,5]
minha_ista3 = ['melao', 1, 9.0, False]

minha_lista1.append("limao")
print(minha_lista1)

#sABER SE EXISTE UM OBJETO NA LISTA 

#Podemos navegar pelo elemento da lista usando um laço
minha_lista1 = ['abacaxi','melancia','abacate']
minha_lista2 = [1,2,3,4,5]
minha_ista3 = ['melao', 1, 9.0, False]
if 'melancia' in minha_lista1:
    print("Existe melancia na lista")

    #Remover objeto da lista 
    #Podemos navegar pelo elemento da lista usando um laço
minha_lista1 = ['abacaxi','melancia','abacate']
minha_lista2 = [1,2,3,4,5]
minha_ista3 = ['melao', 1, 9.0, False]
del minha_lista1 [1] #remover lista inteira ou parte [:]
print(minha_lista1)

#criar e preencher mova lista
#Podemos navegar pelo elemento da lista usando um laço
minha_lista1 = ['abacaxi','melancia','abacate']
minha_lista2 = [1,2,3,4,5]
minha_ista3 = ['melao', 1, 9.0, False]

minha_lista_4 = []
minha_lista_4.append(59)
print(minha_lista_4)

#Ordenar listas
#podendo ser alfabeticamente tambem
lista = [182,22,212,2121,1,232,43,32,112,34,4,0]
lista.sort()
print(lista)

#ORDENAR DE MANEIRA DECRESCENTE
lista = [182,22,212,2121,1,232,43,32,112,34,4,0]
lista.sort(reverse=True)
print(lista)

#inverter a lista
lista = [182,22,212,2121,1,232,43,32,112,34,4,0]
lista.reverse()
print(lista)

#Dicionario
meu_dicionario = {"A":"Ameixa", "B":"Melancia", "C":"Abacate"}
print(meu_dicionario["A"])

#Navegar pelo Dicionario
meu_dicionario = {"A":"Ameixa", "B":"Melancia", "C":"Abacate"}
for chave in meu_dicionario:
    print(chave)


meu_dicionario = {"A":"Ameixa", "B":"Melancia", "C":"Abacate"}
for chave in meu_dicionario:
    print(meu_dicionario[chave])

#nesse caso o dicionario foi convertido em uma tupla (CONJUNTO DE DADOS IMUTAVEIS)
meu_dicionario = {"A":"Ameixa", "B":"Melancia", "C":"Abacate"}
for i in meu_dicionario.items():
    print(i)


meu_dicionario = {"A":"Ameixa", "B":"Melancia", "C":"Abacate"}
for i in meu_dicionario.values(): #RETORNANDO SO OS VALORES
    print(i)


#MANIPULAÇÃO DE ARQUIVO
"""
r = somente leitura
w = escrita (caso o arquivo ja exista ele será apagado e um novo arquivo vazio será criado)
a = leitura e escrita (adiciona o novo conteudo ao fim doa arquivo)
"""
#read()   lê o arquivo inteiro
#readline() Lê uma linha 
 #readlines() Lê arquivo e o armazena em uma linha

 #PARA ABRIR UM ARQUIVO
arquivo = open("arquivo.txt")
linhas = arquivo.readlines()
print(linhas)

 #FUNÇÃO REDLINES
arquivo = open("arquivo.txt")
linhas = arquivo.readlines()
print(linhas)

#linprimindo todas as linhas
arquivo = open("arquivo.txt")
linhas = arquivo.readlines()
for linha in linhas:
    print(linha)


#Abrindo todo o arquivo
arquivo = open("arquivo.txt")
texto_completo = arquivo.read()
print(texto_completo)

#Criando arquivo

criando_arquivo = open("arquivo2.txt", "w")

#Gravando informação no arquivo
criando_arquivo.write("ISSO NAO E UMA CONSPIRACAO")

#Toda vex que abrir um arquivo tem que fechar para salvar
criando_arquivo.close()