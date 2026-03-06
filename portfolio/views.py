from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django.conf import settings
from django.core.mail import send_mail

from .models import (
    Profile,
    Skill,
    Project,
    Experience,
    Service,
    PriseDeContact,
    SocialNetwork,
    Location,
)
from .serializer import (
    ProfileSerializer,
    SkillSerializer,
    ProjectSerializer,
    ExperienceSerializer,
    ServiceSerializer,
    PriseDeContactSerializer,
    SocialNetworkSerializer,
    LocationSerializer,
)


# Profile: retourne le premier profil ou null
@extend_schema(tags=["Profile"])
class ProfileDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        profile = Profile.objects.first()
        if not profile:
            return Response(None)
        return Response(ProfileSerializer(profile, context={'request': request}).data)


@extend_schema(tags=["Skills"])
class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]


# Projects
@extend_schema(tags=["Projects"])
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Projects"])
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Projects"])
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


# Experiences
@extend_schema(tags=["Experiences"])
class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Experiences"])
class ExperienceCreateView(generics.CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Experiences"])
class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


# Services
@extend_schema(tags=["Services"])
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Services"])
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Services"])
class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


# Contact
@extend_schema(tags=["Contacts"])
class PriseDeContactListView(generics.ListAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Contacts"])
class PriseDeContactCreateView(generics.CreateAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        contact = serializer.save()
        subject = f"[Portfolio] Nouveau message : {contact.object}"
        message = (
            f"Nom : {contact.full_name}\n"
            f"Email : {contact.email}\n\n"
            f"Message :\n{contact.message}"
        )
        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None)
        recipient = getattr(settings, "CONTACT_RECIPIENT_EMAIL", None) or from_email

        if from_email and recipient:
            try:
                send_mail(subject, message, from_email, [recipient], fail_silently=True)
            except Exception:
                # On ignore les erreurs d'envoi d'email côté API,
                # le message reste tout de même stocké en base.
                pass


@extend_schema(tags=["Contacts"])
class PriseDeContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


# Social networks
@extend_schema(tags=["Social Networks"])
class SocialNetworkListView(generics.ListAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Social Networks"])
class SocialNetworkCreateView(generics.CreateAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Social Networks"])
class SocialNetworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = [permissions.AllowAny]


# Location
@extend_schema(tags=["Locations"])
class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Locations"])
class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Locations"])
class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]
