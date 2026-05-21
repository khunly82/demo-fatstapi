from fastapi import APIRouter, FastAPI, Request, HTTPException
import controllers

app = FastAPI()

def add_routers(app):
    for item_name in dir(controllers):
        item = getattr(controllers, item_name)
        if isinstance(item, APIRouter):
            app.include_router(item)

add_routers(app)


@app.get('/hello')
def hello(_: Request, name: str = 'Khun'):
    """
    Ce endpoint vous dit bonjour !!
    """
    if name == 'Ingrid':
        raise HTTPException(status_code=401)

    return { 'value':  f'Hello {name} !!' }