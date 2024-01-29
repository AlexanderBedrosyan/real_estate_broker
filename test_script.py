import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "real_estate_broker.settings")
django.setup()

# Import your models
from main_app.models import PersonalInfo


def get_personal_info():
    personal_info = PersonalInfo.objects.first()
    for curr in personal_info.description.split("\n"):
        print(curr)
        break

get_personal_info()