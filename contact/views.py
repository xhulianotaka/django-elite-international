from django.shortcuts import render
from django.views import generic
from envelope.views import ContactView
from contact.forms import *
from braces.views import FormMessagesMixin
from elite.mixins import *

class Contact(MenuMixin, FormMessagesMixin, ContactView):
    form_class = MyContactForm
    template_name = 'contact/contact.html'
    form_invalid_message = "There was an error in the contact form. Please try again."
    form_valid_message = "Thank you for your message."
