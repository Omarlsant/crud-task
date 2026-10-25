# CRUD de tareas

API REST para crear, consultar, actualizar y eliminar tareas mediante Django y
Django REST Framework. Cada tarea tiene título, descripción y estado de
completado.

## Requisitos

- Python 3.13 o superior
- `uv` (recomendado) o un entorno virtual equivalente

## Puesta en marcha

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

La API queda disponible en `http://127.0.0.1:8000/tasks/api/v1/tasks/`.
La documentación navegable está en
`http://127.0.0.1:8000/tasks/docs/`.
La URL raíz `http://127.0.0.1:8000/` muestra enlaces a estos recursos.

Importante: la URL de documentación es `/tasks/docs/`, no se combina con la
URL de la API. La URL `/tasks/api/tasks/` tampoco existe porque la versión
forma parte de la ruta: `/tasks/api/v1/tasks/`.

## Endpoints

| Método | URL | Acción |
| --- | --- | --- |
| GET | `/tasks/api/v1/tasks/` | Listar tareas |
| POST | `/tasks/api/v1/tasks/` | Crear una tarea |
| GET | `/tasks/api/v1/tasks/<id>/` | Consultar una tarea |
| PATCH/PUT | `/tasks/api/v1/tasks/<id>/` | Actualizar una tarea |
| DELETE | `/tasks/api/v1/tasks/<id>/` | Eliminar una tarea |

Ejemplo de creación:

```bash
curl -X POST http://127.0.0.1:8000/tasks/api/v1/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Preparar entrega","description":"Revisar cambios"}'
```

El título es obligatorio; los espacios exteriores se eliminan y un título
formado solo por espacios se rechaza.

## Pruebas

```bash
uv run python manage.py test
```