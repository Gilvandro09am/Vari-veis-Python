print('<Calculando divida com juros(por atraso de pagamento)>')

valor_divida = float(input('informe o valor da divida:'))
dias_atraso = float(input('informe a quantidade de dias em atraso:'))
valor_multa = float(input('informe o valor da multa por dia:'))
calculo_final = valor_divida + (valor_multa * dias_atraso)
print('a divida geral sera',calculo_final)