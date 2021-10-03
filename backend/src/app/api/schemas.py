from typing import List, Optional
from .models import QualityFlag
from pydantic import BaseModel,EmailStr
from datetime import datetime


class MedicionBase(BaseModel):
    id: int
    valor:float

class Medicion(MedicionBase):
    fecha: datetime
    qf: str
    class Config:
        orm_mode = True

class MedicionQf(BaseModel):
    id:int
    qf: QualityFlag


class MedicionView(BaseModel):
    id:int
    estacion:str
    parametro:str
    fecha: datetime
    valor:float
    unidad: str
    qf: str

class DatoEstacionesGeoJsonView(BaseModel):
    estacion:int
    nombre_estacion: str
    variable:str
    fecha: datetime
    valor:float
    unidad: str
    qf: str

class DatoDescargaGeoJsonView(BaseModel):
    estacion:int 
    nombre_estacion: str
    fecha: datetime
    co2:Optional[float]
    ch4:Optional[float]
    humedad:Optional[float]
    temperatura:Optional[float]
    
class Estacion(BaseModel):
    id:int
    nombre: str
    class Config:
        orm_mode = True
        
class Parametro(BaseModel):
    id:int
    nombre:str
    class Config:
        orm_mode = True

class Filtro(BaseModel):
    estacion: int
    parametro:int
    startdate: datetime
    enddate: datetime


class UserBase(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr] = None
    is_superuser: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    ...


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB but not returned by API
class UserInDB(UserInDBBase):
    hashed_password: str


# Additional properties to return via API
class User(UserInDBBase):
    ...

class MedicionProps(BaseModel):
    id:int
    estacion:str
    parametro:str
    fecha: datetime
    valor:float
    unidad: str
    qf: str

