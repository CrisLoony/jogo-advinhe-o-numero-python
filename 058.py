from random import randint
from time import sleep

print('\033[31m§\033[m'*40)
print('\033[35m|{:^38}|\033[m'.format('Tente Advinhar'))
print('\033[31m§\033[m'*40)
print('O computador irá escolher um número de 0 a 10')
print('Você terá que descobrir qual foi!')

pc = randint(0, 10)
user = 0
tentativas = 0
sleep(1.5)
print('O computador já fez a escolha!')

while user != pc:
    user = int(input('Tente advinhar: '))
    print('Processando . . .')
    tentativas = tentativas + 1
    sleep(0.5)
    if user == pc:
        print(f'Parabéns, você acertou! O número escolhido foi {pc}')
    else:
        if user < pc:
            print('Um pouco mais...Tente Novamente!')
        elif user > pc:
            print('Um pouco menos...Tente Novamente!')
print(f'Foram necessárias {tentativas} tentativas antes de você acertar!')
