from django import forms
from .models import Collab, CollabSub

class CollabSubform(forms.ModelForm):
    title = forms.CharField(label='Tytol Utworu')
    msg = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), label='Description')
    file = forms.FileField(label='Plik audio')

    class Meta:
        model = CollabSub
        fields = ['title', 'msg', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')

        if file:
            if file.size > 70*1024*1024:  # limit is set to 70 MB
                raise forms.ValidationError('Maksymalny rozmiar pliku to 70MB')

            if not file.name.endswith('.wav'):
                raise forms.ValidationError('Tylko pliki .wav!')
        
        return file