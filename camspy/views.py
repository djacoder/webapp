from django.shortcuts import render
from camspy.models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def wait(request):
    return render(request, 'wait.html')
