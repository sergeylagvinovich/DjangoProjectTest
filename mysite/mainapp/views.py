from django.shortcuts import render

def index(request):
    return render(request, "mainapp/homePage.html")

def contact(request):
    return render(request, "mainapp/basic.html", {'values': ['Если у Вас остались вопросы, то задавайте их мне по телефону', '(25) 585-54-48']})

# Create your views here.
