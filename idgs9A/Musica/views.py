from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "Musica/inicio.html")

def cancion(request):
    return render(request, "Musica/cancion.html")

def blog(request):
        return render(request, "Musica/blog.html")

def about(request):
        return render(request, "Musica/about.html")

def contact(request):
        return render(request, "Musica/contact.html")


from django.shortcuts import render
