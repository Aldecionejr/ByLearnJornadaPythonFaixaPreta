nota1 = 7.5
nota2 = 4.8

# Função de Verificação de Aprovação
def verificarAprovacao():
    media = calcularMedia([nota1, nota2])

    if media >= 6:
        print('O Aluno Foi Aprovado!')
    else:
        print('O Aluno Foi Reprovado!')

# Função para calcular a media
def calcularMedia(notas):
    qtd = len(notas)

    soma = 0
    for nota in notas:
        soma = soma + nota

    media = soma / qtd
    print('Sua Media é: ', media)
    return media

# Executando a função para verificar aprovação
verificarAprovacao()