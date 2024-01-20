from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def menu(request):
    # return HttpResponse("Menu:")
    return render(request, "menu.html")


def about(request):
    return render(request, "about.html")

    # return HttpResponse("This is about page")


def contact(request):
    return render(request, "contact.html")

    # return HttpResponse("This is  contact page")
