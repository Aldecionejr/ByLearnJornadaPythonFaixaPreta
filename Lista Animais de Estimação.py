animais = [ ]

animal = input('Digite o nome dos seus animais de estimação ou digite 0 se nao tiver nenhum :D ')

while animal != '0':
    especie = input('Digite a Espécie Desse Animal: ')
    animais.append([animal, especie])
    animal = input('Se Tiver Mais Animais, Digite o Nome Dele. ou Digite 0 se nao tiver :D')

if len(animais) == 0:
    print('\nVocê tem os Seguintes Animais')
else:
    print('\n\nVocê Tem os Seguintes Animais: ')
    for animal in animais:
        print('- Nome: ', animal[0], '| Espécie: ', animal[1])