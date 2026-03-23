from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Article
from shemas import ArticleCreate, ArticleUpdate, ArticleResponse
from typing import List, Optional

router = APIRouter()

# Créer un article
@router.post("/articles", response_model=ArticleResponse, status_code=201)
def creer_article(article: ArticleCreate, db: Session = Depends(get_db)):
    nouvel_article = Article(**article.dict())
    db.add(nouvel_article)
    db.commit()
    db.refresh(nouvel_article)
    return nouvel_article

# Lister tous les articles (filtrable)
@router.get("/articles", response_model=List[ArticleResponse])
def lister_articles(
    categorie: Optional[str] = None,
    auteur: Optional[str] = None,
    date: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Article)
    if categorie:
        query = query.filter(Article.categorie == categorie)
    if auteur:
        query = query.filter(Article.auteur == auteur)
    if date:
        query = query.filter(Article.date == date)
    return query.all()


# Rechercher un article
@router.get("/articles/search/query", response_model=List[ArticleResponse])
def rechercher_articles(query: str, db: Session = Depends(get_db)):
    resultats = db.query(Article).filter(
        Article.titre.contains(query) | Article.contenu.contains(query)
    ).all()
    return resultats


# Lire un article par ID
@router.get("/articles/{id}", response_model=ArticleResponse)
def lire_article(id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return article

# Modifier un article
@router.put("/articles/{id}", response_model=ArticleResponse)
def modifier_article(id: int, data: ArticleUpdate, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(article, key, value)
    db.commit()
    db.refresh(article)
    return article



# Supprimer un article
@router.delete("/articles/{id}")
def supprimer_article(id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    db.delete(article)
    db.commit()
    return {"message": "Article supprimé avec succès"}
