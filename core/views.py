from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Imtahan as imtModel

# Create your views here.
from django.views.generic.base import ContextMixin,TemplateView


class BaseContext(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context



def detal(request):
    return render(request, template_name='exam_correct.html')


class Imtahan(BaseContext, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        imtahanlar = imtModel.objects.all().order_by('tarix')
        context.update({'imtahanlar': imtahanlar})

        return context


