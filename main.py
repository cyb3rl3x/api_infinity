#v2
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Livro
from database import engine, Base, get_db
from core import LivroCore
from schemas import LivroRequest, LivroResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/api/livros/")
def find_all(db:Session = Depends(get_db)):
    livros = LivroCore.find_all(db)
    return [LivroResponse.from_orm(livro) for livro in livros]

@app.post("/api/livros/")
def create(request:LivroRequest, db:Session = Depends(get_db)):
    livro = LivroCore.save(db, **request.dict())
    return LivroResponse.from_orm(livro)    













