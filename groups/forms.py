from django import forms
from .models import Brief, Apprenant
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


class ApprenantForm(forms.ModelForm):
    class Meta:
        model = Apprenant
        fields = ['nom_apprenant', 'prenom_apprenant']


class BriefForm(forms.ModelForm):
    class Meta:
        model = Brief
        fields = ['titre_brief', 'url_brief', 'nb_appr_par_nome']


# class ApprenantDelete(DeleteView):
#     model = Apprenant
#     success_url = reverse_lazy('apprenant')

class ApprenantUpdate(UpdateView):
    model = Apprenant
    fields = ['nom_apprenant', 'prenom_apprenant']




  
