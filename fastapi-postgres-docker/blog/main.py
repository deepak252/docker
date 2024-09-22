from fastapi import FastAPI
from . import schemas, models
from .database import engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():    
    return {
        'message': 'Welcome to the Fastapi Blogs'
    }

@app.post('/blog')
def index(request: schemas.Blog):    
    return {
        "message": "Blog created successfully",
        "data": request
    }