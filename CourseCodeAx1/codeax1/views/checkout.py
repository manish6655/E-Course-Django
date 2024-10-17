from django.shortcuts import render
from codeax1.models import Course,Video,Payment,UserCourse
from django.shortcuts import HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from time import time
from CourseCodeAx1.settings import *

import razorpay
client = razorpay.Client(auth=(KEY,SECRET_KEY))

@login_required(login_url="login")
def checkOut(request,slug):
    course = Course.objects.get(slug=slug)

    # If you are enrolled you can watch all the Video
    user = request.user
    action = request.GET.get('action')
    amount = None
    order = None
    payment = None
    error = None
    if action == 'create_payment':
        try:
            UserCourse.objects.get(user = user,course=course)
            error = "You are Aalready Enrolled in this course"

        except:
            pass
        if error is None:
            amount = int((course.price -(course.price*course.discount*0.01)) * 100)
            if amount == 0:
                userCourse = UserCourse(user=user,course=course)
                userCourse.save()
                return redirect("my-courses")

            currency = "INR"
            notes = {
                "email":user.email,
                "name":f'{user.first_name} {user.last_name}'

            }
            receipt = f"codeax1-{int(time())}"
            order =client.order.create({'receipt':receipt,'amount':amount,'notes':notes,'currency':currency})

            # Data add to payment model

            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()
    context = {
        "course":course,
        "order":order,
        "payment":payment,
        "user":user,
        "error":error
    }
    return render(request, template_name="courses/check_out.html",context=context)
@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True
            userCourse = UserCourse(user=payment.user,course=payment.course)
            userCourse.save()
            payment.user_course = userCourse
            payment.save()
            return redirect("my-courses")
        except:
            return HttpResponse("Invalid payment details")