#var_verdade = True #dado tipo Booleano
#var_falso = False

#print(type(var_verdade), type(var_falso))
#print(var_falso)

# if var_verdade == True:
#     print('Var_verdade é verdadeiro')

###primeira parte na lógica booleana
# a = 2
# b = 12
# if a > b:
#     print(a, 'é maior que', b)
# else:
#     print(a, 'não é maior que', b)


####menu com comparações
# print('Opcoes:\n1 = Escreve guilherme\n2 = Escreve joao\n3 = Escreve maria\n')

# opcao = input('Escolha uma opcao: ')

# if opcao == '1':
#     print('Guilherme')
# elif opcao == '2':
#     print('Joao')
# elif opcao == '3':
#     print('Maria')
# else:  
#     print('Opcao invalida')


###not True e if not
# idade = 50

# if not idade == 50:
#     print('Voce não tem tem 50 anos')
# else:
#     print('Voce tem 50 anos')


#exercício 3: Faça um programa que pergunte a idade, peso e altura de uma 
#pessoa e decida se pode ou não entrar no exército.
#condições: < 18 anos, < 60kg e < 1,70m 

### Exemplo de como declarar separado
# idade = input('djsadkjals')
# idade = int(idade)

print("Verificação se pode entrar no exército\n")

#idade = input('Escreva sua idade: ')
idade = int(input('Escreva sua idade: '))
altura = float(input('Escreva sua altura: (em metros)'))
peso = float(input('Escreva seu peso: (em kg)'))

if idade >= 18 and altura >= 1.7 and peso >= 60:
    print('Apto')
else:
    print('Está inapto')    



