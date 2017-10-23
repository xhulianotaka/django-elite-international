from django.shortcuts import render, redirect
from django.views import generic
from job.models import *
from employment_opportunities.forms import *
from braces.views import FormMessagesMixin
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core import urlresolvers
from django.contrib.sites.shortcuts import get_current_site
from datetime import date
from elite.mixins import *
from django.http import JsonResponse
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.conf import settings
import urllib
import json

class EmploymentOpportunities(MenuMixin, generic.ListView):
    model = Job
    today = date.today()
    queryset = Job.objects.filter(last_date__gte=today)
    context_object_name = 'jobs'
    paginate_by = 6
    template_name = 'employment_opportunities/employment_opportunities.html'

def JobApply(request, slug):
    job_apply = Job.objects.get(slug=slug)

    if request.is_ajax():
        template = 'employment_opportunities/job_application_ajax.html'
    else:
        template = 'employment_opportunities/job_application.html'

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                application_form = form.save(commit=False)
                application_form.job = job_apply
                application_form.save()
                application_form.refresh_from_db()

                ''' Begin Send E-mail '''
                subject = "New Job Applocation"
                to = ['taka_xhuliano@hotmail.com']
                from_email = 'hr@eliteinternational.al'
                current_site = get_current_site(request)

                message = render_to_string('email.html', {
                    'domain': current_site.domain,
                    'admin_url': urlresolvers.reverse('admin:job_jobapplication_change', args=(application_form.id,))
                })

                EmailMessage(subject, message, to=to, from_email=from_email).send()
                ''' End Send E-mail '''

                messages.success(request, 'Thank you for your application. We will contact you soon :)')

                if not request.is_ajax():
                    return redirect(reverse('employment_opportunities'))

            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        else:
            messages.error(request, 'There was an error in the application form. Please try again.')
    else:
        form = JobApplicationForm()

    return render(request, template, {'form': form,
                                      'job': job_apply})

class JobDetail(MenuMixin, generic.DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'employment_opportunities/job_detail.html'

def JobDetailAjax(request):
    if request.is_ajax():
        job = Job.objects.get(id=request.POST.get('item'))
        return render(request, 'employment_opportunities/job_detail_ajax.html', {'job': job})
    else:
        raise Http404

class CategoryDetail(MenuMixin, generic.DetailView):
    model = JobCategory
    context_object_name = 'category'
    template_name = 'employment_opportunities/category_detail.html'

class TagDetail(MenuMixin, generic.DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'employment_opportunities/tag_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TagDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['jobs_list'] = Job.objects.filter(tags__name=self.kwargs['slug'])
        return context

