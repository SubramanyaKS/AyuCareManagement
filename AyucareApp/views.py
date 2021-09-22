from django.shortcuts import render

# Create your views here.
def nhome(request):
    return render(request,"home.html")

