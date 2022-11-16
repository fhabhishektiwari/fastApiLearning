from typing import Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn


app=FastAPI()

# @app.get('/')
# def index():
#     return {'data':{'name':'Nishant'}}


@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str]=None):
    # return published

    #only get 10 published blogs
    if published:
        return {'data':f"{limit} published blogs from the db "}
    else:
        return {'data':f"{limit} blogs from the db "}

@app.get('/about')
def about():
    return {'data':'about page'}




@app.get('/blog/unpublished')
def unpublished():
    return {"data":"all blog is unpublished"}


@app.get('/blog/{id}')
def showblog(id:int):
    # fetch blog with id=id
    return {"data":id}



@app.get('/blog/{id}/comments')
def comment(id):
    # fetch comment of blog id=id
    return {"data":{"1","2"}}


class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"Blog is create with title as {blog.title}"}


# if __name__=="__main__":
#     uvicorn.run(app,host='127.0.0.1',port=9000)

