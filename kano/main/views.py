from django.shortcuts import render


# Create your views here.

def main(request):
    name = 'name'
    return render(request, 'main.html', {"name": name})