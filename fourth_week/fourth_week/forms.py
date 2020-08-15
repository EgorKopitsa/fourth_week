from django import forms

from app.models import Application
from app.models import Image


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ['vacancy', 'user']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
