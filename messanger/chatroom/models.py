from django.db import models

# Create your models here.
class Chatroom(models.Model):
    cname=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.cname

class Member(models.Model):
    mname=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.mname

class Message(models.Model):
    msg=models.CharField(max_length=100)
    member=models.ForeignKey('Member',on_delete=models.CASCADE)
    chatroom=models.ForeignKey('Chatroom',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']


