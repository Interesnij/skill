from django.db import models
from ad_posts.models import Ad


class Hobbies(Ad):
    TYPE_BILET=(
        ('Кино','Кино'),
        ('Концерты, выставки','Концерты, выставки'),
        ('Путешествия','Путешествия'),
        ('Спорт','Спорт'),
        ('Театр, опера, балет','Театр, опера, балет'),
        ('Цирк','Цирк'),
        ('Шоу, мюзикл','Шоу, мюзикл'),
        ('Юмор','Юмор'),
    )
    TYPE_FILM=(
        ('DVD','DVD'),
        ('Blu-ray','Blu-ray'),
        ('CD','CD'),
        ('Кассеты VHS','Кассеты VHS'),
    )
    TYPE_CONSOLE=(
        ('Приставки','Приставки'),
        ('Геймпады','Геймпады'),
        ('Датчики движения','Датчики движения'),
        ('Жесткие диски','Жесткие диски'),
        ('Зарядки, аккумуляторы','Зарядки, аккумуляторы'),
        ('Кабели, адаптеры','Кабели, адаптеры'),
        ('Клавиатуры, мыши','Клавиатуры, мыши'),
        ('Подставки','Подставки'),
        ('Аксессуары','Аксессуары'),
    )
    OS_CONSOLE=(
        ('Dendy','Dendy'),
        ('Game Boy','Game Boy'),
        ('Nintendo 3DS','Nintendo 3DS'),
        ('Nintendo DS','Nintendo DS'),
        ('Nintendo DS Lite','Nintendo DS Lite'),
        ('Nintendo GameCube','Nintendo GameCube'),
        ('Nintendo Switch','Nintendo Switch'),
        ('Nintendo Wii','Nintendo Wii'),
        ('Nintendo Wii U','Nintendo Wii U'),
        ('PlayStation 1','PlayStation 1'),
        ('PlayStation 2','PlayStation 2'),
        ('PlayStation 3','PlayStation 3'),
        ('PlayStation 4','PlayStation 4'),
        ('PlayStation  Pro','PlayStation Pro'),
        ('PlayStation Portable','PlayStation Portable'),
        ('PlayStation Vita','PlayStation Vita'),
        ('Sega','Sega'),
        ('Xbox 360','Xbox 360'),
        ('Xbox One','Xbox One'),
    )
    GAME=(
        ('PC, компьютерные игры','PC, компьютерные игры'),
        ('Dendy','Dendy'),
        ('Game Boy','Game Boy'),
        ('Nintendo 3DS','Nintendo 3DS'),
        ('Nintendo DS','Nintendo DS'),
        ('Nintendo DS Lite','Nintendo DS Lite'),
        ('Nintendo GameCube','Nintendo GameCube'),
        ('Nintendo Switch','Nintendo Switch'),
        ('Nintendo Wii','Nintendo Wii'),
        ('Nintendo Wii U','Nintendo Wii U'),
        ('PlayStation 1','PlayStation 1'),
        ('PlayStation 2','PlayStation 2'),
        ('PlayStation 3','PlayStation 3'),
        ('PlayStation 4','PlayStation 4'),
        ('PlayStation  Pro','PlayStation Pro'),
        ('PlayStation Portable','PlayStation Portable'),
        ('PlayStation Vita','PlayStation Vita'),
        ('Sega','Sega'),
        ('Xbox 360','Xbox 360'),
        ('Xbox One','Xbox One'),
    )
    GENRE=(
        ('Аркады','Аркады'),
        ('Гонки','Гонки'),
        ('Драки','Драки'),
        ('Квесты, логические','Квесты, логические'),
        ('Музыкальные','Музыкальные'),
        ('Приключения','Приключения'),
        ('Для детей, развивающие','Для детей, развивающие'),
        ('Ролевые, RPG','Ролевые, RPG'),
        ('Симуляторы','Симуляторы'),
        ('Спортивные','Спортивные'),
        ('Стратегии','Стратегии'),
        ('Экономические','Экономические'),
        ('Экшн, шутеры','Экшн, шутеры'),
    )
    TYPE_BOOK=(
        ('Газеты','Газеты'),
        ('Журналы','Журналы'),
        ('Книги','Книги'),
        ('Комиксы','Комиксы'),
    )
    THEMA=(
        ('Бизнес-литература','Бизнес-литература'),
        ('Дом и семья','Дом и семья'),
        ('Драки','Драки'),
        ('Искусство, культура','Искусство, культура'),
        ('Компьютерная литература','Компьютерная литература'),
        ('Кулинария, рецепты','Кулинария, рецепты'),
        ('Медицина, здоровье','Медицина, здоровье'),
        ('Наука, техника','Наука, техника'),
        ('Поэзия','Поэзия'),
        ('Природа, животные','Природа, животные'),
        ('Психология','Психология'),
        ('Публицистика','Публицистика'),
        ('Путешествия, фото','Путешествия, фото'),
        ('Религия, изотерика','Религия, изотерика'),
        ('Сад и огород','Сад и огород'),
        ('Спорт, фитнес','Спорт, фитнес'),
        ('Справочники, энциклопедии','Справочники, энциклопедии'),
        ('Учебная литература','Учебная литература'),
        ('Хобби, рукоделие, творчество','Хобби, рукоделие, творчество'),
        ('Художественная литература','Художественная литература'),
    )
    COLLECT=(
        ('Антикварная мебель, посуда','Антикварная мебель, посуда'),
        ('Банкноты','Банкноты'),
        ('Билеты','Билеты'),
        ('Вещи знаменитостей, автографы','Вещи знаменитостей, автографы'),
        ('Виниловые пластинки','Виниловые пластинки'),
        ('Военные вещи','Военные вещи'),
        ('Документы','Документы'),
        ('Жетоны, медали, значки','Жетоны, медали, значки'),
        ('Календари','Календари'),
        ('Киндер-сюрпризы','Киндер-сюрпризы'),
        ('Книги, журналы, рукописи','Книги, журналы, рукописи'),
        ('Конверты, открытки','Конверты, открытки'),
        ('Копилки','Копилки'),
        ('Куклы, игрушки','Куклы, игрушки'),
        ('Магниты','Магниты'),
        ('Марки','Марки'),
        ('Модели','Модели'),
        ('Монеты, нумизматика','Монеты, нумизматика'),
        ('Музыкальные инструменты','Музыкальные инструменты'),
        ('Пепельницы, зажигалки','Пепельницы, зажигалки'),
        ('Пластиковые карточки','Пластиковые карточки'),
        ('Предметы искусства, картины','Предметы искусства, картины'),
        ('Статуэтки, фигурки','Статуэтки, фигурки'),
        ('Украшения, аксессуары','Украшения, аксессуары'),
        ('Фотографии, письма','Фотографии, письма'),
        ('Шахматы, игры','Шахматы, игры'),
        ('Шкатулки','Шкатулки'),
        ('Этикетки, бутылки, пробки','Этикетки, бутылки, пробки'),
    )
    CREATIVE=(
        ('Выжигание','Выжигание'),
        ('Вязание','Вязание'),
        ('Лепка, скульптура','Лепка, скульптура'),
        ('Плетение, макраме','Плетение, макраме'),
        ('Поделки из бумаги','Поделки из бумаги'),
        ('Резьба по дереву','Резьба по дереву'),
        ('Рисование, раскраски','Рисование, раскраски'),
        ('Шитье, вышивание','Шитье, вышивание'),
    )
    TYPE_MUSIC=(
        ('CD','CD'),
        ('DVD','DVD'),
        ('Blu-ray','Blu-ray'),
        ('Аудиокассеты','Аудиокассеты'),
        ('Виниловые пластинки','Виниловые пластинки'),
    )
    INS_MUSIC=(
        ('Аккордеоны, гармони, баяны','Аккордеоны, гармони, баяны'),
        ('Акустические гитары','Акустические гитары'),
        ('Бас-гитары','Бас-гитары'),
        ('Электрогитары','Электрогитары'),
        ('Гитарное усиление','Гитарное усиление'),
        ('Духовые инструменты','Духовые инструменты'),
        ('Клавишные','Клавишные'),
        ('Микшерные пульты','Микшерные пульты'),
        ('Народные инструменты','Народные инструменты'),
        ('Педали эффектов','Педали эффектов'),
        ('Скрипки, смычковые','Скрипки, смычковые'),
        ('Ударные инструменты','Ударные инструменты'),
        ('Аксессуары','Аксессуары'),
    )
    DESCTOP=(
        ('Бродилки','Бродилки'),
        ('Викторины','Викторины'),
        ('Домино, лото','Домино, лото'),
        ('Карточные','Карточные'),
        ('Морской бой','Морской бой'),
        ('Паззлы, головоломки','Паззлы, головоломки'),
        ('Романтические','Романтические'),
        ('Слова, ассоциации','Слова, ассоциации'),
        ('Футбол, хоккей, бильярд','Футбол, хоккей, бильярд'),
        ('Шахматы, шашки, нарды','Шахматы, шашки, нарды'),
        ('Экономические','Экономические'),
    )

    type_bilet = models.CharField(max_length=50, blank=True, choices = TYPE_BILET, verbose_name="Билеты")
    type_film = models.CharField(max_length=50, blank=True, choices = TYPE_FILM, verbose_name="Видеофильмы")
    type_console = models.CharField(max_length=50, blank=True, choices = TYPE_CONSOLE, verbose_name="Игровые приставки")
    os_console = models.CharField(max_length=50, blank=True, choices = OS_CONSOLE, verbose_name="ОС приставки")
    game = models.CharField(max_length=50, blank=True, choices = GAME, verbose_name="Игры для приставок и ПК")
    genre = models.CharField(max_length=50, blank=True, choices = GENRE, verbose_name="Жанр")
    type_book = models.CharField(max_length=50, blank=True, choices = TYPE_BOOK, verbose_name="Формат")
    thema = models.CharField(max_length=50, blank=True, choices = THEMA, verbose_name="Тематика")
    collect = models.CharField(max_length=50, blank=True, choices = COLLECT, verbose_name="Коллекционирование")
    creative = models.CharField(max_length=50, blank=True, choices = CREATIVE, verbose_name="Материалы для творчества")
    type_music = models.CharField(max_length=50, blank=True, choices = TYPE_MUSIC, verbose_name="Тип носителя")
    ins_music = models.CharField(max_length=50, blank=True, choices = INS_MUSIC, verbose_name="Музыкальные инструменты")
    desctop = models.CharField(max_length=50, blank=True, choices = DESCTOP, verbose_name="Настольные игры")

    class Meta:
        verbose_name = "Хобби и развлечения"
        verbose_name_plural = "Хобби и развлечения"
