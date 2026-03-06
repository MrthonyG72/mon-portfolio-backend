from rest_framework import generics, permissions
from .serializer import UtilisateurSerializer
from drf_spectacular.utils import extend_schema
from .models import Utilisateur

@extend_schema(tags=['Utilisateur'])
class UtilisateurListView(generics.ListAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.AllowAny]

@extend_schema(tags=['Utilisateur'])
class UtilisateurCreateView(generics.CreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.AllowAny]

@extend_schema(tags=['Utilisateur'])
class UtilisateurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.AllowAny]
