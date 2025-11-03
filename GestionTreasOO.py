import json
class Tarea:
    def __init__(self, titulo, descripcion, prioridad, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def marcar_completada(self):
        self.completada = True
    def actualizar(self, titulo = None, descripcion = None, prioridad = None, fecha_vencimiento = None):
        if(titulo is not None):
            self.titulo = titulo
        if(descripcion is not None):
            self.descripcion = descripcion
        if(prioridad is not None):
            if prioridad in ['Baja','Media','Alta']:
                self.prioridad = prioridad
            else:
                print('QUE HACE QUILLO ESO NO ES UNA PRIORIDAD')
        if(fecha_vencimiento is not None):
            self.fecha_vencimiento = fecha_vencimiento
    def mostrar_informacion(self):
        if(self.completada):
            estado = 'Completada'
        else:
            estado = 'Pendiente'
        return (
            f'Titulo: {self.titulo}\n'
            f'descripcion:{self.descripcion}\n'
            f'prioridad:{self.prioridad}\n'
            f'fecha_vencimiento{self.fecha_vencimiento}\n'
            f'estado{estado}\n'
        )
class GestorTareas : 
    def __init__(self):
        self.listtareas = []
    def agregar_tarea(self,tarea):
        self.listtareas.append(tarea)
    def eliminar_tarea(self,tarea):
        if tarea in self.listtareas:
            self.listtareas.remove(tarea)
            print(f"Tarea '{tarea.titulo}' eliminada correctamente.")
        else:
            print('Machote esta tarea no existe')
    def actualizar_tarea(self, tarea, titulo = None, descripcion = None, prioridad = None, fecha_vencimiento = None ):
        if tarea in self.listtareas:
            tarea.actualizar(titulo,descripcion,prioridad,fecha_vencimiento)
            print(f"La Tarea '{tarea.titulo}' ha sido actualizada")
        else:
            print('La tarea no existe maquina')
    def listar_tareas(self,):
        for tareilla in self.listtareas:
            print(tareilla.mostrar_informacion())
    def guardar_tareas(self, nombre_archivo = "tareas.json"):
        lista = []
        for tarea in self.listtareas:
            tarea_dict = {
                "Titulo" : tarea.titulo,
                "Descripcion" : tarea.descripcion,
                "Prioridad" : tarea.prioridad,
                "Fecha Vencimiento" : tarea.fecha_vencimiento,
                "Completada" : tarea.completada
                }
            lista.append(tarea_dict)
        with open(nombre_archivo, "w") as f:
            json.dump(lista, f, indent=4)
        
        print('Tareas Guardadas en el archivo')
    def cargar_tareas(self, nombre_archivo="tareas.json"):
        try:
            with open(nombre_archivo, "r") as f:
                lista = json.load(f)

            self.listtareas = []  # limpiar lista antes de cargar
            for tarea_dict in lista:
                t = Tarea(
                    tarea_dict['Titulo'],
                    tarea_dict['Descripcion'],
                    tarea_dict['Prioridad'],
                    tarea_dict['Fecha Vencimiento'],
                )
                t.completada = tarea_dict['Completada']
                self.listtareas.append(t)

            print(f"Tareas cargadas desde {nombre_archivo}")

        except FileNotFoundError:
            print("No se encontró el archivo de tareas. Se creará uno nuevo al guardar.")

def menu():
    gestor = GestorTareas()
    while True:
        print('\n 1.Añadir nueva tarea')
        print('2.Marcar tarea completada')
        print('3.Actualizar tarea')
        print('4.Ver Tareas Pendientes')
        print('5.Ver Tareas Completadas')
        print('6.Guardar Tareas')
        print('7.cargar Tareas')
        print('8.Salir')
        opcion = input('Elige una opcion maquina')
        match opcion:
            case '1':
                titulo = input('Introduzca el titulo de la tarea: ')
                descripcion = input('Introduzca la descripcion de la tarea: ')
                prioridad = input('Introduzca la Prioridad de la Tarea(Alta Medio o Baja): ')
                fecha_vencimiento = input('Introduzca la fecha de vencimiento de la tarea: ')

                nueva_tarea = Tarea(titulo,descripcion,prioridad,fecha_vencimiento)

                gestor.agregar_tarea(nueva_tarea)

                print('Tarea Agregada Correctamente')
            case '2':
                titulo = input('Introduce el Titulo de la Tarea: ')

                tarea_encontrada = None
                for tarea in gestor.listtareas:
                    if tarea.titulo == titulo:
                        tarea_encontrada = tarea
                        break
                if tarea_encontrada:
                    tarea_encontrada.marcar_completada()
                    print('Marcada como completa')
                else:
                    print('No existe Tarea con ese titulo')
            case'3':
                tarea_encontrada = None
                for tarea in gestor.listtareas:
                    if tarea.titulo == titulo:
                        tarea_encontrada = tarea
                        break
                if tarea_encontrada:
                    print('Introduzca los valores a cambiar NO DEJE VALORES EN BLANCO')
                    nuevo_titulo = input('Nuevo titulo: ')
                    if nuevo_titulo == "":
                        nuevo_titulo = None
                    nuevo_descripcion = input('Nueva descripcion: ')
                    nuevo_prioridad = input('Nuevo prioridad ')
                    nuevo_fecha_vencimiento = input('Nueva Fecha de vencimiento: ')
                
                    tarea_encontrada.actualizar(
                        titulo=nuevo_titulo,
                        descripcion=nuevo_descripcion,
                        prioridad=nuevo_prioridad,
                        fecha_vencimiento=nuevo_fecha_vencimiento,
                    )
                    print('Tarea Actualizada')
                else:
                    print('Tarea No encontrada')
            case'4':
                tareas_pendientes = [t for t in gestor.listtareas if not t.completada]

                if tareas_pendientes:
                    for t in tareas_pendientes:
                        print(t.mostrar_informacion())
                else:
                    print('No tienes tareas pendientes maquinober')
            case'5':
                tareas_completadas = [t for t in gestor.listtareas if t.completada]

                if tareas_completadas:
                    for t in tareas_completadas:
                        print(t.mostrar_informacion())
                else:
                    print('No tienes Tareas Completadas machote')
            case'6':
                gestor.guardar_tareas()
                print('Tareas Guardadas Macho')
            case'7':
                gestor.cargar_tareas()
            case'8':
                print('Adios Maestro')
                break

if __name__ == '__main__':
    menu()
