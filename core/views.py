from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, template_name='index.html')

def detal(request):
    return render(request, template_name='exam_correct.html')