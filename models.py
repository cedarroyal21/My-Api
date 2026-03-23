from sqlalchemy import Column, Integer, String, Text, Date
from database import Base

class Article(Base):
    __tablename__ = "articles"

    id        = Column(Integer, primary_key=True, index=True)
    titre     = Column(String(200), nullable=False)
    contenu   = Column(Text, nullable=False)
    auteur    = Column(String(100), nullable=False)
    date      = Column(String(20))
    categorie = Column(String(100))
    tags      = Column(String(300))  # stocké comme "python,flask,api"