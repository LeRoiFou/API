"""
Lien : https://www.youtube.com/watch?v=hEng8BjkR6U&list=PL2L4c5jChmcsDrSaaH_5pKdCezAQ01o1a&index=5

Dans ce tuto on insère une condition des données à restituer

On peut mettre également une valeur par défaut, mais dans ce cas, l'utilisateur
n'a pas la possibilité de saisir une valeur dans la base de de données à disposition

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

# Limitation des données à ressortir
@app.get('/users')
def get_users(limit:int = 2): # limite par défaut : 2 premiers composants à afficher
    
    user_list = list(user_db.values())
    return user_list[:limit] # = my_list[:2] -> affichage des 2 premiers composants


# Fonction paramétrée cette fois-ci :
# le fait de laisser à l'utilisateur de saisir un nom, la page web n'affichera pas
# un nom par défaut (ici jack) contrairement à la fonction ci-avant
@app.get('/users/{username}')
def get_users_path(username:str = 'jack'): # ce ne sera pas la valeur par défaut...
    
    # Récupération des données d'une des personnes (username, date_joined...)
    return user_db[username]

# Affichage des 2 premiers composants des valeurs du dictionnaire converti en liste
print(list(user_db.values())[:2])
