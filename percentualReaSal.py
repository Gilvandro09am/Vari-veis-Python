print('<Percentual de reajuste de salario>\n')

salario_atual = float(input('informe o salario atual:'))
percentual_reajuste =float(input('informe o percentual de reajustee:'))
salario_geral = salario_atual * (1 + (percentual_reajuste / 100))
print('o salario geral sera de',salario_geral,'RS')