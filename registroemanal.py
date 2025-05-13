num_estudiantes= int(input("Ingrese la cantidad de estudiantes registrados: "))
registro=[]
for num_estudiantes in range(num_estudiantes):
    nombre=input("Ingrese el nombre del estudiante: ")
    edad=int(input("Ingrese la edad del estudiante: "))
    carrera=input("Ingrese la carrera del estudiante: ")
    registro.append((nombre,edad,carrera))
