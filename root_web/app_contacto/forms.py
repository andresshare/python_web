from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEED TO START WITH Z")

class FormName(forms.Form):
    #code for check
    #name = forms.CharField(validators=[check_for_z])
    name = forms.CharField(validators=[])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    verify_email = forms.CharField(label="Enter your email again")
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

def clean():
    all_clean_data = super().clean()
    email = all_clean_data['email']
    vmail = all_clean_data['verify_mail']
    if email != vmail:
        raise forms.ValidationError("make sure Emails match")


# def clean_botcatcher(self):
#     botcatcher = self.cleaned_data['botcatcher']
#     if len(botcatcher) > 0:
#         raise forms.ValidationError("GOTCHA BOT")
#     return botcatcher




