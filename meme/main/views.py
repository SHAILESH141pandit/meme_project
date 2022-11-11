from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Meme app.")


def register(request):
    if request.method == "POST":

        Fname = request.POST["Fname"]
        Lname = request.POST["Lname"]
        tel = request.POST["tel"]
        email = request.POST["Email"]
        password = request.POST["Password"]

        print(f"    First name : {Fname}")
        print(f"     Last name : {Lname}")
        print(f"Contect number : {tel}")
        print(f"         Email : {email}")
        print(f"      Password : {password}")
        
        print("----------------------------")
        print(request.POST)
        print("----------------------------")
        var = request.POST
        for i in var:
            print(i,":",var[i])
        print("----------------------------")


        return HttpResponse("<h1>This is GET requist.")
    else :
        return render(request, "Register.html")
