from django import forms
from .models import Collab, CollabSub, Stages

class AddStageForm(forms.ModelForm):
    title = forms.CharField(
        label='Stage Name',
        widget=forms.TextInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': "color: black"
        })
    )
    desc = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        }),
        label='Description'
    )
    download_pack = forms.FileField(
        label='Download Pack',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    backing_track = forms.FileField(
        label='Backing Track',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    demo = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    score = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    midi = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    ableton = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    reaper = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    logic = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    wokal = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    instrument = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )
    rap = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        })
    )

    class Meta:
        model = Stages
        fields = ['title', 'desc', 'download_pack', 'backing_track', 'demo', 'score', 'midi', 'ableton', 'reaper', 'logic', 'wokal', 'instrument', 'rap']
    
    
    
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