frutas = ['Maça', 'Banana', 'Pera', 'Uva']
guloseimas = ['Bolacha', 'Batata', 'Fini', 'Chocolate']
comidas = ['Arroz', 'Feijão', 'Carne']
bebidas = ['Refrigerante', 'Suco de Laranja', 'Água']

categoria = ['Frutas', 'Guloseimas', 'Comidas', 'Bebidas']
compras = [frutas, guloseimas, comidas, bebidas]

for indice, categoria in enumerate(categoria):
    print('Você precisa comprar', len(compras[indice]), categoria + ':')
    for compra in compras[indice]:
        print('-', compra)