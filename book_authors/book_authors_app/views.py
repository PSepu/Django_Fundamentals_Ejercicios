from django.shortcuts import render, redirect
from book_authors_app.models import Book, Author

def index(request):

    if request.method == "GET":
        return render(request, 'app/index.html')

    if request.method == "POST":
        print(request.POST)
        # PROCESAR EN BASE DE DATOS
        return redirect("/")

def books(request):

    if request.method == "GET":
        contexto = {
            'books': Book.objects.all().order_by()
        }
        return render(request, 'app/books.html', contexto)

    if request.method == "POST":
        print(request.POST)

        titulo = request.POST['title']
        desc = request.POST['desc']

        Book.objects.create(title=titulo, desc=desc)

        return redirect ("books")

def book_remove(request):
    if request.method == "POST":
        print(request.POST)

        book_to_delete=Book.objects.get(id=request.POST['book_id'])
        book_to_delete.delete()

        return redirect ("books")

def book(request, id):

    if request.method == "GET":

        contexto = {
            'book': Book.objects.get(id=id),
            'authors': Author.objects.all()
        }

        return render (request,'app/book.html',contexto)

def book_add_author(request, id):

    print(request.POST)

    book = Book.objects.get(id=id)
    author = Author.objects.get(id=request.POST['author'])

    book.authors.add(author)

    return redirect(f"/book/{id}/")

def book_remove_author(request, id):

    print(request.POST)

    book = Book.objects.get(id=id)
    author = Author.objects.get(id=request.POST['author'])

    book.authors.remove(author)

    return redirect(f"/book/{id}/")
