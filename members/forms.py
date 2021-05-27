from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from book.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'phone', 'country', 'city', 'street', 'housenumber')
        widgets = {
                'user': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'id', 'type':'hidden'}),
                'phone': forms.NumberInput(attrs={'class':'form-control'}),
                'country': forms.TextInput(attrs={'class':'form-control'}),
                'city': forms.TextInput(attrs={'class':'form-control'}),
                'street': forms.TextInput(attrs={'class':'form-control'}),
                'housenumber': forms.NumberInput(attrs={'class':'form-control'}),
        }