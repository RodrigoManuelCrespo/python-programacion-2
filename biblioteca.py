class Libro:
    def __init__(self, titulo, autor, isbn, disponibilidad = True, prestadoA = False):
        if titulo == "" or autor == "" or isbn == "":
            raise ValueError("Debe ingresar todo los datos solicitados.")
        else: 
            self.titulo = titulo
            self.autor = autor
            self.isbn = isbn
            self.disponibilidad = disponibilidad
            self.prestadoA = prestadoA

    def modificarEstado(self, disponibilidad, prestadoA = False):
        self.disponibilidad = disponibilidad
        self.prestadoA = prestadoA

class Miembros:
    def __init__(self, nombre, dni):
        if nombre == "" or dni == "":
            raise ValueError("Nombre y DNI no pueden estar vacíos")
        if len(dni) < 8 or not dni.isdigit():
            raise ValueError("DNI debe tener 8 digitos numericos")
        if not nombre.replace(" ", "").isalpha():
            raise ValueError("Nombre debe contener solo letras")
        self.nombre = nombre
        self.dni = dni

class Biblioteca: 
    def __init__(self, miembros=None, libros=None):
        self.miembros = miembros if miembros is not None else []
        self.libros = libros if libros is not None else []

    def agregarMiembro(self, nombre, dni):
        if any(miembro.dni == dni for miembro in self.miembros):
            raise ValueError("Ya existe un miembro con ese DNI")
        nuevoMiembro = Miembros(nombre, dni)
        self.miembros.append(nuevoMiembro)
        print(f"Miembro creado con éxito: {nuevoMiembro.nombre} | (DNI: {nuevoMiembro.dni})")

    def agregarLibro(self, titulo, autor, isbn):
            if  any(libro.isbn == isbn for libro in self.libros):
                raise ValueError("Ya existe un libro con ese ISBN")
            nuevoLibro = Libro(titulo, autor, isbn)
            print(f"Libro agregado a la biblioteca: {nuevoLibro.titulo}")
            self.libros.append(nuevoLibro)

    def mostrarLibros(self):
        if len(self.libros) == 0:
            print("No hay libros en esta biblioteca")
            return
        print(f"\n******\nListado de libros:\n******")
        for libro in self.libros:
            print(f"Titulo: {libro.titulo} | Autor: {libro.autor} | ISBN: {libro.isbn}") 

    def mostrarMiembros(self):
        if len(self.miembros) == 0:
            print("No hay miembros cargados")
            return
        print(f"\n******\nListado de miembros:\n******")
        for miembro in self.miembros:
                print(f"Nombre: {miembro.nombre} | DNI: {miembro.dni}")


    def prestarLibro(self, dniMiembro, isbn):
        if not any(str(miembro.dni) == str(dniMiembro) for miembro in self.miembros):
            raise ValueError("No existe un miembro con ese DNI registrado")
        libro = self.buscarLibro(isbn)
        if not libro.disponibilidad:
            raise ValueError("El libro no se encuentra disponible")
        libro.modificarEstado(False, dniMiembro)
        print(f"Libro '{libro.titulo}' prestado correctamente")

    def devolverLibro(self, isbn):
        libro = self.buscarLibro(isbn)        
        if libro.disponibilidad:
            raise ValueError("No se puede modificar el estado, el libro ya se encuentra en la biblioteca")
        libro.modificarEstado(True)
        print("Libro devuelto correctamente")

    def buscarLibro(self, isbn):
        if isbn == "":
            raise ValueError("Debe ingresar el ISBN del libro")
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        raise ValueError("No existe un libro con ese ISBN en la biblioteca")

    def buscarLibrosPorMiembro(self, dni):
        if not any(miembro.dni == dni for miembro in self.miembros):
            raise ValueError("No existe un miembro con ese DNI")
        librosMiembro = []
        for libro in self.libros:
            if libro.prestadoA == dni:
                librosMiembro.append(libro)
        if len(librosMiembro):
            for libro in librosMiembro:
                print(f"- Libro: {libro.titulo}")  
        else:
            print("No tiene libros prestados")

    def consultarEstadoLibros(self):
            if len(self.libros) == 0:
                print("No hay libros cargados")
            else:
                print(f"\n******\nEstado de libros:\n******")
                for libro in self.libros:
                    if libro.disponibilidad:
                        print(f"Titulo: {libro.titulo} | Estado: Disponible")
                    else:
                        print(f"Titulo: {libro.titulo} | Estado: Prestado | DNI del miembro: {libro.prestadoA}")

    def consultarEstadoMiembros(self):
            if len(self.miembros) == 0:
                print("No hay miembros registrados")
                return
            print(f"\n******\nEstado de miembros:\n******")
            for miembro in self.miembros:
                print(f"\nMiembro: {miembro.nombre} | DNI: {miembro.dni}")
                self.buscarLibrosPorMiembro(miembro.dni)

def menu():
    biblioteca = Biblioteca()
    print("Bienvenido a la Biblioteca")

    while True:
        print("\nIngrese una opcion:")
        print("0 - Salir")
        print("1 - Agregar libro")
        print("2 - Agregar miembro")
        print("3 - Mostrar libros")
        print("4 - Mostrar miembros")
        print("5 - Prestar libro")
        print("6 - Devolver libro")
        print("7 - Consultar estado de libros")
        print("8 - Consultar estado de miembros")
        opcion = input("Opción: ")
        try:
            if opcion == "0":
                print("Programa finalizado")
                break
            elif opcion == "1":
                titulo = input("Ingrese titulo: ")
                autor = input("Ingrese autor: ")
                isbn = input("Ingrese ISBN: ")
                biblioteca.agregarLibro(titulo, autor, isbn)

            elif opcion == "2":
                dni = input("Ingrese DNI: ")
                nombre = input("Ingrese nombre: ")
                biblioteca.agregarMiembro(nombre, dni)

            elif opcion == "3":
                biblioteca.mostrarLibros()

            elif opcion == "4":
                biblioteca.mostrarMiembros()

            elif opcion == "5":
                dni = input("Ingrese DNI del miembro: ")
                isbn = input("Ingrese ISBN del libro: ")
                biblioteca.prestarLibro(dni, isbn)

            elif opcion == "6":
                isbn = input("Ingrese ISBN del libro: ")
                biblioteca.devolverLibro(isbn)

            elif opcion == "7":
                biblioteca.consultarEstadoLibros()

            elif opcion == "8":
                biblioteca.consultarEstadoMiembros()

            else:
                print("Opción inválida")

        except ValueError as e:
            print(f"\n******\nError: {e}\n******")

        except Exception as e:
            print(f"\n******\nError inesperado: {e}\n******")

menu()


