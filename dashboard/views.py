# dashboard/views.py

from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, "dashboard/home.html")
        
    else:
        print('NOT authenticated')
        return redirect("login")
