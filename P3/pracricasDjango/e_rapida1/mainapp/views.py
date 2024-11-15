from django.shortcuts import render

# Create your views here.

def index(request):
    mensaje = 'Hola mundo'
    return render(request,'mainapp/index.html', {
        'title':'Inicio',
        'content':'.:: !Bienvenido!::.',
        'mensaje': mensaje

    })

def about(request):
    return render(request,'mainapp/about.html', {
        'title':'Acerca de Mi',
        'content':'soy estudiante de TI'
    })

def mision(request):
    return render(request,'mainapp/mision.html', {
        'title':'mision',
        'content':'Mi mision',
        'mensage_mision' : 'acavar el examen'

    })

def vision(request):
    return render(request,'mainapp/vision.html', {
        'title':'vision',
        'content':'Mi vision',
        'mensage_vicion' : 'Sacar 100 en la materia'
    })