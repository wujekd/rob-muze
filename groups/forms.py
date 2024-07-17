from django import forms

class VerifyMemberForm(forms.Form):
    approve = forms.BooleanField(required=True, label='Approve Membership')