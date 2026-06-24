def mostrar_estudiante (lista_estudiante):
    for est in lista_estudiante:
        print(est)


print("-----AGREGAR ESTUDIANTE A LA ASIGNATURA-----")
estudiantes=[]
for i in range(3):
     rut  = input("Ingrese el rut: ")
     nombre = input("Ingrese nombre del alumno: ")
     edad=int(input("Ingrese la edad: "))
     carrera=input("Ingrese carrera: ")
     estudiante={"Rut": rut,
            "Alumno": nombre,
            "edad": edad,
            "Carrera": carrera
            }
     estudiantes.append(estudiante)


