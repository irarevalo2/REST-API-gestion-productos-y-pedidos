# Flask-REST-API-gestion-productos-y-pedidos

API REST con FastAPI para gestión de productos y pedidos usando estructuras de datos en memoria.

## Descripción

Esta es una API REST construida con FastAPI que permite:
- **Gestionar productos**: Almacenados en un árbol binario de búsqueda ordenado por ID
- **Gestionar pedidos**: Almacenados en una lista enlazada

La API no utiliza persistencia en base de datos, todos los datos se mantienen en memoria.

## Requisitos

- Python 3.14
- Docker y Docker Compose

## Instalación y Ejecución


1. Construir y ejecutar los contenedores:
```bash
docker-compose up --build
```

2. La API estará disponible en: `http://localhost:5000`


## Documentación Interactiva

FastAPI proporciona documentación interactiva automática:

- Swagger UI: `http://localhost:5000/docs`
- ReDoc: `http://localhost:5000/redoc`

