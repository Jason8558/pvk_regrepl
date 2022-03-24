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
            "is_head",
            # "dir",
            # "dep",
            # "subdep",
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
            "comm",
            "disabled"
        ]

    free = forms.BooleanField(label="Ставка свободна" , required=False, widget=forms.CheckboxInput(
            attrs={ 'id': 'id_free', 'onchange':'free_position()'}))

    def saveFirst(self, bound_rr, dir, dep, subdep):
        # b_regrepl = RegularReplacement.objects.get(id=bound_regrepl)

        new_position = RegularReplacementPos.objects.create(

        bound_regrepl_id = bound_rr,
        name = self.cleaned_data["name"],
        dir = dir,
        dep = dep,
        subdep = subdep,
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
        comm = self.cleaned_data["comm"],
        disabled = self.cleaned_data["disabled"] )
    def saveUpd(self, pos, dir, dep, subdep):
        upd_position = RegularReplacementPos.objects.filter(id=pos).update(

                name = self.cleaned_data["name"],
                dir = dir,
                dep = dep,
                subdep = subdep,
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
                comm = self.cleaned_data["comm"],
                disabled = self.cleaned_data["disabled"] )

class Departament_form(forms.ModelForm):
    class Meta:
        model = Departament
        fields = [
                        "name",

                        "location"

                    ]
    def addtodir(self, id):
        dir = DirDepartament.objects.get(id=id)
        dep = Departament.objects.latest('id')
        dir.dep.add(dep)

class SubDepartament_form(forms.ModelForm):
    class Meta:
        model = SubDepartament
        fields = [
                        "name",

                        "location"

                    ]
    def addtodep(self, id):
        dep = Departament.objects.get(id=id)
        subdep = SubDepartament.objects.latest('id')
        dep.subdep.add(subdep)
