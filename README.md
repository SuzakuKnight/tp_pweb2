# Tienda de Libros API

Backend REST desarrollado con Flask para gestionar un carrito de compras de libros.  
Aplicación inspirada en el funcionamiento de Coffee Cart, adaptada al dominio **Tienda de Libros**.

> Persistencia en memoria (sin base de datos).

---

## Objetivo (Etapa 1)

Implementar un servidor backend que exponga APIs RESTful para:

- Listar libros disponibles
- Ver contenido del carrito
- Agregar libros al carrito
- Eliminar libros del carrito
- Calcular el total de la compra

Incluye documentación automática de la API mediante Swagger/OpenAPI y pruebas realizadas con Thunder Client.

---

## Tecnologías utilizadas

- Python
- Flask
- Flasgger (Swagger / OpenAPI)
- Thunder Client (para pruebas de endpoints)

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Crear el entorno virtual
3. Instalar dependencias

```bash
pip install -r requirements.txt
```
---

## Documentación Swagger / OpenAPI

La API cuenta con documentación interactiva generada automáticamente con Flasgger.

Una vez ejecutado el servidor, acceder a:

http://127.0.0.1:5000/apidocs

Desde allí se pueden probar todos los endpoints directamente desde el navegador.
