from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from typing import List
from sqlalchemy.orm import Session
from app.api import services, schemas
from app.api.models import Medicion
from app.db import get_db

router = APIRouter()


@router.get("/monitoreos/", response_model=List[schemas.MedicionView])
def get_monitoreos(skip: int = 0, limit: int = 10000, db: Session = Depends(get_db)):
    monitores = services.get_mediciones(db, skip=skip, limit=limit)
    return monitores

@router.get("/monitoreos/{id}", response_model=schemas.Medicion)
def get_monitoreo(id: int,  db: Session = Depends(get_db)):
    medicion = services.get_medicion(medicion_id=id,db=db)
    return medicion

@router.put('/monitoreos/')
def update_medicion(medicion:schemas.MedicionQf, db:Session = Depends(get_db)):
    return services.update_qf_medicion(db,medicion)

