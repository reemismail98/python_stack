from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from .models import Book,Author
# show all of the data from a table
def index(request):
    context = {
    	"all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all()
    }
    return render(request, "index.html", context)

def bookform(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect("/") 

def authorform(request):
    Author.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'], notes=request.POST['notes'])
    return redirect("/authors") 

def show(request,id):
    context = {
        'book' : Book.objects.get(id=id),
        "all_the_authors": Author.objects.all(),
    }
    return render(request, "books.html", context)

def indexauthor(request):
    context = {
    	"all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def showauthor(request,id):
    context = {
        'author' : Author.objects.get(id=id),
        "all_the_books": Book.objects.all(),
        'bookname' : Author.objects.get(id=id),
    }
    return render(request, "aythorinfirmation.html", context)
def selectauthor(request):
    if request.method == "POST":
        this_book=Book.objects.get(id=request.POST['this_book'])
        this_author=Author.objects.get(last_name=request.POST["authorid"])
        this_book.publishers.add(this_author)
        x="books/"+request.POST["this_book"]
        return redirect(x) 

def selectbook(request):
    if request.method == "POST":
        this_author=Author.objects.get(id=request.POST['this_author'])
        this_book=Book.objects.get(title=request.POST["bookid"])
        this_author.books.add(this_book)
        y="authors/"+request.POST["this_author"]
        return redirect(y)