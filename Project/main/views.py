from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def room(request):
    return render(request, "main/room.html")
