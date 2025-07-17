 📦 Proyecto Docker Compose — Stack de Microservicios

Este proyecto despliega una arquitectura básica de microservicios usando **Docker Compose**, integrando:

- 🐘 Base de datos PostgreSQL  
- ⚙️ API con FastAPI  
- 🧪 Servicio generador de datos falsos  
- 🌐 Frontend web (interfaz visual)  

---

## 📂 Estructura del proyecto

```
.
├── api/               # API con FastAPI
├── faker/             # Generador de datos falsos
├── web/               # Frontend
├── database/
│   └── database.env   # Configuración de PostgreSQL
└── docker-compose.yml
```

---

## ⚙️ Servicios definidos (`docker-compose.yml`)

```yaml
version: '3'

services:
  db:
    image: postgres:12-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    env_file:
      - ./database/database.env
    ports:
      - "5432:5432"

  api-fastapi:
    build: ./api
    ports:
      - "5002:80"
    links:
      - db
    depends_on: 
      - db

  api-faker:
    build: ./faker
    ports:
      - "5005:80"

  web:
    build: ./web
    ports:
      - "5000:80"

volumes:
  postgres_data:
```

---

## 🧠 API FastAPI

### Endpoints:

- **`GET /crear_registros`**: obtiene datos del servicio `api-faker` y los inserta en la base de datos.
- **`GET /registros_falsos`**: devuelve todos los registros guardados.
- **`GET /eliminar_registros`**: elimina todos los registros en la tabla.

### 📄 Modelo de Datos (`models.py`)

```python
datos_falsos = Table(
    "datos_falsos",
    meta,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(255)),
    Column("day_of_month", String(255)),
    Column("day_of_week", String(255)),
    Column("country", String(255)),
    Column("word", String(255)),
)
```

---

## 🧪 Servicio `faker/` — Generador de Datos Falsos

Genera datos aleatorios utilizando `Faker` y los expone mediante Flask.

### Endpoint principal:

```http
GET /datos
```

Devuelve una lista de objetos JSON con datos falsos para ser consumidos por `api-fastapi`.

---

## 🌐 Servicio `web/` — Interfaz Web con Flask

Permite visualizar, crear y eliminar registros desde un navegador.

### Rutas principales:

- `/`: muestra todos los registros
- `/crear_datos`: crea nuevos registros
- `/eliminar_datos`: borra todos los registros

---

## 🔐 Variables de entorno

📄 `database/database.env`

```env
POSTGRES_USER=hello_flask
POSTGRES_PASSWORD=hello_flask
POSTGRES_DB=hello_flask_dev
```

---

## 🚀 Cómo ejecutar el proyecto

```bash
docker-compose up --build
```

Una vez iniciado:

| Servicio     | URL                      |
|--------------|---------------------------|
| Web Frontend | http://localhost:5000     |
| API FastAPI  | http://localhost:5002     |
| Faker API    | http://localhost:5005     |
| PostgreSQL   | localhost:5432            |

---

## 🧪 Pruebas rápidas

```bash
curl http://localhost:5002/crear_registros
curl http://localhost:5002/registros_falsos
curl http://localhost:5002/eliminar_registros
```

---

## 🧼 Limpieza del entorno

```bash
docker-compose down -v
```


