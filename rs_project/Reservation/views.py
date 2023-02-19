from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from datetime import *
from django.shortcuts import render
from .models import * 

#---------------LOGIN----------------
def login(request):
    if request.method == "POST":
        user = request.POST['username']
        passs = request.POST['password']
        user = authenticate(username=user, password=passs)
        if user is not None:
            if user.is_superuser:
                
                return redirect("/home")
        else:   
            msg = "Les données sont  erronés,ressayer"
            return render(request, "Reservation/Login.html", {"msg":msg})
    
    return render (request, 'Reservation/Login.html')






#--------------------------------------------------------------------Home---------------------------------------------------------------------------


def home(request):
    client = Client.objects.all()
    table = Table.objects.all()
    salle = Salle.objects.all()
    resrevation_table = Reservation_table.objects.all()
    resrevation_salle = Reservation_salle.objects.all()
    nb_client = Client.objects.all().count()
    nb_table = Table.objects.all().count()
    nb_salle = Salle.objects.all().count()
    nb_reservation_table = Reservation_table.objects.all().count()
    nb_reservation_salle = Reservation_salle.objects.all().count()
    nb_table_non_reserver = nb_table - nb_reservation_table
    nb_salle_non_reserver = nb_salle - nb_reservation_salle
    totale_reservations = nb_reservation_table + nb_reservation_salle
    context = {'client' : client,
               'table': table,
               'salle': salle,
               'resrevation_table' : resrevation_table,
               'resrevation_salle' : resrevation_salle,
               'nb_client' : nb_client,
               'nb_table' : nb_table,
               'nb_salle' : nb_salle,
               'nb_reservation_table' : nb_reservation_table,
               'nb_reservation_salle' : nb_reservation_salle,
               'totale_reservations':totale_reservations,
               'nb_table_non_reserver':nb_table_non_reserver,
               'nb_salle_non_reserver' : nb_salle_non_reserver}
    return render (request,'Reservation/Tabledebord.html ',context)


#----------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------fonction Reservations--------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------Reservation--------------------------------------------------

  
def reservation(request):
    salle = Reservation_salle.objects.all()
    table = Reservation_table.objects.all()
    context = {'salle' : salle,
               'table' : table}
    return render( request, 'Reservation/Reservation.html',context)

      
#--------------------------------------------------------------Reservation-salle--------------------------------------------------

       
def reservation_salle(request):
    reserv_salle = Reservation_salle.objects.all()
    return render (request, 'Reservation/Reservation_salle.html',{'reserv_salle' : reserv_salle})


#--------------------------------------------------------------Reservation-table--------------------------------------------------
   
def reservation_table(request):
    reserv_table = Reservation_table.objects.all()
    return render(request, 'Reservation/Reservation_Table.html',{'reserv_table' : reserv_table})
      
      
#--------------------------------------------------------------Reservation-salle-table--------------------------------------------------

       
def reservation_salle_table(request):       
    salle = Reservation_salle.objects.all()
    table = Reservation_table.objects.all()
    context = {'salle' : salle,
               'table' : table}
    return render( request, 'Reservation/Reservation_salle_table.html',context)




#---------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------salle----------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------

def salle(request):
    salle = Salle.objects.all()
    res_salle = Reservation_salle.objects.all()
    for s in res_salle:
        n = s.salle.id
        print(n)
               
    reservation = {'salle':salle,
                  'res_salle' : res_salle,
                  'n' : n,
                  's' : s,
                  'Reserver' : "Reserver",
                  'Non_Reserver' : "Non Reserver"}
    return render(request, 'Reservation/Salle.html',reservation) 
 
     
#------------------------------------------------------------------table----------------------------------------------------------------

def table(request):
    K=1
    l=4
    table = Table.objects.all()
    res_table = Reservation_table.objects.all()
    for k in  res_table:
        l = k.table.id
        print(l)
   
        context = {'table':table,
               'res_table' : res_table,
               'k' : k,
               'l' :  l,
               'Reserver' : "Reserver",
               'Non_Reserver' : "Non Reserver"}
    return render(request, 'Reservation/Table.html',context) 




#--------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------client----------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

def client(request):
    client = Client.objects.all()
    return render(request, 'Reservation/Client.html',{'client':client})





#----------------------------------------------------------------------------------------------------------------------------------------------------
#-----°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°---------------------------- FONCTION DE L'AJOUT--------°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------ajout un client----------------------------------------

def ajout_client(request):
    if request.method=="POST":   
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        tel = request.POST['tel']
        c = Client.objects.create(nom=nom, prenom = prenom, email=email, tel=tel )
        c.save()
        return redirect("/client")
    
    return render(request, 'Reservation/Ajout_client.html')

#----------------------------------------------------------------ajout une salle--------------------------------------


def ajout_salle(request):
    if request.method=="POST":   
        numero = request.POST['numero']
        type = request.POST['type']
        c = Salle.objects.create(numero=numero, type = type )
        c.save()
        return redirect("/salle")
    
    return render(request, 'Reservation/ajout_salle.html')


#-----------------------------------------------------------------ajout une table -------------------------------------------


def ajout_table(request):
    if request.method=="POST":   
        numero = request.POST['numero']
        type = request.POST['type']
        iddd = request.POST['idd']
        salle = Salle.objects.get(id=iddd)
        c = Table.objects.create(numero=numero, type=type, salle=salle )
        c.save()
        return redirect("/table")
    salles = Salle.objects.all()
    return render(request, 'Reservation/ajout_table.html',{'salles' : salles})


#-------------------------------------------------ajout reservation salle---------------------------------------------------------


def ajout_reservation_salle(request):
    if request.method=="POST":   
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        tel = request.POST['tel']
        email = request.POST['email']
        iddd = request.POST['idd']
        date_reservation = request.POST['date_reservation']
        salle = Salle.objects.get(id=iddd)
        client = Client.objects.create(nom=nom, prenom=prenom, tel=tel, email=email)
        r = Reservation_salle.objects.create(client = client, salle=salle, date_reservation = date_reservation)
        client.save()
        r.save()
        idd = r.id 
        nom = Reservation_salle.objects.all()
        return render (request, 'Reservation/impression_salle_admin.html', {'idd': idd}) 
    salles = Salle.objects.all()
    return render(request, 'Reservation/Ajout_reservation_salle.html',{'salles':salles})


#--------------------------------------------------ajout reservation table------------------------------------


def ajout_reservation_table(request):
    if request.method=="POST":   
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        tel = request.POST['tel']
        email = request.POST['email']
        iddd = request.POST['idd']
        date_reservation = request.POST['date_reservation']
            
        table = Table.objects.get(id=iddd)
        
        client = Client.objects.create(nom=nom, prenom=prenom, tel=tel, email=email)
        r = Reservation_table.objects.create(client = client, table=table, date_reservation = date_reservation )
        client.save()
        r.save() 
        idd = r.id
        return render(request, 'Reservation/impression_table_admin.html',{'idd': idd}) 
           
    tables = Table.objects.all()
    return render(request,'Reservation/Ajout_reservation_table.html',{'tables' : tables} )


#---------------------------------------------------------------------------------------------------------------
#-----°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°--------- FONCTION DE MODIFICATION--------°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°-----------------
#------------------------------------------------------------------------------------------------------------------

#----------------------------------------------Modifier Client ---------------------------------------------

def modifier_client(request, myid):
    cl = Client.objects.get(id=myid)
    if request.method=="POST":   
        cl.nom = request.POST['nom']
        cl.prenom = request.POST['prenom']
        cl.email = request.POST['email']
        cl.tel = request.POST['tel']
        cl.save()
        return redirect("/client")  
    return render(request, 'Reservation/Modifier_client.html', {'cl': cl}) 

#---------------------------------------------Modifier salle-------------------------------------------------------

def modifier_salle(request, myid):
    v = Salle.objects.get(id=myid)
    if request.method=="POST":   
        v.numero = request.POST['numero']
        v.type = request.POST['type']
        v.save()
        return redirect("/salle")  
    return render(request, 'Reservation/Modifier_salle.html', {'v': v})


#-----------------------------------------------modifier table------------------------------------------------------------------

def modifier_table(request, myid):
    t = Table.objects.get(id=myid)
    if request.method=="POST":   
       t.numero = request.POST['numero']
       t.type = request.POST['type']
       idddd = request.POST['idd']
       salle = Salle.objects.get(id=idddd)
       print(t.numero)
       t.salle = salle
       t.save()
       print(t.numero)
       return redirect("/table")
    s = Salle.objects.all() 
    return render(request, 'Reservation/Modifier_table.html',{'s' : s, 't' : t})


#-----------------------------------------------modifier reservation-salle-----------------------------#--


def modifier_reservation_salle(request, myid):
    S = Reservation_salle.objects.get(id=myid) 
   
    if request.method == "POST":
       S.client.nom = request.POST['nom']
       S.client.prenom = request.POST['prenom']
       S.client.tel = request.POST['tel']
       S.client.email = request.POST['email']
       S.date_reservation = request.POST['date_reservation']
       idddd = request.POST['idd']
       S.sal = Salle.objects.get(id=idddd)
       print(S.salle.numero)
       S.salle = S.sal
       S.save()
       
       return redirect("/reservation_salle")
    salle = Salle.objects.all() 
    return render(request, 'Reservation/Modifier_reservation_salle.html',{'salle' : salle,'S': S})




#---------------------------------------------------------------------------------------------------------------
#-----------------------------------------------FONCTION SUPPRESSION-------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------supprimer un client ---------------------------------------


def supprimer_client(request, myid):
    client = Client.objects.filter(id=myid)
    client.delete()
    return redirect("/client") 



#-----------------------------------------------supprimer une salle ---------------------------------------


def supprimer_salle(request, myid):
    salle = Salle.objects.filter(id=myid)
    salle.delete()
    return redirect("/salle")  


#-----------------------------------------------supprimer une table ---------------------------------------


def supprimer_table(request, myid):
    table = Table.objects.filter(id=myid)
    table.delete()
    return redirect("/table")  
 
  
#-----------------------------------------------supprimer reservation salle ---------------------------------------
  
def supprimer_reservation_salle(request, myid):
    res = Reservation_salle.objects.filter(id=myid)
    res.delete()
    return redirect("/reservation_salle")
 
 
 
#-----------------------------------------------supprimer reservation table ---------------------------------------
 
  
def supprimer_reservation_table(request, myid):
    res = Reservation_table.objects.filter(id=myid)
    res.delete()
    return redirect("/reservation_table")  

#-----------------------------------------------supprimer reservation salle table---------------------------------------
 

def supprimer_reservation_salle_table(request, myid,mid):
    res_s = Reservation_salle.objects.filter(id=myid)
    res_t = Reservation_table.objects.filter(id=mid)
    res_s.delete()
    res_t.delete()
    return redirect("/reservation_salle_table")  




#-----------------------------------------------------Home ----------------------------------------------------


def client_home(request):
    return render(request, 'Reservation/TabledebordClient.html')


#----------------------------------------------------Vos-Rservation----------------------------------------------------


def vos_reservation(request):
    return render(request, 'Reservation/Vos_reservation.html')



#----------------------------------------------------Contactez-Nous-------------------------------------------------------


def contactez_nous(request):
    return render(request, 'Reservation/Contactez_nous.html')






#---------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------FONCTION DE L AJOUT------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------ajout reservation table client ----------------------------------


def ajout_reservation_table_client(request):
    if request.method=="POST":   
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        tel = request.POST['tel']
        email = request.POST['email']
        iddd = request.POST['idd']
        date_reservation = request.POST['date_reservation']
        try:
            
           table = Table.objects.get(id=iddd)
        
           if date_reservation  != Reservation_table.date_reservation :
              client = Client.objects.create(nom=nom, prenom=prenom, tel=tel, email=email)
              r = Reservation_table.objects.create(client = client, table=table, date_reservation = date_reservation )
              client.save()
              r.save() 
              idd = r.id
              return render(request, 'Reservation/impression_table.html',{'idd': idd}) 
           else:
              return render(request, 'Reservation/Salle.html')  
        except:
            res = {'msg' : 1}
            return render(request, 'Reservation/Salle.html',{'res' : res})  
    tables = Table.objects.all()
    return render(request,'Reservation/Ajout_reservation_table_Client.html',{'tables' : tables} )


#-----------------------------------------------------------ajout reservation salle client -------------------------------------------


def ajout_reservation_salle_client(request):
    if request.method=="POST":   
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        tel = request.POST['tel']
        email = request.POST['email']
        iddd = request.POST['idd']
        date_reservation = request.POST['date_reservation']
        salle = Salle.objects.get(id=iddd)
        client = Client.objects.create(nom=nom, prenom=prenom, tel=tel, email=email)
        r = Reservation_salle.objects.create(client = client, salle=salle, date_reservation = date_reservation)
        client.save()
        r.save()
        idd = r.id;
        #return render (request, 'Reservation/impression_salle.html', {'idd': idd}) 
    salles = Salle.objects.all()
    return render(request, 'Reservation/Ajout_reservation_salle_Client.html',{'salles':salles})


#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------- FONCTION RESERVATION---------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------Reservation client----------------------------

def reservation_client(request):
    return render(request, 'Reservation/Ajout_Reservation.html')


#------------------------------------------------------------------------vos reservation salle pour "client"-----------------------------------

def vos_reservation_salle(request):
    
    return render(request, 'Reservation/Vos_reservation_salle.html')

#-------------------------------------------------------------------------vos reservation table pour "client"-----------------------------------

def vos_reservation_table(request):
    
    return render(request, 'Reservation/Vos_reservation_table.html')


#------------------------------------------------------------------------vos reservation salle table pour "client"-----------------------------------

def vos_reservation_salle_table(request):
    return render(request, 'Reservation/Vos_reservation_salle_table.html')









