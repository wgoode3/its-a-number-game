from django.shortcuts import render, redirect
from random import randint

# Create your views here.
def index(request):
    if "num" not in request.session:
        request.session["num"] = randint(1, 100)
    return render(request, "index.html")

def guess(request):
    print(request.POST)
    if len(request.POST["guess"]) < 1:
        request.session["status"] = "You must make a guess first"
        return redirect("/")
    guess = int(request.POST["guess"])
    if guess == request.session["num"]:
        request.session["status"] = "Correct"
    elif guess > request.session["num"]:
        request.session["status"] = "Too High"
    else:
        request.session["status"] = "Too Low"
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")