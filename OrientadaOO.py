class Persona:
    def __init__(self, nombre, apellido, año_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.año_nacimiento = int(año_nacimiento)
        
    def calcuedad(self):
        return 2025 - self.año_nacimiento
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.calcuedad()} años) - Nacido en: {self.año_nacimiento}"
class Estudiante(Persona):
    def __init__(self, nombre, apellido, año_nacimiento):
        super().__init__(nombre, apellido, año_nacimiento)
        self.asignaturas = []
    def nuevaasig(self, asignatura):
        self.asignaturas.append(asignatura)
    def mostrarasigna(self):
        for a in self.asignaturas:
            print(a)
    def profesores(self):
        res = []
        for a in self.asignaturas:
            if a.profesor and a.profesor.nombre not in res:
                res.append(a.profesor.nombre)
        """ for p in res:
            print(p) """
        return res
class Profesor(Persona):
    def __init__(self, nombre, apellido, año_nacimiento):
        super().__init__(nombre, apellido, año_nacimiento)
        self.imparte = []
    def __str__(self):
        imparte_str = ", ".join(str(a) for a in self.imparte)
        return f"{super().__str__()} Imparte: {imparte_str}"
class Asignatura:
    def __init__(self, nombre, nhoras):
        self.nombre = nombre
        self.nhoras = nhoras
        self.profesor = None
    def __str__(self):
        return f"{self.nombre} ({self.nhoras}h)"
class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def nuevoestudiante(self, estudiante):
        if estudiante.nombre not in [e.nombre for e in self.alumnos]:
            self.alumnos.append(estudiante)
    def mostrar_alumnos(self):
        for e in self.alumnos:
            print(e.nombre, e.apellido)

                

miguel = Persona('Miguel', 'Pulido', 2005)
ruben = Estudiante('Ruben', 'Lopez', 2006)
diego = Profesor('Diego', 'La Cabra', 1960)
ana = Profesor('Ana', 'Gomez', 1980)
servidor = Asignatura('Servidor', 25)
bbdd = Asignatura('BBDD', 7)
despliegue = Asignatura('Despliegue', 2)
diego.imparte.append(bbdd)
bbdd.profesor = diego
ana.imparte.append(servidor)
ana.imparte.append(despliegue)
servidor.profesor = ana
despliegue.profesor = ana


ruben.nuevaasig(servidor)
ruben.nuevaasig(bbdd)

print(miguel)
ruben.mostrarasigna()
print(diego)
print(ana)       

print("Profesores de Ruben:")
ruben.profesores()

segundodaw = Grupo('2Daw')

print(segundodaw)

