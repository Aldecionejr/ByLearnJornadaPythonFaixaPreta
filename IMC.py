# IMC  => Peso(KG) / Altura(M)�

def numero_quadrado(numero):
  quadrado = numero * numero
  return quadrado

def calcular_imc(peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meuIMC = peso / altura_quadrada

  return meuIMC

def classificarIMC(meuIMC):
    if imc < 18.5:
      print('Magreza')
    elif imc >= 18.5 and imc < 25:
      print('Normal')
    elif imc >= 25 and imc < 30:
      print('SobrePeso')
    elif imc >= 30 and imc < 40:
      print('Obesidade')
    else:
      print('Obesidade Grave')

imc = calcularIMC(61, 1.74)

print('Seu IMC �: ', imc)

print('Sua classifica��o �:')
classificarIMC(imc)
