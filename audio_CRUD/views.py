from django.shortcuts import render

# Index View Here

def index(request):
    return render(request, 'index.html')