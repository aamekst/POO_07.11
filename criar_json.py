#criar um arquivp o json
import json

clientes = []

#atualiza o json sem isso, ele susbtitui
with open('clientes.json', 'r', encoding='utf-8') as arquivo:
    clientes = json.load(arquivo)

while True:
    id = int(input('id:'))
    if id ==0:
        break
    nome = input('nome:')
    idade = int(input('idade:'))
    n1 = float(input('nota 1:'))
    n2 = float(input('nota 2:'))
    n3 = float(input('nota 3:'))
    notas=[n1, n2,n3]#cria outro dicionario

    dic = {'id': id, 'nome': nome,  
           'idade': idade, 
           'notas': notas}#chama o dicionario dentro do dicionario

    clientes.append(dic)

print(clientes)

#importa o arquivo 
with open('clientes.json', 'w', encoding='utf-8') as arquivo:
    json.dump(clientes,arquivo, indent=4, ensure_ascii=False)