from django.contrib import admin
from .models import Chatroom, Member, Message

# Register your models here.

admin.site.register(Chatroom)
admin.site.register(Member)
admin.site.register(Message)