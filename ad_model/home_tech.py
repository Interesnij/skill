from django.db import models
from ad_posts.models import Ad


class HomeTech(Ad):
    TYPE_SCALE=(
        ('Механические','Механические'),
        ('Электронные','Электронные'),
    )
    APPLIC=(
        ('Напольные','Напольные'),
        ('Кухонные','Кухонные'),
    )
    TYPE_VIT=(
        ('Вытяжки','Вытяжки'),
        ('Фильтры для вытяжек','Фильтры для вытяжек'),
    )
    BRANDS_VIT=(
        ('Bosch','Bosch'),
        ('Elica','Elica'),
        ('Elikor','Elikor'),
        ('Falmec','Falmec'),
        ('Gorenje','Gorenje'),
        ('Hansa','Hansa'),
        ('Jetair','Jetair'),
        ('Korting','Korting'),
        ('Kronasteel','Kronasteel'),
        ('Kuppersberg','Kuppersberg'),
        ('Maunfeld','Maunfeld'),
        ('Panasonic','Panasonic'),
        ('Pentax','Pentax'),
        ('Pixel','Pixel'),
        ("Sigma","Sigma"),
        ('Sony','Sony'),
        ('Zigmund & Shtain','Zigmund & Shtain'),
    )
    TYPE_MIX=(
        ('Блендеры, измельчители','Блендеры, измельчители'),
        ('Кухонные комбайны','Кухонные комбайны'),
        ('Ломтерезки','Ломтерезки'),
        ('Миксеры','Миксеры'),
        ('Мясорубки','Мясорубки'),
    )
    TYPE_CLIMAT=(
        ('Вентиляторы','Вентиляторы'),
        ('Ионизаторы','Ионизаторы'),
        ('Метеостанции, термометры','Метеостанции, термометры'),
        ('Мобильные кондиционеры','Мобильные кондиционеры'),
        ('Настенные кондиционеры','Настенные кондиционеры'),
        ('Обогревающие приборы','Обогревающие приборы'),
        ('Очистители, увлажнители воздуха','Очистители, увлажнители воздуха'),
    )
    TYPE_FILTR=(
        ('Кулеры','Кулеры'),
        ('Фильтры','Фильтры'),
    )
    TYPE_STOVES=(
        ('Плиты','Плиты'),
        ('Варочные панели','Варочные панели'),
        ('Духовые шкафы','Духовые шкафы'),
    )
    TYPE_BURNERS=(
        ('Газовые','Газовые'),
        ('Индукционные','Индукционные'),
        ('Электрические','Электрические'),
    )
    SECURITY=(
        ('Автовыключение','Автовыключение'),
        ('Защита от детей','Защита от детей'),
        ('Защита от перегрева','Защита от перегрева'),
    )
    TYPE_WOSH=(
        ('Полноразмерные','Полноразмерные'),
        ('Компактные, настольные','Компактные, настольные'),
        ('Узкие','Узкие'),
    )
    TYPE_INSTALL=(
        ('Отдельно стоящие','Отдельно стоящие'),
        ('Встраиваемые','Встраиваемые'),
    )
    BRANDS_WOSH=(
        ('AEG','AEG'),
        ('Beco','Beco'),
        ('Bosch','Bosch'),
        ('Candy','Candy'),
        ('Electrolux','Electrolux'),
        ('Gorenje','Gorenje'),
        ('Hansa','Hansa'),
        ('Hotpoint-Ariston','Hotpoint-Ariston'),
        ('Indesit','Indesit'),
        ('Samsung','Samsung'),
        ('Siemens','Siemens'),
        ('Whirlpool','Whirlpool'),
        ('Zanussi','Zanussi'),
    )
    CAP_WOSH=(
        ('12 и более комплектов','12 и более комплектов'),
        ('9-11 комплектов','9-11 комплектов'),
        ('До 6 комплектов','До 6 комплектов'),
    )
    USE=(
        ('Новый','Новый'),
        ('До 6 мес','До 6 мес'),
        ('1 год','1 год'),
        ('2 года','2 года'),
        ('от 3 лет и более','от 3 лет и более'),
    )
    TYPE_FOOD=(
        ('Аэрогрили','Аэрогрили'),
        ('Блинницы','Блинницы'),
        ('йогуртницы','йогуртницы'),
        ('Микроволновые печи','Микроволновые печи'),
        ('Мини-печи, ростеры','Мини-печи, ростеры'),
        ('Мороженицы','Мороженицы'),
        ('Мультиварки','Мультиварки'),
        ('Пароварки','Пароварки'),
        ('Сушилки для овощей, фруктов','Сушилки для овощей, фруктов'),
        ('Сендвичницы, вафельницы','Сендвичницы, вафельницы'),
        ('Тостеры','Тостеры'),
        ('Фритюрницы','Фритюрницы'),
        ('Хлебопечки','Хлебопечки'),
        ('Электрогрили, шашлычницы','Электрогрили, шашлычницы'),
    )
    TYPE_DRINKS=(
        ('Электрочайники, термопоты','Электрочайники, термопоты'),
        ('Соковыжималки','Соковыжималки'),
        ('Кофеварки, кофемашины','Кофеварки, кофемашины'),
        ('Кофемолки','Кофемолки'),
    )
    TYPE_CLEANERS=(
        ('Паровые швабры','Паровые швабры'),
        ('Пароочистители','Пароочистители'),
        ('Пылесосы','Пылесосы'),
        ('Роботы-пылесосы','Роботы-пылесосы'),
    )
    TYPE_CLEANING=(
        ('Сухая','Сухая'),
        ('Влажная','Влажная'),
        ('Сухая и влажная','Сухая и влажная'),
    )
    BRANDS_CLEAN=(
        ('Bosch','Bosch'),
        ('Dyson','Dyson'),
        ('iRobot','iRobot'),
        ('Karcher','Karcher'),
        ('LG','LG'),
        ('Philips','Philips'),
        ('Polaris','Polaris'),
        ('Samsung','Samsung'),
        ('Scarlett','Scarlett'),
        ('Supra','Supra'),
        ('Thomas','Thomas'),
        ('Zelmer','Zelmer'),
    )
    TYPE_WASHING=(
        ('Отдельно стоящие','Отдельно стоящие'),
        ('Встраиваемые','Встраиваемые'),
    )
    BRANDS_WASHING=(
        ('Ardo','Ardo'),
        ('Beco','Beco'),
        ('Bosch','Bosch'),
        ('Candy','Candy'),
        ('Dewoo','Dewoo'),
        ('Electrolux','Electrolux'),
        ('Gorenje','Gorenje'),
        ('Hansa','Hansa'),
        ('Hotpoint-Ariston','Hotpoint-Ariston'),
        ('Indesit','Indesit'),
        ('LG','LG'),
        ('Samsung','Samsung'),
        ('Siemens','Siemens'),
        ('Vestel','Vestel'),
        ('Whirlpool','Whirlpool'),
        ('Zanussi','Zanussi'),
        ('Другая','Другая'),
    )
    LOAD_WASHING=(
        ('До 4 кг','До 4 кг'),
        ('До 5 кг','До 5 кг'),
        ('До 6 кг','До 6 кг'),
        ('До 7 кг','До 7 кг'),
        ('От 7 кг','От 7 кг'),
    )
    SPIN_SPEED=(
        ('700-800 об/мин','700-800 об/мин'),
        ('800-900 об/мин','800-900 об/мин'),
        ('900-1100 об/мин','900-1100 об/мин'),
        ('1100-1200 об/мин','1100-1200 об/мин'),
        ('до 700 об/мин','до 700 об/мин'),
        ('от 1200 об/мин','от 1200 об/мин'),
    )
    TYPE_IRON=(
        ('Утюги','Утюги'),
        ('Отпариватели','Отпариватели'),
        ('Гладильные доски','Гладильные доски'),
        ('Сушилки для белья','Сушилки для белья'),
        ('Сушилки для обуви','Сушилки для обуви'),
    )
    TYPE_REFR=(
        ('Холодильники','Холодильники'),
        ('Морозильники','Морозильники'),
    )
    BRANDS_REFR=(
        ('AEG','AEG'),
        ('Atlant','Atlant'),
        ('Beco','Beco'),
        ('Bosch','Bosch'),
        ('Dewoo','Dewoo'),
        ('Electrolux','Electrolux'),
        ('Gorenje','Gorenje'),
        ('Hotpoint-Ariston','Hotpoint-Ariston'),
        ('Indesit','Indesit'),
        ('LG','LG'),
        ('Liebherr','Liebherr'),
        ('Pozis','Pozis'),
        ('Samsung','Samsung'),
        ('Sharp','Sharp'),
        ('Siemens','Siemens'),
        ('Stinol','Stinol'),
        ('Whirlpool','Whirlpool'),
        ('Бирюса','Бирюса'),
        ('Минск','Минск'),
        ('Саратов','Саратов'),
        ('Другая','Другая'),
    )
    HEIGTH_REFR=(
        ('50-130 см','50-130 см'),
        ('130-150 см','130-150 см'),
        ('150-170 см','150-170 см'),
        ('180-215 см','180-215 см'),
    )
    TYPE_SEWING=(
        ('Вышивальные машины','Вышивальные машины'),
        ('Вязальные машины','Вязальные машины'),
        ('Оверлоки','Оверлоки'),
        ('Швейные машины','Швейные машины'),
        ('Аксессуары и запчасти','Аксессуары и запчасти'),
    )
    BRANDS_SEWING=(
        ('AstraLux','AEG'),
        ('Bernina','Atlant'),
        ('Brother','Beco'),
        ('Elna','Bosch'),
        ('Jaguar','Dewoo'),
        ('Janome','Electrolux'),
        ('Juki','Gorenje'),
        ('Merrylock','Hotpoint-Ariston'),
        ('Singer','Indesit'),
        ('Toyota','LG'),
        ('Тула','Liebherr'),
        ('Чайка','Pozis'),
    )

    type_scale = models.CharField(max_length=50, blank=True, choices = TYPE_SCALE, verbose_name="Тип весов")
    applic = models.CharField(max_length=50, blank=True, choices = APPLIC, verbose_name="Область применения")
    type_vit = models.CharField(max_length=50, blank=True, choices = TYPE_VIT, verbose_name="Тип вытяжки")
    brand_vit = models.CharField(max_length=50, blank=True, choices = BRANDS_VIT, verbose_name="Марка вытяжки")
    type_mix = models.CharField(max_length=50, blank=True, choices = TYPE_MIX, verbose_name="Тип")
    type_climat = models.CharField(max_length=50, blank=True, choices = TYPE_CLIMAT, verbose_name="Тип")
    type_filtr = models.CharField(max_length=50, blank=True, choices = TYPE_FILTR, verbose_name="Тип")
    type_stoves = models.CharField(max_length=50, blank=True, choices = TYPE_STOVES, verbose_name="Плиты и духовые шкафы")
    type_burners = models.CharField(max_length=50, blank=True, choices = TYPE_BURNERS, verbose_name="Тип конфорок")
    security = models.CharField(max_length=50, blank=True, choices = SECURITY, verbose_name="Безопасность")
    timer = models.BooleanField(default=False, verbose_name='Таймер')
    type_wosh = models.CharField(max_length=50, blank=True, choices = TYPE_WOSH, verbose_name="Тип посудомоечной машины")
    type_install = models.CharField(max_length=50, blank=True, choices = TYPE_INSTALL, verbose_name="Тип установки")
    brand_wosh = models.CharField(max_length=50, blank=True, choices = BRANDS_WOSH, verbose_name="Марка посудомоечной машины")
    cap_wosh = models.CharField(max_length=50, blank=True, choices = CAP_WOSH, verbose_name="Вместимость посуды")
    protect = models.BooleanField(default=False, verbose_name='Защита от протечек')
    do_start = models.BooleanField(default=False, verbose_name='Отсрочка запуска')
    use = models.CharField(max_length=50, blank=True, choices = USE, verbose_name="Срок использования")
    type_food = models.CharField(max_length=50, blank=True, choices = TYPE_FOOD, verbose_name="Приготовление еды")
    type_drinks = models.CharField(max_length=50, blank=True, choices = TYPE_DRINKS, verbose_name="Приготовление напитков")
    type_cleaners = models.CharField(max_length=50, blank=True, choices = TYPE_CLEANERS, verbose_name="Пылесосы и пароочистители")
    type_cleaning = models.CharField(max_length=50, blank=True, choices = TYPE_CLEANING, verbose_name="Тип уборки")
    brand_clean = models.CharField(max_length=50, blank=True, choices = BRANDS_CLEAN, verbose_name="Марка")
    brand_washing = models.CharField(max_length=50, blank=True, choices = BRANDS_WASHING, verbose_name="Марка")
    type_washing = models.CharField(max_length=50, blank=True, choices = TYPE_WASHING, verbose_name="Тип")
    load_washing = models.CharField(max_length=50, blank=True, choices = LOAD_WASHING, verbose_name="Загрузка, кг")
    dryer = models.BooleanField(default=False, verbose_name='Сушка')
    spin_speed = models.CharField(max_length=50, blank=True, choices = SPIN_SPEED, verbose_name="Скорость отжима")
    type_iron = models.CharField(max_length=50, blank=True, choices = TYPE_IRON, verbose_name="Тип")
    type_refr = models.CharField(max_length=50, blank=True, choices = TYPE_REFR, verbose_name="Тип холодильника")
    brand_refr = models.CharField(max_length=50, blank=True, choices = BRANDS_REFR, verbose_name="Марка холодильника")
    height_refr = models.CharField(max_length=50, blank=True, choices = HEIGTH_REFR, verbose_name="Высота")
    type_sewing = models.CharField(max_length=50, blank=True, choices = TYPE_SEWING, verbose_name="Тип")
    brand_sewing = models.CharField(max_length=50, blank=True, choices = BRANDS_SEWING, verbose_name="Марка")

    class Meta:
        verbose_name = "Бытовая техника"
        verbose_name_plural = "Бытовая техника"
