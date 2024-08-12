from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseDeDatos = declarative_base()

class Veterinaria(BaseDeDatos):
    __tablename__ = 'Veterinaria'
    
    id_veterinaria = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    
    # Relación uno a muchos con Mascota, con eliminación en cascada
    mascotas = relationship('Mascota', back_populates='veterinaria', cascade='all, delete-orphan')

class Mascota(BaseDeDatos):
    __tablename__ = 'Mascota'
    
    id_mascota = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50))
    edad = Column(Integer)
    
    # Clave foránea que referencia a Veterinaria
    id_veterinaria = Column(Integer, ForeignKey('Veterinaria.id_veterinaria'))
    
    # Relación con Veterinaria
    veterinaria = relationship('Veterinaria', back_populates='mascotas')