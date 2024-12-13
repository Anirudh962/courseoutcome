from django.shortcuts import redirect, render
from .models import course_outcomes
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def outcomes(request):
    return render(request,"course_outcomes.html",{})

def insertuser(request):
    vtucname= request.POST['tucname']; 
    vtudes = request.POST['tudes'];
    vtuchours = request.POST['tuchours'];
    vtumarks = request.POST['tumarks'];
    co= course_outcomes(course_name=vtucname,description=vtudes,contact_hours=vtuchours,marks=vtumarks);
    co.save();
    return render(request,'course_outcomes.html',{})

def view_users(request):
    # Fetch all courses from the database
    courses = course_outcomes.objects.all()
    return render(request, 'viewuser.html', {'courses': courses})

def deleteprofile(request,tucname):
    courses_name=course_outcomes.object.get(course_name=tucname)
    courses_name.delete()
    return redirect("/viewusers")



    

