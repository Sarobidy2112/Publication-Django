from django import forms
from .models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['contenu', 'image']  # Inclure le champ 'image'
        widgets = {
            'contenu': forms.Textarea(attrs={
                'placeholder': 'Écrivez quelque chose...', 
                'rows': 5, 
                'class': 'form-control'
            }),
        }
        labels = {
            'contenu': 'Votre publication',
            'image': 'Ajouter une image (facultatif)',
        }

# class PublicationForm(forms.ModelForm):
#     class Meta:
#         model = Publication
#         fields = ['contenu']  # Seul le champ contenu est éditable par l'utilisateur
#         widgets = {
#             'contenu': forms.Textarea(attrs={
#                 'placeholder': 'Écrivez quelque chose...', 
#                 'rows': 5, 
#                 'class': 'form-control'
#             }),
#         }
#         labels = {
#             'contenu': 'Votre publication',
#         }