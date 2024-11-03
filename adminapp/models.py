from django.db import models


class Task(models.Model):
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.title


from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='example@example.com')  # Add default value
    phone = models.CharField(max_length=15)
    description = models.CharField(max_length=150)

    def _str_(self):
        return self.name

from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number=models.CharField(max_length=20, unique=True)
    Name=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Register_Number


from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='example@example.com')  # Add default value
    phone = models.CharField(max_length=15)
    description = models.CharField(max_length=150)

    def _str_(self):
        return self.name


