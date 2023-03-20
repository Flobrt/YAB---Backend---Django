from django.test import TestCase #lance chaque test dans une transaction pour garantir l’isolation
from groups.forms import ApprenantForm, BriefForm, ApprenantUpdate

# tests here for forms:
class ApprenantFormTest(TestCase):
    def test_apprenant_form_field_label(self):
        form = ApprenantForm()
        self.assertTrue(form.fields['nom_apprenant', 'prenom_apprenant'].label == None or form.fields['nom_apprenant', 'prenom_apprenant'].label == 'nom apprenant', 'prenom apprenant')

class BriefFormTest(TestCase):
    def test_brief_form_field_label(self):
        form = BriefForm()
        self.assertTrue(form.fields['titre_brief', 'url_brief', 'nb_appr_par_nome'].label == None or form.fields['titre_brief', 'url_brief', 'nb_appr_par_nome'].label == 'titre brief', 'url brief', 'nb appr par nome')

class ApprenantUpdateTest(TestCase):
    def test_apprenant_form_field_label(self):
        form = ApprenantUpdate()
        self.assertTrue(form.fields['nom_apprenant', 'prenom_apprenant'].label == None or form.fields['nom_apprenant', 'prenom_apprenant'].label == 'nom apprenant', 'prenom apprenant')