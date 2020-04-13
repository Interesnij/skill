from django.db import models
from ad_posts.models import Ad


class Service(Ad):
    REPAIR=(
        ('Дизайн интерьера','Дизайн интерьера'),
        ('Дома и коттеджи "под ключ"','Дома и коттеджи "под ключ"'),
        ('Земляные работы, колодцы, скважины','Земляные работы, колодцы, скважины'),
        ('Кровельные работы','Кровельные работы'),
        ('Ландшафтный дизайн, обустройство участка','Ландшафтный дизайн, обустройство участка'),
        ('Натяжные потолки','Натяжные потолки'),
        ('Остекленение, ремонт окон','Остекленение, ремонт окон'),
        ('Отделка фасадов','Отделка фасадов'),
        ('Отделочные работы','Отделочные работы'),
        ('Ремонт под ключ','Ремонт под ключ'),
        ('Строительство бань, саун','Строительство бань, саун'),
        ('Строительство кирпичных, блочных домов','Строительство кирпичных, блочных домов'),
        ('Строительство фундаментов','Строительство фундаментов'),
        ('Строительство.сборка деревянных домов','Строительство.сборка деревянных домов'),
        ('Услуги сантехника','Услуги сантехника'),
        ('Услуги электрика','Услуги электрика'),
        ('Установка и ремонт дверей','Установка и ремонт дверей'),
        ('Установка и ремонт отопления, водоснабжения, канализации','Установка и ремонт отопления, водоснабжения, канализации'),
        ('Другие строительные работы','Другие строительные работы'),
    )
    PRICE_INDICATED=(
        ('За час','За час'),
        ('За услугу','За услугу'),
        ('За метраж, объем','За метраж, объем'),
    )
    RENDERING_SERVICES=(
        ('Выезд на дом','Выезд на дом'),
        ('В салоне','В салоне'),
        ('Дома у мастера','Дома у мастера'),
    )
    HOUR=(
        ('Дезинфекция, дезинсекция','Дезинфекция, дезинсекция'),
        ('Изготовление ключей, вскрытие замков','Изготовление ключей, вскрытие замков'),
        ('Мастер на час','Мастер на час'),
        ('Сборка и ремонт мебели','Сборка и ремонт мебели'),
        ('Услуги няни, гувернантки','Услуги няни, гувернантки'),
        ('Услуги сиделки','Услуги сиделки'),
    )
    TRAFFIC=(
        ('Аренда авто','Аренда авто'),
        ('Аренда спецтехники','Аренда спецтехники'),
        ('Вывоз мусора','Вывоз мусора'),
        ('Грузоперевозки','Грузоперевозки'),
        ('Грузчики','Грузчики'),
        ('Пассажирские перевозки','Пассажирские перевозки'),
        ('Услуги водителя','Услуги водителя'),
        ('Услуги эвакуатора','Услуги эвакуатора'),
    )
    BEAUTY=(
        ('Аренда кабинета','Аренда кабинета'),
        ('Косметология','Косметология'),
        ('Макияж','Макияж'),
        ('Маникюр, педикюр','Маникюр, педикюр'),
        ('Массаж','Массаж'),
        ('Наращивание волос','Наращивание волос'),
        ('Наращивание волос, услуги бровиста','Наращивание волос, услуги бровиста'),
        ('СПА-услуги','СПА-услуги'),
        ('Тату, пирсинг','Тату, пирсинг'),
        ('Услуги парикмахера','Услуги парикмахера'),
        ('Эпиляция, депиляция, шугаринг','Эпиляция, депиляция, шугаринг'),
    )
    COMPUTER=(
        ('Веб-дизайн, бренд, арт','Веб-дизайн, бренд, арт'),
        ('Косметология','Косметология'),
        ('Компьютерная помощь, настройка ПК','Компьютерная помощь, настройка ПК'),
        ('Набор текста, ввод данных','Набор текста, ввод данных'),
        ('Подключение интернета','Подключение интернета'),
        ('Создание и продвижение сайтов','Создание и продвижение сайтов'),
        ('Установка ПО','Установка ПО'),
        ('Другие IT-услуги','Другие IT-услуги'),
    )
    AUTO=(
        ('Автоэлектрика','Автоэлектрика'),
        ('Диагностика, подбор авто','Диагностика, подбор авто'),
        ('Кузовные работы, покраска','Кузовные работы, покраска'),
        ('Ремонт двигателя и ходовой','Ремонт двигателя и ходовой'),
        ('Ремонт мототехники','Ремонт мототехники'),
        ('Тюнинг и установка доп. оборудования','Тюнинг и установка доп. оборудования'),
        ('Химчистка, мойка','Химчистка, мойка'),
        ('Шиномонтаж, диски','Шиномонтаж, диски'),
    )
    EQUIPMENT=(
        ('Ремонт газового оборудования','Ремонт газового оборудования'),
        ('Ремонт компьютеров, ноутбуков','Ремонт компьютеров, ноутбуков'),
        ('Ремонт телефонов, смартфонов','Ремонт телефонов, смартфонов'),
        ('Ремонт телевизоров, аудио, видеотехники','Ремонт телевизоров, аудио, видеотехники'),
        ('Ремонт фототехники','Ремонт фототехники'),
        ('Ремонт часов','Ремонт часов'),
        ('Установка кондиционеров','Установка кондиционеров'),
        ('Установка систем безопасности','Установка систем безопасности'),
        ('Установка, ремонт бытовой техники','Установка, ремонт бытовой техники'),
    )
    TRAINING=(
        ('Детское развитие','Детское развитие'),
        ('Мастер-классы, тренинги','Мастер-классы, тренинги'),
        ('Обучение вождению','Обучение вождению'),
        ('Обучение языкам','Обучение языкам'),
        ('Подготовка к экзаменам','Подготовка к экзаменам'),
        ('Профессиональное обучение','Профессиональное обучение'),
        ('Уроки музыки, театрального мастерства','Уроки музыки, театрального мастерства'),
        ('Уроки рисования, дизайна, рукоделия','Уроки рисования, дизайна, рукоделия'),
        ('Услуги логопеда, дефектолога','Услуги логопеда, дефектолога'),
        ('Услуги психолога','Услуги психолога'),
        ('Услуги репетитора','Услуги репетитора'),
        ('Услуги тренера (спорт,танцы)','Услуги тренера (спорт,танцы)'),
    )
    BUSINESS=(
        ('Бизнесс-консультирование','Бизнесс-консультирование'),
        ('Бухгалтерия, финансы','Бухгалтерия, финансы'),
        ('Изготовление вывесок, рекламы','Изготовление вывесок, рекламы'),
        ('Маркетинг, реклама, PR','Маркетинг, реклама, PR'),
        ('Перевод','Перевод'),
        ('Полиграфия, печать, дизайн','Полиграфия, печать, дизайн'),
        ('Риэлторские услуги','Риэлторские услуги'),
        ('Составление документов, сертификации и пр.','Составление документов, сертификации и пр.'),
        ('Юридические услуги','Юридические услуги'),
    )
    HOLIDAYS=(
        ('Аренда оборудования, аттракционов','Аренда оборудования, аттракционов'),
        ('Аренда площадки','Аренда площадки'),
        ('Ведущие, музыканты, артисты','Ведущие, музыканты, артисты'),
        ('Организация мероприятий','Организация мероприятий'),
        ('Приготовление еды, кейтеринг','Приготовление еды, кейтеринг'),
        ('Прокат костюмов','Прокат костюмов'),
        ('Промоутеры, модели','Промоутеры, модели'),
        ('Туризм и отдых','Туризм и отдых'),
        ('Цветы и декор','Цветы и декор'),
    )
    CLEAN=(
        ('Мойка окон, балконов','Мойка окон, балконов'),
        ('Уборка','Уборка'),
        ('Услуги домработницы','Услуги домработницы'),
        ('Химчистка, стирка, глажка','Химчистка, стирка, глажка'),
    )
    CUSTOMIZATION=(
        ('Изготовление и ремонт одежды, обуви, аксессуаров','Изготовление и ремонт одежды, обуви, аксессуаров'),
        ('Кованые изделия на заказ','Кованые изделия на заказ'),
        ('Мебель на заказ','Мебель на заказ'),
        ('Музыка, стихи, озвучка на заказ','Музыка, стихи, озвучка на заказ'),
        ('Печати и штампы на заказ','Печати и штампы на заказ'),
        ('Рисунок, живопись, графика на заказ','Рисунок, живопись, графика на заказ'),
        ('Сувенирная продукция, полиграфия','Сувенирная продукция, полиграфия'),
        ('Другие услуги на заказ','Другие услуги на заказ'),
    )
    FOOD=(
        ('Выпечка, торты на заказ','Выпечка, торты на заказ'),
        ('Продукты питания','Продукты питания'),
        ('Услуги повара','Услуги повара'),
        ('Чай, кофе','Чай, кофе'),
    )
    ANIMAL=(
        ('Вязка','Вязка'),
        ('Дрессировка и выгул','Дрессировка и выгул'),
        ('Передержка','Передержка'),
        ('Стрижка, уход','Стрижка, уход'),
        ('Другие услуги для животных','Другие услуги для животных'),
    )

    repairss = models.CharField(max_length=100, blank=True, choices = REPAIR, verbose_name="Услуги ремонта")
    price_indicated = models.CharField(max_length=100, blank=True, choices = PRICE_INDICATED, verbose_name="Стоимость указана")
    rendering_services = models.CharField(max_length=100, blank=True, choices = RENDERING_SERVICES, verbose_name="Оказание услуг")
    hour = models.CharField(max_length=100, blank=True, choices = HOUR, verbose_name="Мастер на час")
    traffic = models.CharField(max_length=100, blank=True, choices = TRAFFIC, verbose_name="Перевозки")
    beautys = models.CharField(max_length=100, blank=True, choices = BEAUTY, verbose_name="Красота и здоровье")
    computer = models.CharField(max_length=100, blank=True, choices = COMPUTER, verbose_name="Компьютерные услуги")
    autos = models.CharField(max_length=100, blank=True, choices = AUTO, verbose_name="Автоуслуги")
    equipment = models.CharField(max_length=100, blank=True, choices = EQUIPMENT, verbose_name="Ремонт техники")
    training = models.CharField(max_length=100, blank=True, choices = TRAINING, verbose_name="Обучение")
    business = models.CharField(max_length=100, blank=True, choices = BUSINESS, verbose_name="Деловые услуги")
    holidays = models.CharField(max_length=100, blank=True, choices = HOLIDAYS, verbose_name="Организация праздников")
    cleans = models.CharField(max_length=100, blank=True, choices = CLEAN, verbose_name="Уборка")
    customization = models.CharField(max_length=100, blank=True, choices = CUSTOMIZATION, verbose_name="Изготовление на заказ")
    food = models.CharField(max_length=100, blank=True, choices = FOOD, verbose_name="Продукты питания")
    animal = models.CharField(max_length=100, blank=True, choices = ANIMAL, verbose_name="Уход за животными")

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"
