def inserir_item():
    '''
    Inserir um novo produto, informando o nome e o preço
    '''
    tamanho_lista = len(lista_itens)+1
    produto = input ('Digite o nome de novo produto: ')
    preco = float(input('Digite o valor do novo produto '))
    lista_itens.append({
            'id': tamanho_lista,
            'nome': produto,
            'preco': preco
        })

def atualizar_item():
    '''
    Usado para alterar o preco de um produto, informando o seu id 
    '''
    id_produto = int(input('Digite o id do produto que deseja atualizar: ')) 
       
    for item in lista_itens:
        if item['id'] == id_produto:
            print(f'Voce vai alterar o produto {item["nome"]}') 
            preco = float(input('Digite o valor do produto '))
            item['preco'] = preco        


def excluir_item():
    '''
    Excluir um produto, informando seu id
    '''
    id_produto = int(input('Digite o id do produto que deseja excluir: '))
    for item in lista_itens:
        if item['id'] == id_produto:
            print(f'Voce vai excluir o produto {item["nome"]}') 
            lista_itens.remove(item)
    contador = 0
    for item in lista_itens:
        contador += 1
        item['id'] = contador


lista_itens = [
    {
        'id': 1,
        'nome': 'Celular',
        'preco': 1000
    },
    {   
        'id': 2,
        'nome': 'Batedeira',
        'preco': 350
    },
    {
        'id': 3,
        'nome': 'Televisao',
        'preco': 3450
    },
    {
        'id': 4,
        'nome': 'Notebook',
        'preco': 6700
    },
    {
        'id': 5,
        'nome': 'Aparelho DVD',
        'preco': 200
    },
]