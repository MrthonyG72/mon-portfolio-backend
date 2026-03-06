from rest_framework import serializers
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


class AbsoluteImageField(serializers.ImageField):
    """Retourne l'URL absolue pour les fichiers uploadés."""
    def to_representation(self, value):
        if not value:
            return None
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(value.url)
        return value.url


class AbsoluteFileField(serializers.FileField):
    def to_representation(self, value):
        if not value:
            return None
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(value.url)
        return value.url


class ProfileSerializer(serializers.ModelSerializer):
    photo = AbsoluteImageField(read_only=True)
    cv_file = AbsoluteFileField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "full_name",
            "title",
            "email",
            "phone",
            "about_me",
            "cv_file",
            "cv_url",
            "github_url",
            "linkedin_url",
            "photo",
        ]
        read_only_fields = ["id"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "percentage", "order"]


class ProjectSerializer(serializers.ModelSerializer):
    image = AbsoluteImageField(read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "user",
            "resume",
            "title",
            "image",
            "link",
            "technologies",
            "order",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "user",
            "start_date",
            "end_date",
            "role",
            "company_name",
            "description",
            "contract_type",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    icon = AbsoluteImageField(read_only=True)

    class Meta:
        model = Service
        fields = [
            "id",
            "user",
            "name",
            "details",
            "service_type",
            "tools",
            "icon",
            "icon_class",
        ]


class PriseDeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriseDeContact
        fields = [
            "id",
            "user",
            "full_name",
            "object",
            "email",
            "message",
            "creation_date",
        ]
        read_only_fields = ["creation_date"]


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = [
            "id",
            "user",
            "platform_name",
            "link",
        ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "id",
            "user",
            "city",
            "country",
            "longitude",
            "latitude",
        ]
