print('<Descobrindo duracao do jogo(24 hrs)>\n')

hora_inicial = int(input('Informe a hora inicial do jogo: '))
hora_final = int(input('Informe a hora final do jogo: '))
import datetime

if hora_inicial > hora_final:
    x=24-hora_inicial
    y=x+hora_final
    print('O jogo vai durar',y,'horas')
elif hora_final > hora_inicial:
    y=hora_final-hora_inicial
    print('O jogo vai durar',y,'horas')
elif hora_inicial == hora_final:
    y=24
    print('O jogo vai durar',y,'horas')