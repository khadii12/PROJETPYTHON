from . import views

from django.urls import path

#-------------------------------------------------------------Login----------------------------------------------------------------------------
    
 

urlpatterns = [

    path('', views.login, name="login"),

#-------------------------------------------------------------urls Navbar----------------------------------------------------------
    
    path('home/',views.home,name="home"),
    
    path('reservation/',views.reservation, name="reservation"),
    path('reservation_salle/',views.reservation_salle, name="reservation_salle"),
    path('reservation_table/',views.reservation_table, name="reservation_table"),
    path('reservation_salle_table/',views.reservation_salle_table, name="reservation_salle_table"),
   
    path('salle/',views.salle,name="salle"),
    path('table/',views.table, name="table"),
    path('client/',views.client, name="client"),
   
   
   
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------urls L'ajout----------------------------------------------------------

    
    path('ajout_reservation_salle/', views.ajout_reservation_salle, name="ajout_reservation_salle"),
    
    path('ajout_reservation_table/', views.ajout_reservation_table, name="ajout_reservation_table"),
    
    path('ajout_salle/',views.ajout_salle, name="ajout_salle"),
    
    path('ajout_table/',views.ajout_table, name="ajout_table"),
    
    path('ajout_client/', views.ajout_client, name="ajout_client"), 
    
    
   #-------------------------------------------------------------urls modification----------------------------------------------------------

  
    
    path('modifier_reservation_salle/<int:myid>/',views.modifier_reservation_salle, name="modifier_reservation_salle"),
    
    # reste ici fonction modifier_reservation_table !!
    
    path('modifier_salle/<int:myid>/', views.modifier_salle, name="modifier_salle"),
    
    path('modifier_table/<int:myid>/', views.modifier_table, name="modifier_table"),
    
    path('modifier_client/<int:myid>/', views.modifier_client, name="modifier_client"),
    
    
#---------------------------------------------------------suppression------------------------------------------------------------------
    
   
    path('supprimer_reservation_salle/<int:myid>/', views.supprimer_reservation_salle, name="supprimer_reservation_salle"),
    
    path('supprimer_reservation_table/<int:myid>/', views.supprimer_reservation_table, name="supprimer_reservation_table"),
    
    path('supprimer_reservation_salle_table/<int:myid>/<int:mid>/', views.supprimer_reservation_salle_table, name="supprimer_reservation_salle_table"),
    
    path('supprimer_salle/<int:myid>/', views.supprimer_salle, name="supprimer_salle"),
    
    path('supprimer_table/<int:myid>/', views.supprimer_table, name="supprimer_table"),
    
    path('supprimer_client/<int:myid>/', views.supprimer_client, name="supprimer_client"),
    


##--------------------------------------------------------------Urls Navbar client-----------------------------------------------------------------

##-------------------------------------------------------------- Home -----------------------------------------------------------------
    
    path('client_home/',views.client_home, name="client_home"),
    path('reservation_client/',views.reservation_client, name="reservation_client"),
    
##------------------------------------------------------------Vos-Reservation-----------------------------------------------------------------
 ##------------------------------------------------------------Vos-Reservation-----------------------------------------------------------------
   
    path('vos_reservation/', views.vos_reservation, name="vos_reservation"),
    path('vos_reservation_salle/',views.vos_reservation_salle, name="vos_reservation_salle"),
    path('vos_reservation_table/',views.vos_reservation_table, name="vos_reservation_table"),
    path('vos_reservation_salle_table/',views.vos_reservation_salle_table, name="vos_reservation_salle_table"),
    
      
    
    
##------------------------------------------------------------Contactez-Nous-----------------------------------------------------------------
    
    path('contactez_nous/',views.contactez_nous, name="contactez_nous"),
    
##-----------------------------------------------------------------------------------------------------------------------------------------
##-----------------------------------------------------L urls ajout pour partie client----------------------------------------------------------------------
    
    path('ajout_reservation_salle_client/',views.ajout_reservation_salle_client, name="ajout_reservation_salle_client"),
    path('ajout_reservation_table_client/',views.ajout_reservation_table_client, name="ajout_reservation_table_client"),
  


]