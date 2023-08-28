"""
Lien : https://dev.to/ericlecodeur/introduction-a-fastapi-python-partie-2-3eb5
Date : 14-05-23
"""

from fastapi import (FastAPI, 
                     Response # pour le code convention erreur à afficher
                     )
from pydantic import BaseModel # Librairie pour la requête 'post'

# Modèle de classe héritant de la librairie BaseModel
# pour créer un nouveau produit : pour éviter une omission (nom du produit par ex),
# on créé cette classe qui constitue une 'convention' pour créer un nouveau produit
class Product(BaseModel):
    name:str
    price:float

products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 999},
    {"id": 3, "name": "iWatch", "price": 699},
]

app = FastAPI()

# Accès à la liste de tous les produits
@app.get("/products")
def index():
    return products

# Accès à un produit défini à partir de son nom
@app.get("/products/search")
def index(name, response: Response):
    founded_products = [
        product for product in products 
        if name.lower() in product["name"].lower()]

    if not founded_products: 
        response.status_code = 404
        return "No Products Found"

    return (founded_products 
            if len(founded_products) > 1 else founded_products[0])

# Accès à un produit à partir de son n° id
@app.get("/products/{id}")
def index(id: int, response: Response):
    for product in products:
        if product["id"] == id:
            return product

    response.status_code = 404
    return "Product Not found"

# Création d'un nouveau produit
@app.post('/products')
def create(new_product: Product, response: Response):
    product = new_product.dict()
    product["id"] = len(products) + 1
    products.append(product)
    response.status_code = 201
    return product

# Modification des données d'un produit
@app.put("/products/{id}")
def edit_product(id: int, edited_product: Product, response: Response):
    for product in products:
        if product["id"] == id:
            product['name'] = edited_product.name
            product['price'] = edited_product.price      
            response.status_code = 200
            return product
        else:
            response.status_code = 404
            return "Product Not found"

# Suppression d'un produit
@app.delete("/products/{id}")
def destroy_product(id: int, response: Response):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            response.status_code = 204
            return "Product Deleted"
        else:
            response.status_code = 404
            return "Product Not found"
