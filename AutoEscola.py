def validarIdade(idade):
    if idade < 18:
        print('\nDesculpe, você nao tem idade para prosseguir,',nome)
        return False
    else:
        print('\nÓtimo! Podemos Prosseguir,', nome)
        return True

def escolherCarta():
    print( 'Digite uma das opções abaixo: ')
    print('1 - Carro;\n2 - Moto;\n3 - Carro e Moto;')

    return int(input())

def calcularPreco(escolha):
    valorCarro = 1500
    valorMoto = 1000

    if escolha == 1:
        return valorCarro
    elif escolha == 2:
        return valorMoto
    else:
        return valorCarro + valorMoto

def desconto(valor):
    return valor - (valor * 0.10)

nome = input('Digite seu Nome: ')
idade = int(input('digite Sua Idade: '))

if validarIdade(idade):
    escolha = escolherCarta()

    print('\nPerfeito! Vou calcular o Valor')
    valor = calcularPreco(escolha)

    print('\n'+nome, 'o valor total é de ', valor, ' R$')
    print('Mas vou ver com meu gerente se posso dar desconto...')
    valor = desconto(valor)

    print('\nCom desconto eu consigo fazer por ', valor, 'R$')

    print('Te Interessa? \n1 - Sim\n2 - Não')
    interesse = int(input())
    if interesse == 1:
        print('\nPerfeito! :D Começaremos Amanhã!')
    else:
        print('\nTudo Bem :( \nMe Avise se Mudar de Ideia.')