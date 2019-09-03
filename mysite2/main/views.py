from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class DasboardView(TemplateView):
    template_name = 'layouts/default/page.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'