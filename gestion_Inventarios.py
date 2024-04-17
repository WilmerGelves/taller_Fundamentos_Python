import os
if __name__ == '__main__':
    #Valores iniciales
    inventario = []
    opcion = 0
    title = """
    **************************
    * Gestion de Inventarios *
    **************************
    """
    menu = '1.Registrar producto\n2.Visualizar producto\n3.Actualizar Stock\n4.Buscar producto\n5.Salir'

    #Inico del programa 
    while (opcion <5):
        print(title)
        print(menu)
        opcion = int(input('=>_'))
        match(opcion):
            case 1: 
                continuar = True
                while(continuar):
                    os.system('cls')
                    codigo = input('Ingrese el código del producto: ')
                    nombre = input('Ingrese el nombre del producto: ')
                    valorCompra = float(input('Ingrese el valor valor de  compra: '))
                    valorVenta = float(input('Ingrese el valor de venta: '))
                    stcokMinimo = int(input('Ingrese el stcok minimo: '))
                    stockMaximo = int(input('Ingrese el stock maximo: '))
                    provedor = input('Proeedor: ')
                    producto = [codigo,nombre,valorCompra,valorVenta,stcokMinimo,stockMaximo,provedor]
                    inventario.append(producto)
                    continuar = bool(input('Desea agregar otro producto... s(si) o enter(no)'))
            case 2: 
                pass

            case 3: 
                palabra = input('Ingrese el nombre del producto que desea modificar: ').upper()
                for i,item in enumerate(inventario):
                    if palabra in item:
                        if (bool(input('Desea modificar el stock minimo del producto... s(si) o enter(no)'))):
                            item[4] = int(input(f'Ingrese el stock del producto:{item[0]} '))
                        if (bool(input('Desea modificar el stock máximo del producto... s(si) o enter(no)'))):
                            item[5] = int(input(f'Ingrese el stock del prodcuto: {item[0]}'))
            case 4: 
                pass
            case 5: 
                os.system('cls')
            case _:
                print('opcion inválida')
                os.system('cls')
                opcion = 0


    

