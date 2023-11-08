import json

aluno = {}

with open('notas.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        lista = linha.split(',')
        notas = [float(lista[2]), float(lista[3]), float(lista[4]), float(lista[5])]
        print(notas)
    
        dic = {
        'nome': lista[1],
        'notas': notas

        }
    
        aluno[lista[0]] = dic

    


with open('alunos.json', 'w', encoding='utf-8') as arquivo:
    json.dump(aluno,arquivo, indent=4, ensure_ascii=False)