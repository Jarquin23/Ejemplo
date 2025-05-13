#Implemente un programa que simule el control de ventas de alimentos en tres kioscos dentro del campus UAM. Cada kiosco ofrece cinco productos diferentes y se registrarán las ventas durante cuatro días. El programa debe calcular y mostrar el total vendido por producto en cada kiosco, así como el total general por día.
productos = ["Tacos", "Bebidas", "Nacatamales", "Tortas", "Galletas"]
kioscos = ["Kiosco 1", "Kiosco 2", "Kiosco 3"]
ventas = {kiosco: {producto: 0 for producto in productos} for kiosco in kioscos}
total_general = {kiosco: 0 for kiosco in kioscos}
dias = 4
for dia in range(1, dias + 1):
    print(f"\nDía {dia}:")
    for kiosco in kioscos:
        print(f"\n{kiosco}:")
        for producto in productos:
            cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {producto}: "))
            precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))
            total_producto = cantidad_vendida * precio_unitario
            ventas[kiosco][producto] += total_producto
            total_general[kiosco] += total_producto
            print(f"Total vendido de {producto} en {kiosco}: {total_producto:.2f}")       