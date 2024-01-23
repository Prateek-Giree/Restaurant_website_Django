from django.shortcuts import render, redirect
from MyApp.models import Contact
from django.contrib import messages

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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # creating object of Contact
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, "Your message has been sent successfully !")
        
        # to prevent form resubmission
        return redirect("/contact")
    return render(request, "contact.html")

    # return HttpResponse("This is  contact page")
