from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
import datetime as DT
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'lform-input loginField', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'lform-input pwdField',
            'placeholder': '',
            'id': 'hi',
        }
))

class RegularReplacementPos_form(forms.ModelForm):
    class Meta:
        model = RegularReplacementPos
        fields = [
            "bound_regrepl",
            "name",
            "dir",
            "dep",
            "subdep",
            "units",
            "level",
            "cat",
            "payment",
            "salary",
            "units_rr",
            "level_rr",
            "cat_rr",
            "payment_rr",
            "salary_rr",
            "employer1",
            "employer2",
            "employer3",
            "free",
            "comm"
        ]

        def saveFirst(self, bound_regrepl):
            # b_regrepl = RegularReplacement.objects.get(id=bound_regrepl)

            new_position = RegularReplacementPos.objects.create(

            bound_regrepl = bound_regrepl,
            name = self.cleaned_data["name"],
            dir = self.cleaned_data["dir"],
            dep = self.cleaned_data["dep"],
            subdep = self.cleaned_data["subdep"],
            units = self.cleaned_data["units"],
            level = self.cleaned_data["level"],
            cat = self.cleaned_data["cat"],
            payment = self.cleaned_data["payment"],
            salary = self.cleaned_data["salary"],
            units_rr = self.cleaned_data["units_rr"],
            level_rr = self.cleaned_data["level_rr"],
            cat_rr = self.cleaned_data["cat_rr"],
            payment_rr = self.cleaned_data["payment_rr"],
            salary_rr = self.cleaned_data["salary_rr"],
            employer1 = self.cleaned_data["employer1"],
            employer2 = self.cleaned_data["employer2"],
            employer3 = self.cleaned_data["employer3"],
            free = self.cleaned_data["free"],
            comm = self.cleaned_data["comm"] )
