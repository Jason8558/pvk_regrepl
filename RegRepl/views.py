from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
import datetime as DT
from itertools import groupby
from django.contrib.auth.models import *
from django.db.models import Q
from collections import defaultdict
import xlwt
import os

def index(request):
    if request.user.is_authenticated:
        RegRepls = RegularReplacement.objects.all()
        locations = Location.objects.all()
        LastRR = RegularReplacement.objects.latest('id').id
        Total = RegularReplacementPos.objects.filter(bound_regrepl=LastRR)
        busy = Total.filter(free=0)
        free = Total.filter(free=1)

        return render(request,'RegRepl/index.html', context={'RegRepls':RegRepls, 'locs':locations, 'total':len(Total), 'busy':len(busy), 'free':len(free)})
    else:
        return redirect('/accounts/login')

def regrepl_create(request, id):
    if request.user.is_authenticated:
        not_free_pos = RegularReplacementPos.objects.filter(free=0).filter(bound_regrepl_id=id)
        not_free_pos_cnt = len(not_free_pos)
        temp_pos = RegularReplacementPos.objects.filter(~Q(employer2='')).filter(bound_regrepl_id=id)
        print(len(temp_pos))
        print(not_free_pos_cnt)
        dirs_search = request.GET.get('dir_search','')

        RegRepl = RegularReplacement.objects.get(id=id)
        notinsectors = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(subdep=None).order_by('cat','id','dir')
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

            notinsectors = RegularReplacementPos.objects.filter(bound_regrepl=id).filter(dir_id=dirs_search)

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
        'd':d,'count':count, 'rr':RegRepl, 'positions':notinsectors, 'insectors':insectors, 'dirs':dirs, 'deps':deps, 'subdeps':subdeps, 'not_free_pos_cnt':not_free_pos_cnt, 'temp_pos':len(temp_pos)})
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
            dir = request.POST.get('urp_dir', '')
            dep = request.POST.get('urp_dep', '')
            subdep = request.POST.get('urp_subdep', '')
            dir = DirDepartament.objects.get(id=dir)
            dep = Departament.objects.get(id=dep)
            if subdep:
                subdep = SubDepartament.objects.get(id=subdep)
            else:
                subdep = None
            bound_form = RegularReplacementPos_form(request.POST, instance=pos)
            if bound_form.is_valid():
                bound_form.saveUpd(pos.id, dir, dep, subdep)
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
            dir = request.POST.get('nrp_dir', '')
            dep = request.POST.get('nrp_dep', '')
            subdep = request.POST.get('nrp_subdep', '')
            dir = DirDepartament.objects.get(id=dir)
            dep = Departament.objects.get(id=dep)
            if subdep:
                subdep = SubDepartament.objects.get(id=subdep)
            else:
                subdep = None
            pos_form = RegularReplacementPos_form(request.POST)
            if pos_form.is_valid():
                pos_form.saveFirst(id, dir, dep, subdep)
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

        items_sub = RegularReplacementPos.objects.filter(bound_regrepl=old_regrepl).order_by('id')

        for item in items_sub:
            print(str(item.id) + " " + str(item.name))
            if item.disabled == False:


                if not item.subdep_id:

                    item.subdep_id = None


                item.bound_regrepl = new_rr
                item.id = None
                item.save()





        return redirect('/')
    else:
        return redirect('/accounts/login')

def regrepl_search(request, rr):
    if request.user.is_authenticated:
        rr = RegularReplacement.objects.get(id=rr)
        return render(request, 'RegRepl/regrepl_search_dirs.html', context={'rr':rr})

def regrepl_json(request, type, id, rr):
    if request.user.is_authenticated:
        if type == 1:
            positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).filter(dir_id=id).values('id', 'bound_regrepl_id', 'name', 'dir__name', 'dep','dep__name', 'subdep__name', 'units',
            'level',
            'cat_id',
            'cat__name',
            'payment',
            'salary',
            'units_rr',
            'level_rr',
            'cat_rr_id',
            'cat_rr__name',
            'payment_rr',
            'salary_rr',
            'employer1',
            'employer2',
            'employer3',
            'free',
            'comm',
            'disabled' ).order_by('dir_id__iter', 'dep_id__iter', 'subdep_id','-is_head', 'cat_id', 'name',  '-payment', 'employer1' )
            positions = list(positions)
            return JsonResponse(positions, safe=False)
        if type == 2:
            positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).filter(dep_id=id).values('id', 'bound_regrepl_id', 'name', 'dir__name', 'dep','dep__name', 'subdep__name', 'units',
            'level',
            'cat__name',
            'cat_id',
            'payment',
            'salary',
            'units_rr',
            'level_rr',
            'cat_rr__name',
            'cat_rr_id',
            'payment_rr',
            'salary_rr',
            'employer1',
            'employer2',
            'employer3',
            'free',
            'comm',
            'disabled' ).order_by('dir_id__iter', 'dep_id__iter', 'subdep_id','-is_head', 'cat_id', 'name',  '-payment', 'employer1' )
            positions = list(positions)
        if type == 4:
            positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).filter(cat_id=id).values('id','name', 'bound_regrepl_id', 'dir__name', 'dep','dep__name', 'subdep__name', 'units',
            'level',
            'cat__name',
            'cat_id',
            'payment',
            'salary',
            'units_rr',
            'level_rr',
            'cat_rr__name',
            'cat_rr_id',
            'payment_rr',
            'salary_rr',
            'employer1',
            'employer2',
            'employer3',
            'free',
            'comm',
            'disabled' ).order_by('dir_id__iter', 'dep_id__iter', 'subdep_id','-is_head', 'cat_id', 'name',  '-payment', 'employer1' )
            positions = list(positions)
        if type == 5:

            positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).values('bound_regrepl_id', 'id','name', 'dir_id', 'dir__name', 'dep','dep__name', 'subdep' ,'subdep__name', 'units',
            'level',
            'cat__name',
            'cat_id',
            'payment',
            'salary',
            'units_rr',
            'level_rr',
            'cat_rr__name',
            'cat_rr_id',
            'payment_rr',
            'salary_rr',
            'employer1',
            'employer2',
            'employer3',
            'free',
            'comm',
            'disabled' ,
            'is_head').order_by('dir_id__iter', 'dep_id__iter', 'subdep_id','-is_head', 'cat_id', 'name',  '-payment', 'employer1' )

            positions = list(positions)
        if type == 6:

            positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).filter(free=1).values('bound_regrepl_id', 'id','name', 'dir_id', 'dir__name', 'dep','dep__name', 'subdep' ,'subdep__name', 'units',
            'level',
            'cat__name',
            'cat_id',
            'payment',
            'salary',
            'units_rr',
            'level_rr',
            'cat_rr__name',
            'cat_rr_id',
            'payment_rr',
            'salary_rr',
            'employer1',
            'employer2',
            'employer3',
            'free',
            'comm',
            'disabled' ).order_by('dir_id__iter', 'dep_id__iter', 'subdep_id','-is_head', 'cat_id', 'name',  '-payment', 'employer1' )
            print(positions)
            positions = list(positions)

        if type == 7:
            if id == 1:
                positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).filter(~Q(name__contains='ЕМР')).values('bound_regrepl_id', 'id','name', 'dir_id', 'dir__name', 'dep','dep__name', 'subdep' ,'subdep__name', 'units',
                'level',
                'cat__name',
                'cat_id',
                'payment',
                'salary',
                'units_rr',
                'level_rr',
                'cat_rr__name',
                'cat_rr_id',
                'payment_rr',
                'salary_rr',
                'employer1',
                'employer2',
                'employer3',
                'free',
                'comm',
                'disabled' ).order_by('dir_id__iter', 'dep_id__iter', 'subdep_id','-is_head', 'cat_id', 'name',  '-payment', 'employer1' )
            else:
                positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).filter(name__contains='ЕМР').values('bound_regrepl_id', 'id','name', 'dir_id', 'dir__name', 'dep','dep__name', 'subdep' ,'subdep__name', 'units',
                'level',
                'cat__name',
                'cat_id',
                'payment',
                'salary',
                'units_rr',
                'level_rr',
                'cat_rr__name',
                'cat_rr_id',
                'payment_rr',
                'salary_rr',
                'employer1',
                'employer2',
                'employer3',
                'free',
                'comm',
                'disabled' ).order_by('dir_id__iter', 'dep_id__iter', 'subdep_id','-is_head', 'cat_id', 'name',  '-payment', 'employer1' )
            print(positions)
            positions = list(positions)

        return JsonResponse(positions, safe=False)

def get_positions(request, pos, rr):
    if request.user.is_authenticated:
        positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).filter(name__icontains=pos).values('id','name', 'dir__name', 'dep','dep__name', 'subdep__name', 'units',
        'level',
        'cat_id',
        'cat__name',
        'payment',
        'salary',
        'units_rr',
        'level_rr',
        'cat_rr_id',
        'cat_rr__name',
        'payment_rr',
        'salary_rr',
        'employer1',
        'employer2',
        'employer3',
        'free',
        'comm',
        'disabled' ).order_by('dep_id', 'id', 'cat_id',  'subdep_id')
        positions = list(positions)
        return JsonResponse(positions, safe=False)

def get_dirs(request):
    if request.user.is_authenticated:
        dirs = DirDepartament.objects.values('id', 'name').order_by('name')
        dirs = list(dirs)
        return JsonResponse(dirs, safe=False)

def get_deps(request):
    if request.user.is_authenticated:
        deps = Departament.objects.values('iter','name', 'id', 'dirdepartament__name','dirdepartament__id').order_by('iter','name', 'dirdepartament__name')
        deps = list(deps)
        return JsonResponse(deps, safe=False)

def get_cats(request, cat):
    if request.user.is_authenticated:
        positions = RegularReplacementPos.objects.filter(bound_regrepl=rr).filter(cat_id=cat).values('id','name', 'dir__name', 'dep','dep__name', 'subdep__name', 'units',
        'level',
        'cat_id',
        'cat__name',
        'payment',
        'salary',
        'units_rr',
        'level_rr',
        'cat_rr_id',
        'cat_rr__name',
        'payment_rr',
        'salary_rr',
        'employer1',
        'employer2',
        'employer3',
        'free',
        'comm',
        'disabled' ).order_by('dep_id', 'id', 'cat_id',  'subdep_id')
        positions = list(positions)
        return JsonResponse(positions, safe=False)

def deps(request):
    if request.user.is_authenticated:
        return render(request, 'RegRepl/deps.html', context={})

def new_dep(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            dep_form = Departament_form()
            return render(request, 'RegRepl/new_dep.html', context={'form':dep_form})
        else:
            dir = request.POST.get('nd_dir', '')
            dep_form = Departament_form(request.POST)
            if dep_form.is_valid():
                dep_form.save()
                dep_form.addtodir(dir)
                loc = '/deps/'
                return redirect(loc)

def subdeps(request):
    if request.user.is_authenticated:
        return render(request, 'RegRepl/subdeps.html', context={})

def get_subdeps(request):
    if request.user.is_authenticated:
        subdeps = SubDepartament.objects.values('name', 'id', 'departament__name','departament__id').order_by('name','departament__name')
        subdeps = list(subdeps)
        return JsonResponse(subdeps, safe=False)

def new_subdep(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            subdep_form = SubDepartament_form()
            return render(request, 'RegRepl/new_subdep.html', context={'form':subdep_form})
        else:
            dep = request.POST.get('nsd_dep', '')
            subdep_form = SubDepartament_form(request.POST)
            if subdep_form.is_valid():
                subdep_form.save()
                subdep_form.addtodep(dep)
                loc = '/subdeps/'
                return redirect(loc)

def make_excel(request, rr):
    if request.user.is_authenticated:
        regrepl = RegularReplacement.objects.get(id=rr)
        regreplpos = RegularReplacementPos.objects.filter(bound_regrepl=regrepl.id)
        dirs = DirDepartament.objects.all().filter(location_id=1)

        wb = xlwt.Workbook()
        sheet = wb.add_sheet(str(regrepl.duration))

        style = xlwt.easyxf('borders: top thin, bottom thin, left thin, right thin')
        style_free = xlwt.easyxf('pattern: pattern solid, fore_colour yellow; borders: top thin, bottom thin, left thin, right thin')
        style_prof = xlwt.easyxf('font: colour pink; align: horiz center; borders: top thin, bottom thin, left thin, right thin ')
        style_head = xlwt.easyxf(' font: colour red; align: horiz center; borders: top thin, bottom thin, left thin, right thin ')
        style_work = xlwt.easyxf(' font: colour blue; align: horiz center; borders: top thin, bottom thin, left thin, right thin ')
        style_dir = xlwt.easyxf('pattern: pattern solid, fore_colour 27; align: horiz center; borders: top thin, bottom thin, left thin, right thin ')
        style_dep = xlwt.easyxf('pattern: pattern solid, fore_colour 44; align: horiz center')
        style_sdep = xlwt.easyxf('pattern: pattern solid, fore_colour 29; align: horiz center; font: italic 1')
        style_itog = xlwt.easyxf('pattern: pattern solid, fore_colour 22; align: horiz center; borders: top thin, bottom thin, left thin, right thin; font: bold 1  ')
        style_itog_dir = xlwt.easyxf('pattern: pattern solid, fore_colour 31; align: horiz center; borders: top thin, bottom thin, left thin, right thin; font: bold 1, height 250  ')
        style_itog_all = xlwt.easyxf('pattern: pattern solid, fore_colour 2; align: horiz center; borders: top thin, bottom thin, left thin, right thin; font: bold 1, height 500   ')

        i = 2
        all_itog = 0
        all_salary = 0
        allitog_rr = 0
        allitog_salary = 0
        allitog_rr = 0
        allitog_salary_rr = 0
        allitog_temp = 0

        sheet.write_merge(0,0,0,6, 'По штатному расписанию', style_dir)
        sheet.write_merge(0,0,7,15, 'По штатному замещению', style_dir)

        sheet.write(1,0, 'Должность')
        sheet.write(1,1, 'Ед.')
        sheet.write(1,2, 'Разр.')
        sheet.write(1,3, 'Кат.')
        sheet.write(1,4, 'Ступ.')
        sheet.write(1,5, 'БТС')
        sheet.write(1,6, 'МФЗП')

        sheet.write(1,7, 'Ед.')
        sheet.write(1,8, 'Разр.')
        sheet.write(1,9, 'Кат.')
        sheet.write(1,10, 'Ступ.')
        sheet.write(1,11, 'БТС')
        sheet.write(1,12, 'МФЗП')
        sheet.write(1,13, 'ФИО')
        sheet.write(1,14, 'ФИО Вр.')
        sheet.write(1,15, 'ФИО Вр.')

        for dir in dirs:
            diritog = 0
            diritog_salary = 0
            diritog_rr = 0
            diritog_salary = 0
            diritog_rr = 0
            diritog_salary_rr = 0
            diritog_temp = 0
            sheet.write_merge(i,i,0,15, dir.name, style_dir)
            i = i+1
            for dep in dir.dep.all():
                depitog = 0
                depitog_rr = 0
                depitog_salary = 0
                depitog_rr = 0
                depitog_salary_rr = 0
                depitog_temp = 0
                sheet.write_merge(i,i,0,15, dep.name, style_dep)
                i = i+1
                pos  = RegularReplacementPos.objects.filter(bound_regrepl=regrepl.id).filter(dep_id=dep.id).filter(subdep=None).order_by('cat_id', '-payment')
                for p in pos:

                    depitog = depitog + p.units
                    depitog_rr = depitog_rr + p.units_rr

                    if p.salary == 'контракт':
                        depitog_salary = int(depitog_salary) + 0
                        depitog_salary_rr =  int(depitog_salary_rr) + 0
                    else:
                        depitog_salary = depitog_salary + int(p.salary)
                        depitog_salary_rr = depitog_salary_rr + int(p.salary_rr)

                    if p.employer2:
                        depitog_temp = depitog_temp + 1
                    else:
                        pass

                    if p.free:
                        sheet.write(i,0, p.name, style_free)
                        sheet.write(i,1, p.units, style_free)
                        sheet.write(i,2, p.level, style_free)
                        sheet.write(i,3, p.cat.name, style_free)
                        sheet.write(i,4, p.payment, style_free)
                        sheet.write(i,5, p.salary, style_free)
                        sheet.write(i,6, p.salary, style_free)

                        sheet.write(i,7, p.units_rr, style_free)
                        sheet.write(i,8, p.level_rr, style_free)
                        sheet.write(i,9, p.cat_rr.name, style_free)
                        sheet.write(i,10, p.payment_rr, style_free)
                        sheet.write(i,11, p.salary_rr, style_free)
                        sheet.write(i,12, p.salary_rr, style_free)
                        sheet.write(i,13, p.employer1, style_free)
                        sheet.write(i,14, p.employer2, style_free)
                        sheet.write(i,15, p.employer3, style_free)

                    else:
                        sheet.write(i,0, p.name, style)
                        sheet.write(i,1, p.units, style)
                        sheet.write(i,2, p.level, style)
                        if p.cat_id == 1:
                            sheet.write(i,3, p.cat.name, style_head)
                        if p.cat_id == 2:
                            sheet.write(i,3, p.cat.name, style_prof)
                        if p.cat_id == 3:
                            sheet.write(i,3, p.cat.name, style_work)

                        sheet.write(i,4, p.payment, style)
                        sheet.write(i,5, p.salary, style)
                        sheet.write(i,6, p.salary, style)

                        sheet.write(i,7, p.units_rr, style)
                        sheet.write(i,8, p.level_rr, style)
                        if p.cat_rr_id == 1:
                            sheet.write(i,9, p.cat_rr.name, style_head)
                        if p.cat_rr_id == 2:
                            sheet.write(i,9, p.cat_rr.name, style_prof)
                        if p.cat_rr_id == 3:
                            sheet.write(i,9,p.cat_rr.name, style_work)
                        sheet.write(i,10, p.payment_rr, style)
                        sheet.write(i,11, p.salary_rr, style)
                        sheet.write(i,12, p.salary_rr, style)
                        sheet.write(i,13, p.employer1, style)
                        sheet.write(i,14, p.employer2, style)
                        sheet.write(i,15, p.employer3, style)
                    i = i+1
                for s in dep.subdep.all():
                    sheet.write_merge(i,i,0,15, s.name, style_sdep)
                    i = i+1
                    pos  = RegularReplacementPos.objects.filter(bound_regrepl=regrepl.id).filter(dep_id=dep.id).filter(subdep=s.id)
                    for p in pos:
                        depitog = depitog + p.units
                        depitog_rr = depitog_rr + p.units_rr

                        if p.salary == 'контракт':
                            depitog_salary = int(depitog_salary) + 0
                            depitog_salary_rr =  int(depitog_salary_rr) + 0
                        else:
                            depitog_salary = depitog_salary + int(p.salary)
                            depitog_salary_rr = depitog_salary_rr + int(p.salary_rr)

                        if p.employer2:
                            depitog_temp = depitog_temp + 1
                        else:
                            pass

                        if p.free:
                            sheet.write(i,0, p.name, style_free)
                            sheet.write(i,1, p.units, style_free)
                            sheet.write(i,2, p.level, style_free)
                            sheet.write(i,3, p.cat_id, style_free)
                            sheet.write(i,4, p.payment, style_free)
                            sheet.write(i,5, p.salary, style_free)
                            sheet.write(i,6, p.salary, style_free)

                            sheet.write(i,7, p.units_rr, style_free)
                            sheet.write(i,8, p.level_rr, style_free)
                            sheet.write(i,9, p.cat_rr_id, style_free)
                            sheet.write(i,10, p.payment_rr, style_free)
                            sheet.write(i,11, p.salary_rr, style_free)
                            sheet.write(i,12, p.salary_rr, style_free)
                            sheet.write(i,13, p.employer1, style_free)
                            sheet.write(i,14, p.employer2, style_free)
                            sheet.write(i,15, p.employer3, style_free)

                        else:
                            sheet.write(i,0, p.name, style)
                            sheet.write(i,1, p.units, style)
                            sheet.write(i,2, p.level, style)
                            if p.cat_id == 1:
                                sheet.write(i,3, p.cat.name, style_head)
                            if p.cat_id == 2:
                                sheet.write(i,3, p.cat.name, style_prof)
                            if p.cat_id == 3:
                                sheet.write(i,3, p.cat.name, style_work)
                            sheet.write(i,4, p.payment, style)
                            sheet.write(i,5, p.salary, style)
                            sheet.write(i,6, p.salary, style)

                            sheet.write(i,7, p.units_rr, style)
                            sheet.write(i,8, p.level_rr, style)
                            if p.cat_rr_id == 1:
                                sheet.write(i,9, p.cat_rr.name, style_head)
                            if p.cat_rr_id == 2:
                                sheet.write(i,9, p.cat_rr.name, style_prof)
                            if p.cat_rr_id == 3:
                                sheet.write(i,9,p.cat_rr.name, style_work)
                            sheet.write(i,10, p.payment_rr, style)
                            sheet.write(i,11, p.salary_rr, style)
                            sheet.write(i,12, p.salary_rr, style)
                            sheet.write(i,13, p.employer1, style)
                            sheet.write(i,14, p.employer2, style)
                            sheet.write(i,15, p.employer3, style)
                        i=i+1

                # Стиль итогов
                sheet.write(i,0, 'Итого по: ' + str(dep.name), style_itog)
                sheet.write(i,1, depitog, style_itog)
                sheet.write(i,2, '', style_itog)
                sheet.write(i,3, '', style_itog)
                sheet.write(i,4, '', style_itog)
                sheet.write(i,5, '', style_itog)
                sheet.write(i,6, depitog_salary, style_itog)
                sheet.write(i,7, depitog_rr, style_itog)
                sheet.write(i,8, '', style_itog)
                sheet.write(i,9, '', style_itog)
                sheet.write(i,10, '', style_itog)
                sheet.write(i,11, '', style_itog)
                sheet.write(i,12, depitog_salary_rr, style_itog)
                sheet.write(i,13, '', style_itog)
                sheet.write(i,14, 'Временных: ' + str(depitog_temp), style_itog)
                sheet.write(i,15, '', style_itog)
                # --------------------------------------------------------

                diritog = diritog + depitog
                diritog_salary = diritog_salary + depitog_salary
                diritog_rr = diritog_rr + depitog_rr
                diritog_salary_rr = diritog_salary_rr + depitog_salary_rr
                diritog_temp = diritog_temp + depitog_temp

                i=i+1
            # Стиль итогов
            sheet.write(i,0, 'Итого по: ' + str(dir.name), style_itog_dir)
            sheet.write(i,1, diritog, style_itog_dir)
            sheet.write(i,2, '', style_itog_dir)
            sheet.write(i,3, '', style_itog_dir)
            sheet.write(i,4, '', style_itog_dir)
            sheet.write(i,5, '', style_itog_dir)
            sheet.write(i,6, diritog_salary, style_itog_dir)
            sheet.write(i,7, diritog_rr, style_itog_dir)
            sheet.write(i,8, '', style_itog_dir)
            sheet.write(i,9, '', style_itog_dir)
            sheet.write(i,10, '', style_itog_dir)
            sheet.write(i,11, '', style_itog_dir)
            sheet.write(i,12, diritog_salary_rr, style_itog_dir)
            sheet.write(i,13, '', style_itog_dir)
            sheet.write(i,14, 'Временных: ' + str(diritog_temp), style_itog_dir)
            sheet.write(i,15, '', style_itog_dir)
            # --------------------------------------------------------
            all_itog = all_itog + diritog
            all_salary = all_salary + diritog_salary
            allitog_rr = allitog_rr + diritog_rr
            allitog_salary_rr = allitog_salary_rr + diritog_salary_rr
            allitog_temp = allitog_temp + diritog_temp
            i=i+1
        # Стиль итогов
        sheet.write(i,0, 'Итого по предприятию: ', style_itog_all)
        sheet.write(i,1, all_itog, style_itog_all)
        sheet.write(i,2, '', style_itog_all)
        sheet.write(i,3, '', style_itog_all)
        sheet.write(i,4, '', style_itog_all)
        sheet.write(i,5, '', style_itog_all)
        sheet.write(i,6, all_salary, style_itog_all)
        sheet.write(i,7, allitog_rr, style_itog_all)
        sheet.write(i,8, '', style_itog_all)
        sheet.write(i,9, '', style_itog_all)
        sheet.write(i,10, '', style_itog_all)
        sheet.write(i,11, '', style_itog_all)
        sheet.write(i,12, allitog_salary_rr, style_itog_all)
        sheet.write(i,13, '', style_itog_all)
        sheet.write(i,14, allitog_temp, style_itog_all)
        sheet.write(i,15, '', style_itog_all)
        # --------------------------------------------------------




        name = str(regrepl.duration) + '.xls'

        wb.save(name)

        fp = open(name, "rb")
        response = HttpResponse(fp.read())
        fp.close();

        file_type = 'application/octet-stream'
        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(name).st_size)
        print(name)
        response['Content-Disposition'] = "attachment; filename=%s" %name

        return response;
