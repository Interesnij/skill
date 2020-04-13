from django.db import models
from ad_posts.models import Ad


class Child(Ad):
    TYPE=(
        ('Банты','Банты'),
        ('Бижутерия','Бижутерия'),
        ('Галстуки и бабочки','Галстуки и бабочки'),
        ('Заколки, резинки и ободки','Заколки, резинки и ободки'),
        ('Зонты','Зонты'),
        ('Карнавальные костюмы','Карнавальные костюмы'),
        ('Кошельки','Кошельки'),
        ('Очки','Очки'),
        ('Перчатки и варежки','Перчатки и варежки'),
        ('Ремни и пояса','Ремни и пояса'),
        ('Рюкзаки','Рюкзаки'),
        ('Сумки','Сумки'),
        ('Украшения','Украшения'),
        ('Часы','Часы'),
        ('Шарфы и платки','Шарфы и платки'),
    )
    GENDER = (('Мальчикам', 'Мальчикам'), ('Девочкам', 'Девочкам'))
    BRANDS_AKS=(
        ('Adidas','Adidas'),
        ('Angry Birds','Angry Birds'),
        ('Chiggo','Chiggo'),
        ('Chobi','Chobi'),
        ('Cokoon','Cokoon'),
        ('Crockid','Crockid'),
        ('Crocs','Crocs'),
        ('Demix','Demix'),
        ('Didriksons','Didriksons'),
        ('Disney','Disney'),
        ('Ecco','Ecco'),
        ('Grizzly','Grizzly'),
        ('Gulliver','Gulliver'),
        ('Gymboree','Gymboree'),
        ('Happy Baby','Happy Baby'),
        ('Hello Kitty','Hello Kitty'),
        ('Herlitz','Herlitz'),
        ('Hummingbird','Hummingbird'),
        ('Huppa','Huppa'),
        ('I Love Mum','I Love Mum'),
        ('Kerry','Kerry'),
        ('Kivat','Kivat'),
        ("Lego","Lego"),
        ('Molo','Molo'),
        ('MonsterHigh','MonsterHigh'),
        ('Mothercare','Mothercare'),
        ("Mum'S Era","Mum'S Era"),
        ('Nike','Nike'),
        ('Polar','Polar'),
        ('Reike','Reike'),
        ('Reima','Reima'),
        ('Skip Hop','Skip Hop'),
        ('Trunki','Trunki'),
        ('Winx','Winx'),
        ('Батик','Батик'),
        ('Божья Коровка','Божья Коровка'),
        ('Гамма','Гамма'),
        ('Звездочка','Звездочка'),
        ('Карапуз','Карапуз'),
        ('Кит','Кит'),
        ('Котофей','Котофей'),
        ('Маша И Медведь','Маша И Медведь'),
        ('Медвежонок','Медвежонок'),
        ('Пчелка','Пчелка'),
        ('Радуга','Радуга'),
        ('Солнышко','Солнышко'),
        ('Твое','Твое'),
        ('Тим','Тим'),
        ('Умка','Умка'),
    )
    BRANDS=(
        ('Acoola','Acoola'),
        ('Adidas','Adidas'),
        ('Armani','Armani'),
        ('Armani Junior','Armani Junior'),
        ('Babygo','Babygo'),
        ('Barkito','Barkito'),
        ('Blue Seven','Blue Seven'),
        ('Button Blue','Button Blue'),
        ('Calvin Clein','Calvin Clein'),
        ("Carter's","Carter's"),
        ('Chicco','Chicco'),
        ('Choupette','Choupette'),
        ('Cleverly','Cleverly'),
        ('Crockid','Crockid'),
        ('Disney','Disney'),
        ('Duwali','Duwali'),
        ('Futurino','Futurino'),
        ('Gap','Gap'),
        ('Gulliwer','Gulliwer'),
        ('Gemboree','Gemboree'),
        ('Insity','Insity'),
        ('Lacoste','Lacoste'),
        ('Lc Vaikiki','Lc Vaikiki'),
        ("Mango","Mango"),
        ('Mayoral','Mayoral'),
        ('Mix','Mix'),
        ('Modis','Modis'),
        ("Mothercare",'Mothercare'),
        ('Navy','Navy'),
        ('Noble People','Noble People'),
        ('Nova','Nova'),
        ("O'Stin","O'Stin"),
        ('Oodji','Oodji'),
        ('Orkestra','Orkestra&Bear'),
        ('Original Marines','Original Marines'),
        ('Oshkosh','Oshkosh'),
        ('Outwenture','Outwenture'),
        ('Paul Smith','Paul Smith'),
        ('Pelican','Pelican'),
        ('Pinetti','Pinetti'),
        ('PlayTuday','PlayTuday'),
        ('Sela','Sela'),
        ('Silver Spoon','Silver Spoon'),
        ('Sisley','Sisley'),
        ('Sky Lake','Sky Lake'),
        ('Sly','Sly'),
        ('Top Tailor','Top Tailor'),
        ('Tommy Hilfiger','Tommy Hilfiger'),
        ('Tsarevich','Tsarevich'),
        ('United Colors of Benetton','United Colors of Benetton'),
        ('Zara','Zara'),
        ('Дочки-сыночки','Дочки-сыночки'),
        ('Империя детства','Империя детства'),
        ('Карамелли','Карамелли'),
        ('Кит','Кит'),
        ('Маленькая Леди','Маленькая Леди'),
        ('Непоседа','Непоседа'),
        ('Смена','Смена'),
        ('Твое','Твое'),
    )
    COLOR=(
        ('Белый','Белый'),
        ('Хаки','Хаки'),
        ('Серый','Серый'),
        ('Чёрный','Чёрный'),
        ('Коричневый','Коричневый'),
        ('Бордовый','Бордовый'),
        ('Бежевый','Бежевый'),
        ('Красный','Красный'),
        ('Оранжевый','Оранжевый'),
        ('Жёлтый','Жёлтый'),
        ('Зелёный','Зелёный'),
        ('Голубой','Голубой'),
        ('Синий','Синий'),
        ('Фиолетовый','Фиолетовый'),
        ('Пурпурный','Пурпурный'),
        ('Розовый','Розовый'),
        ('Разноцветный','Разноцветный'),
    )
    CONDITION =(
        ('Б/У','Б/У'),
        ('Новое','Новое'),
    )
    BLU_SH =(
        ('Блузы','Блузы'),
        ('Рубашки','Рубашки'),
    )
    SIZE=(
        ('46-50 (0-1 месяц)','44-46 (S)'),
        ('51-56 (2 месяца)','46-48 (M)'),
        ('57-62 (3 месяца)','48-50 (L)'),
        ('63-68 (6 месяцев)','50-52 (XL)'),
        ('69-74 (9 месяцев)','52-54 (XXL)'),
        ('75-80 (1 год)','54-56 (XXXL)'),
        ('81-86 (1.5 года)','44-46 (S)'),
        ('87-92 (2 года)','46-48 (M)'),
        ('93-98 (3 года)','48-50 (L)'),
        ('99-104 (4 года)','50-52 (XL)'),
        ('105-110 (5 лет)','52-54 (XXL)'),
        ('111-116 (6 лет)','54-56 (XXXL)'),
        ('117-122 (7 лет)','44-46 (S)'),
        ('123-128 (8 лет)','46-48 (M)'),
        ('129-134 (9 лет)','48-50 (L)'),
        ('135-140 (10 лет)','50-52 (XL)'),
        ('141-146 (11 лет)','52-54 (XXL)'),
        ('147-152 (12 лет)','54-56 (XXXL)'),
        ('153-158 (13 лет)','52-54 (XXL)'),
        ('159-164 (14 лет)','54-56 (XXXL)'),
    )
    SEASON =(
        ('Демисезон','Демисезон'),
        ('Зима','Зима'),
        ('Лето','Лето'),
    )
    OUTERWEAR=(
        ('Дождевики','Дождевики'),
        ('Дубленки','Дубленки'),
        ('Жилеты','Жилеты'),
        ('Кожаные куртки','Кожаные куртки'),
        ('Комбинезоны и костюмы','Комбинезоны и костюмы'),
        ('Куртки','Куртки'),
        ('накидки и пончо','накидки и пончо'),
        ('Пальто','Пальто'),
        ('Парки','Парки'),
        ('Плащи','Плащи'),
        ('Пуховики','Пуховики'),
        ('Шубы','Шубы'),
    )
    HAT=(
        ('Бейсболки и кепки','Бейсболки и кепки'),
        ('Косынки и банданы','Косынки и банданы'),
        ('Панамы','Панамы'),
        ('Повязки','Повязки'),
        ('Чепчики','Чепчики'),
        ('Шапки','Шапки'),
        ('Шляпы','Шляпы'),
    )
    HOME=(
        ('Пижамы','Пижамы'),
        ('Халаты','Халаты'),
    )
    COVERALL=(
        ('Боди','Боди'),
        ('Комбинезоны','Комбинезоны'),
    )

    UNDERWEAR=(
        ('Бюстгалтеры','Бюстгалтеры'),
        ('Кальсоны','Кальсоны'),
        ('Колготки','Колготки'),
        ('Купальники','Купальники'),
        ('Носки','Носки'),
        ('Плавки','Плавки'),
        ('Термобелье','Термобелье'),
        ('Трусы','Трусы'),
    )
    SHOES=(
        ('Балетки','Балетки'),
        ('Босоножки и сабо','Босоножки и сабо'),
        ('Ботинки','Ботинки'),
        ('Валенки и угги','Валенки и угги'),
        ('Домашняя обувь','Домашняя обувь'),
        ('Дутики','Дутики'),
        ('Кеды','Кеды'),
        ('Кроссовки','Кроссовки'),
        ('Мокасины','Мокасины'),
        ('Обувь на первый шаг','Обувь на первый шаг'),
        ('Ортопедическая обувь','Ортопедическая обувь'),
        ('Пинетки','Пинетки'),
        ('Полуботинки','Полуботинки'),
        ('Резиновые сапоги','Резиновые сапоги'),
        ('Сандалии','Сандалии'),
        ('Сапоги','Сапоги'),
        ('Слипоны','Слипоны'),
        ('Тапочки','Тапочки'),
        ('Туфли','Туфли'),
        ('Чешки','Чешки'),
        ('Шлепанцы и пляжная обувь','Шлепанцы и пляжная обувь'),
    )
    SHOE_SIZE=(
        ('19 и меньше','19 и меньше'),
        ('20','20'),
        ('21','21'),
        ('22','22'),
        ('23','23'),
        ('24','24'),
        ('25','25'),
        ('26','26'),
        ('27','27'),
        ('28','28'),
        ('29','29'),
        ('30','30'),
        ('31','31'),
        ('32','32'),
        ('33','33'),
        ('34','34'),
        ('35','35'),
        ('36','36'),
        ('37 и больше','37 и больше'),
    )
    SUITS=(
        ('Жилетки','Жилетки'),
        ('Костюмы','Костюмы'),
        ('Пиджаки','Пиджаки'),
        ('Школьная форма','Школьная форма'),
    )
    SHIRTS =(
        ('Джинсовые','Джинсовые'),
        ('Длинный рукав','Длинный рукав'),
        ('Короткий рукав','Короткий рукав'),
    )
    SWEETERS=(
        ('Водолазки','Водолазки'),
        ('Джемперы','Джемперы'),
        ('Кардиганы','Кардиганы'),
        ('Кофты','Кофты'),
        ('Лонгсливы','Лонгсливы'),
        ('Олимпайки','Олимпайки'),
        ('Свитеры','Свитеры'),
        ('Свитшоты','Свитшоты'),
        ('Толстовки и худи','Толстовки и худи'),
    )
    SPORTWEAR=(
        ('Верхняя одежда','Верхняя одежда'),
        ('Комбинезоны','Комбинезоны'),
        ('Купальники','Купальники'),
        ('Лосины и гетры','Лосины и гетры'),
        ('Платья и юбки','Платья и юбки'),
        ('Спортивные костюмы','Спортивные костюмы'),
        ('Футболки и топы','Футболки и топы'),
        ('Штаны и шорты','Штаны и шорты'),
    )
    TOPS=(
        ('Майки','Майки'),
        ('Поло','Поло'),
        ('Топы','Топы'),
        ('Футболки','Футболки'),
    )
    PANTS=(
        ('Бриджы','Бриджы'),
        ('Брюки','Брюки'),
        ('Джинсы','Джинсы'),
        ('Леггинсы','Леггинсы'),
        ('Шорты','Шорты'),
    )
    PANT_SIZE=(
        ('28','28'),
        ('29','29'),
        ('30','30'),
        ('31','31'),
        ('32','32'),
        ('33','33'),
        ('34','34'),
        ('35','35'),
        ('36','36'),
        ('37','37'),
        ('38 и больше','38 и больше'),
    )
    DRESSES=(
        ('Платья','Платья'),
        ('Сарафаны','Сарафаны'),
        ('Туники','Туники'),
        ('Юбки','Юбки'),
    )
    LENGTH =(
        ('Макси','Макси'),
        ('Миди','Миди'),
        ('Мини','Мини'),
    )
    SLIDERS =(
        ('Песочники','Песочники'),
        ('Ползунки','Ползунки'),
        ('Распашонки','Распашонки'),
    )


    type = models.CharField(max_length=50, blank=True, choices = TYPE, verbose_name="Тип аксессуара")
    gender = models.CharField(max_length=50, blank=True, choices = GENDER, verbose_name="Пол")
    brand_aks = models.CharField(max_length=50, blank=True, choices = BRANDS_AKS, verbose_name="Бренд аксессуара")
    brand = models.CharField(max_length=50, blank=True, choices = BRANDS, verbose_name="Бренд")
    color=models.CharField(max_length=45, blank=True, choices = COLOR, verbose_name="Цвет")
    condition = models.CharField(max_length=50, blank=True, choices = CONDITION, verbose_name="Состояние")
    size = models.CharField(max_length=50, blank=True, choices = SIZE, verbose_name="Размер / рост")
    blu_sh = models.CharField(max_length=50, blank=True, choices = BLU_SH, verbose_name="Блузы и рубашки")
    season = models.CharField(max_length=50, blank=True, choices = SEASON, verbose_name="Сезон")
    outerwear = models.CharField(max_length=50, blank=True, choices = OUTERWEAR, verbose_name="Верхняя одежда")
    hat = models.CharField(max_length=50, blank=True, choices = HAT, verbose_name="Головные уборы")
    home = models.CharField(max_length=50, blank=True, choices = HOME, verbose_name="Домашняя одежда")
    coverall = models.CharField(max_length=50, blank=True, choices = COVERALL, verbose_name="Комбинезоны")
    underwear = models.CharField(max_length=50, blank=True, choices = UNDERWEAR, verbose_name="Нижнее белье")
    shoes = models.CharField(max_length=50, blank=True, choices = SHOES, verbose_name="Обувь")
    shoe_size = models.CharField(max_length=50, blank=True, choices = SHOE_SIZE, verbose_name="Размер обуви")
    suits = models.CharField(max_length=50, blank=True, choices = SUITS, verbose_name="Пиджаки и костюмы")
    sweaters = models.CharField(max_length=50, blank=True, choices = SWEETERS, verbose_name="Свитера и толстовки")
    sportwear = models.CharField(max_length=50, blank=True, choices = SPORTWEAR, verbose_name="Спортивная одежда")
    tops = models.CharField(max_length=50, blank=True, choices = TOPS, verbose_name="Футболки и поло")
    pants = models.CharField(max_length=50, blank=True, choices = PANTS, verbose_name="Штаны и шорты")
    pant_size = models.CharField(max_length=50, blank=True, choices = PANT_SIZE, verbose_name="Размер штанов")
    dresses = models.CharField(max_length=50, blank=True, choices = DRESSES, verbose_name="Платья и юбки")
    length = models.CharField(max_length=50, blank=True, choices = LENGTH, verbose_name="Длина")
    sliders = models.CharField(max_length=50, blank=True, choices = SLIDERS, verbose_name="Ползунки и распашонки")

    class Meta:
        verbose_name = "Детский гардероб"
        verbose_name_plural = "Детский гардероб"
