print('<Descobrindo quantos litros de gasolina vou abastecer>\n')

valor_combustivel = float(input('Informe o valor do combustivel: \n'))
valor_abastecer = float(input('Informe o valor que deseja abastecer: \n'))
valor_geral = valor_abastecer // valor_combustivel

print('Vai ter',valor_geral,'litros')