from django.template import Library

register = Library()

@register.filter
def cat_region_count(cat, region):
    count = cat.get_ads_in_region_count(region)
    return count

@register.filter
def cat_sity_count(cat, sity):
    count = cat.get_ads_in_city_count(sity)
    return count

@register.filter
def subcat_region_count(subcat, region):
    count = subcat.get_ads_in_region_count(region)
    return count

@register.filter
def subcat_sity_count(subcat, sity):
    count = subcat.get_ads_in_city_count(sity)
    return count
