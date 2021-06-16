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
from collections import defaultdict

def index(request):
    if request.user.is_authenticated:
        RegRepls = RegularReplacement.objects.all()
        locations = Location.objects.all()
        return render(request,'RegRepl/index.html', context={'RegRepls':RegRepls, 'locs':locations})
    else:
        return redirect('/accounts/login')
def regrepl_create(request, id):
    if request.user.is_authenticated:

        dirs_search = request.GET.get('dir_search','')
        print(dirs_search)
        RegRepl = RegularReplacement.objects.get(id=id)
        notinsectors = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(subdep=None).order_by('dir').order_by('cat')
        insectors = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(~Q(subdep=0)).order_by('dir').order_by('cat')
        all = RegularReplacementPos.objects.filter(bound_regrepl=id)
        all_salary_itogo = 0
        all_salaryrr_itogo = 0
        all_units_itogo = 0
        all_unitsrr_itogo = 0
        for pos in all:
            if pos.salary != 'контракт':
                all_salary_itogo = all_salary_itogo + int(pos.salary)
            if pos.salary_rr != 'контракт':
                if pos.salary_rr:
                    all_salaryrr_itogo = all_salaryrr_itogo + int(pos.salary_rr)
            all_units_itogo = all_units_itogo + pos.units
            all_unitsrr_itogo = all_unitsrr_itogo + pos.units_rr

        d = defaultdict(dict)

        deps = Departament.objects.all().order_by('id')
        d_salary = {}
        d_salary_rr = {}
        d_units = {}
        d_units_rr = {}
        for dep in deps:

            positions = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(dep_id=dep.id)
            salary_itogo = 0
            salaryrr_itogo = 0
            units_itogo = 0
            unitsrr_itogo = 0
            for pos in positions:
                if pos.salary != 'контракт':
                    salary_itogo = salary_itogo + int(pos.salary)
                if pos.salary_rr != 'контракт':
                    if pos.salary_rr:
                        salaryrr_itogo = salaryrr_itogo + int(pos.salary_rr)
                units_itogo = units_itogo + pos.units
                unitsrr_itogo = unitsrr_itogo + pos.units_rr
            d_salary[dep.id] = salary_itogo
            d_salary_rr[dep.id] = salaryrr_itogo
            d_units[dep.id] = units_itogo
            d_units_rr[dep.id] = unitsrr_itogo
        if dirs_search:
        
            dirs = DirDepartament.objects.get(id=dirs_search)

        else:
            dirs = DirDepartament.objects.all().order_by('id')
        dir_salary = {}
        dir_salary_rr = {}
        dir_units = {}
        dir_units_rr = {}
        if dirs_search:
            positions = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(dir_id=dirs_search)
            dir_salary_itogo = 0
            dir_salaryrr_itogo = 0
            dir_units_itogo = 0
            dir_unitsrr_itogo = 0
            for pos in positions:
                if pos.salary != 'контракт':
                    dir_salary_itogo = dir_salary_itogo + int(pos.salary)
                if pos.salary_rr != 'контракт':
                    if pos.salary_rr:
                        dir_salaryrr_itogo = dir_salaryrr_itogo + int(pos.salary_rr)
                dir_units_itogo = dir_units_itogo + pos.units
                dir_unitsrr_itogo = dir_unitsrr_itogo + pos.units_rr
        else:
            for dir in dirs:

                positions = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(dir_id=dir.id)

                dir_salary_itogo = 0
                dir_salaryrr_itogo = 0
                dir_units_itogo = 0
                dir_unitsrr_itogo = 0
                for pos in positions:

                    if pos.salary != 'контракт':
                        dir_salary_itogo = dir_salary_itogo + int(pos.salary)
                    if pos.salary_rr != 'контракт':
                        if pos.salary_rr:
                            dir_salaryrr_itogo = dir_salaryrr_itogo + int(pos.salary_rr)
                    dir_units_itogo = dir_units_itogo + pos.units
                    dir_unitsrr_itogo = dir_unitsrr_itogo + pos.units_rr

                dir_salary[dir.id] = dir_salary_itogo
                dir_salary_rr[dir.id] = dir_salaryrr_itogo
                dir_units[dir.id] = dir_units_itogo
                dir_units_rr[dir.id] = dir_unitsrr_itogo











        count = len(all)
        dirs = DirDepartament.objects.all()
        deps = Departament.objects.all()
        subdeps = SubDepartament.objects.all()
        return render(request, 'RegRepl/regrepl_create.html', context={
        'all_salary_itogo':all_salary_itogo,
    'all_salaryrr_itogo':all_salaryrr_itogo,
    'all_units_itogo':all_units_itogo,
    'all_unitsrr_itogo':all_unitsrr_itogo,
        'dir_salary':dir_salary,
    'dir_salary_rr':dir_salary_rr,
    'dir_units':dir_units,
    'dir_units_rr':dir_units_rr,


        'd_salary':d_salary,
    'd_salary_rr':d_salary_rr,
    'd_units':d_units,
    'd_units_rr':d_units_rr,
        'd':d,'count':count, 'rr':RegRepl, 'positions':notinsectors, 'insectors':insectors, 'dirs':dirs, 'deps':deps, 'subdeps':subdeps})
    else:
        return redirect('/accounts/login')
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
                return render(request, 'RegRepl/close.html')
            else:
                print(bound_form.errors.as_data())
    else:
        return redirect('/accounts/login')
def regpos_new(request,id):
    if request.user.is_authenticated:
        if request.method == "GET":
            rr = RegularReplacement.objects.get(id=id)
            pos_form = RegularReplacementPos_form()
            return render(request, 'RegRepl/new_regpos.html', context={'form':pos_form, 'rr':rr})
        else:
            pos_form = RegularReplacementPos_form(request.POST)
            if pos_form.is_valid():
                pos_form.saveFirst(id)
                loc = '/regrepl/create/' + str(id)
                return redirect(loc)
def regrepl_copy(request):
    if request.user.is_authenticated:
        location = request.POST.get('loc', '')
        print('loc= ' + location)

        regrepl = RegularReplacement.objects.filter(location_id=location).latest('id')
        old_regrepl = regrepl.id
        regrepl.id = None
        regrepl.duration = DT.datetime.now()
        regrepl.save()
        new_rr = RegularReplacement.objects.filter(location_id=location).latest('id')

        items_sub = RegularReplacementPos.objects.filter(bound_regrepl=old_regrepl)

        for item in items_sub:
            if item.disabled == False:


                if not item.subdep_id:

                    item.subdep_id = None
                    print(item.id)

                item.bound_regrepl = new_rr
                item.id = None
                item.save()





        return redirect('/')
    else:
        return redirect('/accounts/login')

# def regrepl_search_dir(request, dir):
#     if request.user.is_authenticated:
#
