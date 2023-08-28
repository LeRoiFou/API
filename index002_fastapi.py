"""
Lien : https://www.youtube.com/watch?v=F43rgxq4CKw

Date : 12-05-23
"""

from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
async def root():
    return {'example': 'This is an example', 'data': 0}

@app.get('/random')
async def get_random():
    rn : int = random.randint(0, 100)
    return {'Number': rn, 'Limit': 100}

@app.get('/random{limit}')
async def get_random(limit: int):
    rn : int = random.randint(0, 100)
    return {'Number': rn, 'Limit': limit}
