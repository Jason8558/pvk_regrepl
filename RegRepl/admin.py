from django.contrib import admin
from .models import *
admin.site.register(RegularReplacement)

admin.site.register(DirDepartament)
admin.site.register(Departament)
admin.site.register(Employer)
admin.site.register(SubDepartament)

admin.site.register(RegularReplacementPos)
