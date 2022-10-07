declaracao = True
dados_bancario = []
dados_pessoal = []
lista_nomes = []
while declaracao:
    nome = str(input("Entre com seu nome:"))
    if nome > "":
        conta_bancaria = int(input('Insira o numero da sua conta bancária:'))
        rg = int(input('Entre com seu rg:'))
        celular = int(input('Entre com o seu numero de celular:'))
        lista_nomes.append(nome)
        dados_bancario.append(conta_bancaria)
        dados_pessoal.append(rg)
    else:
        print(lista_nomes)
        print(dados_bancario)
        print(dados_pessoal)
        declaracao = False
