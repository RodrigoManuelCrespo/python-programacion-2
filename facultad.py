class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        if nombre == "" or apellido == "" or matricula == "" or carrera == "":
            raise ValueError("Debe ingresar todos los datos solicitados")
        if not nombre.replace(" ", "").isalpha():
            raise ValueError("Nombre debe contener solo letras")
        if not apellido.replace(" ", "").isalpha():
            raise ValueError("Apellido debe contener solo letras")
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera


class Curso:
    def __init__(self, nombreCurso, codigoCurso, profesor, capacidadMaxima):
        if nombreCurso == "" or codigoCurso == "" or profesor == "":
            raise ValueError("Debe ingresar todos los datos solicitados")
        if capacidadMaxima <= 0:
            raise ValueError("La capacidad máxima debe ser mayor a cero")
        if not profesor.replace(" ", "").isalpha():
            raise ValueError("Profesor debe contener solo letras")
        self.nombreCurso = nombreCurso
        self.codigoCurso = codigoCurso
        self.profesor = profesor
        self.capacidadMaxima = capacidadMaxima
        self.estudiantesInscriptos = []


class Facultad:
    def __init__(self, estudiantes=None, cursos=None):
        self.estudiantes = estudiantes if estudiantes is not None else []
        self.cursos = cursos if cursos is not None else []

    def agregarEstudiante(self, nombre, apellido, matricula, carrera):
        if any(estudiante.matricula == matricula for estudiante in self.estudiantes):
            raise ValueError("Ya existe un estudiante con esa matrícula")
        nuevoEstudiante = Estudiante(nombre, apellido, matricula, carrera)
        self.estudiantes.append(nuevoEstudiante)
        print(f"Estudiante agregado correctamente: {nuevoEstudiante.nombre} {nuevoEstudiante.apellido}")

    def agregarCurso(self, nombreCurso, codigoCurso, profesor, capacidadMaxima):
        if any(curso.codigoCurso == codigoCurso for curso in self.cursos):
            raise ValueError("Ya existe un curso con ese código")
        nuevoCurso = Curso(nombreCurso, codigoCurso, profesor, capacidadMaxima)
        self.cursos.append(nuevoCurso)
        print(f"Curso agregado correctamente: {nuevoCurso.nombreCurso}")

    def mostrarEstudiantes(self):
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados")
            return
        print(f"\n******\nListado de estudiantes:\n******")
        for estudiante in self.estudiantes:
            print(f"Nombre: {estudiante.nombre} {estudiante.apellido} | Matrícula: {estudiante.matricula} | Carrera: {estudiante.carrera}")

    def mostrarCursos(self):
        if len(self.cursos) == 0:
            print("No hay cursos registrados")
            return
        print(f"\n******\nListado de cursos:\n******")
        for curso in self.cursos:
            print(f"Curso: {curso.nombreCurso} | Código: {curso.codigoCurso} | Profesor: {curso.profesor}")

    def buscarCurso(self, codigoCurso):
        if codigoCurso == "":
            raise ValueError("Debe ingresar el código del curso")
        for curso in self.cursos:
            if curso.codigoCurso == codigoCurso:
                return curso
        raise ValueError("No existe un curso con ese código")

    def buscarEstudiante(self, matricula):
        if matricula == "":
            raise ValueError("Debe ingresar la matrícula del estudiante")
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                return estudiante
        raise ValueError("No existe un estudiante con esa matrícula")

    def inscribirEstudiante(self, matricula, codigoCurso):
        estudiante = self.buscarEstudiante(matricula)
        curso = self.buscarCurso(codigoCurso)
        if len(curso.estudiantesInscriptos) >= curso.capacidadMaxima:
            raise ValueError("No hay cupos disponibles")
        if estudiante.matricula in curso.estudiantesInscriptos:
            raise ValueError("El estudiante ya está inscripto")
        curso.estudiantesInscriptos.append(estudiante.matricula)
        print("Estudiante inscripto correctamente")

    def bajaCurso(self, matricula, codigoCurso):
        estudiante = self.buscarEstudiante(matricula)
        curso = self.buscarCurso(codigoCurso)
        if estudiante.matricula not in curso.estudiantesInscriptos:
            raise ValueError("El estudiante no está inscripto en este curso")
        curso.estudiantesInscriptos.remove(matricula)
        print("Baja realizada correctamente")

    def consultarEstadoCursos(self):
        if len(self.cursos) == 0:
            print("No hay cursos registrados")
            return
        print(f"\n******\nEstado de cursos:\n******")
        for curso in self.cursos:
            cantidadInscriptos = len(curso.estudiantesInscriptos)
            cuposDisponibles = curso.capacidadMaxima - cantidadInscriptos
            print(f"Curso: {curso.nombreCurso} | Código: {curso.codigoCurso} | Inscriptos: {cantidadInscriptos} | Cupos disponibles: {cuposDisponibles}")

    def buscarCursosPorEstudiante(self, matricula):
        self.buscarEstudiante(matricula)
        cursosEstudiante = []
        for curso in self.cursos:
            if matricula in curso.estudiantesInscriptos:
                cursosEstudiante.append(curso)
        if len(cursosEstudiante):
            for curso in cursosEstudiante:
                print(f"- Curso: {curso.nombreCurso}")
        else:
            print("No está inscripto en ningún curso")

    def consultarEstadoEstudiantes(self):
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados")
            return
        print(f"\n******\nEstado de estudiantes:\n******")
        for estudiante in self.estudiantes:
            print(f"\nEstudiante: {estudiante.nombre} {estudiante.apellido} | Matrícula: {estudiante.matricula} | Carrera: {estudiante.carrera}")
            self.buscarCursosPorEstudiante(estudiante.matricula)


def menu():
    facultad = Facultad()
    print("Bienvenido al Sistema de Facultad")

    while True:
        print("\nIngrese una opción:")
        print("0 - Salir")
        print("1 - Agregar estudiante")
        print("2 - Agregar curso")
        print("3 - Mostrar estudiantes")
        print("4 - Mostrar cursos")
        print("5 - Inscribir estudiante")
        print("6 - Dar baja de curso")
        print("7 - Consultar estado de cursos")
        print("8 - Consultar estado de estudiantes")
        opcion = input("Opción: ")

        try:
            if opcion == "0":
                print("Programa finalizado")
                break

            elif opcion == "1":
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
                matricula = input("Ingrese matrícula: ")
                carrera = input("Ingrese carrera: ")
                facultad.agregarEstudiante(nombre, apellido, matricula, carrera)

            elif opcion == "2":
                nombreCurso = input("Ingrese nombre del curso: ")
                codigoCurso = input("Ingrese código del curso: ")
                profesor = input("Ingrese profesor: ")
                capacidadMaxima = int(input("Ingrese capacidad máxima: "))
                facultad.agregarCurso(nombreCurso, codigoCurso, profesor, capacidadMaxima)

            elif opcion == "3":
                facultad.mostrarEstudiantes()

            elif opcion == "4":
                facultad.mostrarCursos()

            elif opcion == "5":
                matricula = input("Ingrese matrícula del estudiante: ")
                codigoCurso = input("Ingrese código del curso: ")
                facultad.inscribirEstudiante(matricula, codigoCurso)

            elif opcion == "6":
                matricula = input("Ingrese matrícula del estudiante: ")
                codigoCurso = input("Ingrese código del curso: ")
                facultad.bajaCurso(matricula, codigoCurso)

            elif opcion == "7":
                facultad.consultarEstadoCursos()

            elif opcion == "8":
                facultad.consultarEstadoEstudiantes()

            else:
                print("Opción inválida")

        except ValueError as e:
            print(f"\n******\nError: {e}\n******")

        except Exception as e:
            print(f"\n******\nError inesperado: {e}\n******")


menu()