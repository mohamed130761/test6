from django.shortcuts import render
from django.http import JsonResponse



def api_view(request):
    return JsonResponse({"message": "Hello from the backend!"})
# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def about (request):
    return render(request,'pages/about.html')
