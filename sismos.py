import os
if __name__ == '__main__':
    #Inicializnado variables.
    opcion = 0
    ciudades = []
    registros = []
    informe =  []
    title = """
    **************************
    *  Prevensión de Sismos  *
    **************************
    """
    menu = '1.Registrar ciudad\n2.Registrar sismos.\n3.Buscar sismos por ciudad\n4.Informe de riesgo\n5.Salir'

    while(opcion < 5 ):
        print(title)
        print(menu)
        ocpion =int(input(' => '))
        os.system('cls')
        match(ocpion):
            case 1: 
                continuar = True
                while(continuar):
                    ciudad = input('Nombre de la ciudad: ').upper()
                    ciudades.append(ciudad)
                    continuar = bool(input('Desea registrar otra ciudad... S(si) o Enter(no)'))
                    os.system('cls')
            case 2: 
                for ciudad in ciudades:
                    print(f'Registros de: {ciudad}')
                    limite = int(input('Cuantos sismos registrará: '))
                    for j in (0,limite,1):
                        valor = float(input(f'Resgistro {j+1}:'))
            case 3: 
                print(ciudades)
            case 4: 
                pass
            case 5: 
                pass
            case _:
                print('Opcion inválida')
                os.system('pause')
                opcion = 0