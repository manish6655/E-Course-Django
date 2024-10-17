from django import template
import math
from codeax1.models import UserCourse,course

register = template.Library()

# 100 * discount * 0.01 = selprice

@register.simple_tag
def cal_price(price,discount):
    if discount is None or discount == 0:
        return price
    sellprice = price
    sellprice = price -(price*discount*0.01)
    return math.floor(sellprice)


@register.filter(name="currency")
def currency(price):
    return f'₹{price}'

@register.simple_tag
def is_enrolled(request,course):
    user = None
    if not request.user.is_authenticated:
        return False
    user = request.user
    try:
        UserCourse.objects.get(user = user,course=course)
        return True
    except:
        return False