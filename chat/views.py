from django.shortcuts import render, redirect, get_object_or_404
from .models import Text
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'chat/home.html', {})

@login_required
def text(request):
    texts = Text.objects
    return render(request, 'chat/chat.html',{'texts':texts})

@login_required
def send(request):
    if request.method == 'POST':
        text1 = Text()
        text1.text = request.POST.get('text')
        text1.time = timezone.now()
        text1.member = request.user
        text1.save()
        return redirect('/chat/text/')
                   