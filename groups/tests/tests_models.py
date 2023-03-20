from django.test import TestCase
from groups.models import Brief, Apprenant, Nome


class ApprenantModelTest(TestCase):
    @classmethod
    def setUpTestData(cls): 
        # Set up data for the whole TestCase
        Apprenant.objects.create(nom_apprenant='nom_apprenant', prenom_apprenant='prenom_apprenant')
    # nom apprenant
    def test_nom_apprenant_label(self):
        apprenant = Apprenant.objects.get(id=1)
        field_label = apprenant._meta.get_field('nom_apprenant').verbose_name
        self.assertEquals(field_label, 'nom_apprenant')
    # prenom apprenant

    def test_nom_apprenant_label(self):
        apprenant = Apprenant.objects.get(id=1)
        field_label = apprenant._meta.get_field('prenom_apprenant').verbose_name
        self.assertEquals(field_label, 'prenom apprenant')

    def test_nom_apprenant_max_length(self):
        apprenant = Apprenant.objects.get(id=1)
        max_length = apprenant._meta.get_field('nom_apprenant').max_length
        self.assertEquals(max_length, 30)
    # prenom apprenant
    def test_prenom_apprenant_max_length(self):
        apprenant = Apprenant.objects.get(id=1)
        max_length = apprenant._meta.get_field('prenom_apprenant').max_length
        self.assertEquals(max_length, 30)


class BriefModelTest(TestCase):
    @classmethod
    def setUpTestData(cls): 
        # Set up non-modified objects used by all test methods
        Brief.objects.create(titre_brief='titre_brief', url_brief='url_brief')
    # titre brief
    def test_titre_brief_max_length(self):
        Brief = Brief.objects.get(id=1)
        max_length = Brief._meta.get_field('titre_brief').max_length
        self.assertEquals(max_length, 35)
    # longueur url
    def test_url_brief_max_length(self):
        Brief = Brief.objects.get(id=1)
        max_length = Brief._meta.get_field('url_brief').max_length
        self.assertEquals(max_length, 100)
    # chemin url
    def test_get_absolute_url(self):
        Brief = Brief.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(Brief.get_absolute_url(), '/groups/brief/1')