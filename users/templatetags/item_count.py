from django.template import Library

register = Library()

@register.filter
def sity_count(ad, sity):
    count = ad.get_sity_count(sity)
    return count

@register.filter
def u_sity_count(user, sity):
    count = user.get_sity_count(sity)
    return count
