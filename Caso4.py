#Caso 4: Registro de participación estudiantil por carrera en la UAM
#Desarrolle un programa que registre la participación de estudiantes de la UAM en actividades
#Derecho), cada una con tres años académicos, y cada año con dos secciones. Por cada
#sección, se debe registrar cuántos estudiantes participaron. El programa debe mostrar el total
#por carrera y el total general de participantes. Utilice bucles anidados.


carreras = ["Sistemas", "Marketing", "Derecho"]
total_general = 0

for carrera in carreras:
    print(f"\nIngresando datos para la carrera: {carrera}")
    
    total_carrera = 0
    
    for anio in range(1, 4):  
        print(f"  Año {anio}")
    
        for seccion in range(1, 3): 
            while True:
                try:
                    
                    cantidad = int(input(f"    Ingrese la cantidad de participantes en {carrera} - Año {anio} - Sección {seccion}: "))
                    if cantidad < 0:
                        print("     La cantidad no puede ser negativa. Intente de nuevo.")
                        continue
                    break
                except ValueError:
                    print("     Entrada inválida. Ingrese un número entero.")
            
            total_carrera += cantidad
            total_general += cantidad
    
    print(f" Total de participantes en la carrera {carrera}: {total_carrera}")

print(f"\n TOTAL GENERAL DE PARTICIPANTES EN TODAS LAS CARRERAS: {total_general}")
