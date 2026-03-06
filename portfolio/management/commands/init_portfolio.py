"""
Commande pour créer un profil et des compétences par défaut.
Usage: python manage.py init_portfolio
"""
from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill


DEFAULT_ABOUT = (
    "Je m'appelle Anzouan Gomis Thony Axel, étudiant en Licence 3 en Computer Science "
    "et passionné par le développement logiciel et les nouvelles technologies. "
    "Je m'intéresse particulièrement à la création d'applications web et mobiles modernes "
    "en utilisant des technologies comme Angular, Django, Python, Java et Flutter. "
    "Curieux et orienté innovation, je développe des projets mêlant full-stack, IA et systèmes "
    "intelligents afin de créer des solutions modernes, performantes et utiles."
)

DEFAULT_SKILLS = [
    "Angular",
    "Django REST Framework",
    "Java",
    "Python",
    "Flutter",
    "TypeScript",
    "HTML/CSS",
    "Git",
]


class Command(BaseCommand):
    help = "Crée un profil et des compétences par défaut pour le portfolio."

    def handle(self, *args, **options):
        if Profile.objects.exists():
            self.stdout.write(self.style.WARNING("Un profil existe déjà. Rien à faire."))
            return

        profile = Profile.objects.create(
            full_name="Anzouan Gomis Thony Axel",
            title="L3 Computer Science",
            email="anzouangomisthony@gmail.com",
            phone="+225 0170169013",
            about_me=DEFAULT_ABOUT,
            github_url="https://github.com/MrthonyG72",
            linkedin_url="https://www.linkedin.com/in/gomis-thony-axel-thierry-anzouan-787a122a4/",
        )
        self.stdout.write(self.style.SUCCESS(f"Profil créé: {profile.full_name}"))

        created = 0
        for i, name in enumerate(DEFAULT_SKILLS):
            _, c = Skill.objects.get_or_create(name=name, defaults={"order": i})
            if c:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Compétences: {created} créée(s)."))
        self.stdout.write("Pensez à mettre à jour GitHub, LinkedIn et CV dans l'admin Django.")
