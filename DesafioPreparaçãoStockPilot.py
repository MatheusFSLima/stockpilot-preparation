#Mini sistema de produtos

produtos = []
proximo_id = 1
while True:
    try:
        print ('===== SISTEMA DE PRODUTOS =====\n\n'
        '1 - Cadastrar produto\n'
        '2 - Listar produto\n'
        '3 - Atualizar quantidade de produto\n'
        '4 - Remover produto\n'
        '5 - Sair\n')

        opcao = int(input('Escolha uma opção: '))
#Cadastro de produtos:

        if opcao == 1:
            print ('===== CADASTRAR PRODUTOS =====\n')
            nome_produto=input(f'Digite o nome do produto: ').strip().title()
            if nome_produto.replace (' ',''):
                try:
                    valor_produto=float(input ('Digite o valor do produto: '))
                    if valor_produto >0:
                        quantidade_produto=int(input('Digite a quantidade de produtos: '))
                        if quantidade_produto >=1:
                            produto={'id':proximo_id,'nome':nome_produto,'valor':valor_produto,'quantidade':quantidade_produto}
                            produtos.append(produto)
                            print ('\nProduto cadastrado com sucesso!\n\n'
                                f'ID:{proximo_id}\nProduto: {nome_produto}\nValor:R$ {valor_produto:.2f}\nQuantidade: {quantidade_produto}\n')
                            proximo_id +=1
                        else:
                            print ('Quantidade inválida\n')
                    else:
                        print ('Valor inválido\n')
                except ValueError:
                    print ('Valor/Quantidade inválida\n')
            else:
                print ('Produto inválido\n')

#Listar produtos:

        elif opcao == 2:
            print ('\n===== LISTAR PRODUTOS =====\n')
            print ('1 - Listar produtos cadastrados')
            print ('2 - Procurar produtos cadastrados\n')
            opcao2=int(input('Escolha uma opção: '))

            if opcao2 == 1:
                if len(produtos) >= 1:
                    for produto in produtos:
                        print (f'\nID: {produto["id"]}')
                        print (f'Produto: {produto["nome"]}')
                        print (f'Valor: {produto["valor"]}')
                        print (f'Quantidade: {produto["quantidade"]}\n')
                else:
                    print ('Você não possue produtos cadastrados\n')

            elif opcao2 == 2:
                try:
                    produto_encontrado = False
                    pesquisa_produto=int(input ('Digite o ID do produto: '))
                    for produto in produtos:
                        if pesquisa_produto == produto["id"]:
                            print (f'\nID: {produto["id"]}')
                            print (f'Produto: {produto["nome"]}')
                            print (f'Valor: {produto["valor"]}')
                            print (f'Quantidade: {produto["quantidade"]}\n')

                            produto_encontrado = True
                            break

                    if not produto_encontrado:
                        print('ID inválido\n')

                except ValueError:
                        print('ID inválido\n')

            else:
                print ('Opção inválida\n')


#Atualizar quantidade de produtos:

        elif opcao == 3:
            print ('===== ATUALIZAR QUANTIDADE DE PRODUTOS =====\n')
            try:
                produto_encontrado = False
                pesquisa_produto = int(input('Digite o ID do produto: '))
                for produto in produtos:
                    if pesquisa_produto == produto["id"]:
                        produto_encontrado = True
                        opcao3= (input(f'Produto: {produto["nome"]}. Deseja continuar? s/n: \n')).strip().lower()
                        if opcao3 in ['s','sim']:
                            print (f'\nProduto: {produto["nome"]}\n'
                                   f'Quantidade: {produto["quantidade"]}\n')
                            nova_quantidade= int(input ('Digite a nova quantidade: \n'))
                            produto["quantidade"] = nova_quantidade
                            print(f'\nQuantidade atualizada com sucesso!\n\nProduto: {produto["nome"]}\nNova quantidade: {nova_quantidade}\n')
                            break

                if not produto_encontrado:
                    print ('ID inválido!\n')


            except ValueError:
                print('ID inválido!\n')

        elif opcao == 4:
            print('===== REMOVER PRODUTOS =====\n')
            try:
                produto_encontrado = False
                pesquisa_produto = int ( input ('Digite o ID do produto que deseja remover: '))
                for produto in produtos:
                    if pesquisa_produto == produto["id"]:
                        produto_encontrado = True
                        opcao4 = (input(f'Produto: {produto["nome"]}. Deseja continuar com a remoção? s/n: \n')).strip().lower()
                        if opcao4 in ['s','sim']:
                            produtos.remove(produto)
                            print (f'\nProduto: {produto["nome"]} removido com sucesso!\n')
                            break




                if not produto_encontrado:
                    print('ID inválido!\n')

            except ValueError:
                print('ID inválido!\n')
        elif opcao == 5:
            print ('Sair')
            break

        else:
            print ('Opção inválida')

    except ValueError:
        print  ('Opção inválida')







