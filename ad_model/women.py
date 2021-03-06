from django.db import models
from ad_posts.models import Ad


class Women(Ad):
    TYPE=(
        ('Брелоки и ключницы','Брелоки и ключницы'),
        ('Галстуки','Галстуки'),
        ('Для волос','Для волос'),
        ('Зеркала','Зеркала'),
        ('Зонты','Зонты'),
        ('Косметички','Косметички'),
        ('Кошельки','Кошельки'),
        ('Очки','Очки'),
        ('Перчатки и варежки','Перчатки и варежки'),
        ('Ремни и пояса','Ремни и пояса'),
        ('Рюкзаки','Рюкзаки'),
        ('Свадебные','Свадебные'),
        ('Сумки','Сумки'),
        ('Украшения','Украшения'),
        ('Часы','Часы'),
        ('Чемоданы','Чемоданы'),
        ('Шарфы и платки','Шарфы и платки'),
    )
    BRANDS=(
        ('ACNE STUDIOS','ACNE STUDIOS'),
        ('ADIDAS','ADIDAS'),
        ('Alba','Alba'),
        ('Alexander McQueen','Alexander McQueen'),
        ('Alexander Wang','Alexander Wang'),
        ('Ann Demeulemeester','Ann Demeulemeester'),
        ('Armani','Armani'),
        ('Asos','Asos'),
        ('Avon','Avon'),
        ('Baldinini','Baldinini'),
        ('Balenciaga','Balenciaga'),
        ('Befree','Befree'),
        ('Braccialini','Braccialini'),
        ('Burberry','Burberry'),
        ('Calipso','Calipso'),
        ('Calvin Clein','Calvin Clein'),
        ('Casio','Casio'),
        ('Celine','Celine'),
        ('Chanel','Chanel'),
        ('Chloe','Chloe'),
        ('Chtistian Dior','Chtistian Dior'),
        ("Colin's","Colin's"),
        ('Comme des Garcons','Comme des Garcons'),
        ('Cos','Cos'),
        ('Daniel Wellington','Daniel Wellington'),
        ('Dasigual','Dasigual'),
        ('Diesel','Diesel'),
        ('Diva','Diva'),
        ('Dkny','Dkny'),
        ('Dolce&Cabbana','Dolce&Cabbana'),
        ('Dries Van Noten','Dries Van Noten'),
        ('Ecco','Ecco'),
        ('Escada','Escada'),
        ('Etro','Etro'),
        ('Fendi','Fendi'),
        ('Fjallraven','Fjallraven'),
        ('Furla','Furla'),
        ('Geargio Armani','Geargio Armani'),
        ('Givenchy','Givenchy'),
        ('Gucci','Gucci'),
        ('H&M','H&M'),
        ('Helmut Lang','Helmut Lang'),
        ('Incanto','Incanto'),
        ('Insity','Insity'),
        ('Isabel Marant','Isabel Marant'),
        ('Jil Sander','Jil Sander'),
        ('Jimmy Choo','Jimmy Choo'),
        ('Jast Cavalli','Jast Cavalli'),
        ('Karen Millen','Karen Millen'),
        ('Kenzo','Kenzo'),
        ('Lacoste','Lacoste'),
        ("Livi's","Livi's"),
        ('Louiss Vuitton','Louiss Vuitton'),
        ('Love Republic','Love Republic'),
        ('Maison Margiela','Maison Margiela'),
        ('Maison Kitsune','Maison Kitsune'),
        ('Mango','Mango'),
        ('Marc Jacobs','Marc Jacobs'),
        ('Marni','Marni'),
        ('Mascotte','Mascotte'),
        ('Max Mara','Max Mara'),
        ('Mexx','Mexx'),
        ('Michael Cors','Michael Cors'),
        ('Missoni','Missoni'),
        ('Miu Miu','Miu Miu'),
        ('Mohito','Mohito'),
        ('Moschino','Moschino'),
        ('Motivi','Motivi'),
        ('Neil Barrett','Neil Barrett'),
        ('New Yorker','New Yorker'),
        ('Next','Next'),
        ('Nike','Nike'),
        ("O'Stin","O'Stin"),
        ('Off-White','Off-White'),
        ('Officine Creative','Officine Creative'),
        ('Oysho','Oysho'),
        ('Pinco','Pinco'),
        ('Piquadro','Piquadro'),
        ('Prada','Prada'),
        ('Pull&Bear','Pull&Bear'),
        ('RAFF SIMONS','RAFF SIMONS'),
        ('Ralph Lauren','Ralph Lauren'),
        ('Ray-Ban','Ray-Ban'),
        ('Reebok','Reebok'),
        ('Reserved','Reserved'),
        ('Rick Owens','Rick Owens'),
        ('River Island','River Island'),
        ('Roxy','Roxy'),
        ('Salvatore Ferragamo','Salvatore Ferragamo'),
        ('Sisley','Sisley'),
        ('Skagen','Skagen'),
        ('Stella Mccartney','Stella Mccartney'),
        ('Stradivarius','Stradivarius'),
        ('Sunlight','Sunlight'),
        ('Swarovski','Swarovski'),
        ('Ted Baker','Ted Baker'),
        ('Terranova','Terranova'),
        ('Tods','Tods'),
        ('Tommy Hilfiger','Tommy Hilfiger'),
        ('Topshop','Topshop'),
        ('Toska Blu','Toska Blu'),
        ('Tous','Tous'),
        ('Undercover','Undercover'),
        ('United Colors of Beneton','United Colors of Beneton'),
        ('Valentino','Valentino'),
        ('Vans','Vans'),
        ('Versace','Versace'),
        ("Victoria's Secret","Victoria's Secret"),
        ('Vivienne WestWood','Vivienne WestWood'),
        ('YSL','YSL'),
        ('Yohji Yamamoto','Yohji Yamamoto'),
        ('Yves Saint Laurent','Yves Saint Laurent'),
        ('Zara','Zara'),
        ('Zarina','Zarina'),
        ('Дикая Орхидея','Дикая Орхидея'),
        ('Новая Заря','Новая Заря'),
        ('Эконика','Эконика'),
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
    SIZE=(
        ('40-42 (XS)','40-42 (XS)'),
        ('42-44 (S)','42-44 (S)'),
        ('44-46 (M)','44-46 (M)'),
        ('46-48 (L)','46-48 (L)'),
        ('48-50 (XL)','48-50 (XL)'),
        ('50-52 (XXL)','50-52 (XXL)'),
        ('52-54 (XXXL) и больше','52-54 (XXXL) и больше'),
    )
    TYPE_MOM=(
        ('Блузы и рубашки','Блузы и рубашки'),
        ('Верхняя одежда','Верхняя одежда'),
        ('Домашняя одежда','Домашняя одежда'),
        ('Комбинезоны','Комбинезоны'),
        ('Купальники','Купальники'),
        ('Нижнее белье','Нижнее белье'),
        ('Пиджаки и костюмы','Пиджаки и костюмы'),
        ('Платья и юбки','Платья и юбки'),
        ('Свитера и толстовки','Свитера и толстовки'),
        ('Футболки и топы','Футболки и топы'),
        ('Штаны и шорты','Штаны и шорты'),
    )
    SEASON =(
        ('Демисезон','Демисезон'),
        ('Зима','Зима'),
        ('Лето','Лето'),
    )
    OUTERWEAR=(
        ('Бомберы','Бомберы'),
        ('Ветровки','Ветровки'),
        ('Джинсовые куртки','Джинсовые куртки'),
        ('Дождевики','Дождевики'),
        ('Дубленки','Дубленки'),
        ('Жилеты','Жилеты'),
        ('Кожаные куртки','Кожаные куртки'),
        ('Куртки','Куртки'),
        ('Накидки и пончо','Накидки и пончо'),
        ('Пальто','Пальто'),
        ('Парки','Парки'),
        ('Плащи и тренчи','Плащи и тренчи'),
        ('Полупальто','Полупальто'),
        ('Пуховики','Пуховики'),
        ('Шубы','Шубы'),
    )
    HAT=(
        ('Бейсболки и кепки','Бейсболки и кепки'),
        ('Береты','Береты'),
        ('Платки и косынки','Платки и косынки'),
        ('Повязки','Повязки'),
        ('Шапки','Шапки'),
        ('Шляпы','Шляпы'),
    )
    HOME=(
        ('Ночные сорочки','Ночные сорочки'),
        ('Пеньюары','Пеньюары'),
        ('Пижамы','Пижамы'),
        ('Халаты','Халаты'),
    )
    COVERALL=(
        ('Полукомбинезоны','Полукомбинезоны'),
        ('С брюками','С брюками'),
        ('С шортами','С шортами'),
    )
    SWIMSUITS=(
        ('Бикини','Бикини'),
        ('Лифы','Лифы'),
        ('Плавки','Плавки'),
        ('Раздельные купальники','Раздельные купальники'),
        ('Слитные купальники','Слитные купальники'),
    )
    UNDERWEAR=(
        ('Боди','Боди'),
        ('Бюстгалтеры','Бюстгалтеры'),
        ('Гольфы и гетры','Гольфы и гетры'),
        ('Колготки','Колготки'),
        ('Корректирующее','Корректирующее'),
        ('Корсеты','Корсеты'),
        ('Носки','Носки'),
        ('Пояса для чулок','Пояса для чулок'),
        ('Сорочки','Сорочки'),
        ('Термобелье','Термобелье'),
        ('Трусы','Трусы'),
        ('Чулки','Чулки'),
    )
    SHOES=(
        ('Балетки','Балетки'),
        ('Босоножки','Босоножки'),
        ('Ботильоны','Ботильоны'),
        ('Ботинки','Ботинки'),
        ('Валенки и галоши','Валенки и галоши'),
        ('Домашняя обувь','Домашняя обувь'),
        ('Дутики и луноходы','Дутики и луноходы'),
        ('Кеды','Кеды'),
        ('Кроссовки','Кроссовки'),
        ('Мокасины','Мокасины'),
        ('Полусапожки','Полусапожки'),
        ('Сандалии','Сандалии'),
        ('Сапоги','Сапоги'),
        ('Слипоны','Слипоны'),
        ('Тапочки','Тапочки'),
        ('Туфли','Туфли'),
        ('Угги и унты','Угги и унты'),
        ('Шлепанцы','Шлепанцы'),
    )
    SHOE_SIZE=(
        ('33','33'),
        ('34','34'),
        ('35','35'),
        ('36','36'),
        ('37','37'),
        ('38','38'),
        ('39','39'),
        ('40','40'),
        ('41','41'),
        ('42','42'),
        ('43','43'),
        ('44','44'),
        ('45','45'),
        ('46','46'),
    )
    SUITS=(
        ('Жилетки','Жилетки'),
        ('Костюмы с брюками','Костюмы с брюками'),
        ('Костюмы с юбками','Костюмы с юбками'),
        ('Пиджаки','Пиджаки'),
    )
    DRESSES=(
        ('Вечерние платья','Вечерние платья'),
        ('Вязаные платья','Вязаные платья'),
        ('Джинсовые платья','Джинсовые платья'),
        ('Офисные платья','Офисные платья'),
        ('Платья мини','Платья мини'),
        ('Платья-рубашки','Платья-рубашки'),
        ('Повседневные платья','Повседневные платья'),
        ('Сарафаны','Сарафаны'),
        ('Свадебные платья','Свадебные платья'),
        ('Туники','Туники'),
        ('Юбки','Юбки'),
    )
    LENGTH =(
        ('Макси','Макси'),
        ('Миди','Миди'),
        ('Мини','Мини'),
    )
    SWEETERS=(
        ('Водолазки','Водолазки'),
        ('Джемперы','Джемперы'),
        ('Кардиганы','Кардиганы'),
        ('Кофты','Кофты'),
        ('Олимпайки','Олимпайки'),
        ('Пуловеры','Пуловеры'),
        ('Свитеры','Свитеры'),
        ('Толстовки и худи','Толстовки и худи'),
    )
    SPORTWEAR=(
        ('Верхняя одежда','Верхняя одежда'),
        ('Комбинезоны','Комбинезоны'),
        ('Платья и юбки','Платья и юбки'),
        ('Спортивные костюмы','Спортивные костюмы'),
        ('Футболки и топы','Футболки и топы'),
        ('Штаны и шорты','Штаны и шорты'),
    )
    TOPS=(
        ('Лонгсливы','Лонгсливы'),
        ('Майки','Майки'),
        ('Поло','Поло'),
        ('Топы','Топы'),
        ('Футболки','Футболки'),
    )
    PANTS=(
        ('Бриджы','Бриджы'),
        ('Брюки','Брюки'),
        ('Джинсы','Джинсы'),
        ('Капри','Капри'),
        ('Леггинсы','Леггинсы'),
        ('Шорты','Шорты'),
    )
    PANT_SIZE=(
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
        ('34 и больше','34 и больше'),
    )


    type = models.CharField(max_length=50, blank=True, choices = TYPE, verbose_name="Тип аксессуара")
    brand = models.CharField(max_length=50, blank=True, choices = BRANDS, verbose_name="Бренд")
    color=models.CharField(max_length=45, blank=True, choices = COLOR, verbose_name="Цвет")
    condition = models.CharField(max_length=50, blank=True, choices = CONDITION, verbose_name="Состояние")
    size = models.CharField(max_length=50, blank=True, choices = SIZE, verbose_name="Размер")
    type_mom = models.CharField(max_length=50, blank=True, choices = TYPE_MOM, verbose_name="Тип одежды")
    season = models.CharField(max_length=50, blank=True, choices = SEASON, verbose_name="Сезон")
    outerwear = models.CharField(max_length=50, blank=True, choices = OUTERWEAR, verbose_name="Верхняя одежда")
    hat = models.CharField(max_length=50, blank=True, choices = HAT, verbose_name="Головные уборы")
    home = models.CharField(max_length=50, blank=True, choices = HOME, verbose_name="Домашняя одежда")
    coverall = models.CharField(max_length=50, blank=True, choices = COVERALL, verbose_name="Комбинезоны")
    swimsuits = models.CharField(max_length=50, blank=True, choices = SWIMSUITS, verbose_name="Купальники")
    underwear = models.CharField(max_length=50, blank=True, choices = UNDERWEAR, verbose_name="Нижнее белье")
    shoes = models.CharField(max_length=50, blank=True, choices = SHOES, verbose_name="Обувь")
    shoe_size = models.CharField(max_length=50, blank=True, choices = SHOE_SIZE, verbose_name="Размер обуви")
    suits = models.CharField(max_length=50, blank=True, choices = SUITS, verbose_name="Пиджаки и костюмы")
    dresses = models.CharField(max_length=50, blank=True, choices = DRESSES, verbose_name="Платья и юбки")
    length = models.CharField(max_length=50, blank=True, choices = LENGTH, verbose_name="Длина")
    sweaters = models.CharField(max_length=50, blank=True, choices = SWEETERS, verbose_name="Свитера и толстовки")
    sportwear = models.CharField(max_length=50, blank=True, choices = SPORTWEAR, verbose_name="Спортивная одежда")
    tops = models.CharField(max_length=50, blank=True, choices = TOPS, verbose_name="Футболки и топы")
    pants = models.CharField(max_length=50, blank=True, choices = PANTS, verbose_name="Штаны и шорты")
    pant_size = models.CharField(max_length=50, blank=True, choices = PANT_SIZE, verbose_name="Размер штанов")

    class Meta:
        verbose_name = "Женский гардероб"
        verbose_name_plural = "Женский гардероб"
