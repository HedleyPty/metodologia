from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html", context= {})

@login_required
def protocolo(request):
    pass
@login_required
def evaluacion(request):
    pass