from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from codeax1.models.course import Course
from codeax1.models.video import Video
from django.views import View
from django.contrib.auth import logout,login
from codeax1.forms import RegistrationForm,LoginForm
from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name="courses/signup.html"
    form_class = RegistrationForm
    success_url = "/login"

    def form_valid(self,form):
        form.save() 
        return super().form_valid(form)

'''
class SignupView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, template_name="courses/signup.html",context={'form':form})
    def post(elf,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
        else:
            return render(request, template_name="courses/signup.html", context={'form': form})

'''


class LoginView(FormView):
    template_name="courses/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self,form):
        login(self.request,form.cleaned_data)
        next_page =  self.request.GET.get("next")
        if next_page is not None:
            return redirect("next_page")
        return super().form_valid(form)

'''
class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, template_name="courses/login.html",context=context)
    def post(self,request):
        form = LoginForm(request, data=request.POST)
        context = {
            "form":form
        }
        if(form.is_valid()):
            return redirect("index")
        return render(request, template_name="courses/login.html",context=context)
'''
def signout(request):
    logout(request)
    return redirect("index")