from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    description: str
    
    published: Optional[bool]


class BlogApp:
    def __init__(self):
        self.app = FastAPI()

    def run(self, host: str, port: int):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)

    def index(self):
        """Handler for the root endpoint."""
        return {'data': "Hi sudheer"}

    def unpublished(self):
        """Handler for the '/blog/unpublished' endpoint."""
        return {'data': "unpublished blogs"}

    def blog_details(self, id: int, limit: int = 10, published: bool = True, sort: Optional[str] = None):
        """Handler for the '/blog/{id}' endpoint."""
        return {'id': id, 'limit': limit, 'published': published, 'sort': sort}

    def blog_comments(self, id: int):
        """Handler for the '/blog/{id}/comments' endpoint."""
        return {'id': id, 'comments for this id': [1, 2, 3, 4]}

    def create_blog(self, blog: Blog):
        """Handler for the '/blog' endpoint (POST request)."""
        return {'data': f'Blog is created with the title as {blog.title}'}


# Create an instance of BlogApp
blog_app = BlogApp()

# Define route handlers that delegate to the corresponding methods in BlogApp

@app.get('/')
def index():
    return blog_app.index()

@app.get('/blog/unpublished')
def unpublished():
    return blog_app.unpublished()

@app.get('/blog/{id}')
def blog_details(id: int, limit: int = 10, published: bool = True, sort: Optional[str] = None):
    return blog_app.blog_details(id, limit, published, sort)

@app.get('/blog/{id}/comments')
def blog_comments(id: int):
    return blog_app.blog_comments(id)

@app.post('/blog')
def create_blog(blog: Blog):
    return blog_app.create_blog(blog)


if __name__ == '__main__':
    # Run the BlogApp instance
    blog_app.run(host='127.0.0.1', port=9000)
