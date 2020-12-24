from django.shortcuts import render

def index(request):
    return render(request, 'news/page.html')

# Create your views here.
