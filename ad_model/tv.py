from django.db import models
from ad_posts.models import Ad


class TV(Ad):
    TYPE_TV=(
        ('OLED','Ноутбуки'),
        ('ЖК, LED','Нетбуки'),
        ('ЭЛТ, кинескопные','Трансформеры'),
        ('4K UHD','Ноутбуки'),
    )
    BRANDS_TV=(
        ('Aiwa','Aiwa'),
        ('Akai','Akai'),
        ('Akira','Akira'),
        ('BBK','BBK'),
        ('Daewoo','Daewoo'),
        ('Erisson','Erisson'),
        ('Funai','Funai'),
        ('Fusion','Fusion'),
        ("Goldstar","Goldstar"),
        ('Grundig','Grundig'),
        ('Hitachi','Hitachi'),
        ('Horizont','Horizont'),
        ('JVS','JVS'),
        ('LG','LG'),
        ('Loewe','Loewe'),
        ('Mystery','Mystery'),
        ('Orion','Orion'),
        ('Panasonic','Panasonic'),
        ('Philips','Philips'),
        ('Rolsen','Rolsen'),
        ('Rubin','Rubin'),
        ('Samsung','Samsung'),
        ('Sharp','Sharp'),
        ('Shivaki','Shivaki'),
        ('Sony','Sony'),
        ('Supra','Supra'),
        ('TCL','TCL'),
        ("Telefunken","Telefunken"),
        ('Thomson','Thomson'),
        ('Витязь','Витязь'),
        ('Другая','Другая'),
    )
    DIAGONAL_TV=(
        ('До 15"','До 15"'),
        ('От 15" до 19.9"','От 15" до 19.9"'),
        ('От 20" до 24.9"','От 20" до 24.9"'),
        ('От 25" до 29.9"','От 25" до 29.9"'),
        ('От 30" до 34.9"','От 30" до 34.9"'),
        ('От 35" до 39.9"','От 35" до 39.9"'),
        ('От 40" до 44.9"','От 40" до 44.9"'),
        ('От 45" до 49.9"','От 45" до 49.9"'),
        ('От 50" до 54.9"','От 50" до 54.9"'),
        ('От 55" до 59.9"','От 55" до 59.9"'),
        ('60" и более','60" и более'),
    )
    SCREEN_TV=(
        ('Full HD','Full HD'),
        ('HD-Ready, LED','HD-Ready, LED'),
        ('Ultra HD','Ultra HD'),
    )
    TYPE_PROJECTORS=(
        ('Портативные','Портативные'),
        ('Стационарные','Стационарные'),
    )
    BRANDS_PROJECTORS=(
        ('Acer','Acer'),
        ('ASUS','ASUS'),
        ('BenQ','BenQ'),
        ('Canon','Canon'),
        ('Epson','Epson'),
        ('Hitachi','Hitachi'),
        ('InFocus','InFocus'),
        ('LG','LG'),
        ("NEC","NEC"),
        ('Optoma','Optoma'),
        ('Panasonic','Panasonic'),
        ('Philips','Philips'),
        ('Sanyo','Sanyo'),
        ('Sony','Sony'),
        ('Toshiba','Toshiba'),
        ('Unic','Unic'),
        ('Viewsonic','Viewsonic'),
        ('Vivitek','Vivitek'),
    )
    SCREEN_RES=(
        ('3840x2160','3840x2160'),
        ('2716x1528','2716x1528'),
        ('1920x1200','1920x1200'),
        ('1920x1080','1920x1080'),
        ('1280x720','1280x720'),
        ('1280x800','1280x800'),
        ('1440x900','1440x900'),
        ('1024x768','1024x768'),
        ("800x600","800x600"),
        ('854x480','854x480'),
    )
    TYPE_SOUND=(
        ('Комплекты акустики','Комплекты акустики'),
        ('Сабвуферы','Сабвуферы'),
        ('Звуковые панели, саундбары','Звуковые панели, саундбары'),
        ('Портативные колонки','Портативные колонки'),
        ('Центральные каналы','Центральные каналы'),
        ('Встраиваемые колонки','Встраиваемые колонки'),
        ('Напольные колонки','Напольные колонки'),
        ('Полочные, подвесные колонки','Полочные, подвесные колонки'),
    )
    BRANDS_SOUND=(
        ('Attitude','Attitude'),
        ('Audiovector','Audiovector'),
        ('BBK','BBK'),
        ('Behringer','Behringer'),
        ('Bose','Bose'),
        ('Bowers & Wilkins','Bowers & Wilkins'),
        ('Cambridg Audio','Cambridg Audio'),
        ('Canton','Canton'),
        ("Dali","Dali"),
        ('Denon','Denon'),
        ('Elac','Elac'),
        ('Focal','Focal'),
        ('Gheco','Gheco'),
        ('Harman / Kardon','Harman / Kardon'),
        ('Jamo','Jamo'),
        ('JBL','JBL'),
        ('KEF','KEF'),
        ('LG','LG'),
        ('Monitor Audio','Monitor Audio'),
        ('Mistery','Mistery'),
        ('Onkyo','Onkyo'),
        ('Philips','Philips'),
        ('Pioneer','Pioneer'),
        ('RBH','RBH'),
        ('Referense Audio','Referense Audio'),
        ('REL','REL'),
        ("Samsung","Samsung"),
        ('Sharp','Sharp'),
        ('Sonos','Sonos'),
        ('Sony','Sony'),
        ('Sven','Sven'),
        ('Tannoy','Tannoy'),
        ('Ultimate','Ultimate'),
        ('Vector','Vector'),
        ('Yamaha','Yamaha'),
        ('Радиотехника','Радиотехника'),
    )
    BRANDS_THEATER=(
        ('BBK','BBK'),
        ('Bose','Bose'),
        ('Harman / Kardon','Harman / Kardon'),
        ('LG','LG'),
        ('Mistery','Mistery'),
        ('Onkyo','Onkyo'),
        ('Philips','Philips'),
        ('Pioneer','Pioneer'),
        ("Samsung","Samsung"),
        ('Sharp','Sharp'),
        ('Sony','Sony'),
        ('Yamaha','Yamaha'),
    )
    ACOUSTICS=(
        ('2.1','2.1'),
        ('4.2','4.2'),
        ('5.1','5.1'),
        ('7.1','7.1'),
        ('9.1','9.1'),
    )
    TYPE_DVD=(
        ('Медиаплееры','Медиаплееры'),
        ('DVD плееры','DVD плееры'),
        ('Blu-ray плееры, саундбары','Blu-ray плееры, саундбары'),
        ('VHS видеомагнитофоны','VHS видеомагнитофоны'),
    )
    BRANDS_DVD=(
        ('Akai','Akai'),
        ('Apple','Apple'),
        ('BBK','BBK'),
        ('Dune','Dune'),
        ('Google','Google'),
        ('Hitachi','Hitachi'),
        ('Iconbit','Iconbit'),
        ('JVC','JVC'),
        ('LG','LG'),
        ('Loewe','Loewe'),
        ('Marantz','Marantz'),
        ('MXQ','MXQ'),
        ('Mystery','Mystery'),
        ('Panasonic','Panasonic'),
        ("Philips","Philips"),
        ('Pioneer','Pioneer'),
        ('Rolsen','Rolsen'),
        ('Rombica','Rombica'),
        ('Rubin','Rubin'),
        ('Samsung','Samsung'),
        ('Sanyo','Sanyo'),
        ('Sharp','Sharp'),
        ("Sony","Sony"),
        ('Supra','Supra'),
        ('Sven','Sven'),
        ('Telefunken','Telefunken'),
        ("Thomson","Thomson"),
        ('Toshiba','Toshiba'),
        ('Xiami','Xiami'),
        ('Xoro','Xoro'),
        ('Yamaha','Yamaha'),
    )
    TYPE_CENTER=(
        ('Музыкальные центры','Музыкальные центры'),
        ('Магнитолы, магнитофоны','Магнитолы, магнитофоны'),
        ('Радиоприемники','Радиоприемники'),
        ('CD-проигрыватели','CD-проигрыватели'),
        ('Проигрыватели виниловых дисков','Проигрыватели виниловых дисков'),
    )
    BRANDS_CENTER=(
        ('BBK','BBK'),
        ('Bose','Bose'),
        ('Denon','Denon'),
        ('Huindai','Huindai'),
        ('JVC','JVC'),
        ('LG','LG'),
        ('Onkyo','Onkyo'),
        ('Panasonic','Panasonic'),
        ("Philips","Philips"),
        ('Pioneer','Pioneer'),
        ('Ritmix','Ritmix'),
        ('Samsung','Samsung'),
        ('Sony','Sony'),
        ("Supra","Supra"),
        ('Telefunken','Telefunken'),
        ('Texet','Texet'),
        ('Vitek','Vitek'),
        ('Yamaha','Yamaha'),
    )
    TYPE_MP3=(
        ('MP3, цифровые плееры','MP3, цифровые плееры'),
        ('Диктофоны','Диктофоны'),
        ('CD-плееры','CD-плееры'),
        ('Кассетные плееры','Кассетные плееры'),
    )
    BRANDS_MP3=(
        ('Aiwa','Aiwa'),
        ('Apple','Apple'),
        ('Covon','Covon'),
        ('Digma','Digma'),
        ('Explay','Explay'),
        ('Fiio','Fiio'),
        ('iRiver','iRiver'),
        ('Nexx','Nexx'),
        ("Olympus","Olympus"),
        ('Panasonic','Panasonic'),
        ('Philips','Philips'),
        ('Qumo','Qumo'),
        ('Ritmix','Ritmix'),
        ('Samsung','Samsung'),
        ('Sanyo','Sanyo'),
        ('Sony','Sony'),
        ('Texet','Texet'),
        ('xDuoo','xDuoo'),
    )
    BRANDS_BOOK=(
        ('Amazon','Aiwa'),
        ('Digma','Digma'),
        ('Gmini','Gmini'),
        ('Onix','Onix'),
        ('PocketBook','PocketBook'),
        ('Ritmix','Ritmix'),
        ('Sony','Sony'),
        ('Texet','Texet'),
        ('Wexler','Wexler'),
    )
    DIAGONAL_BOOK=(
        ('До 4.9"','До 4.9"'),
        ('От 5" до 5.9"','От 5" до 5.9"'),
        ('От 6" до 6.9"','От 6" до 6.9"'),
        ('От 7" до 7.9"','От 7" до 7.9"'),
        ('От 8" до 8.9"','От 8" до 8.9"'),
        ('От 9" до 9.9"','От 9" до 9.9"'),
        ('10" и более','10" и более'),
    )
    TYPE_DISPLAY=(
        ('E-lnk','E-lnk'),
        ('LCD, TFT','LCD, TFT'),
    )
    TYPE_SATELLITE=(
        ('Цифровое ТВ, ТВ-ресиверы','Цифровое ТВ, ТВ-ресиверы'),
        ('Спутниковое ТВ','Спутниковое ТВ'),
        ('Антенны, ТВ-ресиверы','Антенны, ТВ-ресиверы'),
        ('Кабельное ТВ','Кабельное ТВ'),
    )
    BRANDS_SATELLITE=(
        ('BBK','BBK'),
        ('Cadena','Cadena'),
        ('D-color','D-color'),
        ('Galaxy Innovations','Galaxy Innovations'),
        ('General satellite','General satellite'),
        ('Harper','Harper'),
        ('OnLime','OnLime'),
        ('Openbox','Openbox'),
        ("Oriel","Oriel"),
        ('Rolsen','Rolsen'),
        ('Selenga','Selenga'),
        ('Skywey','Skywey'),
        ('Supra','Supra'),
        ('Telefunken','Telefunken'),
        ('Tesler','Tesler'),
        ('World vision','World vision'),
        ('MTC','MTC'),
        ('НТВ-плюс','НТВ-плюс'),
        ('Ростелеком','Ростелеком'),
        ('Рускарта','Рускарта'),
        ('Триколор','Триколор'),
    )
    TYPE_RESEVER=(
        ('Усилители','Усилители'),
        ('Ресиверы','Ресиверы'),
        ('AV-процессоры','AV-процессоры'),
    )
    BRANDS_RESEVER=(
        ('Behringer','Behringer'),
        ('Cambridg Audio','Cambridg Audio'),
        ('Denon','Denon'),
        ('Fiio','Fiio'),
        ('Harman / Cardon','Harman / Cardon'),
        ('Kenwood','Kenwood'),
        ('Marantz','Marantz'),
        ('NAD','NAD'),
        ("Onkyo","Onkyo"),
        ('Pioneer','Pioneer'),
        ('Rotel','Rotel'),
        ('Sony','Sony'),
        ('Technics','Technics'),
        ('Yamaha','Yamaha'),
    )
    TYPE_HEAD=(
        ('Вкладыши','Вкладыши'),
        ('Вставные (затычки)','Вставные (затычки)'),
        ('Накладные, полноразмерные','Накладные, полноразмерные'),
        ('Игровые наушники','Игровые наушники'),
    )
    BRANDS_HEAD=(
        ('AKG','AKG'),
        ('Apple','Apple'),
        ('Audio-Technic','Audio-Technic'),
        ('Beats','Beats'),
        ('Bose','Bose'),
        ('Defender','Defender'),
        ('JBL','JBL'),
        ('Meizu','Meizu'),
        ("Panasonic","Panasonic"),
        ("Pkilips","Pkilips"),
        ('Pioneer','Pioneer'),
        ('Platronics','Platronics'),
        ('Razer','Razer'),
        ('Remax','Remax'),
        ('Samsung','Samsung'),
        ('Sennheiser','Sennheiser'),
        ('Sony','Sony'),
        ('SteelSeries','SteelSeries'),
        ('Sven','Sven'),
        ('Xiami','Xiami'),
    )
    TYPE_MICRO=(
        ('Для вокала','Для вокала'),
        ('Петличный','Петличный'),
        ('Студийный','Студийный'),
        ('Универсальный','Универсальный'),
    )
    TYPE_ACCES=(
        ('3D очки','3D очки'),
        ('Батарейки, аккумуляторы','Батарейки, аккумуляторы'),
        ('Кабели, адаптеры','Кабели, адаптеры'),
        ('Кронштейны, подставки','Кронштейны, подставки'),
        ('Пульты дистанционного управления','Пульты дистанционного управления'),
    )

    type_tv = models.CharField(max_length=50, blank=True, choices = TYPE_TV, verbose_name="Тип телевизора")
    brand_tv = models.CharField(max_length=50, blank=True, choices = BRANDS_TV, verbose_name="Марка телевизора")
    diagonal_tv = models.CharField(max_length=50, blank=True, choices = DIAGONAL_TV, verbose_name="Диагональ экрана")
    smart = models.BooleanField(default=False, verbose_name='Smart TV')
    enable_3D = models.BooleanField(default=False, verbose_name='Поддержка 3D')
    screen_tv = models.CharField(max_length=50, blank=True, choices = SCREEN_TV, verbose_name="Разрешение экрана")
    curved_screen = models.BooleanField(default=False, verbose_name='Изогнутый экран')
    wi_fi = models.BooleanField(default=False, verbose_name='Wi-fi')
    HDR = models.BooleanField(default=False, verbose_name='Поддержка HDR')
    type_projectors = models.CharField(max_length=50, blank=True, choices = TYPE_PROJECTORS, verbose_name="Тип проектора")
    brand_projectors = models.CharField(max_length=50, blank=True, choices = BRANDS_PROJECTORS, verbose_name="Марка проектора")
    screen_res = models.CharField(max_length=50, blank=True, choices = SCREEN_RES, verbose_name="Разрешение экрана")
    type_sound = models.CharField(max_length=50, blank=True, choices = TYPE_SOUND, verbose_name="Тип")
    brand_sound = models.CharField(max_length=50, blank=True, choices = BRANDS_SOUND, verbose_name="Марка")
    brand_theater = models.CharField(max_length=50, blank=True, choices = BRANDS_THEATER, verbose_name="Марка кинотеатра")
    karaoke = models.BooleanField(default=False, verbose_name='Караоке')
    acoustics = models.CharField(max_length=50, blank=True, choices = ACOUSTICS, verbose_name="Тип акустики")
    type_dvd = models.CharField(max_length=50, blank=True, choices = TYPE_DVD, verbose_name="Тип")
    portable = models.BooleanField(default=False, verbose_name='Портативный')
    brand_dvd = models.CharField(max_length=50, blank=True, choices = BRANDS_DVD, verbose_name="Марка")
    type_center = models.CharField(max_length=50, blank=True, choices = TYPE_CENTER, verbose_name="Тип")
    brand_center = models.CharField(max_length=50, blank=True, choices = BRANDS_CENTER, verbose_name="Марка")
    type_mp3 = models.CharField(max_length=50, blank=True, choices = TYPE_MP3, verbose_name="Тип")
    brand_mp3 = models.CharField(max_length=50, blank=True, choices = BRANDS_MP3, verbose_name="Марка")
    sensor = models.BooleanField(default=False, verbose_name='Сенсорный экран')
    radio = models.BooleanField(default=False, verbose_name='Радио')
    brand_book = models.CharField(max_length=50, blank=True, choices = BRANDS_BOOK, verbose_name="Марка электронной книги")
    diagonal_book = models.CharField(max_length=50, blank=True, choices = DIAGONAL_BOOK, verbose_name="Диагональ экрана")
    type_display = models.CharField(max_length=50, blank=True, choices = TYPE_DISPLAY, verbose_name="Тип дисплея")
    color_display = models.BooleanField(default=False, verbose_name='Цветной экран')
    light_display = models.BooleanField(default=False, verbose_name='Подсветка')
    type_satellite = models.CharField(max_length=50, blank=True, choices = TYPE_SATELLITE, verbose_name="Тип")
    brand_satellite = models.CharField(max_length=50, blank=True, choices = BRANDS_SATELLITE, verbose_name="Марка")
    type_resever = models.CharField(max_length=50, blank=True, choices = TYPE_RESEVER, verbose_name="Тип")
    brand_resever = models.CharField(max_length=50, blank=True, choices = BRANDS_RESEVER, verbose_name="Марка")
    type_head = models.CharField(max_length=50, blank=True, choices = TYPE_HEAD, verbose_name="Тип наушников")
    brand_head = models.CharField(max_length=50, blank=True, choices = BRANDS_HEAD, verbose_name="Марка наушников")
    volume = models.BooleanField(default=False, verbose_name='Регулировка громкости')
    woter = models.BooleanField(default=False, verbose_name='Водонепроницаемость')
    noise = models.BooleanField(default=False, verbose_name='Шумоподавление')
    type_micro = models.CharField(max_length=50, blank=True, choices = TYPE_MICRO, verbose_name="Тип микрофона")
    type_acces = models.CharField(max_length=50, blank=True, choices = TYPE_ACCES, verbose_name="Тип аксессуара")

    class Meta:
        verbose_name = "ТВ, аудио, видео"
        verbose_name_plural = "ТВ, аудио, видео"
