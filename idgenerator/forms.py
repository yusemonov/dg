from django import forms
from django.forms import widgets
from .models import Doc
from django.core.exceptions import ValidationError


class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = '__all__'
        # localized_fields = '__all__'
