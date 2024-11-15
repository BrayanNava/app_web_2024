from django.shortcuts import render

# Create your views here.

def index(request):
    mensaje = 'soy un mensaje'
    return render(request,'mainapp/index.html', {
        'title':'Inicio',
        'content':'.:: !Bienvenido!::.',
        'mensaje': mensaje

    })

def about(request):
    return render(request,'mainapp/about.html', {
        'title':'Acerca de Nosotros',
        'content':'Somo un Equipo de Desarollo de SW'
    })

def mision(request):
    return render(request,'mainapp/mision.html', {
        'title':'mision',
        'content':'La mision de la empresa',
        'mensage_mision' : 'Ofrecer soluciones tecnológicas innovadoras y sostenibles que mejoren la calidad de vida de nuestros clientes, apoyándonos en un equipo talentoso y comprometido, mientras impulsamos el desarrollo de nuestras comunidades y contribuimos a un mundo más sostenible.'

    })

def vision(request):
    return render(request,'mainapp/vision.html', {
        'title':'vision',
        'content':'La vision de la empresa',
        'mensage_vicion' : 'Ser una empresa líder en innovación y calidad, reconocida a nivel mundial por nuestra capacidad para mejorar la vida de las personas a través de soluciones tecnológicas sostenibles, con un enfoque en la satisfacción del cliente, la responsabilidad social y el desarrollo de nuestros colaboradores.'
    })