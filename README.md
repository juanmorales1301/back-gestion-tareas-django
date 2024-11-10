# Proyecto de Gestión de Tareas

Este es un proyecto de gestión de tareas desarrollado por Juan Carlos Morales. El objetivo es ofrecer una aplicación que permita la creación, gestión y actualización de tareas, utilizando un backend construido en Django y una base de datos PostgreSQL. El frontend está desarrollado en Angular y se despliega como una aplicación móvil híbrida con CapacitorJS.

## Requisitos de versión

Para que este proyecto funcione correctamente, se han utilizado las siguientes versiones de software:

- **Python**: 3.12.7
- **virtualenv**: 20.26.6
- **Django**: 5.1.1
- **PostgreSQL**: Recomendado 14.x o superior (para evitar problemas de compatibilidad).

## Instalación del ambiente virtual

Primero, se debe configurar el ambiente virtual para aislar las dependencias del proyecto. Para ello, se utiliza `virtualenv`. A continuación, los pasos:

1. Instalar virtualenv (si no está instalado):
   ```bash
   pip install virtualenv
   ```

2. Crear un ambiente virtual dentro de la carpeta del proyecto:
   ```bash
   virtualenv venv
   ```

3. Activar el ambiente virtual:
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```

## Instalación de dependencias

Con el ambiente virtual activado, todas las dependencias necesarias se encuentran especificadas en el archivo `requirements.txt`. Para instalarlas, ejecuta:

```bash
pip install -r requirements.txt
```

## Configuración de variables de entorno (`.env`)

El proyecto utiliza variables de entorno para configurar aspectos sensibles como la conexión a la base de datos y las claves secretas. Aquí están las variables más importantes que se deben agregar al archivo `.env`:

- `DATABASE_URL`: La URL de conexión a la base de datos PostgreSQL.
- `SECRET_KEY`: La clave secreta de Django para la seguridad.
- `DEBUG`: Configurar en `True` para desarrollo y `False` en producción.
- `ALLOWED_HOSTS`: Lista de hosts permitidos para el proyecto.

Ejemplo de archivo `.env`:

```
DATABASE_URL=postgres://postgres:PASSWORD@localhost:5432/db_tareas
SECRET_KEY='django-insecure-vx*+w(p2a@uc8hm7$0lvw=o%hc@7ol=zd4f5yk089uaj^!uup!'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Creación de la base de datos

Es importante crear una base de datos PostgreSQL antes de ejecutar las migraciones de Django. Aquí están los pasos recomendados:

1. Abrir la terminal de PostgreSQL:
   ```bash
   psql -U postgres
   ```

2. Crear la base de datos:
   ```sql
   CREATE DATABASE gestor_de_tareas;
   ```

3. Crear el usuario y otorgar permisos (si aún no existe):
   ```sql
   CREATE USER gestor_user WITH PASSWORD 'contraseña_segura';
   GRANT ALL PRIVILEGES ON DATABASE gestor_de_tareas TO gestor_user;
   ```

## Comandos para aplicar migraciones

Una vez configurada la base de datos y las variables de entorno, se deben aplicar las migraciones de Django para crear las tablas necesarias.

1. Crear las migraciones específicas de la aplicación:
   ```bash
   python manage.py makemigrations api
   ```

2. Ejecutar las migraciones en la base de datos:
   ```bash
   python manage.py migrate
   ```

## Ejecutar el servidor de desarrollo

Finalmente, para iniciar la aplicación en modo desarrollo, utiliza el siguiente comando:

```bash
python manage.py runserver
```

Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`.
