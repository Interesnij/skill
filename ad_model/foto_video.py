from django.db import models
from ad_posts.models import Ad


class FotoVideo(Ad):
    TYPE_FOTO=(
        ('Пленочные','Пленочные'),
        ('Цифровые','Цифровые'),
    )
    CAT_FOTO=(
        ('Компактные','Компактные'),
        ('Зеркальные','Зеркальные'),
        ('Беззеркальные со сменной оптикой','Беззеркальные со сменной оптикой'),
        ('Моментальные печати','Моментальные печати'),
    )
    BRANDS_FOTO=(
        ('AAE','AAE'),
        ('BBK','BBK'),
        ('Canon','Canon'),
        ('Casio','Casio'),
        ('Digicare','Digicare'),
        ('Fujifilm','Fujifilm'),
        ('Genius','Genius'),
        ('HP','HP'),
        ('Insignia','Insignia'),
        ('Kodak','Kodak'),
        ('Konica Minolta','Konica Minolta'),
        ('Leica','Leica'),
        ('Lytro','Lytro'),
        ('Nikon','Nikon'),
        ('Olympus','Olympus'),
        ('Polaroid','Polaroid'),
        ('Panasonic Lumix','Panasonic Lumix'),
        ('Pentax','Pentax'),
        ('Rekam','Rekam'),
        ('Ricoh','Ricoh'),
        ('Sanyo','Sanyo'),
        ("Sigma","Sigma"),
        ('Sony','Sony'),
        ('Xiomi, YI','Xiomi, YI'),
        ('Зенит (Zenit)','Зенит (Zenit)'),
    )
    BRANDS_VIDEO=(
        ('AAE','AAE'),
        ('BQ','BQ'),
        ('Canon','Canon'),
        ('Digicare','Digicare'),
        ('Djl','Djl'),
        ('Eken','Eken'),
        ('Ginzzu','Ginzzu'),
        ('Gmini','Gmini'),
        ('GoPro','GoPro'),
        ('JVC','JVC'),
        ('Lexand','Lexand'),
        ('Olympus','Olympus'),
        ('Polaroid','Polaroid'),
        ('Panasonic','Panasonic'),
        ('Rekam','Rekam'),
        ('Ricoh','Ricoh'),
        ('Samsung','Samsung'),
        ("SJCAM","SJCAM"),
        ('Sony','Sony'),
        ('Xiomi, YI','Xiomi, YI'),
        ('X-TRY','X-TRY'),
    )
    STABILIZER=(
        ('Нет','Нет'),
        ('Оптический','Оптический'),
        ('Цифровой','Цифровой'),
    )
    QUALITY=(
        ('576p и менее','576p и менее'),
        ('760p HD','760p HD'),
        ('1080p Full HD','1080p Full HD'),
        ('2.5K QHD','2.5K QHD'),
        ('4K UHD','4K UHD'),
    )
    MEDIA=(
        ('Жесткий диска, Flash','Жесткий диска, Flash'),
        ('Кассета','Кассета'),
        ('Оптический диск','Оптический диск'),
    )
    ZOOM=(
        ('Нет','Нет'),
        ('Менее 5х','Менее 5х'),
        ('От 5 до 9.9х','От 5 до 9.9х'),
        ('От 10 до 19.9х','От 10 до 19.9х'),
        ('От 20 до 29.9х','От 20 до 29.9х'),
        ('От 30 до 39.9х','От 30 до 39.9х'),
        ('От 40 до 49.9х','От 40 до 49.9х'),
        ('50х и более','50х и более'),
    )
    CONTROL=(
        ('IP-камеры','IP-камеры'),
        ('Аналоговые камеры','Аналоговые камеры'),
    )
    CONNECTION=(
        ('Проводные','Проводные'),
        ('Беспроводные','Беспроводные'),
    )
    BRANDS_LENS=(
        ('Canon','Canon'),
        ('Carl Zeiss','Carl Zeiss'),
        ('Fujifilm','Fujifilm'),
        ('Nicon','Nicon'),
        ('Olympus','Olympus'),
        ('Panasonic Lumix','Panasonic Lumix'),
        ('Pentax','Pentax'),
        ('Samyang','Samyang'),
        ("Sigma","Sigma"),
        ('Sony','Sony'),
        ('Tamron','YongNuo'),
        ('YongNuo','YongNuo'),
        ('Зенит','Зенит'),
        ('Юпитер','Юпитер'),
    )
    TYPE_LENS=(
        ('Рыбий глаз','Рыбий глаз'),
        ('Микрообъективы','Микрообъективы'),
        ('Стандартные объективы','Стандартные объективы'),
        ('Телеобъективы','Телеобъективы'),
        ('Широкоугольные объективы','Широкоугольные объективы'),
    )
    TYPE_BAYONET=(
        ('4/3','4/3'),
        ('Bronica','Bronica'),
        ('Canon EF','Canon EF'),
        ('Canon EF-M','Canon EF-M'),
        ('Canon EF-S','Canon EF-S'),
        ('Canon FD','Canon FD'),
        ('Canon Fl','Canon Fl'),
        ('Fujifilm G Mount','Fujifilm G Mount'),
        ('Fujifilm X Mount','Fujifilm X Mount'),
        ('Hasselblad CF','Hasselblad CF'),
        ('Hasselblad HC','Hasselblad HC'),
        ('Hasselblad XCD','Hasselblad XCD'),
        ('Konica AR','Konica AR'),
        ('Leica L','Leica L'),
        ('Leica M','Leica M'),
        ('Leica R','Leica R'),
        ('Leica S','Leica S'),
        ('Leica T','Leica T'),
        ('Mamiya 645','Mamiya 645'),
        ('Mamiya 7','Mamiya 7'),
        ('Micro 4/3','Micro 4/3'),
        ('Minolta A (Sony Alpha)','Minolta A (Sony Alpha)'),
        ('Minolta SR','Minolta SR'),
        ('Nicon 1','Nicon 1'),
        ('Nicon F','Nicon F'),
        ('Olimpus Micro 4/3','Olimpus Micro 4/3'),
        ('Olimpus OM','Olimpus OM'),
        ('Pentacon 6','Pentacon 6'),
        ('Pentax 645','Pentax 645'),
        ('Pentax 67','Pentax 67'),
        ('Pentax KA/KAF/KAF2/KAF3','Pentax KA/KAF/KAF2/KAF3'),
        ('Pentax Q','Pentax Q'),
        ('Ricoh GXR','Ricoh GXR'),
        ('Samsung NX','Samsung NX'),
        ('Samsung NX-M','Samsung NX-M'),
        ('Sigma SA','Sigma SA'),
        ('Sony E','Sony E'),
        ('T-mount','T-mount'),
        ('Резьба М39','Резьба М39'),
        ('Резьба М42','Резьба М42'),
    )
    TYPE_FLASHES=(
        ('Обычные','Обычные'),
        ('Кольцевые','Кольцевые'),
        ('Двухламповые','Двухламповые'),
        ('Для подводной съемки','Для подводной съемкиы'),
    )
    BRANDS_FLASHES=(
        ('Canon','Canon'),
        ('Falcon Eyes','Falcon Eyes'),
        ('Fujifilm','Fujifilm'),
        ('Codox','Codox'),
        ('Kodak','Kodak'),
        ('Nicon','Nicon'),
        ('Meike','Meike'),
        ('Minolta','Minolta'),
        ('Nicon','Nicon'),
        ('Nissin','Nissin'),
        ('Olympus','Olympus'),
        ('Panasonic','Panasonic'),
        ('Pentax','Pentax'),
        ('Pixel','Pixel'),
        ("Sigma","Sigma"),
        ('Sony','Sony'),
        ('YongNuo','YongNuo'),
    )
    TYPE_AKS=(
        ('Адаптеры, переходные кольца','Адаптеры, переходные кольца'),
        ('Аккумуляторы, зарядные устройства','Аккумуляторы, зарядные устройства'),
        ('Бленды, насадки на объективы','Бленды, насадки на объективы'),
        ('Видеоискатели, наглазники','Видеоискатели, наглазники'),
        ('Для подводной съемки','Для подводной съемки'),
        ('Защитные пленки, стекла','Защитные пленки, стекла'),
        ('Конвертеры для объективов','Конвертеры для объективов'),
        ('Крышки на объективы','Крышки на объективы'),
        ('Микрофоны','Микрофоны'),
        ('Провода, кабели','Провода, кабели'),
        ('Пульты дистанционного управления','Пульты дистанционного управления'),
        ('Светофильтры','Светофильтры'),
        ('Сумки, ремни, чехлы','Сумки, ремни, чехлы'),
        ('Фотопленка','Фотопленка'),
    )
    TRIPODS=(
        ('Триподы','Триподы'),
        ('Моноподы','Моноподы'),
        ('Плечевые упоры, обвесы','Плечевые упоры, обвесы'),
        ('Стабилизаторы, Steadicam','Стабилизаторы, Steadicam'),
    )
    STUDIO=(
        ('Лампы, студийный свет','Лампы, студийный свет'),
        ('Отражатели, рефлекторы','Отражатели, рефлекторы'),
        ('Софтбоксы','Софтбоксы'),
        ('Фоны, фромакеи','Фоны, фромакеи'),
        ('Фотобоксы, лайткубы','Фотобоксы, лайткубы'),
    )
    FRAME=(
        ('Менее 7"','Менее 7"'),
        ('От 7.1" до 7.9"','От 7.1" до 7.9"'),
        ('От 9.1" до 12"','От 9.1" до 12"'),
        ('От 12.1" до 15"','От 12.1" до 15"'),
        ('Более 15"','Более 15"'),
    )
    BRANDS_COMPACT=(
        ('Canon','Canon'),
        ('Epson','Epson'),
        ('HP','HP'),
        ('Kodak','Kodak'),
        ('LG','LG'),
        ('Sony','Sony'),
    )
    TYPE_OPTICS=(
        ('Бинокли','Бинокли'),
        ('Лупы','Лупы'),
        ('Микроскопы','Микроскопы'),
        ('Окуляры','Окуляры'),
        ('Подзорные трубы','Подзорные трубы'),
        ('Приборы ночного видения','Приборы ночного видения'),
        ('Телескопы','Телескопы'),
    )

    type_foto = models.CharField(max_length=50, blank=True, choices = TYPE_FOTO, verbose_name="Тип фотоаппарата")
    cat_foto = models.CharField(max_length=50, blank=True, choices = CAT_FOTO, verbose_name="Категория камеры")
    brand_foto = models.CharField(max_length=50, blank=True, choices = BRANDS_FOTO, verbose_name="Марка камеры")
    viewfinder = models.BooleanField(default=False, verbose_name='Видоискатель')
    stabilizer = models.CharField(max_length=50, blank=True, choices = STABILIZER, verbose_name="Стабилизатор изображения")
    type_video = models.CharField(max_length=50, blank=True, choices = BRANDS_VIDEO, verbose_name="Марка видеокамеры")
    quality = models.CharField(max_length=50, blank=True, choices = QUALITY, verbose_name="Качество видео")
    media = models.CharField(max_length=50, blank=True, choices = MEDIA, verbose_name="Формат носителя")
    zoom = models.CharField(max_length=50, blank=True, choices = ZOOM, verbose_name="Оптический Zoom")
    action = models.BooleanField(default=False, verbose_name='Экшн-камера')
    s360 = models.BooleanField(default=False, verbose_name='Съемка в 360 градусов')
    video_control = models.CharField(max_length=50, blank=True, choices = CONTROL, verbose_name="Тип видеонаблюдение")
    connection = models.CharField(max_length=50, blank=True, choices = CONNECTION, verbose_name="Тип подключения")
    wi_fi = models.BooleanField(default=False, verbose_name='Wi-fi')
    monitor_sensor = models.BooleanField(default=False, verbose_name='Датчик движения')
    microfon = models.BooleanField(default=False, verbose_name='Встроенный микрофон')
    brand_lens = models.CharField(max_length=50, blank=True, choices = BRANDS_LENS, verbose_name="Марка объектива")
    type_lens = models.CharField(max_length=50, blank=True, choices = TYPE_LENS, verbose_name="Тип объектива")
    type_bayonet = models.CharField(max_length=50, blank=True, choices = TYPE_BAYONET, verbose_name="Тип байонета")
    autofocus = models.BooleanField(default=False, verbose_name='Автофокус')
    type_flashes = models.CharField(max_length=50, blank=True, choices = TYPE_FLASHES, verbose_name="Тип фотовспышки")
    brand_flashes = models.CharField(max_length=50, blank=True, choices = BRANDS_FLASHES, verbose_name="Марка фотовспышки")
    swivel_head = models.BooleanField(default=False, verbose_name='Поворотная головка')
    type_aks = models.CharField(max_length=50, blank=True, choices = TYPE_FLASHES, verbose_name="Тип аксессуара")
    tripods = models.CharField(max_length=50, blank=True, choices = TRIPODS, verbose_name="Штативы и стабилизаторы")
    studio = models.CharField(max_length=50, blank=True, choices = STUDIO, verbose_name="Студийное оборудование")
    frame = models.CharField(max_length=50, blank=True, choices = FRAME, verbose_name="Фоторамки")
    video = models.BooleanField(default=False, verbose_name='Воспроизведение видео')
    brand_compact = models.CharField(max_length=50, blank=True, choices = BRANDS_COMPACT, verbose_name="Компактные фотопринтеры")
    type_optics = models.CharField(max_length=50, blank=True, choices = TYPE_OPTICS, verbose_name="Тип")

    class Meta:
        verbose_name = "Фото и видео"
        verbose_name_plural = "Фото и видео"
