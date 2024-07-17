# myapp/forms.py
from django import forms

class TextInputForm(forms.Form):
    input_text = forms.CharField(
        label='Enter text',
        max_length=1000,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'cols': 40,
            'placeholder': 'Type your mail text here...'
        })
    )
