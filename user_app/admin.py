from django.contrib import admin
from .models import  Userp,Entre,Investor,Idea
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Userp)
admin.site.register(Idea)
admin.site.register(Investor)
admin.site.register(Entre)
# uname=abc123 pass=abc123
