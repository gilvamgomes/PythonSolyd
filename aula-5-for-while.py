#nomes = ['Guilherme', 'Marcelo', 'João', 'Julia']

#print(nomes[0])

# for nome in nomes: #estrutura do for: para cada nome DENTRO de nomes, vc me mostra um nome
#     print(nome) 

'''
lista_de_numeros = range(5) 
#(5, 10) começa no 5 e vai até '10'
#(0, 100, 2) começa do até '100', espaçando 2 
for item in lista_de_numeros:
    print(item)
'''

'''
for i in range(len(nomes)): #ou range(4), ou 'nomes' direto
    print(nomes[i])
'''

#palavra = 'Guilherme Junqueira'
# for letra in palavra:
#     print(letra)

# i = 0
# while i < 10:
#     print ('i ainda é menor que 10: ', i) 
#     i += 1

# print('Acabou o while: ', i)  

'''
lista_frutas = ['maça', 'pera', 'uva', 'abacaxi', 'goiaba']

contador = 0

for fruta in lista_frutas:
    contador +=1

print(contador)

#ou simplesmente

print(len(lista_frutas))
'''

# numero = 0

# while True:
#     print(numero)
#     if numero == 20:
#         break
#     numero +=1


#exercício: Programa que lê quantidade de pessoas 
#pergunta o nome de todos e acrescenta numa lista de convidados
#dps imprimi os nomes da lista 



lista_convidados = [] #lista zerada, de início

convidado = (input('Insira o nome do convidado: ')) #Aqui recebo o nome do convidado
lista_convidados.append(convidado) #acrescenta o nome na lista

resposta = (input('Tem mais convidados? ')) #pergunta se tem mais nomes para add

while resposta == 'sim' or resposta == 's' or resposta == 'S':
    convidado = (input('Insira o nome do convidado: ')) #Insere o novo nome do convidado
    lista_convidados.append(convidado) #e acrescenta na lista
    resposta = (input('Tem mais convidados? ')) #pergunta novamente 
    resposta == 0
    
    # if resposta != 'sim' or resposta != 's' or resposta != 'S': #se a resposta for diferente de sim, 
    #     break #então sai do loop

#print(len(lista_convidados)) #atualiza o núm. de convidado da lista

for nome_da_pessoa in lista_convidados:
    print(nome_da_pessoa)


########Exercício resolvido
# print('Progra de controle de festinha 1.0')
# print('###############################\n')
    
# numero_de_convidados = input('Coloque o numero de convidados: ')
# lista_de_convidados = []

# i = 1
# while i <= int(numero_de_convidados):
#     nome_do_convidado = input('Coloque o nome do convidado #' + str(i) + ': ')
#     lista_de_convidados.append(nome_do_convidado)
#     i += 1

# for convidado in lista_de_convidados:
#     print(convidado)


#ediçao Samuca

""" lista_convidados = [] 
resposta = ''

def convidados():
    convidado = (input('Insira o nome do convidado: ')) 
    lista_convidados.append(convidado) 
    resposta = input('Tem mais convidados? ').lower()
    if resposta == 'sim' or resposta =='s' or resposta == 'ss'
        convidados()
    else:
        for i in lista_convidados:
            print(i)

convidados() """

