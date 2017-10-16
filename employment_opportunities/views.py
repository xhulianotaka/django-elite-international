from django.shortcuts import render
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

class EmploymentOpportunities(MenuMixin, generic.ListView):
    model = Job
    today = date.today()
    queryset = Job.objects.filter(last_date__gte=today)
    context_object_name = 'jobs'
    paginate_by = 6
    template_name = 'employment_opportunities/employment_opportunities.html'

class JobApply(MenuMixin, FormMessagesMixin, generic.CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    form_invalid_message = "There was an error in the application form. Please try again."
    form_valid_message = "Thank you for your application. We will contact you soon :)"
    template_name = 'employment_opportunities/job_application.html'

    def get_success_url(self):
        # send email using the self.cleaned_data dictionary
        subject = "New Job Applocation"
        to = ['taka_xhuliano@hotmail.com']
        from_email = 'hr@eliteinternational.al'
        current_site = get_current_site(self.request)

        message = render_to_string('email.html', {
            'domain': current_site.domain,
            'admin_url': urlresolvers.reverse('admin:job_jobapplication_change', args=(self.object.id,))
        })

        EmailMessage(subject, message, to=to, from_email=from_email).send()
        return reverse('employment_opportunities')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(JobApply, self).get_context_data(**kwargs)
        context['job'] = Job.objects.get(slug=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        job_apply = Job.objects.get(slug=self.kwargs['slug'])
        form.instance.job = job_apply
        return super(JobApply, self).form_valid(form)

class JobDetail(MenuMixin, generic.DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'employment_opportunities/job_detail.html'

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

def JobDetailAjax(request):
    if request.is_ajax():
        job = Job.objects.get(id=request.POST.get('item'))
        return render(request, 'employment_opportunities/job_detail_ajax.html', {'job': job})
    else:
        raise Http404
