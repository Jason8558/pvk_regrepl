from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('regrepl/create/<int:id>', views.regrepl_create, name='regrepl'),
    path('regrepl/item/new/<int:id>', views.regpos_new, name='regpos_new'),
    path('regrepl/item/upd/<int:id>', views.regpos_update, name='regpos_upd'),
    path('regrepl/item/search/<int:rr>', views.regrepl_json, name='regpos_search'),
    path('regrepl/item/dirsearch/<int:dir>/<int:rr>', views.regrepl_search_dir, name='regpos_dir_search'),
    path('new/', views.regrepl_copy, name='regrepl_copy'),

]
