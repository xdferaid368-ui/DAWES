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

