from django import forms
from .models import Userp,Investor,Idea,Entre
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password');

class UserpForm(forms.ModelForm):
    class Meta:
        model = Userp
        fields = ('phone', 'is_investor', 'is_entre');


class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = "__all__"


class EntreForm(forms.ModelForm):
    class Meta:
        model = Entre
        fields = "__all__"


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('idea_title','idea_desc','amount','no_of_days_req','last_date')