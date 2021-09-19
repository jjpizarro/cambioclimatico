from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from typing import List
from sqlalchemy.orm import Session
from app.api import services, schemas
from app.api.models import Estacion
from app.db import get_db

router = APIRouter()

@router.get("/estaciones", response_model=List[schemas.Estacion])
def get_estaciones(db: Session = Depends(get_db)):
    estaciones = services.get_estaciones(db)
    return estaciones