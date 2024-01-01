from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def hello(request):
    info ={"Name": "Abodunrin Stephen",
           "Gender": "Male",
           "github url": "https://github.com/Donchess1" }
    return JsonResponse(info)