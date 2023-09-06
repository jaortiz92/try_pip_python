import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3]

@app.get('/info')
def get_list():
    return {
        'name': 'Compañia sas'
    }

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return '''
        <h1>Hi, this is the titles</h1>
        <p>Here, you can look the data<p>
    '''

def run():
    store.get_categories()


if __name__ == '__main__':
    run()