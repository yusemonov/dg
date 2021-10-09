from django import forms
from django.forms import widgets
from .models import Doc
from django.core.exceptions import ValidationError


class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ['given_name', 'surname',
                  'passport_number', 'genre', 'birth_date', 'locations', 'photo_doc', 'get_exif_info', 'background', 'background_image']
        # localized_fields = '__all__'
