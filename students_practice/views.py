from django.shortcuts import render
from django.views import generic
from elite.mixins import *

class StudentsPractice(MenuMixin, generic.TemplateView):
    template_name = 'students_practice/students_practice.html'