#Desarrolle un programa que permita simular la venta de vigorón durante una feria gastronómica organizada en la Universidad Americana, UAM Managua. El sistema debe solicitar la cantidad de clientes atendidos y, por cada cliente, cuántas porciones de vigorón compró, junto con el precio unitario por porción. El programa debe calcular el total pagado por cada cliente y mostrar el total de ventas de toda la feria. Utilice estructuras cíclicas anidadas. 
# El programa debe permitir al usuario ingresar la cantidad de clientes atendidos y, por cada cliente, cuántas porciones de vigorón compró, junto con el precio unitario por porción.
# El programa debe calcular el total pagado por cada cliente y mostrar el total de ventas de toda la feria. Utilice estructuras cíclicas anidadas.
num_clientes = int(input("Ingrese la cantidad de clientes atendidos: "))
total_ventas = 0
for num_clientes in range(num_clientes):
    porciones = int(input(f"Ingrese la cantidad de porciones compradas por el cliente {num_clientes+1}: "))
    precio_unitario = float(input(f"Ingrese el precio unitario por porción para el cliente {num_clientes+1}: "))
    total_cliente = porciones * precio_unitario
    total_ventas += total_cliente
    print(f"Total pagado por el cliente {num_clientes+1}: {total_cliente:.2f}")
print(f"Total de ventas de toda la feria: {total_ventas:.2f}")