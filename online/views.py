from django.shortcuts import render

def storView(request):  
    return render(request, "online/store.html")
