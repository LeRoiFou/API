"""
Lien : https://www.youtube.com/watch?v=gUiJsqpvGsI&list=PL2L4c5jChmcsDrSaaH_5pKdCezAQ01o1a&index=4

Dans ce tuto, cette fois-ci on paramètre la fonction, afin que l'utilisateur
ait la possibilité de saisir un nom figurant dans le dictionnaire user_db
afin de ressortir toutes les données de cette personne

Date : 12-05-2023
"""

from fastapi import FastAPI

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

app = FastAPI()


@app.get('/users')
def get_users():
    
    user_list = list(user_db.values())
    return user_list


# Fonction paramétrée cette fois-ci
@app.get('/users/{username}')
def get_users_path(username:str):
    
    # Récupération des données d'une des personnes (username, date_joined...)
    return user_db[username]
