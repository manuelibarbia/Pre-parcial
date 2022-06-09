class Alumno:

    def __init__(self, nombre, dni, hermanos = 0) -> None:
        self.nombre = nombre
        self.dni = dni
        self.legajo = self.generar_legajo(dni)
        self.hermanos = hermanos

    def generar_legajo(self, dni):
        primeros_digitos = str(dni)[:3]
        return('ALU_'+primeros_digitos)

    def completar_materias(self):
        self.materias = []
        materias = int(input("Cantidad de materias: "))
        for x in range(materias):
            self.materias.append(input("Ingrese materia: "))
    
    def registrar_notas(self):
        aprobadas = []
        for materia in self.materias:
            nota = float(input("¿Qué nota sacaste en " + materia + "? "))
            if nota >=6:
                aprobadas.append(materia)
        for aprobada in aprobadas:
            self.materias.remove(aprobada)
        if len(self.materias) == 0:
            print("Todas las materias están aprobadas.")
        elif len(self.materias) == 1:
            print("La materia pendiente es: " + str(self.materias))
        else:
            print("Las materias pendientes son: " + str(self.materias))

alu = Alumno("Javier", 44332445, 5)
alu.completar_materias()
alu.registrar_notas()
