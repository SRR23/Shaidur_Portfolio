from django import forms
from .models import Messages


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_message(self):
        data = self.cleaned_data['message']
        return data

    def save(self, commit=True): 
        instance = Messages(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            message=self.cleaned_data['message'],
        )
        if commit:
            instance.save()
        return instance