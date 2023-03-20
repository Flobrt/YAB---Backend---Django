from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('brief/', views.brief_list, name='brief_list'),
    path('brief/<int:brief_id>/', views.brief_view, name='brief_view'),
    path('apprenant/', views.apprenant_list, name='apprenant_list'),
    path('apprenant/<int:apprenant_id>', views.apprenant_view, name='apprenant_view'),
    path('apprenant/<int:apprenant_id>/delete/', views.apprenant_del, name='apprenant_delete'),
    path('brief/<int:brief_id>/binomotron/', views.binomotron, name='binomotron'),
    path('brief/<int:brief_id>/delete/', views.brief_del ,name="delete"),
    path('brief/<int:pk>/update/', views.BriefUpdate.as_view(), name="brief_update"),
    path('apprenant/<int:pk>/update/', views.ApprenantUpdate.as_view(), name="apprenant_update"),
]
