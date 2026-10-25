# Contexto del proyecto CRUD Python

## Estado inicial

El proyecto es una API REST de tareas construida con Django y Django REST
Framework. Ya incluía:

- Un proyecto Django con SQLite.
- El modelo `Task` con título, descripción y estado de completado.
- Un `ModelViewSet` para el CRUD.
- Rutas versionadas bajo `/tasks/api/v1/tasks/`.
- Documentación navegable bajo `/tasks/docs/`.
- Registro del modelo en el panel `/admin/`.

## Cambios implementados

- Se validan los títulos: se eliminan espacios exteriores y se rechazan títulos
  vacíos.
- Las tareas se listan de más reciente a más antigua.
- Se añadieron pruebas para listar, crear, validar, actualizar y eliminar
  tareas.
- La URL raíz `/` muestra enlaces a la API, la documentación y el
  administrador.
- Se corrigieron las rutas y se documentaron las URLs de uso.
- Se ajustaron las versiones de Django, Django REST Framework y setuptools para
  mantener compatibilidad con la documentación basada en CoreAPI.
- Se eliminó `coreapi` de `INSTALLED_APPS`, porque no es una aplicación Django.

## Puesta en marcha

Desde la raíz del repositorio:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

URLs principales:

- Inicio: `http://127.0.0.1:8000/`
- API: `http://127.0.0.1:8000/tasks/api/v1/tasks/`
- Documentación: `http://127.0.0.1:8000/tasks/docs/`
- Administración: `http://127.0.0.1:8000/admin/`

## Validación

Las comprobaciones ejecutadas fueron:

```bash
uv run python manage.py check
uv run python manage.py test
```

Resultado: comprobaciones Django correctas y 5 pruebas superadas.
