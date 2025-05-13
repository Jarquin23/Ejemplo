#Cree un programa que simule la venta de nacatamales durante cuatro domingos consecutivos en actividades realizadas en la UAM (como torneos, convivencias o ferias). Por cada domingo, se deberá registrar la cantidad de clientes y cuántos nacatamales compró cada uno. El programa debe calcular el total vendido por domingo y el acumulado mensual. Utilice bucles anidados para domingos y clientes.
venta_nacatamales= int(input("Ingrese la cantidad de nacatamales vendidos: "))
acumulador=0
for domingo in range(1, 5):
        print(f"Domingo {domingo}:")
        cantidad_clientes = int(input("Ingrese la cantidad de clientes atendidos: "))
        total_domingo = 0
        for cliente in range(1, cantidad_clientes + 1):
            nacatamales = int(input(f"Ingrese la cantidad de nacatamales comprados por el cliente {cliente}: "))
            precio_unitario = float(input(f"Ingrese el precio unitario por nacatamal para el cliente {cliente}: "))
            total_cliente = nacatamales * precio_unitario
            total_domingo += total_cliente
            print(f"Total pagado por el cliente {cliente}: {total_cliente:.2f}")
        print(f"Total vendido en el domingo {domingo}: {total_domingo:.2f}")
        acumulador += total_domingo