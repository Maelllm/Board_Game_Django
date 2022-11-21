from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ["get"]


class PageNotFoundView(TemplateView):
    template_name = "404.html"
