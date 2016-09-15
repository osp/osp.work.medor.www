from django.conf import settings


PER_ITEM_EUROPE_SHIPPING_COSTS = getattr(settings, 'PER_ITEM_EUROPE_SHIPPING_COSTS', {
    1: 8,   # One
    3: 12,  # Two or three
    6: 24,  # Four, five or six
    15: 30  # Seven to 15
})

SUBSCRIPTION_EUROPE_SHIPPING_COSTS = getattr(settings, 'SUBSCRIPTION_EUROPE_SHIPPING_COSTS', 20)
