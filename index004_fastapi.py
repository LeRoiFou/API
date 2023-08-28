"""
https://www.youtube.com/watch?v=FaogPy1ba1c&list=PL2L4c5jChmcsDrSaaH_5pKdCezAQ01o1a&index=3

La page web ne fonctionne que lorsqu'on a inséré à l'extension du site web ceci :
'/users'

Date : 12-05-23
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
    
    # Conversion des données du dictionnaire en une liste
    user_list = list(user_db.values())
    
    return user_list

