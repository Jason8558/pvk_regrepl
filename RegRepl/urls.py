from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('regrepl/create/<int:id>', views.regrepl_create, name='regrepl'),
    path('regrepl/item/new/<int:id>', views.regpos_new, name='regpos_new'),
    path('regrepl/item/upd/<int:id>', views.regpos_update, name='regpos_upd'),
    path('regrepl/getdata/<int:type>/<int:id>/<int:rr>', views.regrepl_json, name='regpos_json'),
    path('regrepl/getdata/getpos/<int:rr>/<str:pos>', views.get_positions, name='search_get_pos'),
    path('regrepl/item/search/<int:rr>', views.regrepl_search, name='regpos_search'),
    path('new/', views.regrepl_copy, name='regrepl_copy'),
    path('getdirs/', views.get_dirs, name='search_get_dirs'),
    path('getdeps/', views.get_deps, name='search_get_deps'),
    path('deps/', views.deps, name='get_deps'),
    path('deps/new', views.new_dep, name='new_dep'),



]
