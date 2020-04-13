from django.db import models
from ad_posts.models import Ad


class Auto(Ad):
    BRANDS=(
        ('Acura','Acura'),
        ('AC','AC'),
        ('Alfa Romeo','Alfa Romeo'),
        ('Alpina','Alpina'),
        ('Aro','Aro'),
        ('Asia','Asia'),
        ('Aston Martin','Aston Martin'),
        ('Audi','Audi'),
        ('BAW','BAW'),
        ('Bentley','Bentley'),
        ('BMW','BMW'),
        ('Brilliance','Brilliance'),
        ('Bugatti','Bugatti'),
        ('Buick','Buick'),
        ('BYD','BYD'),
        ('Cadillac','Cadillac'),
        ('Changan','Changan'),
        ('ChangFeng','ChangFeng'),
        ('Chery','Chery'),
        ('Chevrolet','Chevrolet'),
        ('Chrysler','Chrysler'),
        ('Citroen','Citroen'),
        ('Dacia','Dacia'),
        ('Dadi','Dadi'),
        ('Daewoo','Daewoo'),
        ('Daihatsu','Daihatsu'),
        ('Daimler','Daimler'),
        ('Datsun','Datsun'),
        ('Derways','Derways'),
        ('Dodge','Dodge'),
        ('Dongfeng','Dongfeng'),
        ('Doninvest','Doninvest'),
        ('DS','DS'),
        ('DW Hover','DW Hover'),
        ('Eagle','Eagle'),
        ('FAW','FAW'),
        ('Ferrari','Ferrari'),
        ('FIAT','FIAT'),
        ('Ford','Ford'),
        ('Foton','Foton'),
        ('GAC','GAC'),
        ('Geely','Geely'),
        ('Genesis','Genesis'),
        ('Geo','Geo'),
        ('GMC','GMC'),
        ('Great Wall','Great Wall'),
        ('Hafei','Hafei'),
        ('Haima','Haima'),
        ('Haval','Haval'),
        ('Hawtai','Hawtai'),
        ('Honda','Honda'),
        ('HuangHai','HuangHai'),
        ('Hummer','Hummer'),
        ('Hyindai','Hyindai'),
        ('Infiniti','Infiniti'),
        ('Iran Khondro','Iran Khondro'),
        ('Isuzu','Isuzu'),
        ('Iveco','Iveco'),
        ('JAC','JAC'),
        ('Jaguar','Jaguar'),
        ('Jeep','Jeep'),
        ('Jinbei','Jinbei'),
        ('JMC','JMC'),
        ('KIA','KIA'),
        ('Lambordhini','Lambordhini'),
        ('Lancia','Lancia'),
        ('Land Rover','Land Rover'),
        ('Landwind','Landwind'),
        ('LDV','LDV'),
        ('Lexus','Lexus'),
        ('LIFAN','LIFAN'),
        ('Lincoln','Lincoln'),
        ('Lotus','Lotus'),
        ('Luxgen','Luxgen'),
        ('Mahindra','Mahindra'),
        ('Maserati','Maserati'),
        ('Maybach','Maybach'),
        ('Mazda','Mazda'),
        ('Mercedes-Benz','Mercedes-Benz'),
        ('Mercury','Mercury'),
        ('Metrocab','Metrocab'),
        ('MG','MG'),
        ('MINI','MINI'),
        ('Mitsubishi','Mitsubishi'),
        ('Mitsuoka','Mitsuoka'),
        ('Morgan','Morgan'),
        ('Morris','Morris'),
        ('Nissan','Nissan'),
        ('Oldsmobile','Oldsmobile'),
        ('Opel','Opel'),
        ('Peugeot','Peugeot'),
        ('Plymouth','Plymouth'),
        ('Pontiac','Pontiac'),
        ('Porsche','Porsche'),
        ('Proton','Proton'),
        ('Ravon','Ravon'),
        ('Renault','Renault'),
        ('Rolls-Royce','Rolls-Royce'),
        ('Ronart','Ronart'),
        ('Rover','Rover'),
        ('Saab','Saab'),
        ('Saturn','Saturn'),
        ('Scion','Scion'),
        ('SEAT','SEAT'),
        ('Shuanghuan','Shuanghuan'),
        ('Scoda','Scoda'),
        ('SMA','SMA'),
        ('Smart','Smart'),
        ('SsangYong','SsangYong'),
        ('Subaru','Subaru'),
        ('Suzuki','Suzuki'),
        ('Talbot','Talbot'),
        ('Tata','Tata'),
        ('Tesla','Tesla'),
        ('Tianma','Tianma'),
        ('Tianye','Tianye'),
        ('Toyota','Toyota'),
        ('Trabant','Trabant'),
        ('Volkswagen','Volkswagen'),
        ('Volvo','Volvo'),
        ('Vortex','Vortex'),
        ('Watrburg','Watrburg'),
        ('Xin Kai','Xin Kai'),
        ('ZOTYE','ZOTYE'),
        ('ZX','ZX'),
        ('ВАЗ (LADA)','ВАЗ (LADA)'),
        ('ВИС','ВИС'),
        ('ГАЗ','ГАЗ'),
        ('ЗАЗ','ЗАЗ'),
        ('ЗИЛ','ЗИЛ'),
        ('ИЖ','ИЖ'),
        ('ЛуАЗ','ЛуАЗ'),
        ('Москвич','Москвич'),
        ('РАФ','РАФ'),
        ('СМЗ','СМЗ'),
        ('ТагАЗ','ТагАЗ'),
        ('УАЗ','УАЗ'),
    )
    CONDITION =(
        ('Не битый','Не битый'),
        ('Битый','Битый'),
    )
    TO =(
        ('Есть сервисная книжка','Есть сервисная книжка'),
        ('Обслуживался у дилера','Обслуживался у дилера'),
        ('На гарантии','На гарантии'),
    )
    PS =(
        ('Гидро-','Гидро-'),
        ('Электро-','Электро-'),
        ('Электрогидро-','Электрогидро-'),
    )
    SALON =(
        ('Кожа','Кожа'),
        ('Ткань','Ткань'),
        ('Велюр','Велюр'),
        ('Комбинированный','Комбинированный'),
    )
    СС =(
        ('Кондиционер','Кондиционер'),
        ('Климат-контроль однозонный','Климат-контроль однозонный'),
        ('Климат-контроль многозонный','Климат-контроль многозонный'),
    )
    AUDIO =(
        ('2 колонки','2 колонки'),
        ('4 колонки','4 колонки'),
        ('6 колонок','6 колонок'),
        ('8+ колонок','8+ колонок'),
    )
    HEADLINES=(
        ('Галогенные','Галогенные'),
        ('Ксеноновые','Ксеноновые'),
        ('Светодиодные','Светодиодные'),
    )
    TIRES=(
        ('7"','7"'),
        ('8"','8"'),
        ('9"','9"'),
        ('10"','10"'),
        ('11"','11"'),
        ('12"','12"'),
        ('13"','13"'),
        ('14"','14"'),
        ('15"','15"'),
        ('16"','16"'),
        ('17"','17"'),
        ('18"','18"'),
        ('19"','19"'),
        ('20"','20"'),
        ('21"','21"'),
        ('22"','22"'),
        ('23"','23"'),
        ('24"','24"'),
        ('25"','25"'),
        ('26"','26"'),
        ('27"','27"'),
        ('28"','28"'),
        ('29"','29"'),
        ('30"','30"'),
    )
    COLOR=(
        ('Белый','Белый'),
        ('Серебряный','Серебряный'),
        ('Серый','Серый'),
        ('Чёрный','Чёрный'),
        ('Коричневый','Коричневый'),
        ('Золотой','Золотой'),
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
    )

    brand = models.CharField(max_length=50, blank=True, choices = BRANDS, verbose_name="Марка автомобиля")
    model = models.CharField(max_length=100, blank=True, verbose_name="Модель автомобиля")
    year = models.CharField(max_length=100, blank=True, verbose_name="Год выпуска")
    color=models.CharField(max_length=45, blank=True, choices = COLOR, verbose_name="Цвет")
    run = models.CharField(max_length=100, blank=True, verbose_name="Пробег")
    condition = models.CharField(max_length=50, blank=True, choices = CONDITION, verbose_name="Состояние")
    to = models.CharField(max_length=50, blank=True, choices = TO, verbose_name="Данные о ТО")
    power_steering = models.CharField(max_length=50, blank=True, choices = PS, verbose_name="Усилитель руля")
    link=models.CharField(max_length=100, blank=True, verbose_name="Видео c YouTube")
    place_of_inspection=models.CharField(max_length=200, blank=True, verbose_name="Место осмотра")

     # Салон
    salon = models.CharField(max_length=50, blank=True, choices = SALON, verbose_name="Салон")
    leather_steering_wheel = models.BooleanField(default=False, verbose_name='Кожаный руль')
    hatch = models.BooleanField(default=False, verbose_name='Люк')

    # Управление климатом
    climate_control = models.CharField(max_length=50, blank=True, choices = СС, verbose_name="Управление климатом")
    steering_wheel_control = models.BooleanField(default=False, verbose_name='Управление на руле')
    athermal_glazing = models.BooleanField(default=False, verbose_name='Атермальное остекление')

    # Обогрев
    heated_front_seats = models.BooleanField(default=False, verbose_name='Обогрев передних сидений')
    heated_reart_seats = models.BooleanField(default=False, verbose_name='Обогрев задних сидений')
    heated_mirrors = models.BooleanField(default=False, verbose_name='Обогрев зеркал')
    heated_rear_window = models.BooleanField(default=False, verbose_name='Обогрев заднего стекла')
    heated_steering_column = models.BooleanField(default=False, verbose_name='Обогрев рулевой колонки')

    # Электропривод
    front_seats = models.BooleanField(default=False, verbose_name='Электропривод передних сидений')
    back_seats = models.BooleanField(default=False, verbose_name='Электропривод задних сидений')
    mirrors = models.BooleanField(default=False, verbose_name='Электропривод зеркал')
    folding_mirrors = models.BooleanField(default=False, verbose_name='Складывание зеркал')
    steering_column = models.BooleanField(default=False, verbose_name='Электропривод рулевой колонки')

    # Память настроек
    memory_front_seats = models.BooleanField(default=False, verbose_name='Память передних сидений')
    memory_reart_seats = models.BooleanField(default=False, verbose_name='Память задних сидений')
    memory_mirrors = models.BooleanField(default=False, verbose_name='Память зеркал')
    memory_steering_column = models.BooleanField(default=False, verbose_name='Память рулевой колонки')

    # Помощь при вождении
    parking_attendant = models.BooleanField(default=False, verbose_name='Автопарковщик')
    rain_sensor = models.BooleanField(default=False, verbose_name='Датчик дождя')
    sheine_sensor = models.BooleanField(default=False, verbose_name='Датчик света')
    rear_parking_sensors = models.BooleanField(default=False, verbose_name='Парктроник задний')
    front_parking_sensors = models.BooleanField(default=False, verbose_name='Парктроник передний')
    blind_spot_monitoring_system = models.BooleanField(default=False, verbose_name='Система контроля слепых зон')
    rear_view_camera = models.BooleanField(default=False, verbose_name='Камера заднего вида')
    cruise_control = models.BooleanField(default=False, verbose_name='Круиз контроль')
    onboard_computer = models.BooleanField(default=False, verbose_name='Бортовой компьютер')

    # Противоугонная система
    signaling = models.BooleanField(default=False, verbose_name='Сигнализация')
    сentral_locking = models.BooleanField(default=False, verbose_name='Центральный замок')
    immobilizer = models.BooleanField(default=False, verbose_name='Иммобилайзер')
    satellite = models.BooleanField(default=False, verbose_name='Спутник')

    # ПОДУШКИ БЕЗОПАСНОСТИ
    front_airbags = models.BooleanField(default=False, verbose_name='Фронтальные')
    knee_airbags = models.BooleanField(default=False, verbose_name='Коленные')
    curtain_airbags = models.BooleanField(default=False, verbose_name='Шторки')
    side_front_airbags = models.BooleanField(default=False, verbose_name='Боковые передние')
    side_rear_airbags = models.BooleanField(default=False, verbose_name='Боковые задние')

    # Активная безопасность
    ABS = models.BooleanField(default=False, verbose_name='Автоблокировка тормозов')
    anti_slip = models.BooleanField(default=False, verbose_name='Антипробуксовка')
    directional_stability = models.BooleanField(default=False, verbose_name='Курсовая устойчивость')
    brake_force_distribution = models.BooleanField(default=False, verbose_name='Распред. тормозных усилий ')
    emergency_braking = models.BooleanField(default=False, verbose_name='Экстренное торможение')
    differential_lock = models.BooleanField(default=False, verbose_name='Блок. дифференциала')
    pedestrian_detection = models.BooleanField(default=False, verbose_name='Обнаружение пешеходов')

    # Мультимедиа и навигация
    CD_DVD = models.BooleanField(default=False, verbose_name='CD/DVD/Blu-ray')
    MP3 = models.BooleanField(default=False, verbose_name='MP3')
    radio = models.BooleanField(default=False, verbose_name='Радио')
    TV = models.BooleanField(default=False, verbose_name='TV')
    video = models.BooleanField(default=False, verbose_name='Видео')
    steering_wheel_control = models.BooleanField(default=False, verbose_name='Управление на руле')
    USB = models.BooleanField(default=False, verbose_name='USB')
    AUX = models.BooleanField(default=False, verbose_name='AUX')
    bluetooth = models.BooleanField(default=False, verbose_name='bluetooth')
    GPS = models.BooleanField(default=False, verbose_name='GPS-навигатор')

    # Аудиосистема
    audio = models.CharField(max_length=50, blank=True, choices = AUDIO, verbose_name="Аудиосистема")
    subwoofer = models.BooleanField(default=False, verbose_name='Сабвуфер')

    # Фары
    headlights = models.CharField(max_length=50, blank=True, choices = HEADLINES, verbose_name="Фары")
    fog = models.BooleanField(default=False, verbose_name='Противотуманные')
    headlight_washers = models.BooleanField(default=False, verbose_name='Омыватели фар')
    adaptive_lighting = models.BooleanField(default=False, verbose_name='Адаптивное освещение')

    # Шины и диски
    tires = models.CharField(max_length=50, blank=True, choices = TIRES, verbose_name="")
    winter_tyre = models.BooleanField(default=False, verbose_name='Зимние шины в комплекте')

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобиль"
