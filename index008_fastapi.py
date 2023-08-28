"""
https://www.youtube.com/watch?v=6mH2461gfjQ&list=PL2L4c5jChmcsDrSaaH_5pKdCezAQ01o1a&index=7

Dans ce cours on apprend à modifier (requêtes "put" et "patch") et à 
supprimer (requête "delete")

Date : 13-05-23
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field # Librairie pour la requête post de fastapi
from typing import Optional
from datetime import date as my_date

user_db = {
    'jack': {
        'username': 'jack', 'date_joined': '2021-12-01', 
        'location': 'New York', 'age': 28},
    'jill': {
        'username': 'jill', 'date_joined': '2021-12-02', 
        'location': 'Los Angeles', 'age': 19},
    'jane': {
        'username': 'jane', 'date_joined': '2021-12-03', 
        'location': 'Toronto', 'age': 52}
}

# Classe pour les nouveaux noms à ajouter
class User(BaseModel):
    # Type des variables créées en variables de classe
    username : str = Field(min_length=3, max_length=20) # nbre de caractères
    date_joined : my_date # librairie date de datetime appelée
    location : Optional[str] = None # librairie Optional : saisie non obligatoire
    age : int = Field(None, lt=5, gt=130) # valeur par défaut None mais si saisie compris entre 5 et 130 ans

app = FastAPI()

# Limitation des données à ressortir : 20 noms max
@app.get('/users')
def get_users(limit : int = 20):
    user_list = list(user_db.values())
    return user_list[:limit]

# Données affichées selon le nom saisie
@app.get('/users/{username}')
def get_users_path(username : str):
    return user_db[username]

# Nouvelle donnée avec la requête "post"
@app.post('/users')
# Appel de la Classe 'User' : instanciation en objet 'user'
def create_users(user : User):
    username = user.username # Appel de la variable de classe User
    user_db[username] = user.dict() # Ajout dans le dictionnaire user_db
    return {'Message': f"Nom {username} créé !"}

# Suppression d'une donnée avec la requête "delete"
@app.delete('/users/{username}')
def delete_user(username : str):
    del user_db[username]
    return {'message': f'Nom {username} supprimé avec succès !'}

# Modification d'une donnée avec la requête "put"
@app.put('/users')
def update_user(user : User):
    username = user.username
    user_db[username] = user.dict()
    return {"message": f"Nom {username} modifié avec succés !"}

# Modification partielle d'une donnée avec la requête "patch"
@app.patch('/users')
def update_user_partial(user : User):
    username = user.username
    user_db[username].update(user.dict(exclude_unset=True))
    return {"message": f"Nom {username} partiellement modifié avec succés !"}
