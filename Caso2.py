#Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
#primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
#ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
#gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
#semanas y días.

semana = 1
total_mes = 0

while semana <= 4:
    print(f"\nSemana {semana}")
    dia = 1
    total_semana = 0

    while dia <= 7:
        gasto = float(input(f"  Día {dia} - Ingrese el gasto: "))
        total_semana += gasto
        dia += 1

    print(f"  Total semana {semana}: {total_semana:.2f}")
    total_mes += total_semana
    semana += 1

print(f"\nTotal gastado en el mes: {total_mes:.2f}")

