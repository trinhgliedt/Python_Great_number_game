from django.shortcuts import render
import random

def index(request):
    
    number = random.randint(1, 100)
    print("Number: ",number)
    request.session["correct_number"] = number
    print("correct_number: ",request.session["correct_number"])
    return render(request, 'index.html')

def process_form(request):
    # request.session['result'] = "Too high!!"
    print("user_guess: ",request.POST["user_guess"])
    request.session["user_input"] = int(request.POST["user_guess"])
    print('type of request.session["user_input"]: ',type(request.session["user_input"]))
    # print('type of request.POST["user_guess"]: ',type(request.POST["user_guess"]))
    print('type of request.session["correct_number"]: ',type(request.session["correct_number"]))
    # request.session['bg_color'] = "red"
    if request.session["user_input"] > request.session["correct_number"]:
        request.session['result'] = "Too high!"
        request.session['bg_color'] = "red"
    elif request.session["user_input"] < request.session["correct_number"]:
        request.session['result'] = "Too low!"
        request.session['bg_color'] = "red"
    elif request.session["user_input"] == request.session["correct_number"]:
        request.session['result'] = str(request.session["user_input"]) + " was the number!"
        request.session['bg_color'] = "green"
    
    print("correct_number: ",request.session["correct_number"])
    return render(request, 'result.html')