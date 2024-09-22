from fastapi import Depends, FastAPI
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

@app.get('/')
def index():    
    return {
        'message': 'Welcome to the Fastapi Blogs'
    }

@app.post('/blogs')
def create_blog(request: schemas.Blog, db: Session = Depends(get_db) ):    
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    # return {
    #     "message": "Blog created successfully",
    #     "data": request
    # }

@app.get('/blogs')
def get_blogs(db: Session = Depends(get_db) ):    
    return db.query(models.Blog).all()

@app.get('/blogs/{blog_id}')
def get_blog(blog_id: int, db: Session = Depends(get_db) ):    
    return db.query(models.Blog).filter(models.Blog.id==blog_id).first()
    