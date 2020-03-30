from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'main.html')


def a(request):
    name = 'name'
    return render({"name": name})
