from django.db import models
from .course import Course
class Video(models.Model):
    title = models.CharField(max_length=30,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    video_id = models.CharField(max_length=50,null=False)
    isPreview = models.BooleanField(default=False)
    serial_number = models.IntegerField(null=False)

    def __str__(self):
        return self.title