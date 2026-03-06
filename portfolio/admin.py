from django.contrib import admin
from django.utils.html import mark_safe
from .models import Profile, Skill, Project, Experience, Service, PriseDeContact, SocialNetwork, Location


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email", "photo_preview", "updated_at")
    fieldsets = (
        ("Identité", {"fields": ("full_name", "title", "photo")}),
        ("Contact", {"fields": ("email", "phone")}),
        ("Bio", {"fields": ("about_me",)}),
        ("Liens", {"fields": ("github_url", "linkedin_url", "cv_file", "cv_url")}),
    )

    @admin.display(description="Photo")
    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="40" height="40" style="border-radius:50%;object-fit:cover;" />')
        return "-"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage", "order")
    list_editable = ("percentage", "order")
    ordering = ("order", "name")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "technologies", "order", "link", "image_preview")
    list_editable = ("order",)
    list_filter = ("technologies",)
    search_fields = ("title", "resume", "technologies")
    ordering = ("order", "-created_at")
    fieldsets = (
        (None, {"fields": ("title", "resume", "technologies", "link", "order")}),
        ("Image", {"fields": ("image",)}),
    )

    @admin.display(description="Aperçu")
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="60" style="object-fit:cover;border-radius:4px;" />')
        return "-"


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company_name", "start_date", "end_date", "contract_type")
    list_filter = ("contract_type",)
    ordering = ("-start_date",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "service_type", "tools", "icon_preview")
    fieldsets = (
        (None, {"fields": ("name", "details", "service_type", "tools")}),
        ("Icône", {"fields": ("icon", "icon_class"),
                   "description": "Uploadez une image OU renseignez une classe CSS d'icône."}),
    )

    @admin.display(description="Icône")
    def icon_preview(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" width="32" height="32" />')
        return obj.icon_class or "-"


@admin.register(PriseDeContact)
class PriseDeContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "object", "creation_date")
    readonly_fields = ("full_name", "email", "object", "message", "creation_date")
    ordering = ("-creation_date",)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ("platform_name", "link")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("city", "country", "latitude", "longitude")
