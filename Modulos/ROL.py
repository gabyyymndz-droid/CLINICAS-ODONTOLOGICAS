from datetime import date

class Rol:
    def __init__(self, idRol: str, nombreRol: str, Descripcion: str):
        self.idRol = idRol
        self.nombreRol = nombreRol
        self.Descripcion = Descripcion

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Rol): 
            return NotImplementedError("Operación no permitida: los tipos de datos no son iguales")
        return self.idRol == otro.idRol

    def validacion_rol(self, lista_roles: list) -> list:
        errores = []

        if not self.idRol or not str(self.idRol).strip():
            errores.append("El ID del Rol no puede estar vacio")
        if self in lista_roles: 
            errores.append(f"El rol {self.idRol} ya existe en el sistema")

        return errores