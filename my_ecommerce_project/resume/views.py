from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def home(request):
    return HttpResponse('<h1>HOME PAGE</h1>')

def index(request):
    return render(request, 'resume/index.html')