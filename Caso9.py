#Implemente un programa que simule una encuesta realizada a estudiantes de la UAM para
#conocer su acceso a internet en casa. Se trabajará con tres carreras, cada una con tres grupos,
#y se entrevistará a cinco estudiantes por grupo. Se debe registrar si el estudiante tiene acceso
#estable, intermitente o no tiene internet. Al final, mostrar un conteo de cada tipo de acceso por
#carrera y el total general.
accesos = ['estable', 'intermitente', 'no tiene']
total_general = {a: 0 for a in accesos}

for carrera in range(1, 4):
    print(f"\nCarrera {carrera}")
    total_carrera = {a: 0 for a in accesos}

    for grupo in range(1, 4):
        for estudiante in range(1, 6):
            while True:
                resp = input(f"Grupo {grupo} - Estudiante {estudiante} ({accesos}): ").lower()
                if resp in accesos:
                    break
                print("Opción no válida, intenta otra vez.")
            total_carrera[resp] += 1
            total_general[resp] += 1

    print(f"Totales Carrera {carrera}:")
    for a in accesos:
        print(f"  {a.capitalize()}: {total_carrera[a]}")

print("\nTotal General:")
for a in accesos:
    print(f"{a.capitalize()}: {total_general[a]}")
