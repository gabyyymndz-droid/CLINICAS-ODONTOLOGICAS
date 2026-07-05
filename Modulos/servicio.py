class Servicio:
    def __init__(self, id_servicio: str, descripcion_servicio: str, jvp_doctor: str):
        self.id_servicio: str = id_servicio
        self.descripcion_servicio: str = descripcion_servicio
        self.jvp_doctor: str = jvp_doctor

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Servicio): 
            return NotImplementedError("Operación no permitida: los tipos de datos no son iguales")
        return self.id_servicio == otro.id_servicio

    def validacion_servicio(self, lista_roles: list) -> list:
        errores = []

        if not self.id_servicio or not str(self.id_servicio).strip():
            errores.append("El ID del servicio no puede estar vacio")
        if self in lista_roles: 
            errores.append(f"El rol {self.id_servicio} ya existe en el sistema")

        return errores

    def registrar_servicio(self) -> None:
        print(f"[Servicio] Servicio '{self.descripcion_servicio}' configurado")