"""
https://www.youtube.com/watch?v=zV-6HLTFDF8&list=PL2L4c5jChmcsDrSaaH_5pKdCezAQ01o1a&index=8

Dans ce cours on apprend à gérer les erreurs avec l'instruction 'raise'

En exemple, on créé un utilisateur 'Jack' alors qu'il y a déjà un 'Jack' déjà
présent dans la base de données.
Cette base de données étant de type dictionnaire, il n'y a jamais de doublons
(comme pour les ensembles et contrairement aux listes), donc cette nouvelle
donnée va remplacer l'ancienne.

Afin d'éviter cette erreur de saisie, on créé une exception avec l'instruction
raise error dans la fonction recourant à la requête post (créer), c'est à dire
dans la fonction 'create_user'.

Et en parallèle, on modifie le code erreur ressorti lorsqu'on demande les données
d'une personne qui ne figure pas dans la base de données, en intervenant dans la
requête get, et plus précisemment dans la fonction 'get_users_path'

En plus du front-end / back-end et des requêtes (post, put, patch, get, delete), il
existe des codes conventions selon le rendu de la page web :
    -> de 100 à 199 : information
    -> de 200 à 299 : succès
    -> de 300 à 399 : redirection
    -> de 400 à 499 : erreur client
    -> de 500 à 599 : erreur serveur

Date : 13-05-23
"""

from fastapi import (
    FastAPI, 
    HTTPException, # Gestion des erreurs
    status, # codes conventions
    ) 
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

    # Si le nom saisie ne figure pas dans la base de données user_db (dictionnaire)
    if username not in user_db:
        # Affichage de l'erreur selon le code convention modifié (anciennement 500)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ce gars au nom de {username} n'existe pas !")
    
    return user_db[username]

# Nouvelle donnée avec la requête "post"
@app.post('/users')
# Appel de la Classe 'User' : instanciation en objet 'user'
def create_users(user : User):
    username = user.username # Appel de la variable de classe User
    
    # Si le nom à créer existe déjà dans la base de données dictionnaire user.db
    if username is user_db:
        # Affichage de l'erreur selon le code convention affecté :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Impossible de créer le gars. Ce gars {username} existe déjà')
    
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
