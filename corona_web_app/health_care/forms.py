from django import forms

class HealthCheck(forms.forms):
    labels = ['呼吸苦']
    SINGLE_CHOICE = [('あり')]
    
    check = forms.MultipleChoiceField(
        label= labels[0],
        required= False,
        disabled= False,
        initial=[],
        choices=SINGLE_CHOICE
        widget=forms.forms.CheckboxSelectMultiple(attrs={
            'id': 'checks','class' : 'form-check-input'
        })
    )
