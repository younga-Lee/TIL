from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chattings/index.html')

def create(request):
    return render(request, 'chattings/create.html')