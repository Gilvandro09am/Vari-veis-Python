print('<Descobrindo quantas carteiras cabe na sala>\n')

comprimento_sala = float(input('informe o comprimento da sala: \n'))
largura_sala = float(input('informe a largura da sala: \n'))
comprimento_carteira = float(input('informe o comprimento da carteira: \n'))
largura_carteira = float(input('informe a largura da carteira: \n'))

carteiras_largura = (largura_sala + 0.5) // (largura_carteira + 0.5)
carteiras_comprimento = (comprimento_sala - 1.5 + 0.2) // (comprimento_carteira + 0.2)

carteiras_sala = carteiras_largura * carteiras_comprimento
print('Vai caber',carteiras_sala,'carteiras na sala')