from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'books/home.html')

def books(request):
    return render(request, 'books/books.html')

def prestamos(request):
    return render(request, 'books/prestamos.html')