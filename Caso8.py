#Caso 8: Registro de consumo eléctrico por edificio en la UAM
#Desarrolle un programa que permita registrar el consumo eléctrico de cinco edificios del campus
#UAM (como aulas, biblioteca, administración, laboratorios y cafetería) durante tres turnos del
#día (mañana, tarde y noche), por una semana. El programa debe mostrar el consumo por edificio
#y el total general semanal.

edificios = ["Aulas", "Biblioteca", "Administración", "Laboratorios", "Cafetería"]

turnos = ["Mañana", "Tarde", "Noche"]

total_general = 0

for edificio in edificios:
    print(f"\n Edificio: {edificio}")
    
    total_edificio = 0 

    for dia in range(1, 8):
        print(f"   Día {dia}:")
        
        for turno in turnos:
            while True:
                try:
                    consumo = float(input(f"Ingrese el consumo en kWh para el turno {turno}: "))
                    if consumo < 0:
                        print("El consumo no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")

            total_edificio += consumo
            total_general += consumo

    print(f" Total semanal del edificio {edificio}: {total_edificio:.2f} kWh")

print(f"\n CONSUMO TOTAL DE TODOS LOS EDIFICIOS: {total_general:.2f} kWh")
