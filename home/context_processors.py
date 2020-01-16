from django.conf import settings
from django import template
from .models import BioCard

register = template.Library()

@register.inclusion_tag('bio_card.html')
def show_bio_cards(request):
    cards = BioCard.objects.all()
    context = {
        'cards' : cards,
    }

    return context