import time;

#DECLARACION DE VARIABLES

#VARIABLES CONTADORES
c_handroll_pollo = int(0)
c_handroll_carne = int(0)
c_handroll_vegano = int(0)
c_handroll_4estaciones = int(0)
c_sushi_burger = int(0)
c_promo_30 = int(0)
c_promo_40 = int(0)
c_promo_50 = int(0)
v_opcion = int(0)
total_pedido = int(0)

print(" ")
print("==================================================================")
print("BIENVENIDO AL SISTEMA DE COMANDA DE SUSHINITO")
print("==================================================================")
print(" ")
time.sleep(1)

nombre_cliente = str(input("Por favor, ingrese el nombre del cliente: \n "))
rut_cliente = str(input("Por favor, ingrese el rut del cliente: \n"))
direccion_cliente = str(input("Por favor, ingrese la direccion del cliente: \n"))
fono_cliente = str(input("Por favor, ingrese el fono del cliente: \n"))
time.sleep(2)

while v_opcion != 10:
    print("==================================================================")
    print("MENU DE COMANDA")
    print("==================================================================")
    print(" ")
    print("1) Handroll Pollo")
    print("2) Handroll Carne")
    print("3) Handroll Vegano")
    print("4) Handroll 4 Estaciones")
    print("5) Sushi Burger")
    print("6) Promocion 30 Cortes Frios")
    print("7) Promocion 40 Cortes Frios")
    print("8) Promocion 50 Cortes Mixtos")
    print("9) Imprimir Comanda")
    print("10) Salir del sistema") 
    print(" ")

    v_opcion = int(input("INGRESE LA OPCION DESEADA: "))

    if v_opcion == 1:
        c_handroll_pollo = c_handroll_pollo + 1
        total_pedido = total_pedido + 2990
    if v_opcion == 2:
        c_handroll_carne = c_handroll_carne + 1
        total_pedido = total_pedido + 3490
    if v_opcion == 3:
        c_handroll_vegano = c_handroll_vegano + 1
        total_pedido = total_pedido + 3490
    if v_opcion == 4:
        c_handroll_4estaciones = c_handroll_4estaciones + 1
        total_pedido = total_pedido + 3990
    if v_opcion == 5:
        c_sushi_burger = c_sushi_burger + 1
        total_pedido = total_pedido + 5490
    if v_opcion == 6:
        c_promo_30 = c_promo_30 + 1
        total_pedido = total_pedido + 7990
    if v_opcion == 7:
        c_promo_40 = c_promo_40 + 1
        total_pedido = total_pedido + 8990
    if v_opcion == 8:
        c_promo_50 = c_promo_50 + 1
        total_pedido = total_pedido + 10990
    if v_opcion == 9:
        print("==============================================")
        print("COMANDA PEDIDO SUSHINITO")
        print("==============================================")
        print(" ")
        print("DATOS DEL CLIENTE\n")
        print("NOMBRE CLIENTE: ",nombre_cliente)
        print("RUT CLIENTE: ",rut_cliente)
        print("DIRECCION CLIENTE: ",direccion_cliente)
        print("FONO CLIENTE",fono_cliente)
        print(" ")
        print("==============================================")
        print("DETALLE PEDIDO")
        print("---------------------------------------------------------")
        print("VALOR TOTAL PEDIDO",total_pedido)
        print("---------------------------------------------------------")
        if c_handroll_pollo !=0:
            print("CANTIDAD DE HANDROLL'S DE POLLO: ",c_handroll_pollo)
        if c_handroll_carne !=0:
            print("CANTIDAD DE HANDROLL'S DE CARNE: ",c_handroll_carne)
        if c_handroll_vegano !=0:
            print("CANTIDAD DE HANDROLL'S VEGANOS: ",c_handroll_vegano)
        if c_handroll_4estaciones !=0:
            print("CANTIDAD DE HANDROLL'S 4 ESTACIONES: ",c_handroll_4estaciones)
        if c_sushi_burger !=0:
            print("CANTIDAD DE SUSHI BURGER'S: ",c_sushi_burger)
        if c_promo_30 !=0:
            print("CANTIDAD DE PROMO SUSHI 30 CORTES FRIOS: ",c_promo_30)
        if c_promo_40 !=0:
            print("CANTIDAD DE PROMO SUSHI 40 CORTES FRIOS: ",c_promo_40)
        if c_promo_50 !=0:
            print("CANTIDAD DE PROMO SUSHI 50 CORTES MIXTOS: ",c_promo_50)
        
        time.sleep(3)
    if v_opcion == 10:
        print("---------------------------------------------------------")
        print("MUCHAS GRACIAS POR UTILIZAR EL SISTEMA DE COMANDA")
        print("---------------------------------------------------------")
        exit(1)
    time.sleep(1)
