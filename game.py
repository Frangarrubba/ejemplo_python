# coding=utf-8
from random import choice, randrange
from datetime import datetime


# Operadores posibles
operators = ['+', '-', '*', '/']
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo
# Esto toma fecha y hora actual
init_time = datetime.now()
correcto = 0
incorrecto = 0
print(f'¡Veremos cuanto tardas en responder estas {times} operaciones!')
for i in range(0, times):
    # Se eligen numeros y operadores al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Indico como debe ser la cuenta dependiendo el operador
    if operator == '+':
        resultado = number_1 + number_2
    elif operator == '-':
        resultado = number_1 - number_2
    elif (operator == '/') and (number_2 != 0):
        resultado = number_1 / number_2
    else:
        resultado = number_1 * number_2

    # Se imprime la cuenta
    print(f'{i+1}- Cuanto es {number_1} {operator} {number_2}')

    # Le pedimos al usuario el resultado
    result = int(input('Ingrese el resultado: '))

    # Compruebo si el resultado es correcto
    if result == resultado:
        print('El resultado es correcto')
        correcto += 1
    else:
        print('El resultado es incorrecto')
        incorrecto += 1

# Al terminar la cantidad de cuentas a resolver
# Se vuelve a tomar la fecha y hora
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido
total_time = end_time - init_time
# Mostramos el tiempo en segundos
print(f'\nTardaste {total_time.seconds} segundos')
print(f'La cantidad de resultados correctos fue de {correcto}')
print(f'La cantidad de resultados incorrectos fue de {incorrecto}')
