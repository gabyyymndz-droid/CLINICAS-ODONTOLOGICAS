class Especialidad:
    def __init__(self, idEspecialidad: str, especialidadDescripcion: str):
        self.idEspecialidad = idEspecialidad
        self.especialidadDescripcion = especialidadDescripcion
        self.doctores_registrados: list = [] 

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Especialidad): 
            return NotImplemented
        return self.idEspecialidad == otro.idEspecialidad

    def validacion_especialidad(self, lista_especialidades: list) -> list:
        errores = []
        if not self.idEspecialidad or not str(self.idEspecialidad).strip():
            errores.append("El ID de la especialidad no puede estar vacio")
        if self in lista_especialidades: 
            errores.append(f"La especialidad {self.idEspecialidad} ya existe")

        return errores