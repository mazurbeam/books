from django.shortcuts import render, redirect
from .models import Book
# Create your views here.

def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'books/index.html', context)

def create(request):
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
