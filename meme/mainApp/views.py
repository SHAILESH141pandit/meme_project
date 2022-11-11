from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Meme app.")





# for Registation 
def register(request):
    if request.method == "POST":

        Fname = request.POST["Fname"]
        Lname = request.POST["Lname"]
        tel = request.POST["Tel"]
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

        return HttpResponse("<h1>This is GET requist for Registation.")
    else :
        return render(request, "Register.html")




# for Login
def login(request):
    if request.method == "POST":

        email = request.POST["Email"]
        password = request.POST["Password"]
        print(f"         Email : {email}")
        print(f"      Password : {password}")

        return HttpResponse("<h1>This is GET requist for Login.")

    else:
        return render(request, "Login.html")