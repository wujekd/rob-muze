from django import forms
from . models import AnkietaOtw, OdpowiedzOtw

INPUT_CLASSES = 'h-20 w-1/2 mt-8 bg-gray200 rounded-xl border text-gray-800'


class AnkietaOtw_form(forms.ModelForm):
    class Meta:
        model = OdpowiedzOtw
        fields = ('answer', )
        widgets = {
            'answer': forms.Textarea(attrs={'class': INPUT_CLASSES}),
  }
        

class RandomPollForm(forms.Form):
    name = forms.CharField(max_length=100)