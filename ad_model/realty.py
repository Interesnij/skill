from django.db import models
from ad_posts.models import Ad


class Realty(Ad):
    TYPE = (('Вторичка', 'Вторичка'), ('Новостройка', 'Новостройка'))
    TYPE_HOUSE=(
        ('Панельный','Панельный'),
        ('Кирпичный','Кирпичный'),
        ('Монолит','Монолит'),
        ('Кирпично-монолитный','Кирпично-монолитный'),
        ('Блочный','Блочный'),
        ('Деревянный','Деревянный'),
    )
    TO_METRO=(
        ('До 5 мин. пешком','До 5 мин. пешком'),
        ('5-15 мин. пешком','5-15 мин. пешком'),
        ('Более 15 мин. пешком','Более 15 мин. пешком'),
        ('На транспорте','На транспорте'),
        ('Метро планируется','Метро планируется'),
        ('Нет метро','Нет метро'),
    )
    ELEVATORS=(
        ('Нет','Нет'),
        ('Легковой','Легковой'),
        ('Грузовой','Грузовой'),
        ('3 и более лифтов','3 и более лифтов'),
    )
    INFRASTRUCTURE=(
        ('Детская площадка','Детская площадка'),
        ('Школа','Школа'),
        ('Детский сад','Детский сад'),
        ('Поликлиника','Поликлиника'),
        ('Магазины','Магазины'),
        ('Спорт','Спорт'),
        ('Транспорт','Транспорт'),
        ('Кафе и рестораны','Кафе и рестораны'),
        ('Развлечения','Развлечения'),
        ('Парки и места для отдыха','Парки и места для отдыха'),
    )
    ROOMS=(
        ('1 комната','1 комната'),
        ('2 комнаты','2 комнаты'),
        ('3 комнаты','3 комнаты'),
        ('4 комнаты','4 комнаты'),
        ('5 и более комнат','5 и более комнат'),
        ('Свободная планировка','Свободная планировка'),
        ('Студия','Студия'),
    )
    REPAIR=(
        ('Требуется ремонт','Требуется ремонт'),
        ('Не требуется','Не требуется'),
        ('Косметический','Косметический'),
        ('Евроремонт','Евроремонт'),
        ('Дизайнерский','Дизайнерский'),
        ('Капитальный ремонт','Капитальный ремонт'),
    )
    BATHROOM_UNIT=(
        ('Совмещенный','Совмещенный'),
        ('Раздельный','Раздельный'),
        ('2 и более','2 и более'),
    )
    BALCONY=(
        ('Нет','Нет'),
        ('Балкон','Балкон'),
        ('Лоджия','Лоджия'),
        ('Несколько балконов','Несколько балконов'),
    )
    TENURE=(
        ('До 3-х лет','До 3-х лет'),
        ('От 3 до 5 лет','От 3 до 5 лет'),
        ('Более 5 лет','Более 5 лет'),
    )
    HOUSE=(
        ('Дом','Дом'),
        ('Таунхаус','Таунхаус'),
        ('Коттедж','Коттедж'),
        ('Дача','Дача'),
    )
    MATERIAL_HOUSE=(
        ('Кирпичный','Кирпичный'),
        ('Монолит','Монолит'),
        ('Блочный','Блочный'),
        ('Щитовой','Щитовой'),
        ('Деревянный','Деревянный'),
    )
    ELECTRO=(
        ('Нет','Нет'),
        ('Подключено','Подключено'),
    )
    HEATING=(
        ('Нет','Нет'),
        ('Автономное','Автономное'),
        ('Централизованное','Централизованное'),
    )
    GAS=(
        ('Нет','Нет'),
        ('По границе','По границе'),
        ('Подведен','Подведен'),
    )
    WATER_SUPPLY=(
        ('Нет','Нет'),
        ('Автономное','Автономное'),
        ('Централизованное','Централизованное'),
    )
    GARAGE=(
        ('Нет','Нет'),
        ('В доме','В доме'),
        ('Отдельно стоящий','Отдельно стоящий'),
    )
    PLOT=(
        ('Сельхоз (СНТ или ДНП)','Сельхоз (СНТ или ДНП)'),
        ('Фермерское хоз-во','Фермерское хоз-во'),
        ('Поселения (ИЖС)','Поселения (ИЖС)'),
        ('Земля промназначения','Земля промназначения'),
        ('Инвестпроект','Инвестпроект'),
    )
    PREPAYTMENT=(
        ('Без предоплаты','Без предоплаты'),
        ('1 месяц','1 месяц'),
        ('2 месяца','2 месяца'),
        ('3 месяца','3 месяца'),
        ('Больше 3 месяцев','Больше 3 месяцев'),
    )
    COMISSION=(
        ('Нет','Нет'),
        ('30%','30%'),
        ('50%','50%'),
        ('100%','100%'),
        ('Другая','Другая'),
    )
    TYPE_BUILD=(
        ('Помещение свободного назначения','Помещение свободного назначения'),
        ('Торговое помещение','Торговое помещение'),
        ('Офисное помещение','Офисное помещение'),
        ('Производство','Производство'),
        ('Склад','Склад'),
        ('Другое','Другое'),
    )
    TYPE_OTHER=(
        ('Баня','Баня'),
        ('Сарай','Сарай'),
        ('Бытовка','Бытовка'),
        ('Гараж','Гараж'),
        ('Машиноместо','Машиноместо'),
        ('Другое','Другое'),
    )
    PUBLIC_UTIL = (('Включены', 'Включены'), ('Не включены', 'Не включены'))
    TYPE_TRANS = (('Аренда', 'Аренда'), ('Продажа', 'Продажа'))

    type = models.CharField(max_length=50, blank=True, choices = TYPE, verbose_name="Тип")
    year = models.CharField(max_length=100, blank=True, verbose_name="Год постройки")
    type_house = models.CharField(max_length=50, blank=True, choices = TYPE_HOUSE, verbose_name="Тип дома")
    to_metro = models.CharField(max_length=50, blank=True, choices = TO_METRO, verbose_name="До метро")
    elevators = models.CharField(max_length=50, blank=True, choices = ELEVATORS, verbose_name="Лифты")
    infrastructure = models.CharField(max_length=50, blank=True, verbose_name="Инфраструктура")
    rooms = models.CharField(max_length=50, blank=True, choices = ROOMS, verbose_name="Комнат в квартире")
    level = models.CharField(max_length=100, blank=True, verbose_name="Этаж")
    levels = models.CharField(max_length=100, blank=True, verbose_name="Этажность")
    total_area = models.CharField(max_length=100, blank=True, verbose_name="Общая площадь")
    comn_area = models.CharField(max_length=100, blank=True, verbose_name="Площадь комнаты")
    living_area = models.CharField(max_length=100, blank=True, verbose_name="Жилая площадь")
    kitchen_area = models.CharField(max_length=100, blank=True, verbose_name="Площадь кухни")
    ceiling_height = models.CharField(max_length=100, blank=True, verbose_name="Высота потолка")
    repairs = models.CharField(max_length=50, blank=True, choices = REPAIR, verbose_name="Ремонт")
    bathroom_unit = models.CharField(max_length=50, blank=True, choices = BATHROOM_UNIT, verbose_name="Санузлы")
    balcony = models.CharField(max_length=50, blank=True, choices = BALCONY, verbose_name="Балкон")
    tenure = models.CharField(max_length=50, blank=True, choices = TENURE, verbose_name="Срок владения")
    house = models.CharField(max_length=50, blank=True, choices = HOUSE, verbose_name="Тип дома")
    material_house = models.CharField(max_length=50, blank=True, choices = MATERIAL_HOUSE, verbose_name="Материал дома")
    house_area = models.CharField(max_length=50, blank=True, verbose_name="Площадь дома")
    number_of_bedrooms = models.CharField(max_length=50, blank=True, verbose_name="Количество спален")
    electricity = models.CharField(max_length=50, blank=True, choices = ELECTRO, verbose_name="Электричество")
    heating = models.CharField(max_length=50, blank=True, choices = HEATING, verbose_name="Обогрев")
    gas = models.CharField(max_length=50, blank=True, choices = GAS, verbose_name="Газ")
    water_supply = models.CharField(max_length=50, blank=True, choices = WATER_SUPPLY, verbose_name="Водоснабжение")
    garage = models.CharField(max_length=50, blank=True, choices = WATER_SUPPLY, verbose_name="Гараж")
    plottage = models.CharField(max_length=50, blank=True, verbose_name="Площадь участка")
    type_plot = models.CharField(max_length=50, blank=True, choices = PLOT, verbose_name="Тип участка")
    refrigerator = models.BooleanField(default=False, verbose_name='Холодильник')
    dishwasher = models.BooleanField(default=False, verbose_name='Посудомоечная машина')
    washing_machine = models.BooleanField(default=False, verbose_name='Стиральная машина')
    prepaytment = models.CharField(max_length=50, blank=True, choices = PREPAYTMENT, verbose_name="Предоплата")
    public_utilities = models.CharField(max_length=50, blank=True, choices = PUBLIC_UTIL, verbose_name="Коммунальные услуги")
    comission = models.CharField(max_length=50, blank=True, choices = COMISSION, verbose_name="Комиссия")
    type_build = models.CharField(max_length=50, blank=True, choices = TYPE_BUILD, verbose_name="Тип строения")
    type_transaction = models.CharField(max_length=50, blank=True, choices = TYPE_TRANS, verbose_name="Тип сделки")
    type_other = models.CharField(max_length=50, blank=True, choices = TYPE_OTHER, verbose_name="Тип строения")
    auction = models.BooleanField(default=False, verbose_name='Торг возможен')

    class Meta:
        verbose_name = "Недвижимость"
        verbose_name_plural = "Недвижимость"
