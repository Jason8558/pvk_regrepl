from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
import datetime as DT
from itertools import groupby
from django.contrib.auth.models import *
from django.db.models import Q

def index(request):
    RegRepls = RegularReplacement.objects.all()

    return render(request,'RegRepl/index.html', context={'RegRepls':RegRepls})

def regrepl_create(request, id):
    # RegRepl = RegularReplacement.objects.get(id=id)
    notinsectors = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(subdep=0).order_by('dir')
    insectors = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(~Q(subdep=0)).order_by('dir')
    dirs = DirDepartament.objects.all()
    deps = Departament.objects.all()
    subdeps = SubDepartament.objects.all()
    return render(request, 'RegRepl/regrepl_create.html', context={'positions':notinsectors, 'insectors':insectors, 'dirs':dirs, 'deps':deps, 'subdeps':subdeps})

def regpos_update(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            pos = RegularReplacementPos.objects.get(id=id)
            bound_form = RegularReplacementPos_form(instance=pos)
            return render(request, 'RegRepl/upd_regpos.html', context={'form':bound_form, 'pos':pos})
        else:
            pos = RegularReplacementPos.objects.get(id=id)

            bound_form = RegularReplacementPos_form(request.POST, instance=pos)
            if bound_form.is_valid():
                bound_form.save()
                loc = '/regrepl/create/' + str(pos.bound_regrepl.id)
                return redirect(loc)
