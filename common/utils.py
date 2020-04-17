def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def last_ads_for_russia():
    from ad_posts.models import Ad
    from django.db.models import Q

    ads_query = Q(city__region__country__id=1, creator__is_blocked=False, is_deleted=False, is_active=True)
    ads = Ad.objects.filter(ads_query)
    return ads[:21]

def get_first_location(request, user):
    import json, requests
    from users.model.profile import OneUserLocation
    from users.model.profile import IPUser

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    olds_ip = IPUser.objects.create(user=user)
    response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + ip)
    data = response.json()
    loc = OneUserLocation.objects.create(user=user)
    sity = data['city']
    region = data['region']
    country = data['country']
    loc.city_ru = sity['name_ru']
    loc.city_en = sity['name_en']
    loc.city_lat = sity['lat']
    loc.city_lon = sity['lon']
    loc.region_ru = region['name_ru']
    loc.region_en = region['name_en']
    loc.country_ru = country['name_ru']
    loc.country_en = country['name_en']
    loc.phone = country['phone']
    olds_ip.ip_1 = ip
    olds_ip.save()
    loc.save()


def get_location(request):
    import json, requests

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        olds_ip = request.user.user_ip
    except:
        from users.model.profile import IPUser
        olds_ip = IPUser.objects.create(user=request.user)

    if not olds_ip.ip_1:
        response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + ip)
        data = response.json()
        try:
            loc = request.user.user_location
        except:
            from users.model.profile import OneUserLocation
            loc = OneUserLocation.objects.create(user=request.user)
        sity = data['city']
        region = data['region']
        country = data['country']
        loc.city_ru = sity['name_ru']
        loc.city_en = sity['name_en']
        loc.city_lat = sity['lat']
        loc.city_lon = sity['lon']
        loc.region_ru = region['name_ru']
        loc.region_en = region['name_en']
        loc.country_ru = country['name_ru']
        loc.country_en = country['name_en']
        loc.phone = country['phone']
        olds_ip.ip_1 = ip
        olds_ip.save()
        loc.save()
    elif not olds_ip.ip_2 and olds_ip.ip_3 != ip and olds_ip.ip_2 != ip and olds_ip.ip_1 != ip:
        response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + ip)
        data = response.json()
        try:
            loc = request.user.user_location_2
        except:
            from users.model.profile import TwoUserLocation
            loc = TwoUserLocation.objects.create(user=request.user)
        sity = data['city']
        region = data['region']
        country = data['country']
        loc.city_ru = sity['name_ru']
        loc.city_en = sity['name_en']
        loc.city_lat = sity['lat']
        loc.city_lon = sity['lon']
        loc.region_ru = region['name_ru']
        loc.region_en = region['name_en']
        loc.country_ru = country['name_ru']
        loc.country_en = country['name_en']
        loc.phone = country['phone']
        olds_ip.ip_2 = ip
        olds_ip.save()
        loc.save()
    elif not olds_ip.ip_3 and olds_ip.ip_3 != ip and olds_ip.ip_2 != ip and olds_ip.ip_1 != ip:
        response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + ip)
        data = response.json()
        try:
            loc = request.user.user_location_3
        except:
            from users.model.profile import ThreeUserLocation
            loc = ThreeUserLocation.objects.create(user=request.user)
        sity = data['city']
        region = data['region']
        country = data['country']
        loc.city_ru = sity['name_ru']
        loc.city_en = sity['name_en']
        loc.city_lat = sity['lat']
        loc.city_lon = sity['lon']
        loc.region_ru = region['name_ru']
        loc.region_en = region['name_en']
        loc.country_ru = country['name_ru']
        loc.country_en = country['name_en']
        loc.phone = country['phone']
        olds_ip.ip_3 = ip
        olds_ip.save()
        loc.save()
    elif olds_ip.ip_3 and olds_ip.ip_3 != ip and olds_ip.ip_2 != ip and olds_ip.ip_1 != ip:
        response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + ip)
        data = response.json()
        sity = data['city']
        region = data['region']
        country = data['country']
        loc.city_ru = sity['name_ru']
        loc.city_en = sity['name_en']
        loc.region_ru = region['name_ru']
        loc.region_en = region['name_en']
        loc.country_ru = country['name_ru']
        loc.country_en = country['name_en']
        loc.phone = country['phone']
        olds_ip.ip_1 = ip
        olds_ip.save()
        loc.save()

    else:
        pass

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
        elif request.user.is_blocked_with_user_with_id(user_id=self.pk):
            template_name = "main/you_are_block.html"
        elif request.user.is_deleted:
            template_name = "main/deleted_page.html"
        elif request.user.is_blocked:
            template_name = "main/blocked_page.html"
        else:
            template_name = folder + template
    elif request.user.is_anonymous:
        template_name = folder + "anon/" + template

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        template_name = "mob_" + template_name
        if request.user.is_authenticated:
            AdNumbers.objects.create(user=request.user.pk, ad=ad.pk, platform=1)
    else:
        if request.user.is_authenticated:
            AdNumbers.objects.create(user=request.user.pk, ad=ad.pk, platform=0)
    return template_name
