from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.utils.translation import gettext as _
from account.models import Account
from django.core.exceptions import ValidationError



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl blk-txt'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl blk-txt'
    }))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = _('Nazwa Użytkownika')
        self.fields['password'].widget.attrs['placeholder'] = _('Hasło')
    


# class SignupForm(UserCreationForm):
#     cokolwiek = forms.CharField(widget=forms.TextInput, max_length=34, required=False)
    
#     class Meta:
#         model = User
#         fields = ('username', 'cokolwiek', 'email', 'password1', 'password2')
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder ' : 'Your username',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
    
#     email = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder ' : 'Your email',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder ' : 'Your password',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder ' : 'Repeat your password',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         count = User.objects.filter(email=email).count()
#         print(count)
#         if count > 0:
#             raise forms.ValidationError('Ten adres email jest juz zajety!')
#         return email


class SignupForm2(forms.Form):
#     PROFESJA_CHOICES = [
#     ('Wybierz', _('Wybierz')),
#     ('Wokal/Inst', _('Wokal/Inst')),
#     ('Produkcja', _('Produkcja')),
#     ('Zadnej pracy sie nie boje', _('Zadnej pracy sie nie boje')),
# ]
    
    profesja = forms.ChoiceField(
        # choices=PROFESJA_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full py-4 px-6 rounded-xl  blk-txt',
        })
    )
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'w-full py-3 px-6 rounded-xl blk-txt' }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full py-3 px-6 rounded-xl blk-txt'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-3 px-6 rounded-xl blk-txt'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-3 px-6 the rounded-xl blk-txt'}))
    
    
    
    captcha = ReCaptchaField(
    widget=ReCaptchaV2Checkbox(),
    error_messages={
        'required': _('Udowodnij ze nie jestes robotem, zarejestruj sie potem.'),
    }
)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = _('Nazwa Użytkownika')
        self.fields['password1'].widget.attrs['placeholder'] = _('Hasło')
        self.fields['password2'].widget.attrs['placeholder'] = _('Potwierdź hasło')
        self.fields['email'].widget.attrs['placeholder'] = _('Adres email')
        self.fields['profesja'].choices = [
            ('Wybierz', _('Wybierz')),
            ('Wokal/Inst', _('Wokal/Inst')),
            ('Produkcja', _('Produkcja')),
            ('Zadnej pracy sie nie boje', _('Zadnej pracy sie nie boje')),
        ]
        
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(_('Hasla do siebie nie pasuja.'))
        return password2
    def clean_profesja(self):
        profesja = self.cleaned_data.get('profesja')
        if profesja == 'Wybierz':
            raise forms.ValidationError('Wybierz z listy czym zajmujesz sie w muzyce!')
        return profesja
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        count = User.objects.filter(email=email).count()
        print(count)
        if count > 0:
            raise forms.ValidationError('Ten adres email jest juz zajety!')
        return email
    
    
    
class emailUpdate(forms.ModelForm):
    email = forms.EmailField(required=True,
                                widget=forms.TextInput())
    
    class Meta:
        model = User
        fields = ['email']





class profilePicForm(forms.ModelForm):
    pic = forms.FileField(label='', widget=forms.ClearableFileInput(attrs={
        'class': 'downloadbtn bg-secondary hover:bg-teal-700 w-full py-4 px-6 rounded-xl white-txt',}))

    class Meta:
        model = Account
        fields = ['pic']
        
    def clean_pic(self):
        pic = self.cleaned_data.get('pic')
        if pic:
            # Check if the picture size is greater than 5MB (5242880 bytes)
            if pic.size > 5242880:  # 5MB in bytes
                raise ValidationError("The maximum file size is 5MB.")
        return pic