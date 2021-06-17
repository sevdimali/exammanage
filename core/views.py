from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Imtahan as imtModel, ExamCorrect

# Create your views here.
from django.views.generic.base import ContextMixin, TemplateView


class BaseContext(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class Imtahan(BaseContext, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        imtahanlar = imtModel.objects.all().order_by('tarix')
        context.update({'imtahanlar': imtahanlar})

        return context


class DuzgunCavab(BaseContext, TemplateView):
    template_name = 'exam_correct.html'
    duzgun = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = self.kwargs.get('pk')
        imtahan = get_object_or_404(imtModel, pk=pk)
        self.duzgun = ExamCorrect.objects.filter(imtahan_id=imtahan).order_by('imtahan_id')
        context.update({'duzgun': self.duzgun})

        return context
