
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import Student, Course


def home(request):
    error = None

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        course_id = request.POST.get("course", "")

        if not name or not email or not course_id:
            error = "All fields are required."
        else:
            course = get_object_or_404(Course, id=course_id)

            try:
                Student.objects.create(
                    name=name,
                    email=email,
                    course=course
                )
                return redirect("home")
            except IntegrityError:
                error = "This email is already registered."

    students = Student.objects.select_related("course").all()
    courses = Course.objects.all()

    return render(request, "home.html", {
        "students": students,
        "courses": courses,
        "error": error,
    })


def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    error = None

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        course_id = request.POST.get("course", "")

        if not name or not email or not course_id:
            error = "All fields are required."
        else:
            course = get_object_or_404(Course, id=course_id)

            student.name = name
            student.email = email
            student.course = course

            try:
                student.save()
                return redirect("home")
            except IntegrityError:
                error = "This email is already used by another student."

    return render(request, "update.html", {
        "student": student,
        "courses": courses,
        "error": error,
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("home")

    return render(request, "delete.html", {"student": student})
