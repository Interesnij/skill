from django import template
register=template.Library()


@register.filter
def is_ad_favorite(user, ad_id):
    if user.is_ad_in_favorite(ad_id):
        return True
    else:
        return False

@register.filter
def is_course_favorite(user, course_id):
    if user.is_course_in_favorite(course_id):
        return True
    else:
        return False

@register.filter
def is_anketa_favorite(user, anketa_id):
    if user.is_anketa_in_favorite(anketa_id):
        return True
    else:
        return False

@register.filter
def is_user_blocked(user, anketa_id):
    if user.is_anketa_in_favorite(anketa_id):
        return True
    else:
        return False
