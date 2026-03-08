#Mini sistema de produtos

produtos = []
while True:
    try:
        print ('===== SISTEMA DE PRODUTOS =====\n\n'
        '1 - Cadastrar produto\n'
        '2 - Listar produto\n'
        '3 - Atualizar quantidade de produto\n'
        '4 - Remover produto\n'
        '5 - Sair\n')

        opcao = int(input('Escolha uma opção: '))
        print()

#Cadastro de produtos:

        if opcao == 1:
            print ('===== CADASTRAR PRODUTOS ======')
            print ()


            id_produto=len(produtos)+1
            nome_produto=input(f'Digite o nome do produto de ID #{id_produto}: ').strip().title()
            if nome_produto.replace (' ',''):
                try:
                    valor_produto=float(input ('Digite o valor do produto: '))
                    if valor_produto >0:
                        quantidade_produto=int(input('Digite a quantidade de produtos: '))
                        if quantidade_produto >=1:
                            produto={'id':id_produto,'nome':nome_produto,'valor':valor_produto,'quantidade':quantidade_produto}
                            produtos.append(produto)
                            print ('Produto cadastrado com sucesso!\n\n'
                                f'ID:{id_produto}\nProduto: {nome_produto}\nValor:R$ {valor_produto:.2f}\nQuantidade: {quantidade_produto}')
                            print ()


                        else:
                            print ('Quantidade inválida')
                            print()
                    else:
                        print ('Valor inválido')
                        print()
                except ValueError:
                    print ('Valor/Quantidade inválida')
                    print()
            else:
                print ('Produto inválido')
                print()






        elif opcao == 2:
            print ('===== LISTAR PRODUTOS ======')
            print ()
            print ('1 - Listar produtos cadastrados')
            print ('2 - Procurar produto cadastrado')
            print ()
            opcao2=int(input('Escolha uma opção: '))
            print()

            if opcao2 == 1:
                if len(produtos) >= 1:
                    for produto in produtos:
                        print (f'ID: {produto["id"]}')
                        print (f'Produto: {produto["nome"]}')
                        print (f'Valor: {produto["valor"]}')
                        print (f'Quantidade: {produto["quantidade"]}')
                        print ()
                else:
                    print ('Você não possue produtos cadastrados')
                    print ()

            elif opcao2 == 2:
                try:
                    pesquisa_produto=int(input ('Digite o ID do produto: '))
                    print()
                    produto_encontrado= False
                    for produto in produtos:
                        if pesquisa_produto == produto["id"]:
                            print (f'ID: {produto["id"]}')
                            print (f'Produto: {produto["nome"]}')
                            print (f'Valor: {produto["valor"]}')
                            print (f'Quantidade: {produto["quantidade"]}')
                            print ()

                            produto_encontrado = True
                            break

                    if not produto_encontrado:
                        print('ID inválido')
                        print()


                except ValueError:
                        print('ID inválido')
                        print()

            else:
                print ('Opção inválida')
                print()



        elif opcao == 3:
            print ('Atualizar quantidade de produto')

        elif opcao == 4:
            print ('Remover produto')

        elif opcao == 5:
            print ('Sair')
            break

        else:
            print ('Opção inválida')

    except ValueError:
        print  ('Opção inválida')







