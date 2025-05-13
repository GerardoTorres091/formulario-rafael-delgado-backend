# Configuración de SQLAlchemy para conectar con PostgreSQL desde FastAPI
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a PostgreSQL
# Formato: postgresql://usuario:contraseña@host:puerto/nombre_base
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor de conexión
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crea la sesión que se inyecta en cada petición
SessionLocal = sessionmaker(
    autocommit=False,  # los cambios se confirman manualmente
    autoflush=False,   # no guarda automáticamente en cada query
    bind=engine        # se asocia al motor definido arriba
)

# Clase base para los modelos (como Respuesta)
Base = declarative_base()

# Dependency para inyectar sesión de DB en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db  # se usa como dependency en FastAPI
    finally:
        db.close()  # asegura que la conexión se cierre después de cada uso
