from django.shortcuts import render
from Getter.models import Student
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    Stud = Student.objects.all()
    dict = {
        'Stud':Stud,
    }
    return render(request,"index.html", dict)