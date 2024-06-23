from django import forms
from .models import Ideas





class AddIdeaForm(forms.ModelForm):
    title_en = forms.CharField(
        label='Idea title',
        widget=forms.TextInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': "color: black"
        })
    )
    desc_en = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'w-full py-4 px-6 rounded-xl',
            'style': 'color: black'
        }),
        label='Description'
    )
    file = forms.FileField(
        label='Plik audio',
        widget=forms.ClearableFileInput(attrs={
            'class': 'downloadbtn bg-secondary hover:bg-teal-700 w-full py-4 px-6 rounded-xl'
        })
    )
    vocals = forms.BooleanField(
        label='Vocals',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'mr-2 leading-tight'
        })
    )
    acoustic = forms.BooleanField(
        label= 'Acoustic',
        required = False,
        widget=forms.CheckboxInput(attrs={
            'class': 'mr-2 leading-tight'
        })
    )
    electronic = forms.BooleanField(
        label='Electronic',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'mr-2 leading-tight'
        })
    )
    drums = forms.BooleanField(
        label='Drums',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'mr-2 leading-tight'
        })
    )
    rap = forms.BooleanField(
        label='Rap',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'mr-2 leading-tight'
        })
    )
    beat = forms.BooleanField(
        label='Beat',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'mr-2 leading-tight'
        })
    )
    

    class Meta:
        model = Ideas  # Ensure the correct model is used
        fields = ['title_en', 'desc_en', 'file', 'vocals', 'acoustic', 'rap']

    def clean_file(self):
        file = self.cleaned_data.get('file')

        if file:
            if file.size > 100 * 1024 * 1024:
                raise forms.ValidationError('Maksymalny rozmiar pliku to 100MB')

            # if not file.name.endswith('.wav'):
            #     raise forms.ValidationError('Tylko pliki .wav!')

        return file


# class AddIdeaForm(forms.ModelForm):
#     title_en = forms.CharField(label='Idea title', widget=forms.TextInput(attrs={
#         'class': 'w-full py-4 px-6 rounded-xl', 'style' : "color: black"}))
#     desc_en = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'class': 'w-full py-4 px-6 rounded-xl', "style" : 'color: black'}), label='Description',)
    
#     file = forms.FileField(label='Plik audio', widget=forms.ClearableFileInput(attrs={
#         'class': 'downloadbtn bg-secondary hover:bg-teal-700 w-full py-4 px-6 rounded-xl',}))
    
    

#     class Meta:
#         model = Ideas
#         fields = ['title_en', 'desc_en', 'file', 'vocals', 'acoustic', 'electronic', 'drums', 'rap',]


#     def clean_file(self):
#         file = self.cleaned_data.get('file')


#         if file:
#             if file.size > 100*1024*1024:
#                 raise forms.ValidationError('Maksymalny rozmiar pliku to 100MB')

#             # if not file.name.endswith('.wav'):
#             #     raise forms.ValidationError('Tylko pliki .wav!')
            
#         return file