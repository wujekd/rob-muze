from django import forms
from .models import Collab, CollabSub

class CollabSubform(forms.ModelForm):
    class Meta:
        model = CollabSub
        fields = ['title', 'msg', 'file']
        
    title = forms.CharField(label='Tytol Utworu')
    msg = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), label='Description')
    file = forms.FileField(label='Plik audio')
