from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    """Profil du propriétaire du portfolio (une seule instance)."""
    full_name = models.CharField(max_length=100, verbose_name="Full name", default="")
    title = models.CharField(max_length=100, verbose_name="Title", default="")
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Phone", blank=True)
    about_me = models.TextField(verbose_name="About me", blank=True)
    cv_file = models.FileField(upload_to="cv/", verbose_name="CV (PDF)", blank=True, null=True)
    cv_url = models.URLField(verbose_name="CV URL (fallback)", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    photo = models.ImageField(upload_to="profile/", verbose_name="Photo", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.full_name or "Portfolio Profile"


class Skill(models.Model):
    name = models.CharField(max_length=80, verbose_name="Skill name")
    percentage = models.PositiveIntegerField(default=50, verbose_name="Proficiency (%)")
    order = models.PositiveIntegerField(default=0, verbose_name="Display order")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="projects",
        null=True,
        blank=True
    )
    resume = models.TextField(verbose_name="Project summary")
    title = models.CharField(max_length=120, verbose_name="Title")
    image = models.ImageField(upload_to="projects/", verbose_name="Image du projet", blank=True, null=True)
    link = models.URLField(max_length=500, verbose_name="Link (e.g. GitHub)", blank=True)
    technologies = models.CharField(max_length=255, verbose_name="Technologies (comma-separated)", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Display order")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["order", "-created_at"]


class Experience(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="experiences",
        null=True,
        blank=True,
    )
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    role = models.CharField(max_length=30, verbose_name="Role")
    company_name = models.CharField(max_length=30, verbose_name="Company name")
    description = models.TextField(verbose_name="Description")  # TextField au lieu de CharField
    contract_type = models.CharField(max_length=30, verbose_name="Contract type")
    
    def __str__(self):
        return f"{self.role} at {self.company_name}"
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

class Service(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="User", 
        related_name="services",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=80, verbose_name="Nom du service")
    details = models.TextField(verbose_name="Détails")
    service_type = models.CharField(max_length=30, verbose_name="Type de service")
    tools = models.CharField(max_length=100, verbose_name="Outils")
    icon = models.ImageField(upload_to="services/", verbose_name="Icône du service", blank=True, null=True)
    icon_class = models.CharField(max_length=80, verbose_name="Classe CSS icône (ex: icon-laptop2)", blank=True) 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class PriseDeContact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User", related_name="contacts_recus", null=True, blank=True)
    full_name = models.CharField(max_length=70, verbose_name="Full name")
    object = models.CharField(max_length=30, verbose_name="Object")
    email = models.EmailField(verbose_name="Email")  # EmailField au lieu de CharField
    message = models.TextField(verbose_name="Message")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    
    def __str__(self):
        return f"{self.full_name} - {self.object}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class SocialNetwork(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="User", 
        related_name="social_networks",
        null=True,
        blank=True
    )
    platform_name = models.CharField(max_length=30, verbose_name="Platform name")
    link = models.URLField(verbose_name="Link")  # URLField au lieu de CharField
    
    def __str__(self):
        return self.platform_name
    
    class Meta:
        verbose_name = "Social network"
        verbose_name_plural = "Social networks"

class Location(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="User", 
        related_name="locations",
        null=True,
        blank=True
    )
    city = models.CharField(max_length=50, verbose_name="City")
    country = models.CharField(max_length=50, verbose_name="Country")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    
    def __str__(self):
        return f"{self.city}, {self.country}"
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"