from django.db import models
from ad_posts.models import Ad


class Baby(Ad):

    BRANDS_CAR_SEAT=(
        ('Baby Care','Baby Care'),
        ('Bertoni Lorelli','Bertoni Lorelli'),
        ('Bebe Comfort','Bebe Comfort'),
        ('BRITAX ROMER','BRITAX ROMER'),
        ('Carmate','Carmate'),
        ('Chicco','Chicco'),
        ('Crocs','Crocs'),
        ('Coto Baby','Coto Baby'),
        ('Cybex','Cybex'),
        ('Graco','Graco'),
        ('Happy Baby','Happy Baby'),
        ('Inglesina','Inglesina'),
        ('Kenga','Kenga'),
        ('Lider Kids','Lider Kids'),
        ('Maxi-Cosi','Maxi-Cosi'),
        ('Nania','Nania'),
        ('Peg-Perego','Peg-Perego'),
        ('Recaro','Recaro'),
        ('Siger','Siger'),
        ('Рант','Рант'),
        ('Мишутка','Мишутка'),
    )
    GROUP=(
        ('0 (до 10кг)','0 (до 10кг)'),
        ('0+ (до 13кг)','0+ (до 13кг)'),
        ('0/1 (до 18кг)','0/1 (до 18кг)'),
        ('0/1/2 (до 25кг)','0/1/2 (до 25кг)'),
        ('0/1/2/3 (до 36кг)','0/1/2/3 (до 36кг)'),
        ('1 (9-18 кг)','1 (9-18 кг)'),
        ('1/2 (9-25 кг)','1/2 (9-25 кг)'),
        ('1/2/3 (9-36 кг)','1/2/3 (9-36 кг) Baby'),
        ('2/3 (15-36 кг)','2/3 (15-36 кг)'),
        ('3 (22-26 кг)','3 (22-26 кг)'),
    )
    BINDING=(
        ('Isofix','Isofix'),
        ('Latch','Latch'),
        ('Автомобильные ремни','Автомобильные ремни'),
    )
    FEATURE=(
        ('Ручка для переноски','Ручка для переноски'),
        ('Поворотный механизм','Поворотный механизм'),
        ('Автоматическое натяжение ремня','Автоматическое натяжение ремня'),
        ('Фиксатор натяжения ремня','Фиксатор натяжения ремня'),
        ('Система упора в пол','Система упора в пол'),
        ('Пятиточечные ремни','Пятиточечные ремни'),
        ('Съемная обивка','Съемная обивка'),
    )
    REGULATION=(
        ('Боковина','Боковина'),
        ('Ручка','Ручка'),
        ('Спинка','Спинка'),
        ('Подголовник','Подголовник'),
        ('Положение для сна','Положение для сна'),
    )
    HEALTH=(
        ('Гигиена полости рта','Гигиена полости рта'),
        ('Детские весы','Детские весы'),
        ('Кремы, присыпки','Кремы, присыпки'),
        ('Назальные аспираторы','Назальные аспираторы'),
        ('Прорезыватели','Прорезыватели'),
        ('Термометры','Термометры'),
    )
    GAME=(
        ('Воздушные змеи','Baby Care'),
        ('Детские бассейны','Bertoni Lorelli'),
        ('Детские батуты','Bebe Comfort'),
        ('Железные дороги','BRITAX ROMER'),
        ('Играем в профессии','Carmate'),
        ('Игровые домики, палатки','Chicco'),
        ('Игровые комплексы, горки','Crocs'),
        ('Игрушечное оружие','Coto Baby'),
        ('Игрушки для ванной','Cybex'),
        ('Каталки, качалки','Graco'),
        ('Квадрокоптеры','Happy Baby'),
        ('Конструкторы','Inglesina'),
        ('Куклы','Kenga'),
        ('Машинки, техника','Lider Kids'),
        ('Мобили в кроватку','Maxi-Cosi'),
        ('Музыкальные игрушки','Nania'),
        ('Мыльные пузыри','Peg-Perego'),
        ('Мягкие игрушки','Recaro'),
        ('Напольные коврики','Siger'),
        ('Обучающие игрушки','Рант'),
        ('Пазлы','Мишутка'),
        ('Песочницы и игрушки','Maxi-Cosi'),
        ('Погремушки','Nania'),
        ('Роботы','Peg-Perego'),
        ('Сборные модели','Recaro'),
        ('Фигурки, солдатики','Siger'),
        ('Электромобили','Рант'),
    )
    BRANDS_PRAM=(
        ('Adamex','Adamex'),
        ('Anex','Anex'),
        ('Aprica','Aprica'),
        ('Baby Care','Baby Care'),
        ('Babyhit','Babyhit'),
        ('Baby Design','Baby Design'),
        ('Baby-Merc','Baby-Merc'),
        ('Babetto','Babetto'),
        ('BeBe-Mobile','BeBe-Mobile'),
        ('Bertoni Lorelli','Bertoni Lorelli'),
        ('Camarelo','Camarelo'),
        ('Capella','Capella'),
        ('Chicco','Chicco'),
        ('Cosatto','Cosatto'),
        ('Emmaljunga','Emmaljunga'),
        ('Esspero','Esspero'),
        ('FD Design','FD Design'),
        ('FoppaPedretti','FoppaPedretti'),
        ('Geaby','Geaby'),
        ('Happi Baby','Happi Baby'),
        ('Hauck','Hauck'),
        ('Inglesina','Inglesina'),
        ('Indigo','Indigo'),
        ('Jane','Jane'),
        ('Jedo','Jedo'),
        ('Jetem','Jetem'),
        ('Lonex','Lonex'),
        ('Maclarem','Maclarem'),
        ('Marimex','Marimex'),
        ('Maxima','Maxima'),
        ('Navington','Navington'),
        ('Noordline','Noordline'),
        ('Peg-Perego','Peg-Perego'),
        ('Phil&Teds','Phil&Teds'),
        ('Reindeer','Reindeer'),
        ('ROAN','ROAN'),
        ('Rico','Rico'),
        ('Silver Cross','Silver Cross'),
        ('Slaro','Slaro'),
        ('Tutis','Tutis'),
        ('Teutonia','Teutonia'),
        ('Tutic','Tutic'),
        ('Tutec','Tutec'),
        ('Мишутка','Мишутка'),
    )
    TYPE_PRAM=(
        ('Люлька','Люлька'),
        ('Прогулочная','Прогулочная'),
        ('Трансформер','Трансформер'),
        ('Универсальная','Универсальная'),
    )
    AGE_PRAM=(
        ('До 1 года','До 1 года'),
        ('До 2 лет','До 2 лет'),
        ('До 3 лет','До 3 лет'),
        ('До 4 лет','До 4 лет'),
        ('До 5 лет','До 5 лет'),
    )
    NUMBER_BLOCKS=(
        ('Для одного','Для одного'),
        ('Для двойни','Для двойни'),
        ('Для тройни','Для тройни'),
        ('Для погодок','Для погодок'),
    )
    TYPE_WHEEL=(
        ('Пневматические','Пневматические'),
        ('Пластиковые','Пластиковые'),
        ('Гелевые','Гелевые'),
        ('Резиновые','Резиновые'),
    )
    PROPERTIES=(
        ('Сумка','Сумка'),
        ('Дождевик','Дождевик'),
        ('Матрас','Матрас'),
        ('Корзина для покупок','Корзина для покупок'),
        ('Конверт','Конверт'),
        ('Муфта','Муфта'),
        ('Москитная сетка','Москитная сетка'),
        ('Чехол на ноги','Чехол на ноги'),
        ('Ремни','Ремни'),
        ('Бампер','Бампер'),
        ('Козырек от солнца','Козырек от солнца'),
        ('Для бега','Для бега'),
    )
    FEEDING=(
        ('Бутылочки, ниблеры','Бутылочки, ниблеры'),
        ('Детская посуда','Детская посуда'),
        ('Детское питание','Детское питание'),
        ('Молокоотсосы','Молокоотсосы'),
        ('Нагрудники, слюнявчики','Нагрудники, слюнявчики'),
        ('Накладки для груди','Накладки для груди'),
        ('Поильники','Поильники'),
        ('Соски','Соски'),
        ('Стерилизаторы, подогреватели','Стерилизаторы, подогреватели'),
        ('Хранение грудного молока','Хранение грудного молока'),
    )
    BATH=(
        ('Ванночки','Ванночки'),
        ('Круги на шею','Круги на шею'),
        ('Мочалки, губки','Мочалки, губки'),
        ('Нарукавники','Нарукавники'),
        ('Сиденья, горки','Сиденья, горки'),
        ('Шампуни, мыло','Шампуни, мыло'),
    )
    ROOM=(
        ('Защитные накладки, барьеры','Защитные накладки, барьеры'),
        ('Качели, шезлонги','Качели, шезлонги'),
        ('Колыбели, люльки','Колыбели, люльки'),
        ('Кроватки','Кроватки'),
        ('Манежи','Манежи'),
        ('Ночники','Ночники'),
        ('Пеленальные столики','Пеленальные столики'),
        ('Постельные принадлежности','Постельные принадлежности'),
        ('Ростомеры','Ростомеры'),
        ('Стульчики для кормления','Стульчики для кормления'),
        ('Ходунки, прыгунки','Ходунки, прыгунки'),
    )
    DIAPERS=(
        ('Горшки, сиденья','Горшки, сиденья'),
        ('Накопители подгузников','Накопители подгузников'),
        ('Пеленки, клеенки','Пеленки, клеенки'),
        ('Подгузники','Подгузники'),
    )
    BABYSITTER=(
        ('Видеоняня','Видеоняня'),
        ('Радионяня','Радионяня'),
    )
    MOM=(
        ('Бандажи','Бандажи'),
        ('Подушки, кресла для мам','Подушки, кресла для мам'),
        ('Сумки-кенгуру, слинги','Сумки-кенгуру, слинги'),
    )
    STUDY=(
        ('Глобусы, карты','Глобусы, карты'),
        ('Доски, мольберты','Доски, мольберты'),
        ('Канцтовары','Канцтовары'),
        ('Пеналы','Пеналы'),
        ('Учебники','Учебники'),
    )

    brand_car_seat = models.CharField(max_length=50, blank=True, choices = BRANDS_CAR_SEAT, verbose_name="Марка автокресла")
    group = models.CharField(max_length=50, blank=True, choices = GROUP, verbose_name="Группа")
    binding = models.CharField(max_length=50, blank=True, choices = BINDING, verbose_name="Крепление")
    feature = models.CharField(max_length=50, blank=True, choices = FEATURE, verbose_name="Особенности")
    regulation = models.CharField(max_length=50, blank=True, choices = REGULATION, verbose_name="Регулировки")
    health = models.CharField(max_length=50, blank=True, choices = HEALTH, verbose_name="Здоровье и уход")
    game = models.CharField(max_length=50, blank=True, choices = GAME, verbose_name="Игрушки, игры")
    brand_pram = models.CharField(max_length=50, blank=True, choices = BRANDS_PRAM, verbose_name="Марка коляски")
    type_pram = models.CharField(max_length=50, blank=True, choices = TYPE_PRAM, verbose_name="Тип коляски")
    age_pram = models.CharField(max_length=50, blank=True, choices = AGE_PRAM, verbose_name="Возраст")
    number_blocks = models.CharField(max_length=50, blank=True, choices = NUMBER_BLOCKS, verbose_name="Количество блоков")
    type_wheel = models.CharField(max_length=50, blank=True, choices = TYPE_WHEEL, verbose_name="Тип колес")
    properties = models.CharField(max_length=50, blank=True, choices = PROPERTIES, verbose_name="Особенности")
    feeding = models.CharField(max_length=50, blank=True, choices = FEEDING, verbose_name="Кормление и питание")
    bath = models.CharField(max_length=50, blank=True, choices = BATH, verbose_name="Купание")
    room = models.CharField(max_length=50, blank=True, choices = ROOM, verbose_name="Обустройство детской")
    diapers = models.CharField(max_length=50, blank=True, choices = DIAPERS, verbose_name="Подгузники и горшки")
    babysitter = models.CharField(max_length=50, blank=True, choices = BABYSITTER, verbose_name="Радио- и видеоняня")
    mom = models.CharField(max_length=50, blank=True, choices = MOM, verbose_name="Товары для мам")
    study = models.CharField(max_length=50, blank=True, choices = STUDY, verbose_name="Товары для учебы")

    class Meta:
        db_table = "Детские товары"
        verbose_name = "Детские товары"
        verbose_name_plural = "Детские товары"
