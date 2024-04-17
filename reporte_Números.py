import os 
if __name__ == '__main__':
    #Inicialización de las variables.
    limite = 0
    numero = 0
    pares = 0
    promPares = 0.0
    impares = 0
    promImpares = 0.0
    menores = 0
    rango = 0
    mayores = 0
    #Inicio del programa 
    limite = int(input('Cuntos números desea ingresar: '))
    os.system('cls')
    for i in range(1,limite+1,1):
        numero = int(input(f'Ingrese el Nro-{i} :'))
        os.system('cls')
        if(numero > 0 ) and (numero % 2 == 0):
            pares += 1
            promPares += numero
            if (numero < 10):
                menores += 1
            elif ((numero >= 20) and (numero <= 50)):
                rango += 1
            elif(numero > 100):
                mayores += 1

            
        elif((numero >0) and (numero % 2 != 0)):
            impares += 1
            promImpares += numero
            if (numero < 10):
                menores += 1
            elif ((numero >= 20) and (numero <= 50)):
                rango += 1
            elif(numero > 100):
                mayores += 1
        
        elif(numero < 0):
            try:
                promPares = (promPares/pares)
            except ZeroDivisionError:
                promPares = 0
            try:
                promImpares = (promImpares/impares)
            except ZeroDivisionError:
                promImpares = 0
            print(f'Total de número ingresados: {i-1}')
            print(f'Números pares: {pares}')
            print(f'Promedio de los números pares: {round(promPares,2)}')
            print(f'Promedio de los números impares: {round(promImpares, 2)}')
            print(f'Menores de 10: {menores}')
            print(f'Números entre 20 y 50: {rango}')
            print(f'Numeros mayores de 100: {mayores}')
            os.system('pause')
            exit()
            
    os.system('pause')
    try:
        promPares = (promPares/pares)
    except ZeroDivisionError:
        promPares = 0
    try:
        promImpares = (promImpares/impares)
    except ZeroDivisionError:
        promImpares = 0
    print(f'Total de número ingresados: {i}')
    print(f'Números pares: {pares}')
    print(f'Promedio de los números pares: {round(promPares,2)}')
    print(f'Promedio de los números impares: {round(promImpares, 2)}')
    print(f'Menores de 10: {menores}')
    print(f'Números entre 20 y 50: {rango}')
    print(f'Numeros mayores de 100: {mayores}')