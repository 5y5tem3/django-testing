from django.shortcuts import render

def pfView(request):
    return render(request,"accounts/profile.html")
