import enum
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Float , Enum,
    String,
    
    ForeignKey,
)
from sqlalchemy.sql import func
from app.db import Base
from sqlalchemy import Boolean

class EstadoEstacion(str, enum.Enum):
    activa = "Activa"
    inactiva = "Inactiva"

class QualityFlag(str, enum.Enum):
    bueno = "Bueno"
    no_verificado = "No Verificado"
    sospechoso = "Sospechoso"
    malo = "Malo"
    dato_faltante = "Dato Faltante"



class Estacion(Base):
    __tablename__ = "estaciones"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    latitud = Column(Float)
    longitud = Column(Float)
    fecha_creacion = Column(DateTime, default=func.now(), nullable=False)
    #Enum("female", "male", name="gender_enum", create_type=False)
    estado = Column(Enum(EstadoEstacion))
    mediciones = relationship("Medicion", back_populates="estacion") 

class Medicion(Base):
    __tablename__ = "mediciones"
    id = Column(Integer, primary_key= True, index=True)
    fecha = Column(DateTime, nullable=False)
    valor = Column(Float)
    qf = Column(Enum(QualityFlag))
    estacion_id = Column(Integer,ForeignKey('estaciones.id'))
    parametro_id = Column(Integer,ForeignKey('parametros.id'))
    estacion = relationship("Estacion", back_populates="mediciones")
    parametro = relationship("Parametro", back_populates="mediciones")

class Parametro (Base):
    __tablename__ = "parametros"
    id = Column(Integer, primary_key= True, index=True)
    nombre = Column(String, nullable=False)
    min_valor = Column(Float)
    max_valor = Column(Float)
    unidad = Column(String)
    mediciones = relationship("Parametro", back_populates="mediciones",uselist=False)
