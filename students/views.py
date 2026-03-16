from django.shortcuts import render, redirect
from students.models import Student

def students_list(request):
         students=Student.objects.all()
         return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        email = request.POST.get('email')
        course = request.POST.get('course')

        Student.objects.create(
            name=name,
            roll_no = int(roll_no),
            email=email,
            course=course
        )

        return redirect('student_list')

    return render(request, 'students/add_student.html')

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.roll_no = request.POST.get('roll_no')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.save()

        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student})

def students_list(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, 'students/student_list.html', {'students': students})
