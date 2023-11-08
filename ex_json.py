#arquivo json
# r - read

import json

with open('dados.json', 'r', encoding='uft8') as arquivo:
    dicionario = json.load(arquivo) #le o arquivo e transforma em um dicionario
    print(dicionario)
    print(dicionario['cliente']['id'])#chave e entra em outro dicionario
    print(dicionario['cliente']['nome'])
    #print(lista[0]) percorre a lista


