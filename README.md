# My-Api 📝

API REST pour gérer les articles d'un blog, développée dans le cadre du TAF1 - INF222 EC1.

## Technologies utilisées

- Python 3.10
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/cedarroyal21/My-Api.git
cd My-Api
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install fastapi uvicorn sqlalchemy
```

### 4. Lancer le serveur
```bash
uvicorn main:app --reload
```

- API : http://127.0.0.1:8000  
- Documentation Swagger : http://127.0.0.1:8000/docs  
- Documentation ReDoc : http://127.0.0.1:8000/redoc

## Endpoints

| Méthode | Endpoint | Description | Code retour |
|---|---|---|---|
| POST | `/api/articles` | Créer un article | 201 |
| GET | `/api/articles` | Lister tous les articles | 200 |
| GET | `/api/articles?categorie=Tech` | Filtrer par catégorie | 200 |
| GET | `/api/articles?auteur=Cedrik` | Filtrer par auteur | 200 |
| GET | `/api/articles?date=2026-03-21` | Filtrer par date | 200 |
| GET | `/api/articles/{id}` | Lire un article par ID | 200 |
| PUT | `/api/articles/{id}` | Modifier un article | 200 |
| DELETE | `/api/articles/{id}` | Supprimer un article | 200 |
| GET | `/api/articles/search/query?query=texte` | Rechercher un article | 200 |

## Structure du projet
```
blog-api/
├── main.py        # Point d'entrée de l'application
├── database.py    # Connexion à la base de données SQLite
├── models.py      # Modèle de la table articles
├── schemas.py     # Validation des données (Pydantic)
├── routes.py      # Définition de tous les endpoints
└── README.md      # Documentation
```

## Format d'un article
```json
{
  "titre": "Mon article",
  "contenu": "Contenu de l'article",
  "auteur": "Cedrik",
  "date": "2026-03-21",
  "categorie": "Technologie",
  "tags": "python,fastapi,backend"
}
```

## Exemples d'utilisation

### Créer un article
```bash
curl -X POST http://127.0.0.1:8000/api/articles \
  -H "Content-Type: application/json" \
  -d '{
    "titre": "Introduction à FastAPI",
    "contenu": "FastAPI est un framework Python moderne.",
    "auteur": "Cedrik",
    "date": "2026-03-21",
    "categorie": "Technologie",
    "tags": "python,fastapi"
  }'
```

### Lister tous les articles
```bash
curl http://127.0.0.1:8000/api/articles
```

### Rechercher un article
```bash
curl http://127.0.0.1:8000/api/articles/search/query?query=fastapi
```

## Codes HTTP

| Code | Signification |
|---|---|
| 200 | OK |
| 201 | Création réussie |
| 404 | Article non trouvé |
| 422 | Données invalides |
| 500 | Erreur serveur |

## Auteur

**Cedrik** — INF222 EC1 TAF1  
Université de Yaoundé I
