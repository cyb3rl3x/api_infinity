from sqlalchemy import Column, Integer, String

from database import Base

class Livro(Base):
    __tablename__ = 'livros'

    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str =  Column(String(100), nullable=True)
    descricao: str =  Column(String(100), nullable=True)
    numero_paginas: int = Column(Integer, nullable=True)


