from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def test():
    return {'message': 'hello world'}

@app.get('/{id}')
def test(id: int):
        return {'request id is': f'{id}'}