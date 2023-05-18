palavra = 'palavras testes, para o negócio aqui'

lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']

lista_nomes.append('Geralda') #acrescenta item na lista
lista_nomes.append('Lorena')
lista_nomes.append('Maria')

lista_nomes.remove('João') #remove da lista

#lista_nomes.clear() > limpa a lista

lista_nomes.insert(0, 'primeiro da lista') #acrecenta item numa posição especifica
lista_nomes[0] = 'Teste1' #substitui algum da lista

#contador_maria = lista_nomes.count('Maria')
#print(contador_maria)


#print(lista_nomes)
#print(lista_nomes[::-1]) > coloca a lista de trás para frente/espelhada
#print(len(lista_nomes)) #conta os itens da lista

frase_separada = palavra.split(',') #cria lista a partir de frase, apontando o que serpara um item do outro
print(frase_separada[1]) 
