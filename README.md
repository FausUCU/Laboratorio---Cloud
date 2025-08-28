# Portal de Noticias - Azure Cloud Lab

## Arquitectura y Servicios de Azure

### Servicios Utilizados

Este proyecto utiliza los siguientes servicios de Azure:

1. **Azure Functions** - Backend serverless para la lógica de negocio
2. **Azure Table Storage** - Base de datos NoSQL para almacenar noticias
3. **Azure Storage Account** - Proporciona la conexión para Table Storage

### Comunicación Entre Servicios

#### Flujo de Datos

```
Frontend (HTML/JS)
    ↓ HTTP Requests
Azure Functions (Backend)
    ↓ Azure SDK
Azure Table Storage (Database)
```

#### Detalles de Comunicación

1. **Frontend → Azure Functions**

   - El frontend hace peticiones HTTP REST a las Azure Functions
   - Endpoints disponibles:
     - `POST /api/AddNews` - Agregar nueva noticia
     - `GET /api/GetNews` - Obtener todas las noticias
     - `POST /api/LogAccess` - Registrar acceso (logging)

2. **Azure Functions → Azure Table Storage**

   - Las funciones usan el SDK de Azure (`azure.data.tables`)
   - Conexión mediante connection string desde variables de entorno
   - Operaciones realizadas:
     - Crear tabla "NewsTable" si no existe
     - Insertar entidades con PartitionKey="News"
     - Consultar entidades por PartitionKey

3. **Configuración de CORS**
   - Azure Functions configuradas para permitir requests desde el frontend
   - CORS habilitado para `http://localhost:5500` (Live Server)

#### Estructura de Datos

**Tabla: NewsTable**

- **PartitionKey**: "News" (fijo)
- **RowKey**: UUID único generado automáticamente
- **Title**: Título de la noticia
- **Content**: Contenido de la noticia

## ⚙️ Requisitos

- **Node.js** (v18+)
- **Python 3.12** (o compatible con tu entorno)
- **Azure Functions Core Tools**
  ```bash
  npm install -g azure-functions-core-tools@4 --unsafe-perm true
  ```
- **VSCode** (opcional, recomendado)
- **Extensión Live Server** (para el frontend)

### Paquetes Python:

```bash
pip install -r api/requirements.txt
```

## Ejecución

### 1. Backend (Azure Functions)

Entrar a la carpeta del backend:

```bash
cd Laboratorio1/api
```

Activar el entorno virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Levantar Azure Functions (habilitando CORS para el frontend):

```bash
func start --cors "http://localhost:5500"
```

Para pruebas rápidas, también se puede usar `--cors "*"`.

### 2. Frontend

Entrar a la carpeta frontend:

```bash
cd ../frontend
```

Abrir `index.html` con Live Server en VSCode:

- Click derecho → Open with Live Server

Debe abrirse como: `http://localhost:5500/index.html`

Usar el portal para agregar y ver noticias.

## 🔧 Configuración de Azure

Para desplegar en Azure, necesitarás:

1. **Azure Storage Account** con Table Storage habilitado
2. **Azure Function App** configurada con Python runtime
3. **Connection String** de Azure Storage configurada en las variables de entorno de la Function App

### Variables de Entorno Requeridas:

- `AzureWebJobsStorage`: Connection string de Azure Storage
