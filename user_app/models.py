from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Userp(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_investor = models.BooleanField(default=True)
    is_entre = models.BooleanField(default=False)
    phone = models.CharField(max_length=13, default="")
    def __str__(self):
        return self.user.username;


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea_title = models.CharField(max_length=60, unique=True,default=" " )
    idea_desc = models.CharField(max_length=2048,default=" ")
    amount = models.IntegerField(default=0)
    no_of_days_req = models.IntegerField(default=0)
    last_date = models.DateField(null=True, blank=True,default=datetime.now)
    logo = models.ImageField(upload_to="idea/logo", default="d.jpg")
    def __str__(self):
        return self.idea_title;


class Entre(models.Model):
    user = models.ForeignKey(Userp, on_delete=models.CASCADE, null=True, related_name='entre_profile')
  #  idea_title = models.ForeignKey(Idea, on_delete=models.CASCADE, null=True, blank=True )
    logo = models.ImageField(upload_to="entre/logo", default="d.jpg")

    # class Meta:
    #     unique_together = ('idea_title','user.username')
    # def __str__(self):
    #     return self.user.username

class Investor(models.Model):
    user = models.ForeignKey(Userp, on_delete=models.CASCADE, null=True, related_name='investor_profile')
    total_funds =models.IntegerField(default=0)
    previous_proj = models.CharField(max_length=1000,default="nan")
    logo = models.ImageField(upload_to="investor/logo", default="d.jpg")

    # def __str__(self):
    #     return self.user.username


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     print('****', created)
#     if instance.is_intern:
#         Investor.objects.get_or_create(user=instance)
#     else:
#         Entre.objects.get_or_create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print('_-----')
#     # print(instance.internprofile.bio, instance.internprofile.location)
#     if instance.is_investor:
#         instance.investor_profile.save()
#     else:
#         instance.entre_profile.save()
