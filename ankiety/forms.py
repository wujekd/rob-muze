from django import forms
from . models import AnkietaOtw, OdpowiedzOtw

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border text-gray-800'


class AnkietaOtw_form(forms.ModelForm):
    class Meta:
        model = OdpowiedzOtw
        fields = ('answer',)
        widgets = {
            'answer': forms.Textarea(attrs={'class': INPUT_CLASSES}),
  }