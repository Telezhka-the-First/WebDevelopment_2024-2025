from .models import Feedback
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша обратная связь'
            })
        }