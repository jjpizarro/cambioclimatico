import enum
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Float , Enum,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.sql import func
from app.db import Base
from sqlalchemy import Boolean

class EstadoEstacion(str, enum.Enum):
    activa = "Activa"
    inactiva = "Inactiva"

class QualityFlag(str, enum.Enum):
    bueno = "bueno"
    no_verificado = "no_verificado"
    sospechoso = "sospechoso"
    malo = "malo"
    dato_faltante = "dato_faltante"



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
    descripcion = Column(String, nullable=False)
    min_valor = Column(Float)
    max_valor = Column(Float)
    unidad = Column(String)
    mediciones = relationship("Medicion", back_populates="parametro",uselist=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)