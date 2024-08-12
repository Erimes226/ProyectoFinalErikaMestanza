class VeterinariaDTO:
    def __init__(self, id_veterinaria=None, nombre=None):
        self._id_veterinaria = id_veterinaria
        self._nombre = nombre

    @property
    def id_veterinaria(self):
        return self._id_veterinaria

    @id_veterinaria.setter
    def id_veterinaria(self, value):
        if isinstance(value, int) or value is None:
            self._id_veterinaria = value
        else:
            raise ValueError("El ID de la veterinaria debe ser un número entero o None")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str) or value is None:
            self._nombre = value
        else:
            raise ValueError("El nombre debe ser una cadena de texto o None")


class MascotaDTO:
    def __init__(self, id_mascota=None, nombre=None, tipo=None, edad=None, id_veterinaria=None):
        self._id_mascota = id_mascota
        self._nombre = nombre
        self._tipo = tipo
        self._edad = edad
        self._id_veterinaria = id_veterinaria

    @property
    def id_mascota(self):
        return self._id_mascota

    @id_mascota.setter
    def id_mascota(self, value):
        if isinstance(value, int) or value is None:
            self._id_mascota = value
        else:
            raise ValueError("El ID de la mascota debe ser un número entero o None")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str) or value is None:
            self._nombre = value
        else:
            raise ValueError("El nombre debe ser una cadena de texto o None")

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        if isinstance(value, str) or value is None:
            self._tipo = value
        else:
            raise ValueError("El tipo debe ser una cadena de texto o None")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if isinstance(value, int) or value is None:
            self._edad = value
        else:
            raise ValueError("La edad debe ser un número entero o None")

    @property
    def id_veterinaria(self):
        return self._id_veterinaria

    @id_veterinaria.setter
    def id_veterinaria(self, value):
        if isinstance(value, int) or value is None:
            self._id_veterinaria = value
        else:
            raise ValueError("El ID de la veterinaria debe ser un número entero o None")



    