from django.db import models

class Location(models.Model):
    name = models.CharField(verbose_name='Наименование ', max_length=256,)
    class Meta:
        ordering = ["id"]
        verbose_name = 'Территория'

    def __str__(self):
        fullname = self.name
        return fullname

class RegularReplacement(models.Model):



    duration = models.DateField(help_text="Введите дату" , verbose_name='Дата', db_index=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, verbose_name='Территория ', max_length=256,default='1')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Штатное замещение'


    def __str__(self):
        fullname = "Штатное замещение за " + self.duration.strftime('%d.%m.%Y')
        return fullname



class DirDepartament(models.Model):
    name = models.CharField(max_length=256,  help_text="Введите название дирекции", verbose_name="Название дирекции ", db_index=True)
    dep = models.ManyToManyField('Departament', blank=True,verbose_name = 'Подразделения ')
    location = models.ForeignKey('Location', on_delete=models.CASCADE, verbose_name='Территория ', max_length=256,  default='1')
    class Meta:
        ordering = ["id"]
        verbose_name = 'Дирекция'

    def __str__(self):
        fullname = self.name
        return fullname


class Departament(models.Model):
    name = models.CharField(max_length=256,  help_text="Введите название подразделения", verbose_name="Название подразделения ", db_index=True)
    subdep = models.ManyToManyField('SubDepartament',blank=True, verbose_name = 'Cубподразделения ')
    location = models.ForeignKey('Location', on_delete=models.CASCADE, verbose_name='Территория ', max_length=256,default='1')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Подразделение'

    def __str__(self):
        fullname = self.name
        return fullname


class SubDepartament(models.Model):
    name = models.CharField(max_length=256,  help_text="Введите название субподразделения", verbose_name="Название субподразделения ", db_index=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, verbose_name='Территория ', max_length=256, default='1')


    class Meta:
        ordering = ["id"]
        verbose_name = 'Субподразделение'

    def __str__(self):
        fullname = self.name
        return fullname


class Employer(models.Model):
    name = models.CharField(max_length=256,  help_text="Введите ФИО сотрудника", verbose_name="Сотрудник ", db_index=True)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Сотрудник'

    def __str__(self):
        fullname = self.name
        return fullname

class RegularReplacementPos(models.Model):
    CATEGORY_CHOICES = [
    ('РУК', 'РУК'),
    ('СПЕЦ', 'СПЕЦ'),
    ('РАБ', 'РАБ'),

]
    bound_regrepl = models.ForeignKey('RegularReplacement', on_delete=models.CASCADE, verbose_name="Штатное замещение ", default='None')
    name = models.CharField(max_length=256,  help_text="Введите должность", verbose_name="Название должности ", db_index=True)
    dir = models.ForeignKey('DirDepartament', on_delete=models.CASCADE, verbose_name="Дирекция ",default="None")
    dep = models.ForeignKey('Departament', on_delete=models.CASCADE, verbose_name="Подразделение ",default="None")
    subdep = models.ForeignKey('SubDepartament', null=True, blank=True,on_delete=models.CASCADE, verbose_name="Субподразделение ", default="None")
    units = models.FloatField(max_length=256, verbose_name="Кол-во едениц по штатному расписанию ", db_index=True)
    level = models.CharField(verbose_name='Разряд по штатному расписанию',blank=True, max_length=256)
    cat = models.CharField(choices=CATEGORY_CHOICES, verbose_name='Категория по штатному расписанию ', max_length=256)
    payment = models.CharField(verbose_name='Ступень оплаты по штатному расписанию', max_length=3)
    salary = models.CharField(max_length=256, verbose_name="Оклад по штатному расписанию ", db_index=True)
    units_rr = models.FloatField(max_length=256, verbose_name="Кол-во едениц по штатному замещению ", db_index=True)
    level_rr = models.CharField(verbose_name='Разряд по штатному замещению',blank=True, max_length=256)
    cat_rr = models.CharField(choices=CATEGORY_CHOICES,verbose_name='Категория по штатному замещению ', max_length=256)
    payment_rr = models.CharField(verbose_name='Ступень оплаты по штатному замещению', max_length=3)
    salary_rr = models.CharField(max_length=256, verbose_name="Оклад по штатному замещению ", db_index=True)
    employer1 = models.CharField(max_length=256,  verbose_name="Сотрудник 1 ", blank=True, db_index=True, default="")
    employer2 = models.CharField(max_length=256,  verbose_name="Сотрудник 2 ", blank=True,db_index=True,default="")
    employer3 = models.CharField(max_length=256,  verbose_name="Сотрудник 3 ", blank=True,db_index=True,default="")
    free = models.BooleanField(verbose_name='Ставка свободна ', default=False)
    comm = models.CharField(max_length=256,  verbose_name="Комментарий ", blank=True, db_index=True,default="")
    class Meta:
        ordering = ["id"]
        verbose_name = 'Позиция штатного замещения'

    def __str__(self):


        fullname = self.name + self.employer1
        return fullname
