from django.contrib.auth.models import User
from django.db import models
from django import forms



class LectureUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    def update_rating(self, new_rating):
        self.rate = (self.rate * self.count + new_rating) / (self.count + 1)
        self.count += 1
        self.save()

    def __str__(self):
        return self.title

class Lecture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()\

    def __str__(self):
        return f"{self.user.username} {self.age}"

class RatingForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=10, required=True)


    # Create your models here.
