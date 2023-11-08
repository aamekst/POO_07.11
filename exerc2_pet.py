import json

pet = []

with open('pet.json', 'r', encoding='utf-8') as arquivo:
    pet = json.load(arquivo)


while True:
    print('1 - Inserir')
    print('2 - Excluir')
    print('3 - listar')
    print('4 - sair')
    op = int(input('Escolha: '))

    for  p in range(1):
        if op == 1:
            while True:
                tipo = input('tipo:')
                nome = input('nome:')
                idade = int(input('idade:'))
                pergunta = input('Deseja continuar? S/N ')

                dic = {'tipo': tipo,  
                        'nome': nome,
                        'idade': idade}

                pet.append(dic)

                if pergunta in ['N','n']:
                    break

                print(pet)

            with open('pet.json', 'w', encoding='utf-8') as arquivo:
                json.dump(pet,arquivo, indent=4, ensure_ascii=False)
        
        elif op == 2:
            with open('pet.json', 'r', encoding='utf-8') as arquivo:
                pet = json.load(arquivo)
            
                nome = input('Excluir qual animal: ') 
                
                for valor in pet:       
                    #print(valor)  
                    print('-'*20)
                    if valor ['nome'] == nome:
                        pet.remove(valor) 
                        break

                with open('pet.json', 'w', encoding='utf-8') as arquivo:
                 json.dump(pet,arquivo, indent=4, ensure_ascii=False)

                #print(pet)
                

                    
        elif op == 3:
            with open('pet.json', 'r', encoding='utf-8') as arquivo:
                pet = json.load(arquivo)
                print(pet)
        elif op ==4:
            exit
        else: 
            print('erro')

