from django.shortcuts import render

from .models import About,Education,Skills,Projects,Contact


def index(request):
    return render(request,"minthantkyaw/index.html")

def about(request):
    
    about_texts=About.objects.all()
    about_text=[]
    for text in about_texts:
       about_text.append(f"{text.p_text}")

    return render(request,"minthantkyaw/About.html",{"about_text":about_text})

def education(request):

    education=Education.objects.all()

    return render(request,"minthantkyaw/Education.html",{"education":education})

def skills(request):

    skills=Skills.objects.all()

    return render(request,"minthantkyaw/Skills.html",{"skills":skills})

def projects(request):

    projects=Projects.objects.all()

    return render(request,"minthantkyaw/Projects.html",{"projects":projects})

def contact(request):

    contacts=Contact.objects.all()

    return render(request,"minthantkyaw/Contact.html",{"contacts":contacts})