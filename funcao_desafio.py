import funcoes_usadas

entrada = 0
while entrada != 5:
    entrada = int(input('Digite o que deseja dentre as opcoes:\n 1- Veja todos os itens. \n 2- Inserir um item \n 3- Atualizar produto \n 4- Excluir produto \n 5- Sair. \n Opção: '))
    
    if entrada == 1:
        print(funcoes_usadas.lista_itens)        
    elif entrada == 2:
        funcoes_usadas.inserir_item()  
    elif entrada == 3:
        funcoes_usadas.atualizar_item()
    elif entrada == 4:
        funcoes_usadas.excluir_item()
    elif entrada == 5:
        print('Tchau')