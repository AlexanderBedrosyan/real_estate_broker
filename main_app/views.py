from django.shortcuts import render
from .models import PersonalInfo, AdvertisementInfo

# Create your views here.


def home(request):
    personal_info = PersonalInfo.objects.first()
    title = personal_info.title
    description = personal_info.description
    picture_path = personal_info.picture

    adv_info = AdvertisementInfo.objects.first()
    adv_title = adv_info.title
    adv_description = adv_info.description
    gif_path = adv_info.video

    context = {
        'title': title,
        'description': [text for text in description.split('\n')],
        'picture_path': picture_path,
        'adv_title': adv_title,
        'adv_description': [text for text in adv_description.split('\n')],
        'gif_path': gif_path
    }
    return render(request, 'home.html', context)