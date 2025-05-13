# Modelo de base de datos para respuestas del formulario
from sqlalchemy import Column, Integer, String
from database import Base

# Representa la tabla 'respuestas' en la base de datos PostgreSQL
class Respuesta(Base):
    __tablename__ = "respuestas"

    # ID único autoincremental por cada respuesta
    id = Column(Integer, primary_key=True, index=True)

    # Edad del ciudadano (opcional)
    edad = Column(Integer, nullable=True)

    # Nombre del barrio o colonia (requerido)
    colonia = Column(String, nullable=False)

    # Preguntas abiertas opcionales para opinión general
    pregunta1 = Column(String, nullable=True)
    pregunta2 = Column(String, nullable=True)

    # Pregunta obligatoria sobre necesidad puntual
    necesidad = Column(String, nullable=False)

    # IP desde la que se envió la respuesta (usada para validar duplicados)
    ip = Column(String, nullable=False, index=True)  # index mejora el rendimiento en consultas por IP
