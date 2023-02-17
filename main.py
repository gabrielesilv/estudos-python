'''
CURSO UDEMY
Autora: Gabriele
Data: 04/01/2023
Versão do código: 1.0
'''

print("Olá")
print('Tudo bem?')
print('Que dia é hoje?')

print()

# VARIÁVEIS (str, integer, float, bool) - sempre em minúsculo

'''
 1 - integer
 "texto" - string
 2.0 - float ou double
 ["Ola1", "Ola2"] - array de String
 Verdadeiro/Falso - verdadeiro/falso
'''

# a variável poderá ser mudada a qualquer momento, será atualizado no console.
# variável = dado

x = 2.5
print(x + x)

y = 'olá'
print(y)

z = 5
print(z - z)


print()

'''
MUDANÇA DE DADOS
- transformando integer em string, para que o python entenda o número como um texto
'''

a = str(3)
# quando somado (a+a), o python entenderá como um texto = (a+a = 33, texto 3 + texto 3)
b = int(4)
c = float(5)

print(a)
print(b)
print(c)

print(a + a)
print(b + b)
print(c + c)

print() #--------------------------------------------------------------------------------------------------------------------------------------------------


'''
Ex 1: A Gabi tem 20 anos de idade e mora na cidade de São Paulo.
- Variáveis: nome, idade e cidade
'''
nome = 'Gabi'
idade = 20
cidade = 'São Paulo'

print(' A ' + nome + ' tem ' + str(idade) + ' anos de idade e mora em ' + cidade + '.')
# o python não entende str e integer em um mesmo print, tendo que colocar o tipo de dado à frente da variável: ex. str(idade)
# espaços entre as aspas e o texto para que o print não saia sem espaçamento

print() #--------------------------------------------------------------------------------------------------------------------------------------------------

'''
Ex 2: Fui à feira paulista e comprei 12 bananas
- Variáveis: lugar, quantidade e fruta
'''

lugar = 'feira paulista'
quantidade = 12
quantidade = str(quantidade)
fruta = 'bananas'

print(' Fui à ' + lugar + ' comprar ' + str(quantidade) + fruta + '.')

print() #--------------------------------------------------------------------------------------------------------------------------------------------------

'''
Ex 3: Ela comprou 10 bolachas para a Maria e o valor foi de 26 reais.
- Variáveis: quantidade, nome e valor
'''

quantidade = 10
quantidade = str(quantidade)
nome = 'Maria'
valor = 26
valor = str(valor)

print(' Ela comprou ' + quantidade + ' bolachas para a ' + nome + ' e o valor foi de ' + valor + ' reais. ')

print() #--------------------------------------------------------------------------------------------------------------------------------------------------

'''
Ex 4: Hoje é dia 9 de Janeiro de 2023 e são 19 horas.
- Variáveis: data, mês, ano e hora
'''

data = 9
mes = 'Janeiro'
ano = 2023
hora = 19

print(' Hoje é dia ' + str(data) + ' de ' + mes + ' de ' + str(ano) + ' e são ' + str(hora) + ' horas. ')

print() #--------------------------------------------------------------------------------------------------------------------------------------------------



# Interação com o usuário: INPUT
# A Gabi tem 20 anos de idade e mora na cidade de São Paulo.

'''
nome = input('Qual é o seu nome: ')
# a tag input permite interação com usuário
idade = input('Qual é a sua idade: ')
idade = str(idade)
cidade = input('Onde você mora?')

print(' A ' + nome + ' tem ' + idade + ' anos de idade e mora em ' + cidade + '.')

    Ex:
Qual é o seu nome: Larissa
Qual é a sua idade: 29
Onde você mora? Salvador
A Larissa tem 29 anos de idade e mora em Salvador.
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
lugar = input('Onde você foi: ')
quantidade = 12
quantidade = str(quantidade)
fruta = input('O que você foi comprar na feira: ')

print(' Fui à ' + lugar + ' comprar ' + str(quantidade) + ' ' + fruta + '.')


    Ex 2:
Onde você foi: feira paulista
O que você foi comprar na feira: bananas
Fui à feira paulista comprar 12 bananas.
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
3# A Erenice tem 56 anos e gosta da cor amarelo

nome = input('Qual o seu nome? ')
idade = input('Quantos anos você tem? ')
idade = str(idade)
cor = input('Qual a sua cor favorita? ')

print(' A ' + nome + ' tem ' + idade + ' e gosta da cor ' + cor + '.')
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#CALCULANDO A IDADE COM INPUT 


# Qual minha idade em 2023:

ano_nascimento = 2002
idade = 2023 - ano_nascimento

print(idade)
# = 21

#TYPE: identifica o tipo de dado da variável:
'''ano_nascimento = input('Em que ano você nasceu? ')
print(type(ano_nascimento))

idade = 2023
print(type(idade))

#para calcular minha idade, meu str (input) precisa ser lido como integer:

idade = 2023 - int(ano_nascimento)
print(idade)
'''
'''
nascimento_ano = input('Em que ano nasceu a Erenice? ')
print(type(nascimento_ano))

age = 2023
print(type(age))

age = 2023 - int(nascimento_ano)
print(age)
'''


print() #---------------------------------------------------------------------------------------------------------------------------------------------------


# SLICE: corte do dado str da variável por meio do index
fruta = 'abacaxi'
#INDEX   0123456

print(fruta[6])
#index 6: i

print(fruta[2])
#index 2: a

'''
hardwere = 'mouse'
print(hardwere[2])
#index 2: u
'''

#para selecionar mais index, deve ser identificado do n0 index inicial:final, porém o último index selecionado nao é mostrado, voltando 1 index automaticamente

objeto = 'Tesoura'
print(objeto[1:4])
# foi impresso somente eso, ou seja, de 1:3

#também é possível usar número negativo, que irá contar os index de trás para frente. Ex. [-1] = a
print(objeto[-2])
#index -2: r


valor = 99.75
valor = str(valor) #NECESSÁRIO CONVERTER PARA STRING
print(valor[0:3])
print(valor[:2])
print(valor[3:])


print() #---------------------------------------------------------------------------------------------------------------------------------------------------


# FORMATED STRINGS

'''
facilita a leitura das strings (não é necessário converter números em string)
# A Gabriele Monteiro e uma excelente [desenvolvedora]
'''

nome = 'Gabriele'
sobrenome = 'Monteiro'
profissao = 'Desenvolvedora'

#impressão comum: texto = 'A' + nome + sobrenome + ' e uma excelente ' + '[' + profissao + ']'
#                 print(texto)

#uso de  formated string: abrir sempre com f e colocar as váriaveis entre chaves {}
text1 = f'A {nome} {sobrenome} e uma excelente [{profissao}]'
print(text1)

print()  #---------------------------------------------------------------------------------------------------------------------------------------------------

# O Gabriel Silva trabalha como (PROGRAMADOR)
nome = 'Gabriel'
sobrenome = ' Silva'
profissao = 'PROGRAMADOR'

text2 = f'O {nome} {sobrenome} trabalha como ({profissao})'
print(text2)

print() #---------------------------------------------------------------------------------------------------------------------------------------------------

# No ano de 2012 fui viajar em família para Porto Seguro de aviao e fiquei hospedada em um hotel por 1 semana

ano = 2012
quem_foi_viajar = 'família'
local = 'Porto Seguro'
meio_de_locomoção = 'aviao'
quanto_tempo = 1

text3 = f'No ano de {ano} fui viajar em {quem_foi_viajar} para {local} de {meio_de_locomoção} e fiquei hospedada em um hotel por {quanto_tempo} semana.'
print(text3)


print()  #---------------------------------------------------------------------------------------------------------------------------------------------------


# MÉTODOS PARA STRING
'''
lower: torna tudo minúsculo
upper: torna tudo maiúsculo
capitalize: torna o primeiro caractere da primeira string maiúsculo
title: torna o primeiro caractere de cada string maiúsculo
replace: substituição de letra(s) ou palavras '*' , '*'
strip: remove espaços
slice: corte da string
concatenação: juntar strings
list: cria uma nova lista com os caracteres em sequência para poder alterar um caractere sem criar uma nova variável
'''

# print(variável.método())
mensagem = 'Eu AMO comida caseira'
print(mensagem.lower()) 

#mensagem2 = input('Qual comida você mais gosta? ') 
#print(mensagem2.upper())

mensagem3 = 'hoje fui no mercado'
print(mensagem3.capitalize())

mensagem4 = 'Eu gosto de azul'
#index       01234567
print(mensagem4.find('g'))

mensagem5 = 'amanha vou ao cinema'
print(mensagem5.find('vou'))

mensagem6 = 'comprei uma maquiagem'
print(mensagem6.replace('e', 'u'))
print(mensagem6.replace('comprei', 'adquiri'))

mensagem7 = '    Hoje eu dancei'
print(mensagem7.strip())

mensagem8 = 'vou dormir'
print(mensagem8.title())


print()  #---------------------------------------------------------------------------------------------------------------------------------------------------


# OPERAÇÕES MATEMÁTICAS EM PYTHON

''' ORDEM
1 - parenteses
2 - exponenciais
3 - divisão e multiplicação (se tiver as 2 formas, é calculado da esq-dir)
4 - adição e subtração

'''

calculo = 2 + 2 * 3 /2
# 2*3 - 6/2 - 3+2 = 5
print(calculo)

# PARENTESES: dicionando parenteses para definir o primeiro cálculo (primeiro é eliminado os parenteses)
calculo2 = (2 + 2) * 2
# 2+2 - 4*2 = 8
print(calculo2) 

# VALORES EXPONENCIAIS: calculado logo após a eliminação dos parenteses


print() #---------------------------------------------------------------------------------------------------------------------------------------------------


''' OPERADORES DE COMPARAÇÃO (comparison operators)

== Equal
!= Not equal
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
'''

operadores = 2 == 2
print(operadores) #true

operadores2 = 'chá' != 'Chá'
print(operadores2) #true

operadores3 = 10 > 13
print(operadores3) #false

operadores4 = 22 < 30
print(operadores4) #true

operadores5 = 3 >= 4
print(operadores5) #false

operadores6 = 5 <= 5
print(operadores6) #true


print() #---------------------------------------------------------------------------------------------------------------------------------------------------


''' OPERADORES DE ATRIBUIÇÃO (assignment operators)

operação matemática + sinal de igual
'''
#ex
x = 10
x = x + 5       # =15 (forma comum)

x += 5          # =15 (forma simplificada)
x -= 5          # =5
x *= 5          # =50
x /= 5          # =2
x %= 3          # =1 (3 cabe 3 vezes no 10, sobrando 1)
x %= 2          # =0 (o 2 cabem 5 vezes no 10, sobrando 0)

y = 30
y /= 15
print(y)


print() #---------------------------------------------------------------------------------------------------------------------------------------------------


''' DECLARAÇÕES CONDICIONADAS (conditional statements)

if: se for maior que... - TRUE
else: senão; se o if não aconteceu, faça isso (ex. velocidade abaixo do permitido) - FALSE
else if = elif: se for menor que... (pode ser colocado várias vezes) 

indetation: recuo de 4 caracteres para o que estiver dentro das statementes
'''

velocidade = 59                                       #velocidade atual do motorista
if velocidade > 110:                                  #se a velocidade for maior que 110, avisar as seguintes infos (em indetation):
    print('Acima da velocidade permitida')
    print('Favor reduzi-la')
elif velocidade < 60:                                 #o elif avisará caso a velocidade estiver abaixo do mínimo - 80km/h
    print('Favor dirigir acima de 80km/h')
else:
    print('Velocidade permitida')                     #velocidade ok, pois está abaixo do permitido - 110km/h


grau_chapinha = 120
if grau_chapinha > 220:
    print('Seu cabelo será danificado, favor reduzir')
elif grau_chapinha < 80:
    print('É necessário aumentar os graus para ter melhor efeito')
else:
    print('A temperatuda da chapinha está ideal')


cor = 'laranja'
if cor == 'verde':
    print('SIGA')
elif cor == 'amarelo':
    print('ATENÇÃO')
else:
    print('PARE')                                     #se a cor não for verde ou amarelo, terá a informação PARE


idade = 20
if idade == 18:
    print('Pode dirigir')
elif idade < 18:
    print('Você é menor de idade')
else:
    print('Você é maior de idade')

idade2 = 62
if idade2 < 60:
    print('Você é adulto')
else:
    print('Você é idoso')

idade3 = 15
if idade3 < 12:
    print('criança')
elif idade3 < 18:
    print('adolescente')
elif idade3 < 60:
    print('adulto')
else:
    print('idoso')

#user = 'gmonteirot'
#if user == input('Digite o seu login: '):
#    print(f'Meu login é {user}')
#    print('Login correto')
#else:
#    print('Login incorreto')

print() #---------------------------------------------------------------------------------------------------------------------------------------------------


''' OPERADORES LÓGICOS (logical operators)
and - esse e esse
or - esse ou esse

and: todos tem que ser true para ser aprovado 
or: no mínimo um dos critérios tem que ser true para ser aprovado

Boolean Type (BOOL): true e false
'''

#ex. aprovação de financiamento de carro
#fatores: nome limpo e renda acima de 5.000

renda_acima_5mil = True
nome_limpo = False
if renda_acima_5mil and nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')                      #financiamento negado pois um dos critérios é false 

#estoque completo camiseta e tênis

estoque_camiseta = False
estoque_tenis = True

if estoque_camiseta or estoque_tenis:
    print('Estoque renovado')
else:
    print('Fazer encomenda')


print() #---------------------------------------------------------------------------------------------------------------------------------------------------


''' OPERADOR TERNÁRIO (ternary operator)
forma de economizar linhas com if, else statements

variável = 'texto print true' - if - variável - operador de comparação - 'dado da variável' - else - 'texto print false'
'''

age = 13
#if age >= 16:
#    resultado = print('Voto permitido')
#else:
#    resultado = print('Voto não permitido')

resultado = 'Voto permitido' if age >= 16 else 'Voto não permitido'
print(resultado)


senha = 124
senha = 'Senha correta' if senha == 123 else 'Senha incorreta'
print(senha)


#nick = 'gabizinha'
#nick = input('Digite seu nick: ')
#nick = 'Digite sua senha' if nick == 'gabizinha' else 'Nick incorreto'
#print(nick)


print() #---------------------------------------------------------------------------------------------------------------------------------------------------


''' MÚLTIPLOS OPERADORES DE COMPARAÇÃO (multiple comparison operator)
and, or, >, <=...
'''

valor = 15

#if valor >= 20 and valor < 40:                    #múltiplos operadores de comparação: >=, and, <
if 20 <= valor < 40:                               # < (maior que) variável < (menor que)
    print('O produto foi aceito')
else:
    print('Produto não aceito')


#ex. promoção de sabonete mínimo 15 unid e máximo 30
promocao = 15
#if promocao >= 15 and promocao < 30:
if 15 <= promocao < 30:
    print('Compra aceita')
else:
    print('Necessário maior quantidade')
   

soma_1 = 2 + 4
soma_2 = 2 + 1

if 10 <= soma_1 + soma_2:
    print('Soma maior que 10')
else:
    print('Soma menor que 10')


idade_lucas = 17
idade_carolina = 21

if 18 <= idade_lucas and idade_carolina:
    print('Lucas e Carolina são maiores de idade')
else:
    print('Um dos dois não é maior de idade')


print() #---------------------------------------------------------------------------------------------------------------------------------------------------


''' For Loop - looping (utilizando NÚMEROS)
for variável in range(limite):

- for = executa uma ação em um determinado número de vezes (looping)
- variável
- in = dentro de que
- range = quantidade de vezes que o for loop vai girar dentro de si mesmo valores de 0 a 9

é contado por index, ou seja, a partir do 0
'''

#imprimir de 0 a 5:
for numero in range(6):                     #0, 1, 2, 3, 4, 5 (start)
    print(numero)

print()
#imprimir de 1 a 5:
for numero in range(1, 6):                  #1, 2, 3, 4, 5 (start e stop)
    print(numero)

print()
#imprimir de 1 a 13 de 2 em 2:
for numero in range(0, 13, 2):              #1, 3, 5, 7, 9, 11, 13 (start, stop e step)
    print(numero)

print()
for loop in range(3, 99, 20):
    print(loop)

print()
for palavra in range(1, 4,):
    print(palavra)
    print('palavra')


print()
''' For Loop - Looping (utilizando STRINGS)
impressão de cada index da minha string
'''

for letra in 'Google':                      #associa a variável a cada index da string
    print(letra)

print()
palavras = 'texto'
for alfabeto in palavras:
    print(alfabeto + ' está dentro da palavra texto')

print()
comida = 'alimento'
for nutricao in comida:
    print(f'{nutricao} esta dentro da palavra {comida}')

print()
variavel = 'DADOS'
for armazenamento in variavel:
    print(f'a letra {armazenamento} contém na palavra {variavel}')


print()
''' 
For Loop (utilizando IF e ELSE)
'''

#Ex. Enviar um e-mail com os detalhes da compra online (máx. 3 tentativas) para compras confirmadas.
compra_confirmada = True
dados_compra = 'Compra confirmada no valor de R$ 12,50 e entrega autorizada'

for enviar in range(3):                     #imprima se for verdadeira na tentativa de 3x do cliente
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail')
        break                               #verifica se é true e interrompe o looping após imprimir o if 1x
else:
    print('Falha na compra')
        

#idade dos meus doguinhos (5 anos)
lola = 5
lorenzo = 3
for acerto in range(3):
    if lola and lorenzo == 5:
        print('Idade correta')
        break
    else:
        print('Idade incorreta')
        break


print()
'''
For Loop - Nasted loops (for loop dentro de outro for loop)

*outer loop
    *inner loop
'''

for numero1 in range(3):          #outer loop (looping de fora): gira 1 número a cada inner loop
    print(numero1)
    for numero2 in range(3):      #inner loop (looping de dentro): gira os 3 números a cada outer loop
        print(numero2)

print()
for produto in range(1,4):
    print('Produto ' + str(produto))
    for produto2 in range (3):
        print(produto, produto2)

print()
for roupa in range(1,4):
    print('Roupa ' + str(roupa))
    for roupa2 in range(1,4):
        print(roupa, roupa2)


print()
'''
For Loop - Separando strings
end='': finaliza quando o print finalizar (imprime cada index na mesma linha - "é um argumento da função print() que contém uma string a ser inserida ao final da linha")
'''

#Ex. alterar a palavra FANTASTICO para F A N T A S T I C O
palavra2 = 'FANTASTICO'
for spaco in palavra2:
    #abre com formated string, fecha e adiciona o comando end=''
    #print(spaco, end='')            #FANTASTICO
    print(f' {spaco}', end='')       #utilizado espaço após abrir a formated string para separar cada caractere = F A N T A S T I C O

print()
for doce in 'CHICLETE':
    print(doce + ' ', end='')        #forma comum de concatenação

print()
objeto = 'TESOURA'
for corte in objeto:
    print(f' {corte}', end='')


print()
'''
For Loop - Criando um retangulo

ex. retangulo 3x3 com o símbolo @
'''

linhas = 3
colunas = 3
simbolo = '$'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()  #está imprimindo um enter após rodar o outer loop


linhas2 = 4
colunas2 = 6
icone = '-'

for li in range(linhas2):
    for co in range(colunas2):
        print(icone, end='')
    print()


print()
'''
While Loop - gira mais um looping quando se tem uma condição
muito usado para lops dependentes de uma condição
- while = enquanto a condição (variável)...
'''

#Ex. criar uma promoção para um produto no valor de 100,00, e subtrair 5,00 a cada dia 
v = 100
dia = 0
while v > 20:    #o valor só será impresso se for > 20
    dia += 1     #a cada giro do while é adicionado mais 1 dia
    print(f' No dia {dia}, o valor será cobrado por R${v} reais.')
    v -= 5       #subtrai 5 do valor a cada dia

print()
d = 30
mes = 12
while mes > 0:
    print(f' No mês {mes} tem {d} dias')
    mes -= 1
    

print()
'''
DIFERENÇAS - IF E ELSE, FOR LOOP E WHILE LOOP

- IF e ELSE: condição de verdadeiro ou falso e é executado 1 vez.

- FOR LOOP: quando quero determinar a quantidade de giros de looping.

- WHILE LOOP: quando não sei quantas vezes quero que gire e espero atingir um objetivo (para essa variável, se for isso ou aquilo, gire essa quantidade).
'''


'''
Criando condições com While Loop
'''

#Ex. Publicar um produto com comissão de 10% se for acima de R$20:
valor2 = 21 #int(input('Digite o valor do seu produto em R$: '))

while valor2 > 20:
    valor2 = (valor2 * 0.10) + valor2    
    print(f'O valor final do seu produto será de R$ {valor2}')
    break