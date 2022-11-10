from random import randint
from time import sleep

n= randint(0,5)
print('Vou pensar em numero de 0 a 5 tente acertar')
print('_=_'*20)
usuario = int(input('Qual numero eu pensei \n'))
print('PROCESSANDO')
sleep(2)
if usuario == n:
   print('Você venceu')
else:
   print('Errou, eu pensei no numero {} e não {}'.format(n,usuario))
