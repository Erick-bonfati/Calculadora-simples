'''
Calculadora simples
'''

while True:
    print()
    num_1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    num_2 = input('Digite outro número: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(f'Resultado é : {num_1} + {num_2} = {num_1 + num_2}')
    elif operador == '-':
        print(f'Resultado é : {num_1} - {num_2} = {num_1 - num_2}')
    elif operador == '/':
        print(f'Resultado é : {num_1} / {num_2} = {num_1 / num_2}')
    elif operador == '*':
        print(f'Resultado é : {num_1} * {num_2} = {num_1 * num_2}')
    else:
        print('O operador é inválido')

    while True:

        sair = input('Deseja sair? [s]im ou [n]ão: ')
        sair = sair.upper()
        if sair == 'S':
            raise SystemExit()
        elif sair != 'N':
            print(f'Digite somente S ou N ')
        else:
            break
