from typing import Union

from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Nishant'}}

@app.get('/about')
def about():
    return {'data':'about page'}