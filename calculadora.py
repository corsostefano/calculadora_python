print('*** Calculadora en Python ***')
valor_1 = valor_2 = resultado = 0
salir = False
while not salir:
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoje una opción: '))
    if 1 <= opcion <= 4:
        valor_1 = float(input('Introduzca el valor N° 1: '))
        valor_2 = float(input('Introduzca el valor N° 2: '))
    if opcion == 1:
        resultado = valor_1 + valor_2
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2:
        resultado = valor_1 - valor_2
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    elif opcion == 3:
        resultado = valor_1 * valor_2
        print(f'El resultado de la multiplicacion es: {resultado:.2f}\n')
    elif opcion == 4:
        resultado = valor_1 / valor_2
        print(f'El resultado de la división es: {resultado:.2f}\n')
    elif opcion == 5:
        print('Saliendo de la calculadora')
        salir = True
    else:
        print('Por favor ingrese una opción valida')
