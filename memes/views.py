from django.shortcuts import render
from .models import Home, Message

# Create your views here.
def home(request):
    titles = Home.objects.all()
    context = {
        'titles' : titles
    }
    return render(request, 'main/index.html',context)

def content(request):
    memes = Message.objects.all()
    context = {
        'memes':memes
    }
    return render(request, 'main/content.html',context)

