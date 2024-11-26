from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'inventory/home.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        category = request.POST['category']
        price = request.POST['price']
        quantity = request.POST['quantity']
        Book.objects.create(title=title, author=author, category=category, price=price, quantity=quantity)
        return redirect('home')
    return render(request, 'inventory/add_book.html')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('home')
