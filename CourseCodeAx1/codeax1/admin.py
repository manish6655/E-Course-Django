from django.contrib import admin
from codeax1.models import Course,Tag,Prerequisite,Learning,UserCourse,Payment
from codeax1.models import Video
from django.utils.html import format_html

class VideoAdmin(admin.TabularInline):
    model = Video
class TagAdmin(admin.TabularInline):
    model = Tag
class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite
class LearningAdmin(admin.TabularInline):
    model = Learning

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,LearningAdmin,PrerequisiteAdmin,VideoAdmin]
    list_display = ["name","get_price","get_discount","active"]

    def get_price(self,course):
        return f'₹ {course.price}'
    def get_discount(self,course):
        return f'{course.discount} %'
    
class UserCourseAdmin(admin.TabularInline):
    model = UserCourse
    

class PaymentAdmin(admin.ModelAdmin):
    list_display = ["get_user","order_id","get_course","status"]
    list_filter = ["status","course"]

    def get_user(self,payment):
        return format_html(f"<a target='_blank' href='/adminPage/auth/user/{payment.user.id}'>{payment.user}</a>")
    
    def get_course(self,course):
        return format_html(f"<a target='_blank' href='/adminPage/codeax1/course/{course.user.id}'>{course.course}</a>")




admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(UserCourse)
admin.site.register(Payment,PaymentAdmin)
