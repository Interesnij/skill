from django.template import Library

register = Library()

@register.filter
def cat_region_count(cat, region_id):
    count = cat.get_course_in_region_count(region_id)
    return count

@register.filter
def cat_city_count(cat, city_id):
    count = cat.get_course_in_city_count(city_id)
    return count

@register.filter
def subcat_region_count(subcat, region_id):
    count = subcat.get_course_in_region_count(region_id)
    return count

@register.filter
def subcat_city_count(subcat, city_id):
    count = subcat.get_course_in_city_count(city_id)
    return count
