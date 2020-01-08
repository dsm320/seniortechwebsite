from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from sendgrid_backend.mail import SendgridBackend

from contact.forms import ContactForm

# Create your views here.

def contact_index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            template = get_template('contact_template.txt')

            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            context = {
                'name' : name,
                'from_email' : from_email,
                'message' : message,
            }

            content = template.render(context)

            html_thanks = render_to_string("email.html", context)

            try:
                request_email = EmailMessage(name + ' - Customer Contact Request', content, 'Your Website<noreply@seniortechnologyllc.com>', ['seniortechnologyassociates@gmail.com'], reply_to=[from_email])
                thanks_email = EmailMessage('DO NOT REPLY - Senior Technology Associates', html_thanks, 'seniortechnologyassociates@gmail.com', [from_email])
                thanks_email.content_subtype = 'html'
                sg = SendgridBackend()
                sg.send_messages([request_email, thanks_email])
                messages.success(request, 'Message Recieved: Senior Technology Associates will get back to you ASAP')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('home_index')

    messages.info(request, 'Please pardon our appearance, this page is under construction.')
    
    return render(request, "contact_index.html", {'form': form})
