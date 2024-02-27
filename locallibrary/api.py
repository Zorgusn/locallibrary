from ninja import NinjaAPI, Schema
from typing import List
from catalog.models import Book, Author, Genre
from django.shortcuts import get_object_or_404

api = NinjaAPI()

class HelloSchema(Schema):
    name: str = "world"

@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}!"

@api.get("/math/{a}and{b}")
def math(request, a:int, b:int):
    return {'add': a+b, "multiply":a*b}

class BookOut(Schema):
    id: int
    title: str
    isbn: str  
    # author: Author
    summary: str
    # genre: Genre 

@api.get("/books/{book_id}", response=BookOut)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book

@api.get("/books", response=List[BookOut])
def list_books(request):
    books = Book.objects.all()
    return books