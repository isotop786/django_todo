from django import forms
from django.forms import ModelForm, fields
from .models import Todo


class TodoForm(forms.ModelForm):
    # class meta
    class Meta:
        model = Todo
        fields = (
            'title',
            'description',
        )
    
