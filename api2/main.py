from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return { 'data' : "Hi sudheer"};

@app.get('/blog/unpublished')
def unpublished():
    return {'data': "unpublished blogs"}

@app.get('/blog/{id}')
def blog(id:int,limit:int=10,published:bool = True,sort: Optional[str] = None):
    if published:
        return {'id' : id,'limit':limit,'published':published,'sort':sort}
    else:
        return {'id' : id,'limit':limit,'published':published,'sort':sort}
  
@app.get('/blog/{id}/comments')
def blog(id:int):
    return {'id' : id,'comments for this id' : [1,2,3,4]}

class Blog(BaseModel):
    title : str
    description : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(Blog : Blog):
    return {'data': f'Blog is created with the title as {Blog.title}'}


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=9000)