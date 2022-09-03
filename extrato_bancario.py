repeticao = 3
extratos_bancarios = []
data_base_agora = []
horario_base_agora = []
print(f'Opção: [1] Depósito')
for c in range(repeticao):
    escolha = int(input('O que deseja fazer?'))
    if escolha == 1:
        deposito = int(input("Insira um valor para depósito:"))
        if deposito <= 300000:
            print('_______________________________________________')
            print(f"Valor em Solicitação:", '{}'.format(deposito))
            print(f'Valor aprovado com sucesso, depósito concluido!')
            from datetime import datetime
            data_tempo_real = datetime.now()
            horario_tempo_real = 'Em desenvolvimento'
            extratos_bancarios.append(deposito)
            data_base_agora.append(data_tempo_real)
            horario_base_agora.append(horario_tempo_real)
            print('_______________________________________________')
            print(f'Extrato Bancário:')
            print('_______________________________________________')
            print(f'Valor:', extratos_bancarios[c])
            print(f'Data de alteração:- ', data_base_agora[c])
            print(f'Horário de Alteração:', horario_base_agora[c])
            print('_______________________________________________')
    else:
        print('O seu banco não autorizou a transação, por favor, entre em contato com sua central de atendimento.')
