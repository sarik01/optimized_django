from django import forms
from django.core.exceptions import ValidationError

from services.models import Plan


class PanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'


class PanConfirmDelete(forms.Form):
    confirm_delete = forms.BooleanField(required=False)

    def clean(self):
        if self.cleaned_data['confirm_delete'] is False:
            raise ValidationError("You must confirm this form!")
        return super(PanConfirmDelete, self).clean()