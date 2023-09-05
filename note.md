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
    
