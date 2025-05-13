#Elabore un programa que procese las calificaciones de varios estudiantes de la carrera de Ingeniería en Sistemas de la Información en la UAM. Por cada estudiante, se ingresarán las calificaciones de tres asignaturas, y cada asignatura incluirá tres tareas y un examen. El programa debe calcular el promedio por asignatura y el promedio general del estudiante. Utilice estructuras cíclicas anidadas para manejar estudiantes, asignaturas y evaluaciones. 

calificaciones = []
num_estudiantes = int(input("Ingrese el número de estudiantes: "))
for i in range(num_estudiantes):
    print(f"\nEstudiante {i + 1}:")
    estudiante_calificaciones = []
    for j in range(3):  # 3 asignaturas
        print(f"Asignatura {j + 1}:")
        tareas = []
        for k in range(3):  # 3 tareas
            tarea = float(input(f"Ingrese la calificación de la tarea {k + 1}: "))
            tareas.append(tarea)
        examen = float(input("Ingrese la calificación del examen: "))
        
        promedio_asignatura = (sum(tareas) + examen) / 4
        estudiante_calificaciones.append(promedio_asignatura)
    
    promedio_general = sum(estudiante_calificaciones) / len(estudiante_calificaciones)
    calificaciones.append((estudiante_calificaciones, promedio_general))