from django import forms

from .models import PlusOneGuest, Comment


class PlusOneForm(forms.ModelForm):
    class Meta:
        model = PlusOneGuest
        fields = ['name', 'last_name', 'drink_check', 'is_veggie']
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'drink_check': 'Bebe alcohol?',
            'is_veggie': 'Es vegetariano o vegano?'
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': ''
        }
