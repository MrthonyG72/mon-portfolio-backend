from rest_framework import serializers
from .models import Utilisateur
# On utilise les noms exacts définis dans portfolio/serializer.py
from portfolio.serializer import (
    ProjectSerializer,
    ExperienceSerializer,
    ServiceSerializer,
    SocialNetworkSerializer,
    LocationSerializer
)

class UtilisateurSerializer(serializers.ModelSerializer):
    # Tu peux maintenant les utiliser ici sans erreur
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Utilisateur
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'photo_de_profile', 'description', 'age', 'lien_cv', 
            'telephone', 'projects'
        ]