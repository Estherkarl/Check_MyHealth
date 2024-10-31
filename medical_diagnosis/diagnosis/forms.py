from django import forms

class SymptomsForm(forms.Form):
    symptom = forms.CharField(
        max_length=100,
        label='Enter your symptoms',
        widget=forms.Textarea(attrs={'placeholder': 'Enter symptoms separated by commas'})
    )
