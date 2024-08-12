from accessData.conexionOrm import Database
from accessData.entities.model import Veterinaria, Mascota
from dominio.entities.modelsOrm.dto import VeterinariaDTO, MascotaDTO
from servicios.logService import LogService
from abc import ABC, abstractmethod

class BaseService(ABC):

    @abstractmethod
    def crear_veterinaria(self, dto):
        pass

    @abstractmethod
    def ver_veterinarias(self):
        pass

    @abstractmethod
    def buscar_veterinaria(self, id_):
        pass

    @abstractmethod
    def actualizar_veterinaria(self, dto):
        pass

    @abstractmethod
    def borrar_veterinaria(self, id_):
        pass


class VeterinariaService(BaseService):
    
    def __init__(self, database: Database):
        self.db = database
        self.log_service = LogService()
        
    def crear_veterinaria(self, vete: VeterinariaDTO):
        self.log_service.logger("entro al metodo crear_veterinaria: "+str(vete.nombre))
        session = self.db.get_session()
        db_veterinaria = Veterinaria(id_veterinaria= vete.id_veterinaria, nombre = vete.nombre)
        session.add(db_veterinaria)
        session.commit()
        session.refresh(db_veterinaria)
        session.close()
        return db_veterinaria

    def ver_veterinarias(self):
        self.log_service.logger("entro al metodo ver_veterinarias")
        session = self.db.get_session()
        vete = session.query(Veterinaria).all()
        session.close()
        return vete

    def buscar_veterinaria(self, vete_id):
        self.log_service.logger("entro al metodo buscar_veterinarias: "+str(vete_id))
        session = self.db.get_session()
        person = session.query(Veterinaria).filter(Veterinaria.id_veterinaria == vete_id).first()
        session.close()
        return person


    def actualizar_veterinaria(self, vete: VeterinariaDTO):
        self.log_service.logger("entro al metodo actualizar_veterinaria: "+str(vete.nombre))
        session = self.db.get_session()
        veterinaria = session.query(Veterinaria).filter(Veterinaria.id_veterinaria == vete.id_veterinaria).first()
        if vete.nombre:
            veterinaria.nombre = vete.nombre
        if vete.id_veterinaria:
            veterinaria.id_veterinaria = vete.id_veterinaria
        session.commit()
        session.refresh(veterinaria)
        session.close()
        return veterinaria


    def borrar_veterinaria(self, veterinaria_id):
        self.log_service.logger("entro al metodo crear_veterinaria: "+str(veterinaria_id))
        session = self.db.get_session()
        veterinaria = session.query(Veterinaria).filter(Veterinaria.id_veterinaria == veterinaria_id).first()
        session.delete(veterinaria)
        session.commit()
        session.close()
        return {"message": "Deleted successfully"}
    

    #gestion de mascotas
    def crear_mascota(self, vete: MascotaDTO):
        self.log_service.logger("entro al metodo crear_mascota: "+str(vete.nombre))
        session = self.db.get_session()
        db_mascota = Mascota(id_mascota= vete.id_mascota, nombre = vete.nombre, tipo=vete.tipo, edad=vete.edad, id_veterinaria=vete.id_veterinaria)
        session.add(db_mascota)
        session.commit()
        session.refresh(db_mascota)
        session.close()
        return db_mascota

    def ver_mascotas(self):
        self.log_service.logger("entro al metodo ver_mascotas")
        session = self.db.get_session()
        vete = session.query(Mascota).all()
        session.close()
        return vete 

    def buscar_mascota(self, mascota_id):
            self.log_service.logger("entro al metodo buscar_mascot "+str(mascota_id))
            session = self.db.get_session()
            mascota = session.query(Mascota).filter(Mascota.id_mascota == mascota_id).first()
            if mascota:
                veterinaria = session.query(Veterinaria).filter(Veterinaria.id_veterinaria == mascota.id_veterinaria).first()
            else:
                veterinaria = None
            session.close()
            return mascota, veterinaria
        

    def actualizar_mascota(self, mascota_dto: MascotaDTO):
        self.log_service.logger("entro al metodo actualizar_mascota: "+str(mascota_dto.nombre))
        session = self.db.get_session()
        
        # Obtener la mascota que se va a actualizar
        mascota = session.query(Mascota).filter(Mascota.id_mascota == mascota_dto.id_mascota).first()
        
        if mascota:
            # Actualizar los datos de la mascota
            if mascota_dto.nombre:
                mascota.nombre = mascota_dto.nombre
            if mascota_dto.edad:
                mascota.edad = mascota_dto.edad
            if mascota_dto.tipo:
                mascota.tipo = mascota_dto.tipo
            if mascota_dto.id_veterinaria:
                # Actualizar la veterinaria en la que se encuentra la mascota
                mascota.id_veterinaria = mascota_dto.id_veterinaria

            # Guardar los cambios en la base de datos
            session.commit()
            session.refresh(mascota)
        
        session.close()
        return mascota

    def borrar_mascota(self, mascota_id):
        self.log_service.logger("entro al metodo borrar_mascota: "+str(mascota_id))
        session = self.db.get_session()
        mascota = session.query(Mascota).filter(Mascota.id_mascota == mascota_id).first()
        
        if mascota:
            session.delete(mascota)
            session.commit()
            mensaje = "Mascota eliminada exitosamente"
        else:
            mensaje = "Mascota no encontrada"
        
        session.close()
        return {"message": mensaje}


    def cerrarConexion(self):
        session = self.db.get_session()
        session.close()
