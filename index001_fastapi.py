"""
Lien : https://www.youtube.com/watch?v=-ykeT6kk4bk : 35 minutes
Cours : Tutoriel de FastApi

Modules installés : 
pip install fastapi
pip install uvicorn

Les 4 requêtes web http à retenir :
GET : OBTENIR / RÉCUPÉRER des informations 
POST : PUBLIER / CRÉER des informations 
INPUT : MODIFIER des informations
DELETE : SUPPRIMER des informations

Les données à afficher sont toujours représentées selon le format d'un fichier
JSON (JS -> JavaScript) qui est similiaire à un dictionnaire sous Python

Date : 14-04-23

Vidéo discutée via WhatsApp avec Christophe :
https://www.youtube.com/watch?v=z6q9kug0PL0 -> début de requêtage... insuffisant

https://www.youtube.com/watch?v=x6Q6-gY1Pzc : c'est avec cette vidéo
que j'ai compris !!! (Date : 12-05-2023)
"""

import uvicorn
from fastapi import FastAPI

# Initialisation de la librairie
app = FastAPI()

# Création d'un "endpoint" avec pour finalité "/"
# (point final d'une URL : https://facebook/home -> endpoint : /home)
@app.get("/")
def home():
    return {"C'est la clé d'un dictionnaire": "C'est un item d'un dictionnaire"}

# Création d'un deux "endpoint" avec pour finalité "/about"
@app.get("/about")
def about():
    return {"Un dictionnaire Python":"= un fichier JSON"}

# Inventaire sous la forme d'un dictionnaire Python {clé : items}
# similaire à un fichier JSON
my_inventory = {
    1:{'name':'Fromage', 'price':3, 'brand':'Vache qui rit'},
    2:{'name':'Fruit', 'price':5, 'brand':'Bananes !'},
    3:{'name':'Légumes', 'price':4, 'brand':'Courgettes'},
}

# Affichage de l'inventaire avec la terminaison : /get_id/n° clé du dictionnaire
@app.get("/get_id/{id}")
def get_id(id:int): # pour tout paramètre, indiquer le type à appliquer (ici entier)
    # Récupération des items du dictionnaire selon la clé saisie (1 ou 2 ou 3)
    return my_inventory[id]

# Cette fois-ci on récupère le nom du stock inventorié selon le n° de clé
@app.get("/get_id/{id}/{name}")
def get_id(id:int, name:str):
    return my_inventory[id][name]

# Cette fois-ci on récupère le nom du stock inventorié selon le n° de clé
@app.get("/get_id/{id}")
def get_id(id:int):
    return my_inventory[id]

# Récupération avec pour terminaison : "?name=..."
@app.get('/get_name/{name}')
def get_name(name:str):
    for item_id in my_inventory:
        if my_inventory[item_id]['name'] == name:
            return my_inventory[item_id]
    return {'data':'non trouvé'}

# Au lieu d'avoir saisi et lancé le fichier :
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)

# J'ai saisi ceci dans le terminal :
# uvicorn index001_fastapi:app --reload

# Avec la saisie directe dans le terminale, la mise à jour des données se fait
# contrairement au lancement de l'application avec if __name__...