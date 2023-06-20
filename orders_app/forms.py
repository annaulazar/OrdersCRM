from django import forms
from django.contrib.auth.models import User

from orders_app.models import Orders
from users_app.forms import StyleFormMixin


class CreateOrderForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Orders
        fields = ('title', 'category', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Краткое описание'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Подробное описание'}),
        }
        labels = {
            'title': 'Что случилось?',
            'description': 'Описание проблемы',
        }


class TargetEmployerForm(StyleFormMixin, forms.ModelForm):
    master = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='masters'))

    class Meta:
        model = Orders
        fields = ('master',)
