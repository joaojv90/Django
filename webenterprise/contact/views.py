from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contactForm = ContactForm()
    if request.method == 'POST':
        contactForm = ContactForm(data = request.POST)
        # capturar la información que se recibe desde el Get
        name = request.POST.get('name','')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')

        email = EmailMessage(
            "La Caffettiera : Nuevo mensaje de contacto",
            "De {} <{}>\n\nEscribir:\n\n{}".format(name, email, content),
            "no-contestar@inbox.mailtrap.io",
            ["jojaramillo@itsqmet.edu.ec"],
            reply_to=[email]
        )

        #Enviar mail
        try:
            email.send()
            return redirect(reverse('contact') + '?ok')
        except:
            return redirect(reverse('contact') + '?fail')
    
    return render(request, 'contact/contact.html',{'contactForm':contactForm})