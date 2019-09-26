from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def apphome(request):
    return HttpResponse('this is first app')