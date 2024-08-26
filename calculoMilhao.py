print('<Calculo para conseguir um milhao>\n')

salario_mensal = float(input('informe o salario mensal:'))
despesa_mensal = float(input('informe a despesa mensal:'))
sobra_anual = (salario_mensal - despesa_mensal)  * 12
print('vai sobrar anualmente',sobra_anual)
juntar_milhao = 1000000 // sobra_anual
print('vai conseguir juntar 1 milhao de reias em quantos anos',juntar_milhao)