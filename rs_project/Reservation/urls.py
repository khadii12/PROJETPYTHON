from . import views

from django.urls import path

#-------------------------------------------------------------Login----------------------------------------------------------------------------
    
 

urlpatterns = [

    path('', views.login, name="login"),

]