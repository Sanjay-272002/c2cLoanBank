from django import forms
from .models import UserModel

class UserForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Name Here'}), required=True, error_messages={'required':'Must Enter a Correct Name'})
    interest = forms.CharField(label='Interest rate', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter Your interest rate Here(in integers)', 'rows':1, 'cols': 50}), error_messages={'required':'Must Enter a interest'})

    class Meta:
        model = UserModel
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email Here'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Enter Amount Here'}),
            'tenture': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Enter tenture Here in MONTHS'}),
            'occupation': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'language': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'gender' : { 'required' : 'Must Select a Gender'},
            'email' : { 'required' : 'Enter Correct Email'},
            'amount' : { 'required' : 'Enter Correct amount'},
            'income' : { 'required' : 'Select Your annual income'},
        }
