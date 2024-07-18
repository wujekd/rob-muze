from django import forms

class VerifyMemberForm(forms.Form):
    approve = forms.BooleanField(required=True, label='Approve Membership')
    
class JoinGroupForm(forms.Form):
    token = forms.CharField(max_length=64, required=False, help_text="Enter your invitation token if you have one.")
