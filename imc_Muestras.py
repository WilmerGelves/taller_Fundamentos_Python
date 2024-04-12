import os 
import msvcrt
if __name__ == '__main__':
    #Inicialización de las variables.
    poblacion = 0
    nombreAlumno = ''
    edad = ''
    peso = 0.0
    altura= 0.0
    imc = 0.0 
    ideal = 0
    sobrepeso = 0
    obesidad1 = 0
    obesidad2 = 0
    obesidad3 = 0
    poblacion = int(input('Ingrese el número de estudiantes que se estudiarán:  '))
    os.system('cls')
    #Ingreso de información y calculo.
    for i in range(0,poblacion,1):   
        nombreAlumno = str(input('Ingrese el nombre del alumno: '))
        edad = str(input('Ingrese su edad: '))
        peso = float(input('Peso(kg): '))
        altura = float(input('Altura: '))
        imc = (peso)/(pow(altura,2))
        #Condicionales(clasificacion del Imc)
        if ((imc >= 18.5) and (imc <=24.9)):
            print(f'El alumno {nombreAlumno} tiene {edad} años de edad.\nTiene un IMC de {round(imc,2)}.\nSe clasifica como "Normal"') 
            ideal += 1
        elif((imc >= 25) and (imc <=29.9)):
            print(f'El alumno {nombreAlumno} tiene {edad} años de edad.\nTiene un IMC de {round(imc,2)}.\nSe clasifica con "Sobrepeso"')
            sobrepeso += 1
        elif((imc >= 30) and (imc <=34.9)):
            print(f'El alumno {nombreAlumno} tiene {edad} años de edad.\nTiene un IMC de {round(imc,2)}.\nSe clasifica con "obsidad I"')
            obesidad1 += 1
        elif((imc >= 35) and (imc <=39.9)):
            print(f'El alumno {nombreAlumno} tiene {edad} años de edad.\nTiene un IMC de {round(imc,2)}.\nSe clasifica con "obsidad II"')
            obesidad2 += 1
        elif(imc >= 0):
            print(f'El alumno {nombreAlumno} tiene {edad} años de edad.\nTiene un IMC de {round(imc,2)}.\nSe clasifica con "obsidad III"')
            obesidad3 += 1
        else:
            print('Verifique los valores ingresados')
        print("Es importante que tome nota de los resultados.\nCuando lo haga presione una tecla para continuar...")
        msvcrt.getch()
        os.system('cls')
    print(f'Datos del estudio.\nEstudiantes con peso ideal:{ideal}\nEstudiantes con sobrepeso: {sobrepeso}\nCantidad de estudiantes con obesidad I: {obesidad1}\nCantidad de estudiantes con obesidad II: {obesidad2}\nCantidad de estudiantes con obesidad III: {obesidad3}')