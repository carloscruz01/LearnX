#Crie um programa que leia quanto de dinheiro uma pessoa tem
#na carteira e mostre quantos dólares ela pode comprar.
name = str(input('What is your name?'))
wallet = float(input('enter a value:'))
cotacao_dolar = 3.27
conversao = wallet / cotacao_dolar
print('Hi,', name, """
                   Você possui: BRL${}
                   Cotação do Dólar: USD${:2}
                   Você pode comprar: USD${:2}""".format(wallet,
                                                         cotacao_dolar,
                                                         conversao))
