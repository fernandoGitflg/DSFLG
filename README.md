# API REST CRUD de Usuarios 
Proyecto desarrollado con Node.js, Express y MongoDB. Dockerizado completamente con Docker Compose. 
## Ejecución 
Asegúrate de tener Docker instalado.Para levantar todo el sistema:
```
docker compose up -d
```

La API estará disponible en:
```
docker compose up -d
```

## Endpoints

### Crear usuario
POST /api/users

Body:
```
{
  "nombre": "Fernando",
  "email": "fernando@example.com",
  "edad": 25
}
```

La id que te generará sera algo asi 69a03f39f5c12dce4887728f ya que mongodb al ser una base de datos no relacional es los tipos de id que maneja
### Listar usuarios
GET /api/users

### Obtener usuario por ID
GET /api/users/:id

### Actualizar usuario
PUT /api/users/:id aunque para esto deberiamos indicar todo el bloque que queremos remplazar ya que sino pondra en null los campos no indicados

Body:
```
  {
    "nombre": "Fernando2",
    "email": "fer@example.com",
    "edad": 25,
  },
```
otra opcion es usar 
PATCH /api/users/:id

Body:
```
  {
    "nombre": "Fernando2"
  },
```
De este modo solo nos cambiaría el nombre y no todo el bloque, pero no esta implementado en la API demomento
### Eliminar usuario
DELETE /api/users/:id