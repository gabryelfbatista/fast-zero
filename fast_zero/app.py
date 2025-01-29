from fastapi import FastAPI  # type: ignore
from fastapi.responses import HTMLResponse  # type: ignore

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', response_class=HTMLResponse)
def read_page():
    return """
    <html>
        <body>
            <h1> Pagina de retorno </h1>
        </body>
    </html>
    """
