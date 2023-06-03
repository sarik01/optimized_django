from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django import forms

from services.models import Plan
from .forms import PanForm, PanConfirmDelete
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# class PlanFormView(FormView):
#     template_name = 'pan_form.html'
#     form_class = PanForm
#     success_url = '/web/plans'
#
#     def form_valid(self, form):
#         Plan.objects.create(**form.cleaned_data)
#         return super().form_valid(form)
#


class PlanFormView(CreateView):
    template_name = 'pan_form.html'
    model = Plan
    fields = '__all__'
    success_url = '/web/plans'


class PlanUpdateView(UpdateView):
    model = Plan
    fields = '__all__'
    template_name_suffix = '_update_form'
    template_name = 'pan_confirm_delete.html'




class DeletePlanView(DeleteView):
    model = Plan
    form_class = PanConfirmDelete
    success_url = reverse_lazy('web:create_plan')
    f = PanConfirmDelete
    template_name = 'pan_confirm_delete.html'



