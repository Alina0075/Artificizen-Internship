from fastapi import FastAPI, HTTPException
app=FastAPI()

@app.get('/')
def question1():
    return {"message": "Hello, Artificizen"}


@app.get('/users/{user_id}')
def get_user_id(user_id:int):
    if user_id > 100:
        raise HTTPException(
            status_code=404,
            detail='User not found'
        )
    return {"user_id": user_id}


@app.get('/items')
def get_items(skip: int =0, limit: int=10):
    items = [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Phone",
        "Camera",
        "Printer",
        "Tablet",
        "Speaker",
        "Headphones",
        "Microphone",
        "Router"
    ]
    return items[skip: skip +limit]


@app.post('/ping', status_code=201)
def ping():
    return {'Status':'created'}
