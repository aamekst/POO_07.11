#arquivo txt

with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        lista = linha.split(';')
        nome = lista[0]
        notas = [float(lista[1]), float(lista[2]), float(lista[3]), float(lista[4])]
        media = sum(notas)/ len(notas)
        print('-'*10)
        print(f'{nome} media: {media:.2f}')