from django.urls import path
from .views import index,coursePage,SignupView,LoginView,signout,checkOut,verifyPayment,MyCourseList
from .views import HomePageView
urlpatterns = [
    path("",index,name="index"),
    path("course/",HomePageView.as_view(),name="course"),
    path("signup",SignupView.as_view(),name="signup"),
    path("login",LoginView.as_view(),name="login"),
    path("logout",signout,name="logout"),
    path("my-courses", MyCourseList.as_view(), name="my-courses"),
    path('coursepage/<str:slug>', coursePage, name='checkout'),
    path('check-out/<str:slug>', checkOut, name='check-out'),
    path('verify_payment', verifyPayment, name='verify_payment')
]
