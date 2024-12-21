from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course, Lecture, RatingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView





def course_list(request):
    courses = Course.objects.all()
    return render(request, "exam/course_list.html", {"courses": courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            new_rating = form.cleaned_data["rating"]
            course.update_rating(new_rating)
            return redirect("course_detail", course_id=course_id)
    else:
        form = RatingForm()
    return render(request, "exam/course_detail.html", {"course": course, "form": form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'exam/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'exam/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'logged_out.html'

# Create your views here.
