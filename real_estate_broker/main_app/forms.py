from django import forms
from .models import Consultation


class BaseConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'


class ConsultationCreateForm(BaseConsultationForm):
    class Meta(BaseConsultationForm.Meta):
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Първо име...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Електронна поща...'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон за връзка...'}),
            'choices': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'first_name': 'Първо име',
            'last_name': 'Фамилия',
            'email': 'Електронна поща',
            'phone_number': 'Телефон за връзка',
            'choices': 'Консултация за:'
        }