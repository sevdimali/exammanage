from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .forms import ExamCorrectForms, NeticelerForms
from .models import Imtahan as imtModel, ExamCorrect,Neticeler

# Create your views here.
from django.views.generic.base import ContextMixin, TemplateView


class BaseContext(LoginRequiredMixin,ContextMixin):
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


    def post(self, request, pk):
        exam_form = ExamCorrectForms(request.POST, request.FILES)
        if exam_form.is_valid():
            ec_inst = exam_form.save()
            exam = get_object_or_404(imtModel, pk=pk)
            ec_inst.imtahan_id.add(exam)
            ec_inst.author = request.user
            ec_inst.save()
        return redirect('exam_correct', pk=pk)


class NeticeV(BaseContext, TemplateView):
    template_name = 'neticeler.html'
    duzgun = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = self.kwargs.get('pk')
        imtahan = get_object_or_404(imtModel, pk=pk)
        self.duzgun = Neticeler.objects.filter(imtahan_id=imtahan).order_by('imtahan_id')
        context.update({'duzgun': self.duzgun})

        return context


    def post(self, request, pk):
        exam_form = NeticelerForms(request.POST, request.FILES)
        if exam_form.is_valid():
            ec_inst = exam_form.save()
            exam = get_object_or_404(imtModel, pk=pk)
            ec_inst.imtahan_id.add(exam)
            ec_inst.author = request.user
            ec_inst.save()
        return redirect('neticeler', pk=pk)