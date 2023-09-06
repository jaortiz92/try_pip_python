# All Projects 
```sh
git clone https://github.com/jaortiz92/try_pip_python.git
```

## Game Project

Instructions to use the game

```sh
cd game
python3 main.py
```

## Project charts

```sh
cd project_charts
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
mkdir images
```
You can use main.py to save a chart with percentage population
You can look the new image in the folder images

```sh
py main.py
```

You can use main_country.py to save a chart with historic information country population.
You can look the new image in the folder images 
```sh
py main_country.py
```

## Web server
```sh
cd web-server
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn main:app
```