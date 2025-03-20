from django import forms
from .models import Collections

class UsersForm(forms.ModelForm):
    class Meta:
        model = Collections
        fields = ['name', 'phone', 'address', 'city']
