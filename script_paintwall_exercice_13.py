largura = float(input('Insira a largura da parede:'))
altura = float(input('Insira a altura da parde:'))
area = largura * altura
#Na variavel quantidade_tinta irá especificar a quantidade de tinta necessaria para pintar a parede
quantidade_tinta = area / 2
print("""\nÁrea da parede: {}m
         \nQuantidade de tinta necessária: {}LT""".format(area,
                                                          quantidade_tinta))
