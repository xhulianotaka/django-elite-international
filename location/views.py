from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

def location(request, id):
    name = "Irdjan"
    return render(request, 'location/test.html', {'person_name': name, 'id': id})




