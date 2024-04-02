from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def home(request):
    std = Student.objects.all()

    return render(request, 'std/home.html', {'std':std})


def add_std(request):
    if request.method=='POST':
        print('Added')
        std_roll = request.POST.get('std_roll')
        std_name = request.POST.get('std_name')
        std_email = request.POST.get('std_email')
        std_address = request.POST.get('std_address')
        std_phone = request.POST.get('std_phone')

        s = Student()
        s.roll=std_roll
        s.email=std_email
        s.name=std_name
        s.address=std_address
        s.phone=std_phone

        s.save()

        # return redirect('/add_std/home/')

    return render(request, 'std/add_std.html', {})

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect('/student/home')


def update_std(request,roll):
    std=Student.objects.get(pk=roll)

    return render(request,'student/update_std.html',{'std':std})

def do_update_std(request,roll):
    std_roll = request.POST.get('std_roll')
    std_name = request.POST.get('std_name')
    std_email= request.POST.get('std_email')
    std_address = request.POST.get('std_address')
    std_phone = request.POST.get('std_phone')

    std = Student.objects.get(pk=roll)

    std.roll = std_roll
    std.name = std_name
    std.email = std_email
    std.address = std_address
    std.phone = std_phone

    std.save()
    return redirect('/student/home')