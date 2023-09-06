Comandos Utilizados
- python
- python3
- exit() para salir de la interfaz de python

Instalación
- apt update
- sudo apt update
- sudo apt -y upgrade

Verificar Instalación de python

- python3 -V

Instalación de gestor de paquetes de dependencias

- sudo apt insstall -y python3-pip

Verificar Instalación del gestor

- pip3 -V

Dependencias en entorno profesional

- apt install -y build-essential libssl-dev libffi-dev python3-dev

## Git
- git init
- git remote add origin <URL>
- git remote -v (Ver las rutas remote)
- git pus origin master (Cargar informacion a git)
## gitignore
- https://www.toptal.com/developers/gitignore generar el git segun nuestras necesidades
    - windows
    - linux
    - python

## Pip
- Info: pypi.org
- pip install pack
- pip freeze -> packs installed

## Ambientes Virtuales
- which python -> Indica la ruta de donde se ejecuta (Python) el programa indicado
- Instalar
    - python3 -m pip install --user virtualenv
    - pip freeze | grep virtualenv -> Validar instalación
- Crear entorno
    - python3 -m venv /path/to/new/virtual/environment
- Activar entorno
    - source /path/virtual/environment/bin/activate
- Desactivar entorno
    - deactivate
- Guardar las dependencias instaladas
    - pip freeze > requirements.txt
- Usar requirements.txt
    - pip install -r requirements.txt
    
## FastAPI
- pip install fastapi
- pip install "uvicorn[standard]"

## Docker
- Pasos
    1. Crear dockefile
    2. Crear docker-compose.yml
    3. docker-compose build -> Construir el compose
    4. docker-compose up -d -> Correr el proceso
    5. docker-compose ps -> Ver los procesos activos
    6. docker-compose exec app-name bash -> Entrar al servicio a la terminal
    7. docker-compose down -> Para matar el servicio
- Update_script
    1. Add Volumenes al docker-compose
        - volumes:
            - .:/app
    2. docker-compose up -d -> Correr el proceso