"""
https://www.youtube.com/watch?v=r4UVY0EqD7k&list=PL2L4c5jChmcsDrSaaH_5pKdCezAQ01o1a&index=2

Exemple le plus simple pour afficher une page web avec FastApi

Pour visualiser les requêtes appelées, saisir après la terminaison : '/docs'

Date : 12-05-23
"""

from fastapi import FastAPI

# Instanciation de la librairie en objet
app = FastAPI()

# Décorateur : recours à la requête 'get' (obtenir)
@app.get('/')
def my_func_fastapi():
    
    return {'Output': 'My first API'}
