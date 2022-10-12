import random
lista_1 = []
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
           29,
           30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
           56,
           57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]


numeros_de_jugador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                      30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                      57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]

def intrucioness():
    print('las intruciones son'
          '\n1.primero se juega de a 2 jugadores'
          '\n2.se les dara una planilla de numeros'
          '\n3.saldran numeros aleatorios y si estan en su planilla se los eliminara'
          '\nel numero de la planilla'
          '\n4.el primero que se quede sin numeros gana')


def listaAleatorios_1(n):
    lista = []
    for i in range(n):
        carton = random.choice(numeros_de_jugador)
        if carton in numeros_de_jugador:
            numeros_de_jugador.remove(carton)
            lista.append(carton)
    return lista


remeras = []
precio_remeras = []
stock_remeras = []

zapatillas = []
precio_zapatillas = []
stock_zapatillas = []

pantalones = []
precio_pantalones = []
stock_pantalones = []

abrigo = []
precio_abrigo = []
stock_abrigo = []

extra = []
precio_extra = []
stock_extra = []


carrito = 0
plata_de_compador = 0

print('que queres hacer \n>>preciona 1 para jugar mini-bingo\n>>preciona 2 para ir a tienda de ropa')
primer_opcion = int(input('>>'))
if primer_opcion == 1:
    jugador1 = listaAleatorios_1(12)
    jugador2 = listaAleatorios_1(12)

    ingreso = input('quieres jugar el mini-bingo?\n>>').lower()
    if ingreso == 'si':
        print('okey empesemos el juego')
        print('*********************************************************')
        intrucioness()
        print('*********************************************************')
        precionar = int(input('\nprecione 1 para iniciar\n>>'))
        if precionar == 1:
            while True:
                op = input('precionar enter para jugar la siguiente ronda \n>>').lower()
                if op == '':
                    print('jugador 1:\n>>', jugador1)
                    print('jugador 2\n>>', jugador2)

                    numero_aleatorio = random.choice(numeros)
                    if numero_aleatorio in numeros:
                        numeros.remove(numero_aleatorio)

                    print('salio el numero', numero_aleatorio)

                    if numero_aleatorio in jugador1 and numero_aleatorio in jugador2:
                        jugador1.remove(numero_aleatorio)
                        jugador2.remove(numero_aleatorio)
                    if numero_aleatorio in jugador1:
                        jugador1.remove(numero_aleatorio)
                    elif numero_aleatorio in jugador2:
                        jugador2.remove(numero_aleatorio)
                    if jugador1 == lista_1:
                        print('\nEL JUGADOR 1 GANO!!')
                        break
                    elif jugador2 == lista_1:
                        print('\nEL JUGADOR 2 GANO!!')
                        break
                else:
                    break
    else:
        print('okey chau')

# opcion de minibingo y tienda de ropa
elif primer_opcion == 2:
    opcion = int(input('que quieres hacer \n>>ser vendedor apretar 1.\n>> '))
    if opcion == 1:
        while True:
            # doy las opciones que hay para hacer
            opcion2 = int(input('estas en modo vendedor. que quieres hacer\n>>1.agregar remeras\n>>2.agregar zapatilas'
                                '\n>>3.agregar pantalones\n>>4.agregar abrigo'
                                '\n>>5.agregar extra\n>>6.ver tienda\n>>7.cambiar de modo'
                                '\n>>8.salir\n>>'
                                ''))
            if opcion2 == 1:
                print('que remera queres agregar, marca y nombre ')
                rem = str(input('>>'))
                print('precio')
                precio_rem = int(input('>>'))
                print('ingrese el stock')
                stock_rem = int(input('>>'))
                remeras.append(rem)
                precio_remeras.append(precio_rem)
                stock_remeras.append(stock_rem)
            elif opcion2 == 2:
                print('que zapatillas queres agregar, marca y nombre ')
                zap = input('>>')
                print('precio')
                precio_zap = int(input('>>'))
                print('ingrese el stock')
                stock_zap = int(input('>>'))
                zapatillas.append(zap)
                precio_zapatillas.append(precio_zap)
                stock_zapatillas.append(stock_zap)
            elif opcion2 == 3:
                print('que pantalones queres agregar, marca y nombre ')
                pant = input('>>')
                print('precio')
                precio_pant = int(input('>>'))
                print('ingrese el stock')
                stock_pant = int(input('>>'))
                pantalones.append(pant)
                stock_pantalones.append(stock_pant)
                precio_pantalones.append(precio_pant)
            elif opcion2 == 4:
                print('que abrigo queres agregar, marca y nombre ')
                abr = input('>>')
                print('precio')
                precio_abr = int(input('>>'))
                print('ingrese el stock')
                stock_abr = int(input('>>'))
                abrigo.append(abr)
                stock_abrigo.append(stock_abr)
                precio_abrigo.append(precio_abr)
            elif opcion2 == 5:
                print('que extra queres agregar, marca y nombre ')
                ext = input('>>')
                print('precio')
                precio_ext = int(input('>>'))
                print('ingrese el stock')
                stock_ext = int(input('>>'))
                extra.append(ext)
                stock_extra.append(stock_ext)
                precio_extra.append(precio_ext)
            elif opcion2 == 6:
                print('*******************************************************************************')
                print('remeras', remeras, 'stock', stock_remeras, 'precio', precio_remeras)
                print('pantalones', pantalones, 'stock', stock_pantalones, 'precio', precio_pantalones)
                print('zapatillas', zapatillas, 'stock', stock_zapatillas, 'precio', precio_zapatillas)
                print('abrigo', abrigo, 'stock', stock_abrigo, 'precio', precio_abrigo)
                print('extra', extra, 'stock', stock_extra, 'precio', precio_extra)
                print('*******************************************************************************')

            elif opcion2 == 7:
                print('******************************************************************************************')
                print('estas en modo comprador')
                while True:
                    opcion_comp = int(input('que quieres hacer \n>> 1 ver tienda\n>>2.comprar producto\n>>3.ver carrito'
                                            '\n>>4.agregar plata a la cartera\n>>5.salir\n>>'))
                    if opcion_comp == 1:
                        print('******************************************************************************')
                        print('remeras', remeras, 'stock', stock_remeras, 'precio', precio_remeras)
                        print('pantalones', pantalones, 'stock', stock_pantalones, 'precio', precio_pantalones)
                        print('zapatillas', zapatillas, 'stock', stock_zapatillas, 'precio', precio_zapatillas)
                        print('abrigo', abrigo, 'stock', stock_abrigo, 'precio', precio_abrigo)
                        print('extra', extra, 'stock', stock_extra, 'precio', precio_extra)
                        print('******************************************************************************')
                    elif opcion_comp == 2:
                        print('que producto quieres comprar \n>>1remeras\n>>2.zapatillas\n>>3.pantalones\n>>4.abrigo\n>>5.extra')
                        cosas = int(input('>>'))
                        # cosas son las opciones de comrpa
                        if cosas == 1:
                            print('remeras', remeras, 'stock', stock_remeras, 'precio', precio_remeras)
                            posicion1 = int(input('A que producto de la lista quieres comprar?'
                                                  '\n 0: primero \n 1: segundo\n etc\n>> '))
                            suma1 = int(input("Cuanto?\n>>"))
                            if stock_remeras[posicion1] >= suma1:
                                stock_remeras[posicion1] = stock_remeras[posicion1] - suma1
                                precio1 = precio_remeras[posicion1]
                                mult1 = int(precio1*suma1)
                                carrito += mult1

                                if stock_remeras == 0:
                                    remeras.remove(remeras[posicion1])
                                    precio_remeras.remove(precio_remeras[posicion1])

                            else:
                                print('no queda esa cantidad de stock,queda:', stock_remeras[posicion1])
                        elif cosas == 2:
                            print('zapatillas', zapatillas, 'stock', stock_zapatillas, 'precio', precio_zapatillas)
                            posicion2 = int(input('A que producto de la lista queres comprar?'
                                                  '\n 0: primero \n 1: segundo\n etc\n> '))
                            suma2 = int(input("Cuanto?\n>"))
                            if stock_zapatillas[posicion2] >= suma2:
                                stock_zapatillas[posicion2] = stock_zapatillas[posicion2] - suma2
                                precio2 = precio_zapatillas[posicion2]
                                carrito += precio2 * suma2
                            else:
                                print('no queda esa cantidad de stock,queda:', stock_zapatillas[posicion2])
                        elif cosas == 3:
                            print('pantalones', pantalones, 'stock', stock_pantalones, 'precio', precio_pantalones)
                            posicion3 = int(input('A que producto de la lista queres comprar?'
                                                  '\n 0: primero \n 1: segundo\n etc\n> '))
                            suma3 = int(input("Cuanto?\n>>"))
                            if stock_pantalones[posicion3] >= suma3:
                                stock_pantalones = stock_pantalones[posicion3] - suma3
                                precio3 = precio_pantalones[posicion3]
                                carrito += precio3 * suma3
                            else:
                                print('no queda esa cantidad de stock,queda:', stock_pantalones[posicion3])
                        elif cosas == 4:
                            print('abrigo', abrigo, 'stock', stock_abrigo, 'precio', precio_abrigo)
                            posicion4 = int(input('A que producto de la lista queres comprar?'
                                                  '\n 0: primero \n 1: segundo\n etc\n>> '))
                            suma4 = int(input("Cuanto?\n>>"))
                            if stock_abrigo[posicion4] >= suma4:
                                stock_abrigo = stock_abrigo[posicion4] - suma4
                                precio4 = precio_abrigo[posicion4]
                                carrito += suma4 * precio4
                            else:
                                print('no queda esa cantidad de stock,queda:', stock_abrigo[posicion4])
                        if cosas == 5:
                            print('extra', extra, 'stock', extra, 'precio', precio_extra)
                            posicion5 = int(input('A que producto de la lista queres comprar?'
                                                  '\n 0: primero \n 1: segundo\n etc\n>> '))
                            suma5 = int(input("Cuanto?\n>"))
                            if stock_extra[posicion5] >= suma5:
                                stock_extra = stock_extra[posicion5] - suma5
                                precio5 = extra[posicion5]
                                carrito += precio5 * suma5
                            else:
                                print('no queda esa cantidad de stock,queda:', stock_extra[posicion5])
                    elif opcion_comp == 3:

                        print('el precio final es :', carrito)
                        print('la plata en su cartera es de', plata_de_compador)
                        compra_final = str(input('quieres comprar todo lo del carrito\n>>'))
                        if compra_final == 'si':
                            if plata_de_compador >= carrito:
                                plata_de_compador = plata_de_compador - carrito
                                carrito = 0
                                print('gracias por su compra')
                                print('le queda', plata_de_compador, 'dolares')
                            else:
                                print('su saldo es insuficiente')
                        elif compra_final == 'no':
                            borrar_carrito = input('quieres eliminar todo el carrito\n>>')
                            if borrar_carrito == 'si':
                                carrito = 0

                    elif opcion_comp == 4:
                        print('cuanta plata quieres agregar max 5000 por pedido')
                        plata = int(input('>>'))
                        if plata <= 5000:
                            plata_de_compador += plata
                        else:
                            print('se ebsedio del maximo de ingreso de plata')
                    elif opcion_comp == 5:
                        break
            elif opcion2 == 8:
                break
else:
    print('el comando no es valido')