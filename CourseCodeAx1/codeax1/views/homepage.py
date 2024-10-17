from django.shortcuts import render
from codeax1.models.course import Course
from django.views.generic import ListView


def index(request):
    return render(request,"courses/index.html")


class HomePageView(ListView):
    template_name = "courses/course.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = "courses"