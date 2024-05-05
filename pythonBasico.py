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