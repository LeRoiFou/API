from typing import Annotated
from fastapi import FastAPI, UploadFile, File
import polars as pl

app = FastAPI()

# Conversion du FEC
class SettingsConversion:

    # Chargement du FEC à convertir
    @app.post("/")
    def conversion_load_file(my_file : UploadFile = File(...)):
        return {"Nom du fichier chargé": my_file}
    
    @app.post("/files/")
    def create_file(my_file: Annotated[bytes, File()]):
        return {"file_size": len(my_file)}
    
    
if __name__ == '__main__':
    app = FastAPI()
    load_file = SettingsConversion()
    load_file.test()
