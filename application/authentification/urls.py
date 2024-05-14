from django.contrib import admin
from django.urls import path, include
from .views import acceuil, connexion, inscription, deconnexion, forgot, update

urlpatterns = [
   path('', acceuil, name='acceuil'),
   path('login', connexion, name='connexion'),
   path('inscrire/', inscription, name='inscription'),
   path('logout/', deconnexion, name='deconnexion'),
   path('forgot/', forgot, name='forgot'),
   path('update/<str:token>/<str:uid>/', update, name='update'),
]