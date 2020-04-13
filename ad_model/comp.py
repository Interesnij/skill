from django.db import models
from ad_posts.models import Ad


class Comp(Ad):
    TYPE_LAPTOP=(
        ('Ноутбуки','Ноутбуки'),
        ('Нетбуки','Нетбуки'),
        ('Трансформеры','Трансформеры'),
    )
    TYPE_COMP=(
        ('Настольные, системные блоки','Настольные, системные блоки'),
        ('Моноблоки','Моноблоки'),
        ('Мини ПК, неттопы','Мини ПК, неттопы'),
    )
    BRANDS_LAPTOP=(
        ('Acer','Acer'),
        ('Alienware','Alienware'),
        ('Apple','Apple'),
        ('ASUS','ASUS'),
        ('DELL','DELL'),
        ('Dexp','Dexp'),
        ('DNS','DNS'),
        ('Fujitsu','Fujitsu'),
        ("Haier","Haier"),
        ('HP','HP'),
        ('Huawei','Huawei'),
        ('Lenovo','Lenovo'),
        ('MSI','MSI'),
        ('Packard Bell','Packard Bell'),
        ('Panasonic','Panasonic'),
        ('Prestigio','Prestigio'),
        ('Samsung','Samsung'),
        ('Sony','Sony'),
        ('Toshiba','Toshiba'),
    )
    DIAGONAL=(
        ('12.5" и менее','12.5" и менее'),
        ('От 13" до 14.6"','От 13" до 14.6"'),
        ('От 15" до 16.4"','От 15" до 16.4"'),
        ('От 16.5" и более','От 16.5" и более'),
    )
    OPERATIV=(
        ('До 1 ГБ','До 1 ГБ'),
        ('1 Гб','1 Гб'),
        ('2 Гб','2 Гб'),
        ('3 Гб','3 Гб'),
        ('4 Гб','4 Гб'),
        ('6 Гб','6 Гб'),
        ('8 Гб','8 Гб'),
        ('12 Гб','12 Гб'),
        ('16 Гб','16 Гб'),
        ('24 Гб','24 Гб'),
        ('32 Гб','32 Гб'),
        ('64 Гб','64 Гб'),
        ('Более 64 Гб','Более 64 Гб'),
    )
    USE=(
        ('Новый','Новый'),
        ('До 6 мес','До 6 мес'),
        ('1 год','1 год'),
        ('2 года','2 года'),
        ('от 3 лет и более','от 3 лет и более'),
    )
    VIDEO_CARD=(
        ('Встроенная','Встроенная'),
        ('Дискретная','Дискретная'),
    )
    TYPE_DRIVE=(
        ('Blu-ray','Blu-ray'),
        ('DVD','DVD'),
        ('DVD-RW','DVD-RW'),
        ('DVD-CD/RW','DVD-CD/RW'),
        ('Отсутствует','Отсутствует'),
    )
    TYPE_MONITOR=(
        ('Для дома и офиса','Для дома и офиса'),
        ('Игровой','Игровой'),
        ('Профессиональный','Профессиональный'),
    )
    BRANDS_MONITOR=(
        ('Acer','Acer'),
        ('AOC','AOC'),
        ('Apple','Apple'),
        ('ASUS','ASUS'),
        ('BenQ','BenQ'),
        ('DELL','DELL'),
        ('HP','HP'),
        ('Liyama','Liyama'),
        ('Lenovo','Lenovo'),
        ('LG','LG'),
        ('NEC','NEC'),
        ('Packard Bell','Packard Bell'),
        ('Philips','Philips'),
        ('Samsung','Samsung'),
        ('Toshiba','Toshiba'),
        ('Viewsonic','Viewsonic'),
    )
    DIAGONAL_MON=(
        ('Менее 14"','Менее 14"'),
        ('От 14" до 14.9"','От 14" до 14.9"'),
        ('От 15" до 15.9"','От 15" до 15.9"'),
        ('От 16" до 16.9"','От 16" до 16.9"'),
        ('От 17" до 17.9"','От 17" до 17.9"'),
        ('От 18" до 18.9"','От 18" до 18.9"'),
        ('От 19" до 19.9"','От 19" до 19.9"'),
        ('От 20" до 20.9"','От 20" до 20.9"'),
        ('От 21" до 21.9"','От 21" до 21.9"'),
        ('От 22" до 22.9"','От 22" до 22.9"'),
        ('От 23" до 23.9"','От 23" до 23.9"'),
        ('От 24" до 24.9"','От 24" до 24.9"'),
        ('От 25" до 25.9"','От 25" до 25.9"'),
        ('От 26" до 26.9"','От 26" до 26.9"'),
        ('От 27" до 27.9"','От 27" до 27.9"'),
        ('От 28" до 28.9"','От 28" до 28.9"'),
        ('От 29" до 29.9"','От 29" до 29.9"'),
        ('От 30" и более','От 30" и более'),
    )
    HDMI=(
        ('1 шт','1 шт'),
        ('2 шт','2 шт'),
        ('4 шт','4 шт'),
    )
    TYPE_KEY=(
        ('Клавиатуры','Клавиатуры'),
        ('Мыши','Мыши'),
    )
    TYPE_CONNECT=(
        ('Проводные','Проводные'),
        ('Беспроводные','Беспроводные'),
    )
    BRANDS_KEY=(
        ('A4Tech','A4Tech'),
        ('Apple','Apple'),
        ('ASUS','ASUS'),
        ('Defender','Defender'),
        ('Genius','Genius'),
        ('HP','HP'),
        ('Logitech','Logitech'),
        ('Microsoft','Microsoft'),
        ('Oklick','Oklick'),
        ('Razer','Razer'),
        ('Steel Series','Steel Series'),
        ('Sven','Sven'),
    )
    OFFICE=(
        ('Принтеры','Принтеры'),
        ('3D принтеры','3D принтеры'),
        ('Сканеры','Сканеры'),
        ('Плоттеры','Плоттеры'),
        ('Копиры','Копиры'),
        ('МФУ','МФУ'),
        ('Шредеры, уничтожители бумаг','Шредеры, уничтожители бумаг'),
        ('Факсы','Факсы'),
        ('Ламинаторы','Ламинаторы'),
        ('Переплетчики, брошюровщики','Переплетчики, брошюровщики'),
        ('Картриджи, чернила, тонеры','Картриджи, чернила, тонеры'),
        ('Бумага для печати','Бумага для печати'),
        ('Аксессуары для оргтехники','Аксессуары для оргтехники'),
    )
    NETWORK=(
        ('ADSL модемы','ADSL модемы'),
        ('USB, 3G модемы','USB, 3G модемы'),
        ('Роуторы, маршрутизаторы','Роуторы, маршрутизаторы'),
        ('Коммутаторы','Коммутаторы'),
        ('Точки доступа','Точки доступа'),
        ('Усилители сигнала, антенны','Усилители сигнала, антенны'),
        ('Серверы','Серверы'),
        ('Принт-серверы','Принт-серверы'),
        ('Сетевые карты','Сетевые карты'),
        ('Сетевые хранилища (NAS)','Сетевые хранилища (NAS)'),
        ('Сетевые кабели, разъемы','Сетевые кабели, разъемы'),
        ('Трансиверы, конвертеры','Трансиверы, конвертеры'),
        ('WI-FI, bluetooth адаптеры','WI-FI, bluetooth адаптеры'),
        ('VoIP-оборудование','VoIP-оборудование'),
    )
    MULTIMEDIA=(
        ('Веб-камеры','Веб-камеры'),
        ('Графические планшеты','Графические планшеты'),
        ('Очки виртуальной реальности','Очки виртуальной реальности'),
        ('Компьютерные колонки','Компьютерные колонки'),
        ('Компьютерные гарнитуры','Компьютерные гарнитуры'),
        ('Компьютерные микрофоны','Компьютерные микрофоны'),
    )
    FLASH=(
        ('Карты памяти','Карты памяти'),
        ('USb флеш-карты','USb флеш-карты'),
        ('Очки виртуальной реальности','Очки виртуальной реальности'),
        ('Внешние жесткие диски','Внешние жесткие диски'),
        ('Диски, дискеты','Диски, дискеты'),
    )
    PO=(
        ('Антивирусы','Антивирусы'),
        ('Восстановление данных','Восстановление данных'),
        ('Графика, дизайн','Графика, дизайн'),
        ('Обработка аудио, видео','Обработка аудио, видео'),
        ('Обучение, образование','Обучение, образование'),
        ('Операционные системы','Операционные системы'),
        ('Офисные программы','Офисные программы'),
        ('Управление предприятием','Управление предприятием'),
        ('Утилиты, драйверы','Утилиты, драйверы'),
    )
    PAD=(
        ('Геймпады','Геймпады'),
        ('Рули','Рули'),
        ('Джойстики, штурвалы','Джойстики, штурвалы'),
    )
    BRANDS_PAD=(
        ('A4Tech','A4Tech'),
        ('Defender','Defender'),
        ('Dialog','Dialog'),
        ('Exeq','Exeq'),
        ('Genius','Genius'),
        ('Logitech','Logitech'),
        ('Microsoft','Microsoft'),
        ('Momo','Momo'),
        ('Oklick','Oklick'),
        ('Razer','Razer'),
        ('Saltek','Saltek'),
        ('SpeedLink','SpeedLink'),
        ('ThrustMaster','ThrustMaster'),
        ('Thrust','Thrust'),
        ('Xiami','Xiami'),
    )
    SPARE=(
        ('CD, DVD, Blu-ray приводы','CD, DVD, Blu-ray приводы'),
        ('Аккумуляторы','Аккумуляторы'),
        ('Блоки питания','Блоки питания'),
        ('Видеокарты','Видеокарты'),
        ('Жесткие диски','Жесткие диски'),
        ('Звуковые карты','Звуковые карты'),
        ('Клавиатуры для ноутбуков','Клавиатуры для ноутбуков'),
        ('Контроллеры','Контроллеры'),
        ('Корпуса','Корпуса'),
        ('Кулеры, системы охлаждения','Кулеры, системы охлаждения'),
        ('Материнские платы','Материнские платы'),
        ('Матрицы, экраны','Матрицы, экраны'),
        ('Оперативная память','Оперативная память'),
        ('Процессоры','Процессоры'),
        ('TV-тюнеры, видеозахват','TV-тюнеры, видеозахват'),
        ('Шлейфы','Шлейфы'),
    )
    ACS=(
        ('USB-контроллеры, хабы','USB-контроллеры, хабы'),
        ('USB-гаджеты','USB-гаджеты'),
        ('Кабели, разъемы, переходники','Кабели, разъемы, переходники'),
        ('Коврики для мышей','Коврики для мышей'),
        ('Подставки, кронштейны','Подставки, кронштейны'),
        ('Сумки, чехлы для ноутбуков','Сумки, чехлы для ноутбуков'),
    )
    DEVICE=(
        ('Для компьютеров','Для компьютеров'),
        ('Для ноутбуков','Для ноутбуков'),
    )

    type_laptop = models.CharField(max_length=50, blank=True, choices = TYPE_LAPTOP, verbose_name="Тип ноутбука")
    brand_laptop = models.CharField(max_length=50, blank=True, choices = BRANDS_LAPTOP, verbose_name="Марка ноутбука")
    diagonal = models.CharField(max_length=50, blank=True, choices = DIAGONAL, verbose_name="Диагональ экрана")
    operative = models.CharField(max_length=50, blank=True, choices = OPERATIV, verbose_name="Оперативная память")
    use = models.CharField(max_length=50, blank=True, choices = USE, verbose_name="Срок использования")
    game = models.BooleanField(default=False, verbose_name='Игровой')
    type_comp = models.CharField(max_length=50, blank=True, choices = TYPE_COMP, verbose_name="Тип компьютера")
    video_card = models.CharField(max_length=50, blank=True, choices = VIDEO_CARD, verbose_name="Тип видеокарты")
    type_drive = models.CharField(max_length=50, blank=True, choices = TYPE_DRIVE, verbose_name="Тип оптического привода")
    type_monitor = models.CharField(max_length=50, blank=True, choices = TYPE_MONITOR, verbose_name="Тип монитора")
    brand_monitor = models.CharField(max_length=50, blank=True, choices = BRANDS_MONITOR, verbose_name="Марка монитора")
    diagonal_mon = models.CharField(max_length=50, blank=True, choices = DIAGONAL_MON, verbose_name="Диагональ экрана")
    hdmi = models.CharField(max_length=50, blank=True, choices = HDMI, verbose_name="Разъем HDMI")
    dinam = models.BooleanField(default=False, verbose_name='Встроенные динамики')
    USB = models.BooleanField(default=False, verbose_name='USB разъем')
    type_key = models.CharField(max_length=50, blank=True, choices = TYPE_KEY, verbose_name="Тип")
    type_connect = models.CharField(max_length=50, blank=True, choices = TYPE_CONNECT, verbose_name="Тип подключения")
    brand_key = models.CharField(max_length=50, blank=True, choices = BRANDS_KEY, verbose_name="Бренд")
    office = models.CharField(max_length=50, blank=True, choices = OFFICE, verbose_name="Оргтехника и расходники")
    network = models.CharField(max_length=50, blank=True, choices = NETWORK, verbose_name="Сетевое оборудование")
    multimedia = models.CharField(max_length=50, blank=True, choices = MULTIMEDIA, verbose_name="Мультимедиа")
    flash = models.CharField(max_length=50, blank=True, choices = FLASH, verbose_name="Накопители данных и картридеры")
    po = models.CharField(max_length=50, blank=True, choices = PO, verbose_name="Программное обеспечение")
    pad = models.CharField(max_length=50, blank=True, choices = PAD, verbose_name="Рули, джойстики, геймпады")
    brand_pad = models.CharField(max_length=50, blank=True, choices = BRANDS_PAD, verbose_name="Марка")
    spare = models.CharField(max_length=50, blank=True, choices = SPARE, verbose_name="Запчасти")
    acs = models.CharField(max_length=50, blank=True, choices = ACS, verbose_name="Аксессуары")
    device = models.CharField(max_length=50, blank=True, choices = DEVICE, verbose_name="Устройство")

    class Meta:
        verbose_name = "Компьютерная техника"
        verbose_name_plural = "Компьютерная техника"
