from django.urls import path
from app1 import views
urlpatterns = [
path('',views.accueil,name='urlaccueil'),
#module gestion etudiant
path('allstudent',views.alls,name='urlallstudent'),
path('addstudent',views.addetu,name='urladdstudent'),
path('updatestudent/<pk>/',views.update,name='urlupdatestudent'),
path('delete/<pk>/',views.supprim,name='urldeletestudent'),
path('edit/<pk>/',views.edite, name='urleditestudent'),
#module de gestion des cours
path('alcourse', views.allcours,name='urlallcours'),
path('addcourse', views.addcours,name='urladdcours'),
path('updatecourse/<pk>/',views.updatecours,name='urlupdatecourse'),
path('deletecourse/<pk>/',views.suppri,name='urldeletecourse'),
path('editecourse/<pk>/',views.editecou,name='urleditecourse'),

]