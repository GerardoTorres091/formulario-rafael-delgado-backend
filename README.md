# API - Formulario Ciudadano

Backend en FastAPI que recibe y guarda respuestas del formulario ciudadano para el municipio de Rafael Delgado, Veracruz.

---

## Tecnologías

- FastAPI
- SQLAlchemy
- PostgreSQL
- Render.com (deploy)
- Docker

---

## Funcionalidad

- Recibe datos enviados desde el frontend (Vue)
- Valida que una IP no pueda enviar más de una vez
- Guarda edad (opcional), colonia, dos preguntas abiertas y una necesidad principal

---

## Endpoints

### POST `/responder`

Registra una respuesta del formulario.

**Body (JSON):**

```json
{
  "edad": 23,
  "colonia": "Jalapilla",
  "pregunta1": "Mejoraría la luz",
  "pregunta2": "Un parque",
  "necesidad": "Alumbrado público"
}