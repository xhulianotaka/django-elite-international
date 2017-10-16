from envelope.forms import ContactForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib import messages

class MyContactForm(ContactForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    def __init__(self, *args, **kwargs):
        super(MyContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'nk-form-style-1'
        self.helper.add_input(Submit('submit', 'Submit', css_class='nk-btn nk-btn-rounded nk-btn-color-dark-2 nk-btn-block'))
