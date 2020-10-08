horario = 'manhã'
clima = 'ensolarado'
temperatura = 'quente'

if horario == 'manhã' or horario == 'tarde':
    if clima == 'ensolarado' and temperatura == 'quente':
        print('Uma Piscina Cairia Bem :D')
        
    if clima == 'ensolarado' or clima == 'nublado' and temperatura == 'amena' or temperatura == 'frio':
         print('Seria Legal Praticar Algum Esporte!')

    if clima == 'chuvoso':
        print('Aproveite Para Treinar Python')
else:
    if clima == 'chuvoso':
            print('Que Tal um Filme, Série ou Jogatina? ')
    else:
        print('Um Jantar Fora Parece Interessante...')