# Importación de FastAPI y módulos auxiliares
from fastapi import FastAPI, Request, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Respuesta
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

# Genera automáticamente las tablas definidas en los modelos si no existen
Base.metadata.create_all(bind=engine)

# Instancia principal de la aplicación FastAPI
app = FastAPI()

# Middleware para permitir peticiones desde otro dominio (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cambiar a origen específico (ej: frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquema de entrada para la API /responder
# Define los campos que se esperan en el cuerpo de la solicitud
class RespuestaInput(BaseModel):
    edad: Optional[int] = None
    colonia: str
    pregunta1: Optional[str] = None
    pregunta2: Optional[str] = None
    necesidad: str

# Endpoint POST para registrar una respuesta del formulario
@app.post("/responder")
def registrar_respuesta(
    data: RespuestaInput,
    request: Request,
    db: Session = Depends(get_db)  # Inyección de la sesión de base de datos
):
    # Obtiene la IP del cliente para evitar duplicados
    ip = request.client.host

    # Verifica si ya se registró una respuesta desde esta IP
    existe = db.query(Respuesta).filter_by(ip=ip).first()
    if existe:
        raise HTTPException(status_code=409, detail="Ya has respondido antes.")

    # Crea una nueva instancia del modelo con los datos enviados
    nueva = Respuesta(**data.dict(), ip=ip)

    # Inserta la nueva respuesta en la base de datos
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    # Retorna un mensaje de éxito con el ID de la respuesta
    return {"mensaje": "Recibido", "id": nueva.id}