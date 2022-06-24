from django import forms
from django.forms import ModelForm

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class FlyerForm(ModelForm):

    class Meta:
        model = Flyer
        fields = ('Boro', 'Event_type', 'Event_date',
                 'Contact_information', 'Address','Flyer_image',)

class Flyer_ImageForm(forms.ModelForm):
    
    class Meta:
        model = Flyer_Image
        fields = ('Flyer_image',)