from django import forms
from .models import Collab, CollabSub

class CollabSubform(forms.ModelForm):
    title = forms.CharField(label='Tytół Utworu', widget=forms.TextInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl', 'style' : "color: black"}))
    msg = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'class': 'w-full py-4 px-6 rounded-xl', "style" : 'color: black'}), label='Description',)
    
    file = forms.FileField(label='Plik audio', widget=forms.ClearableFileInput(attrs={
        'class': 'downloadbtn bg-secondary hover:bg-teal-700 w-full py-4 px-6 rounded-xl',}))

    class Meta:
        model = CollabSub
        fields = ['title', 'msg', 'file', 'volumeOffset']


    def clean_file(self):
        file = self.cleaned_data.get('file')


        if file:
            if file.size > 100*1024*1024:
                raise forms.ValidationError('Maksymalny rozmiar pliku to 100MB')

            # if not file.name.endswith('.wav'):
            #     raise forms.ValidationError('Tylko pliki .wav!')
        
        return file
    
    
class SubCheckForm(forms.ModelForm):
    class Meta:
        model = CollabSub
        fields = ['volumeOffset', 'approved']
        widgets = {
            'volumeOffset': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '10', 'step': '0.1'}),
            'approved': forms.CheckboxInput()
        }
