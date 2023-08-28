from fastapi import FastAPI

app = FastAPI()

@app.get('/{data}')
def my_func_fastapi(data:int):
    my_result = data **2
    return my_result
