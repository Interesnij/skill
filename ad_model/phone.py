from django.db import models
from ad_posts.models import Ad


class PhoneAd(Ad):
    BRANDS_PHONE=(
        ('iPhone','iPhone'),
        ('Samsung','Samsung'),
        ('Xiami','Xiami'),
        ('Nokia','Nokia'),
        ('ASUS','ASUS'),
        ('Acer','Acer'),
        ('Alcatel','Alcatel'),
        ('BQ','BQ'),
        ('BlackBerry','BlackBerry'),
        ('Dexp','Dexp'),
        ('Digma','Digma'),
        ('DNS','DNS'),
        ('Doogee','Doogee'),
        ('Explay','Explay'),
        ('Fly','Fly'),
        ('Nania','Nania'),
        ('Ginzzu','Ginzzu'),
        ('Google','GoogleGoogle'),
        ('Highscreen','Highscreen'),
        ('Homtom','Homtom'),
        ('HTC','HTC'),
        ('Jinga','Jinga'),
        ('LeEco','LeEco'),
        ('Lenovo','Lenovo'),
        ('LG','LG'),
        ('Meizu','Meizu'),
        ('Micromax','Micromax'),
        ('Microsoft','Microsoft'),
        ('Motorola','Motorola'),
        ('Philips','Philips'),
        ('Prestigio','Prestigio'),
        ('Siemens','Siemens'),
        ('Sony','Sony'),
        ('Texet','Texet'),
        ('Vertu','Vertu'),
        ('WileyFox','WileyFox'),
        ('ZTE','ZTE'),
        ('MTC','MTC'),
        ('Билайн','Билайн'),
        ('Мегафон','Мегафон'),
        ('ТЕЛЕ2','ТЕЛЕ2'),
        ('Другая','Другая'),
    )
    BRANDS_SPARE=(
        ('3Q','3Q'),
        ('4GOOD','4GOOD'),
        ('iPhone','iPhone'),
        ('Samsung','Samsung'),
        ('Xiami','Xiami'),
        ('Nokia','Nokia'),
        ('ASUS','ASUS'),
        ('Acer','Acer'),
        ('Archos','Archos'),
        ('Alcatel','Alcatel'),
        ('BQ','BQ'),
        ('BlackBerry','BlackBerry'),
        ('DELL','DELL'),
        ('Dexp','Dexp'),
        ('Digma','Digma'),
        ('DNS','DNS'),
        ('Doogee','Doogee'),
        ('Explay','Explay'),
        ('Fly','Fly'),
        ('Nania','Nania'),
        ('Ginzzu','Ginzzu'),
        ('Google','GoogleGoogle'),
        ('Highscreen','Highscreen'),
        ('Homtom','Homtom'),
        ('Huawei','Huawei'),
        ('HP','HP'),
        ('HTC','HTC'),
        ('Jinga','Jinga'),
        ('Irbis','Irbis'),
        ('LeEco','LeEco'),
        ('Lenovo','Lenovo'),
        ('LG','LG'),
        ('Meizu','Meizu'),
        ('Micromax','Micromax'),
        ('Microsoft','Microsoft'),
        ('Motorola','Motorola'),
        ('Nvidia','Nvidia'),
        ('Oysters','Oysters'),
        ('Philips','Philips'),
        ('PlayPad','PlayPad'),
        ('Prestigio','Prestigio'),
        ('Qumo','Qumo'),
        ('Siemens','Siemens'),
        ('Sony','Sony'),
        ('Supra','Supra'),
        ('Telefunken','Telefunken'),
        ('Vertex','Vertex'),
        ('Vertu','Vertu'),
        ('Texet','Texet'),
        ('Wexler','Wexler'),
        ('WileyFox','WileyFox'),
        ('ZTE','ZTE'),
        ('MTC','MTC'),
        ('Билайн','Билайн'),
        ('Мегафон','Мегафон'),
        ('ТЕЛЕ2','ТЕЛЕ2'),
        ('Другая','Другая'),
    )
    BRANDS_PADE=(
        ('Apple','Apple'),
        ('Samsung','Samsung'),
        ('ASUS','ASUS'),
        ('Archos','Archos'),
        ('Alcatel','Alcatel'),
        ('BQ','BQ'),
        ('Dell','Dell'),
        ('Dexp','Dexp'),
        ('Digma','Digma'),
        ('DNS','DNS'),
        ('Explay','Explay'),
        ('Fly','Fly'),
        ('Nania','Nania'),
        ('Ginzzu','Ginzzu'),
        ('Google','GoogleGoogle'),
        ('Haler','Haler'),
        ('Homtom','Homtom'),
        ('HTC','HTC'),
        ('HP','HP'),
        ('Huawei','Huawei'),
        ('Iconbit','Iconbit'),
        ('Irbis','Irbis'),
        ('Lenovo','Lenovo'),
        ('LG','LG'),
        ('Microsoft','Microsoft'),
        ('Nvidia','Nvidia'),
        ('Oysters','Oysters'),
        ('PlayPad','PlayPad'),
        ('Prestigio','Prestigio'),
        ('Qumo','Qumo'),
        ('Sony','Sony'),
        ('Supra','Supra'),
        ('Telefunken','Telefunken'),
        ('Texet','Texet'),
        ('Wexler','Wexler'),
        ('Xiami','Xiami'),
        ('ZTE','ZTE'),
        ('3Q','3Q'),
        ('MTC','MTC'),
        ('Билайн','Билайн'),
        ('Мегафон','Мегафон'),
        ('Другая','Другая'),
    )
    BRANDS_SMARTWATH=(
        ('Apple','Apple'),
        ('Samsung','Samsung'),
        ('ASUS','ASUS'),
        ('Alcatel','Alcatel'),
        ('Casio','Casio'),
        ('Fitbit','Fitbit'),
        ('Huawei','Huawei'),
        ('Jawbone','Iconbit'),
        ('LG','LG'),
        ('Motorola','Motorola'),
        ('Pebble','Pebble'),
        ('Polar','Polar'),
        ('Sony','Sony'),
        ('Suunto','Suunto'),
        ('Xiami','Xiami'),
        ('Другая','Другая'),
    )
    OS=(
        ('Android','Android'),
        ('IOS','IOS'),
        ('Windows','Windows'),
        ('Simbian','Simbian'),
        ('Bada','Bada'),
        ('Dlackberry OS','Dlackberry OS'),
        ('Linux','Linux'),
    )
    SCREEN=(
        ('4" и менее','4" и менее'),
        ('от 4.1" до 4.9"','от 4.1" до 4.9"'),
        ('от 5.0" до 5.4"','от 5.0" до 5.4"'),
        ('5.5" и более','5.5" и более'),
    )
    INTERNAL=(
        ('2 Гб и менее','2 Гб и менее'),
        ('4 Гб','4 Гб'),
        ('8 Гб','8 Гб'),
        ('16 Гб','16 Гб'),
        ('32 Гб','32 Гб'),
        ('64 Гб','64 Гб'),
        ('128 Гб','128 Гб'),
        ('256 Гб','256 Гб'),
        ('512 Гб','512 Гб'),
    )
    SLOT=(
        ('Есть','Есть'),
        ('Нет','Нет'),
    )
    CAMERA=(
        ('Нет камеры','Нет камеры'),
        ('Менее 2 Мпикс','Менее 2 Мпикс'),
        ('от 2 до 4.9 Мпикс','от 2 до 4.9 Мпикс'),
        ('от 5 до 9.9 Мпикс','от 5 до 9.9 Мпикс'),
        ('10 Мпикс и более','10 Мпикс и более'),
    )
    FRONT=(
        ('Нет камеры','Нет камеры'),
        ('Менее 1 Мпикс','Менее 1 Мпикс'),
        ('от 1 до 2.9 Мпикс','от 1 до 2.9 Мпикс'),
        ('от 3 до 4.9 Мпикс','от 3 до 4.9 Мпикс'),
        ('5 Мпикс и более','5 Мпикс и более'),
    )
    SIM=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('Более 4','Более 4'),
    )
    USE=(
        ('Новый','Новый'),
        ('До 6 мес','До 6 мес'),
        ('1 год','1 год'),
        ('2 года','2 года'),
        ('от 3 лет и более','от 3 лет и более'),
    )

    OS_PAD=(
        ('Android','Android'),
        ('IOS','IOS'),
        ('Windows','Windows'),
    )
    SCREEN_PAD=(
        ('7" и менее','7" и менее'),
        ('от 7" до 7.9"','от 7" до 7.9"'),
        ('от 8" до 8.9"','от 8" до 8.9"'),
        ('от 9" до 9.9"','от 9" до 9.9"'),
        ('от 10" до 11.9"','от 10" до 11.9"'),
        ('12" и более','12" и более'),
    )
    INTERNAL_PAD=(
        ('2 Гб и менее','2 Гб и менее'),
        ('4 Гб','4 Гб'),
        ('8 Гб','8 Гб'),
        ('16 Гб','16 Гб'),
        ('32 Гб и более','32 Гб и более'),
    )
    OPERATIVE=(
        ('512 Mб и менее','512 Mб и менее'),
        ('1 Гб','1 Гб'),
        ('1.5 Гб','1.5 Гб'),
        ('2 Гб','2 Гб'),
        ('3 Гб','3 Гб'),
        ('4 Гб','4 Гб'),
        ('8 Гб и более','8 Гб и более'),
    )
    OPERATIVE_PAD=(
        ('128 Mб','128 Mб'),
        ('256 Mб','256 Mб'),
        ('512 Mб','512 Mб'),
        ('1 Гб','1 Гб'),
        ('1.5 Гб','1 Гб'),
        ('3 Гб','2 Гб'),
        ('4 Гб','4 Гб'),
        ('8 Гб и более','8 Гб и более'),
    )
    TYPE_SMARTWATH=(
        ('Умные часы','Умные часы'),
        ('Фитнесс-браслеты','Фитнесс-браслеты'),
        ('Ремешки, аксессуары','Ремешки, аксессуары'),
    )
    CALL=(
        ('С помощью телефона/планшета','С помощью телефона/планшета'),
        ('Собственная SIM-карта','Собственная SIM-карта'),
    )
    PHONE=(
        ('Проводные телефоны','Проводные телефоны'),
        ('Радиотелефоны','Радиотелефоны'),
    )
    RADIOS=(
        ('Аналоговые рации','Аналоговые рации'),
        ('Цифровые рации','Цифровые рации'),
        ('Спутниковые телефоны','Спутниковые телефоны'),
    )
    SPARE=(
        ('Аккумуляторы, батареи','Аккумуляторы, батареи'),
        ('Антенны','Антенны'),
        ('Вибромоторы','Вибромоторы'),
        ('Держатели SIM-карт','Держатели SIM-карт'),
        ('Джойстики','Джойстики'),
        ('Динамики','Динамики'),
        ('Дисплеи, тачскрины','Дисплеи, тачскрины'),
        ('Задние крышки','Задние крышки'),
        ('Инструменты для ремонта','Инструменты для ремонта'),
        ('Камеры','Камеры'),
        ('Клавиатуры','Клавиатуры'),
        ('Кнопки','Кнопки'),
        ('Корпусы','Корпусы'),
        ('Крышки аккумуляторов','Крышки аккумуляторов'),
        ('Микросхемы, платы','Микросхемы, платы'),
        ('Микрофоны','Микрофоны'),
        ('Панели','Панели'),
        ('Разъемы','Разъемы'),
        ('Шлейфы','Шлейфы'),
    )
    DEVICE=(
        ('Для смартфонов','Для смартфонов'),
        ('Для планшетов','Для планшетов'),
        ('Для телефонов','Для телефонов'),
    )
    BATTERY=(
        ('До 3000 мАч','До 3000 мАч'),
        ('От 3000 до 4990 мАч','От 3000 до 4990 мАч'),
        ('От 5000 до 9990 мАч','От 5000 до 9990 мАч'),
        ('От 10000 до 14990 мАч','От 10000 до 14990 мАч'),
        ('От 15000 до 19990 мАч','От 15000 до 19990 мАч'),
        ('От 20000 мАч и более','От 20000 мАч и более'),
    )
    CHARGER_TYPE=(
        ('Автомобильные','Автомобильные'),
        ('Адаптеры в розетку','Адаптеры в розетку'),
        ('Беспроводные','Беспроводные'),
        ('Док-станции','Док-станции'),
    )
    ACSESSUARE=(
        ('Проводные гарнитуры','Проводные гарнитуры'),
        ('Bluetooth-гарнитуры','Bluetooth-гарнитуры'),
        ('Моноподы, палки для селфи','Моноподы, палки для селфи'),
        ('Защитные пленки, стекла','Защитные пленки, стекла'),
        ('Наклейки, стикеры','Наклейки, стикеры'),
        ('Кабели, переходники','Динамики'),
        ('Очки виртуальной реальности','Очки виртуальной реальности'),
        ('Стилусы','Стилусы'),
        ('Объективы','Объективы'),
        ('Вспышки, селфи кольца','Вспышки, селфи кольца'),
        ('Держатели, коврики','Держатели, коврики'),
        ('Коробка от телефона','Коробка от телефона'),
        ('Клавиатуры','Клавиатуры'),
        ('Геймпады','Геймпады'),
    )

    brand_phone = models.CharField(max_length=50, blank=True, choices = BRANDS_PHONE, verbose_name="Марка телефона")
    os = models.CharField(max_length=50, blank=True, choices = OS, verbose_name="Операционная система")
    screen = models.CharField(max_length=50, blank=True, choices = SCREEN, verbose_name="Диагональ экрана")
    internal = models.CharField(max_length=50, blank=True, choices = INTERNAL, verbose_name="Встроенная память")
    slot = models.CharField(max_length=50, blank=True, choices = SLOT, verbose_name="Слот для карты памяти")
    camera = models.CharField(max_length=50, blank=True, choices = CAMERA, verbose_name="Основная камера")
    front = models.CharField(max_length=50, blank=True, choices = FRONT, verbose_name="Фронтальная камера")
    a3G = models.BooleanField(default=False, verbose_name='3G')
    LTE = models.BooleanField(default=False, verbose_name='4G')
    sim = models.CharField(max_length=50, blank=True, choices = SIM, verbose_name="Количество SIM-карт")
    GPS = models.BooleanField(default=False, verbose_name='GPS')
    NFC = models.BooleanField(default=False, verbose_name='NFC')
    IP = models.BooleanField(default=False, verbose_name='Защита от пыли и влаги')
    use = models.CharField(max_length=50, blank=True, choices = USE, verbose_name="Срок использования")
    brand_pad = models.CharField(max_length=50, blank=True, choices = BRANDS_PADE, verbose_name="Марка планшета")
    os_pad = models.CharField(max_length=50, blank=True, choices = OS_PAD, verbose_name="Операционная система")
    screen_pad = models.CharField(max_length=50, blank=True, choices = SCREEN_PAD, verbose_name="Диагональ экрана")
    internal_pad = models.CharField(max_length=50, blank=True, choices = INTERNAL_PAD, verbose_name="Встроенная память")
    operative = models.CharField(max_length=50, blank=True, choices = OPERATIVE, verbose_name="Оперативная память")
    operative_pad = models.CharField(max_length=50, blank=True, choices = OPERATIVE_PAD, verbose_name="Оперативная память")
    brand_wath = models.CharField(max_length=50, blank=True, choices = BRANDS_SMARTWATH, verbose_name="Бренд")
    type_wath = models.CharField(max_length=50, blank=True, choices = TYPE_SMARTWATH, verbose_name="Тип")
    android = models.BooleanField(default=False, verbose_name='Совместимость с Android')
    IOS = models.BooleanField(default=False, verbose_name='Совместимость с iOS')
    protection = models.BooleanField(default=False, verbose_name='Влагозащита')
    pedometer = models.BooleanField(default=False, verbose_name='Шагомер')
    heart_monitor = models.BooleanField(default=False, verbose_name='Пульсометр')
    sleep = models.BooleanField(default=False, verbose_name='Мониторинг сна')
    call = models.CharField(max_length=50, blank=True, choices = CALL, verbose_name="Телефонные звонки")
    phone = models.CharField(max_length=50, blank=True, choices = PHONE, verbose_name="Тип")
    answering = models.BooleanField(default=False, verbose_name='Автоответчик')
    AON = models.BooleanField(default=False, verbose_name='АОН')
    radios = models.CharField(max_length=50, blank=True, choices = RADIOS, verbose_name="Рации и спутниковые телефоны")
    spare = models.CharField(max_length=50, blank=True, choices = SPARE, verbose_name="Запчасти")
    device = models.CharField(max_length=50, blank=True, choices = DEVICE, verbose_name="Устройство")
    brand_spare = models.CharField(max_length=50, blank=True, choices = BRANDS_SPARE, verbose_name="Бренд запчасти")
    battery = models.CharField(max_length=50, blank=True, choices = BATTERY, verbose_name="Емкость батареи")
    charger_type = models.CharField(max_length=50, blank=True, choices = CHARGER_TYPE, verbose_name="Тип зарядного устройства")
    acsessuare = models.CharField(max_length=50, blank=True, choices = ACSESSUARE, verbose_name="Тип аксессуара")

    class Meta:
        verbose_name = "Телефоны и планшеты"
        verbose_name_plural = "Телефоны и планшеты"
