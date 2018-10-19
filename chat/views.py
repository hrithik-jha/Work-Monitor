from django.shortcuts import render, redirect
from .models import Text
from django.utils import timezone
from django.template import RequestContext

def home(request):
    return render(request, 'chat/home.html', {})

def text(request):
    if request.method == 'POST':
        if request.POST['text']:
            text = Text()
            text.text = request.POST['text']
            text.time = timezone.now()
            
            #return render(request, 'chat/chat.html')

        return render(request, 'chat/chat.html')

    else:
        return render(request, 'chat/chat.html')