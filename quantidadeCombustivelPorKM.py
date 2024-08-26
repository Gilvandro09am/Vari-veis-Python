print('Quantidade de combustivel gasto por km')

km_inicial = float(input('informe o km inicial: '))
km_final = float(input('informe o km final: '))
litro = float(input('informe a quantidade de litro gasta: '))
media = litro // (km_final - km_inicial)
print('A quantiade de combustível gasto foi',media,'litro(s) por KM')