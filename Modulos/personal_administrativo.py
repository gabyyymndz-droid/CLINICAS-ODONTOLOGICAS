from Modulos.rol import Rol

class PersonalAdministrativo:
    def __init__(self, idPersonalAdministrativo: str, nombrePersonalAdministrativo: str, rol: Rol):
        self.idPersonalAdministrativo = idPersonalAdministrativo
        self.nombrePersonalAdministrativo = nombrePersonalAdministrativo
        self.rol = rol

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, PersonalAdministrativo): 
            return NotImplementedError("Operación no permitida: los tipos de datos no son iguales")
        return self.idPersonalAdministrativo == otro.idPersonalAdministrativo

    def validacion_personal_admin(self, lista_personal: list) -> list:
        errores = []

        if not self.idPersonalAdministrativo or not str(self.idPersonalAdministrativo).strip():
            errores.append("El ID del personal no puede estar vacio")

        if self in lista_personal: 
            errores.append(f"El personal {self.idPersonalAdministrativo} ya existe")

        return errores

    def Disponibilidad(self):
        pass