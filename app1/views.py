from django.shortcuts import render,redirect
from app1.models import Etudiant,Cours
# Create your views here.
def accueil(request):

    return render(request, 'pages/index.html')
#module gestion etudiant
def alls(request):
    data=Etudiant.objects.all().order_by('-id')
    return render(request, 'pages/etudiant/all.html',{'data':data})

def addetu(request):
    if request.method == 'POST':
        data=request.POST
        isinstance=Etudiant.objects.create( nom = data.get('nom'),
            prenom=data.get('prenom'),
            niveau=data.get('niveau'),
            option=data.get('option'),
            adresse=data.get('adresse'),
            tel=data.get('tel'),
            matricule=data.get('matricule'),
            #courssuivi=data.get('cours'),
            date_naiss=data.get('datenaiss'),
           # image = request.FILES.get('image') 
                                           )

    return render(request, 'pages/etudiant/add.html')

def update(request,pk):
    data=Etudiant.objects.get(secrete_key=pk)
    if request.method == 'POST':
        values= request.POST
        data.nom=values.get('nom')
        data.prenom=values.get('prenom')
        data.niveau=values.get('niveau')
        data.option=values.get('option')
        data.adresse=values.get('adresse')
        data.tel=values.get('tel')
        data.matricule=values.get('matricule')
        #data.courssuivi=values.get('cours')
        data.date_naiss=values.get('datenaiss')
        #data.image = request.FILES.get('image') 
        data.save()
        return redirect('urlallstudent')
    return render(request, 'pages/etudiant/update.html',{'data':data})

def supprim(request,pk):
    data=Etudiant.objects.get(secrete_key=pk)
    data.delete()  
    return redirect('urlallstudent')      

def edite(request,pk):
    data=Etudiant.objects.get(secrete_key=pk)
    return render(request, 'pages/etudiant/edite.html',{'data':data})

#Module gestion cours
def allcours(request):
    data=Cours.objects.all().order_by('-id')
    return render(request, 'pages/cours/all.html',{'data':data})

def addcours(request):
    if request.method == 'POST':
        data=request.POST
        isinstance=Cours.objects.create(
            code=data.get('code'),
            nom=data.get('nom'),
            description=data.get('description'),
            prof=data.get('prof'),
            nbcredit=data.get('nbcredit'),
            #image = request.FILES.get('image') 
        )
    return render(request, 'pages/cours/add.html')

def updatecours(request, pk):

    data=Cours.objects.get(secrete_key=pk)
    if request.method == 'POST':
        values=request.POST
        data.code=values.get('code')
        data.nom=values.get('nom')
        data.description=values.get('description')
        data.prof=values.get('prof')
        data.nbcredit=values.get('nbcredit')
        #data.image = request.FILES.get('image') 
        data.save()
        return redirect('urlallcours')
    return render(request, 'pages/cours/update.html',{'data':data})

def suppri(request, pk):
    data=Cours.objects.get(secrete_key=pk)
    data.delete()
    return redirect('urlallcours')

def editecou(request,pk):
    data=Cours.objects.get(secrete_key=pk)
    return render(request, 'pages/cours/edite.html',{'data':data})