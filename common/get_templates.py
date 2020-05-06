def get_template_ad_detail(ad, folder, template, request):
    import re
    from stst.models import AdNumbers

    cat_pk = str(ad.category.category.pk)
    template = cat_pk + template
    if ad.creator.pk == request.user.pk:
        if not request.user.is_phone_verified:
            template_name = "main/phone_verification.html"
        else:
            template_name = folder + "my/" + template
    elif request.user.pk != ad.creator.pk and request.user.is_authenticated:
        if not request.user.is_phone_verified:
            template_name = "main/phone_verification.html"
        elif request.user.is_blocked_with_user_with_id(user_id=ad.creator.pk):
            template_name = "generic/you_are_block.html"
        elif request.user.is_deleted:
            template_name = "generic/deleted_page.html"
        elif request.user.is_blocked:
            template_name = "generic/blocked_page.html"
        else:
            template_name = folder + template
    elif request.user.is_anonymous:
        template_name = folder + "anon/" + template

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        template_name = "mob_" + template_name
        if request.user.is_authenticated and ad.creator.pk != request.user.pk:
            AdNumbers.objects.create(user=request.user.pk, ad=ad.pk, platform=1)
    else:
        if request.user.is_authenticated and ad.creator.pk != request.user.pk:
            AdNumbers.objects.create(user=request.user.pk, ad=ad.pk, platform=0)
    return template_name
