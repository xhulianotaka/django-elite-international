from job.models import *
from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class JobApplicationForm(ModelForm):
    class Meta:
        model = JobApplication
        exclude = ('job',)
        widgets = {
            'additional_information': Textarea(attrs={'rows': 5}),
        }

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'nk-form nk-form-style-1'
    helper.add_input(Submit('submit', 'Apply', css_class='nk-btn nk-btn-block nk-btn-rounded nk-btn-color-dark-2'))
