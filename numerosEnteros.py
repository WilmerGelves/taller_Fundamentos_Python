import os 
if __name__ == '__main__':
    numero = 0
    suma = 0
    for i in range(1,4,1):
        numero = int(input(f'Ingrese el Nro{i}:'))
        os.system('cls')
        if numero < 0:
            while (numero < 0):
                numero = int(input('Número invalido, ingrese nuevamente el número: '))
                os.system('cls')
        
        suma += numero
        os.system('cls')
    print(f'La suma de los números es: {suma} ')