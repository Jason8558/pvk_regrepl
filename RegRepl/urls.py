from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('regrepl/create/<int:id>', views.regrepl_create, name='regrepl'),
    path('regrepl/item/upd/<int:id>', views.regpos_update, name='regpos_upd'),

]
