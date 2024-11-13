from django.shortcuts import render,get_object_or_404
from . models import Students
# Create your views here.
def home(request):
    students = Students.objects.all()
    return render(request,"students/home.html",{'students':students})

def details(request,slug):
    student = get_object_or_404(Students,slug=slug)
    return render(request,"students/details.html",{'student':student})

def details_without_slug(request, id):  # Updated to match the URL pattern
    student = get_object_or_404(Students, id=id)
    return render(request, "students/details.html", {'student': student})
