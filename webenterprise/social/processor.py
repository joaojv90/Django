from .models import Social

def ctx_dict(request):
    ctx = {}
    socialList = Social.objects.all()
    #agregar datos al diccionario
    for social in socialList:
        ctx[social.key]=social.url
    return ctx