from django import forms
from mcontroller.models import Masturbation


class SubmitMasturbationForm(forms.ModelForm):
    class Meta:
        model = Masturbation
        fields = ('m_reason', 'm_method', 'm_duration')
        labels = {
            'm_reason': 'What is the reason?',
            'm_method': 'What method have you used?',
            'm_duration': 'The duration of the process (in minutes)?',
        }
        widgets = {
            'm_reason': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols': '10',
                                              'placeholder': 'Stress, sexual thoughts,...'}),
            'm_method': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols': '10',
                                              'placeholder': 'Watch porn, hentai,...'}),
        }