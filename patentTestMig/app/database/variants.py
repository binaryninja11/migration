from app.schemas import schema


variant1 = {
    "variant_id": 1,
    "body": {
        schema.SectionName.listing: [
            {
                "task_name": "Задание 1",
                "header": "Прослушайте диалог и определите, где они говорят. Выберите правильный ответ.",
                "file_name": "file11.mp3",
                "body": "Они говорят",
                "answers": ["в продуктовом магазине", "в кассе кинотеатра", "в магазине «Игрушки»"]
            },
            {
                "task_name": "Задание 2",
                "header": "Прослушайте диалог и выберите правильный ответ.",
                "file_name": "file12.mp3",
                "body": "Что сделал Антон?",
                "answers": ["Он не дал мобильный телефон сестре.", "Он потерял мобильный телефон.", "Он дал мобильный телефон сестре."]
            }
        ],
        schema.SectionName.reading: [
            {
                "task_name": "Задание 3",
                "header": "Прочитайте объявление и выберите правильный ответ.",
                "body": "Уважаемые пассажиры!\nОплачивайте проезд при входе.\n\nТакое объявление можно прочитать",
                "answers": ["в кино", "в автобусе", "в магазине"]
            },
            {
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Дорогой друг!\nПриглашаю тебя на мой День рождения!\nПраздник будет 19 ноября (в четверг) с 15 до 20 часов.\nЖду тебя в кафе «Уют».",
                "answers": ["в 15 часов", "в 19 часов", "в 20 часов"]
            }
        ],
        schema.SectionName.writing: [
            {
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Нариман приехал из Узбекистана. Нариман – врач.\n\nВпишите нужное слово в анкету.\nАнкета",
                "answers": ["1. Как Вас зовут?   Меня зовут Нариман.", "2. Откуда Вы приехали?   Я приехал из Узбекистана.", "3.Кто Вы по профессии?   Я ___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "task_name": "Задание 6",
                "body": "Сегодня четверг, а брат приедет завтра, _____________________.",
                "answers": ["в среду", "в пятницу", "в субботу"]
            },
            {
                "task_name": "Задание 7",
                "body": "Моя сестра _______________ в больнице.",
                "answers": ["живёт", "гуляет", "работает"]
            },
            {
                "task_name": "Задание 8",
                "body": "– Как тебя зовут\n– _______________ зовут Олег.",
                "answers": ["Мне", "Меня", "Я"]
            },
            {
                "task_name": "Задание 9",
                "body": "Друг спросил меня: «_______________ ты провёл выходные?»",
                "answers": ["Как", "Почему", "Что"]
            }
        ],
        schema.SectionName.history: [
            {
                "task_name": "Задание 10",
                "body": "4 ноября в России празднуют?",
                "answers": ["Международный женский день", "День народного единства", "День Победы"]
            },
            {
                "task_name": "Задание 11",
                "body": "Какой город в России называют «второй столицей»?",
                "answers": ["Екатеринбург", "Владивосток", "Санкт-Петербург"]
            },
            {
                "task_name": "Задание 12",
                "body": "Союзник СССР в Великой Отечественной войне – это:",
                "answers": ["Япония", "Германия", "Великобритания"]
            },
            {
                "task_name": "Задание 13",
                "body": "Знаменитый полководец Великой Отечественной войны – это",
                "answers": ["А.В. Суворов", "Г.К. Жуков", "Ю.А. Гагарин"]
            },
            {
                "task_name": "Задание 14",
                "body": "Укажите флаг Российской Федерации.",
                "answers": ["img11.jpg", "img12.jpg", "img13.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "task_name": "Задание 15",
                "body": "Что говорит Конституция России о правах иностранцев в России?",
                "answers": ["Иностранцы имеют все права и обязанности как граждане России","Иностранцы имеют права и обязанности, кроме случаев, установленных законом","Иностранцы не имеют прав в России"]
            },
            {
                "task_name": "Задание 16",
                "body": "В какой форме заключается трудовой договор в России?",
                "answers": ["в письменной", "в устной", "в любой"]
            },
            {
                "task_name": "Задание 17",
                "body": "Окажут ли срочную медицинскую помощь иностранцу?",
                "answers": ["за плату", "бесплатно", "если есть трудовой договор"]
            },
            {
                "task_name": "Задание 18",
                "body": "Какую цель нужно указать в миграционной карте для получения патента?",
                "answers": ["отдых", "работа", "частная"]
            },
            {
                "task_name": "Задание 19",
                "body": "Какой кодекс регулирует правила въезда иностранцев в Россию?",
                "asnwers": ["Трудовой кодекс", "Кодекс об административных правонарушениях", "Гражданский кодекс"]
            },
            {
                "task_name": "Задание 20",
                "body": "Если иностранец вовремя не подал на патент, его депортируют. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}

variant2 = {
    "variant_id": 2,
    "body": {
        schema.SectionName.listing: [
            {
                "task_name": "Задание 1",
                "header": "Прослушайте объявление и определите, где можно его услышать. Выберите правильный ответ.",
                "file_name": "file21.mp3",
                "body": "Объявление можно услышать",
                "answers": ["в ресторане", "в магазине", "в библиотеке"]
            },
            {
                "task_name": "Задание 2",
                "header": "Прослушайте объявление и выберите правильный ответ.",
                "file_name": "file22.mp3",
                "body": "Спросите о потерянных вещах",
                "answers": ["у покупателей", "у администратора", "у директора магазина"]
            }
        ],
        schema.SectionName.reading: [
            {
                "task_name": "Задание 3",
                "header": "Прочитайте киноафишу и выберите правильный ответ.",
                "body": "Осенью смотрите фильм о русском музыканте П.И. Чайковском!\n\nНовый фильм снят",
                "answers": ["о спорте", "о музыке", "о кино"]
            },
            {
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Меня зовут Рушан. Летом я ездил в Узбекистан к родителям. Я увидел своего брата и его семью. А в конце лета я с женой и детьми\nпоехал на море.\n\nРушан поехал на море",
                "answers": ["с женой и детьми", "с родителями", "с братом"]
            }
        ],
        schema.SectionName.writing: [
            {
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Анвар Рустамов хочет получить работу плотника.\nВпишите нужное слово в его заявление.\n\nЗаявление\nПрошу принять меня на должность",
                "answers": ["___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "task_name": "Задание 6",
                "body": "В магазине «Продукты» я купил _______________.",
                "answers": ["диван", "куртку", "фрукты"]
            },
            {
                "task_name": "Задание 7",
                "body": "Мой папа любит _______________ исторические книги.",
                "answers": ["смотреть", "слушать", "читать"]
            },
            {
                "task_name": "Задание 8",
                "body": "Сколько _______________ лет?",
                "answers": ["Вы", "Вам", "у Вас"]
            },
            {
                "task_name": "Задание 9",
                "body": "Карим сказал, _______________ он приедет в отпуск весной.",
                "answers": ["что", "потому что", "когда"]
            }
        ],
        schema.SectionName.history: [
            {
                "task_name": "Задание 10",
                "body": "12 июня в России празднуют",
                "answers": ["День России", "Праздник Весны и Труда", "День защитника Отечества"]
            },
            {
                "task_name": "Задание 11",
                "body": "Какой из этих городов российский?",
                "answers": ["Будапешт", "Казань", "Братислава"]
            },
            {
                "task_name": "Задание 12",
                "body": "Кто командовал русской армией в войне 1812 года?",
                "answers": ["Г.К. Жуков", "Дмитрий Донской", "М.И. Кутузов"]
            },
            {
                "task_name": "Задание 13",
                "body": "Когда было создано СНГ?",
                "answers": ["в 1612 году", "в 1941 году", "в 1991 году"]
            },
            {
                "task_name": "Задание 14",
                "body": "Укажите герб Российской Федерации.",
                "answers": ["img21.jpg", "img22.jpg", "img23.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "task_name": "Задание 15",
                "body": "Какое право иностранцу гарантирует Конституция России?",
                "answers": ["голосовать на выборах","выбирать работу","занимать государственные должности"]
            },
            {
                "task_name": "Задание 16",
                "body": "Как дети иностранцев учатся в России?",
                "answers": ["бесплатно, как и дети граждан России", "только платно", "не имеют права посещать школы и детсады"]
            },
            {
                "task_name": "Задание 17",
                "body": "Куда обратиться, если ограбили?",
                "answers": ["в полицию", "в суд", "на работу"]
            },
            {
                "task_name": "Задание 18",
                "body": "Что нужно получить и заполнить при въезде в Россию?",
                "answers": ["заявление на патент", "миграционную карту", "заявление на работу"]
            },
            {
                "task_name": "Задание 19",
                "body": "Сколько дней у иностранца для подачи документов на патент?",
                "asnwers": ["30 дней", "20 дней", "10 дней"]
            },
            {
                "task_name": "Задание 20",
                "body": "Eсли иностранец не уехал после окончания срока пребывания, он нарушает закон. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}

variant3 = {
    "variant_id": 3,
    "body": {
        schema.SectionName.listing: [
            {
                "task_name": "Задание 1",
                "header": "Прослушайте диалог и определите, где происходит разговор. Выберите правильный ответ.",
                "file_name": "file31.mp3",
                "body": "Они говорят",
                "answers": ["в магазине", "в автомастерской", "в центре тестирования"]
            },
            {
                "task_name": "Задание 2",
                "header": "Прослушайте объявление и выберите правильный ответ.",
                "file_name": "file32.mp3",
                "body": "Вам нужно",
                "answers": ["ехать дальше", "сделать пересадку", "выйти из вагона"]
            }
        ],
        schema.SectionName.reading: [
            {
                "task_name": "Задание 3",
                "header": "Прочитайте объявление и выберите правильный ответ.\n\nСлужебное помещение: вход только для персонала!",
                "body": "Вы можете увидеть это объявление",
                "answers": ["в лифте","в ресторане","в автобусе"]
            },
            {
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Меня зовут Тимур. Вчера я со своими друзьями ходил на концерт. Концерт был в парке. Нам очень понравилось. После концерта мы\nрешили поужинать в кафе.\n\nВчера Тимур и его друзья были",
                "answers": ["на концерте","в музее","в театре"]
            }
        ],
        schema.SectionName.writing: [
            {
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Далер приехал из Таджикистана. Далер – кассир.\nВпишите нужное слово в анкету.\n\nАнкета",
                "answers": ["1. Как Вас зовут?  Меня зовут Далер.","2. Откуда Вы приехали?   Я приехал из Таджикистана.","3. Кто Вы по профессии?	Я ___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "task_name": "Задание 6",
                "body": "Я с друзьями поеду в горы _____________, чтобы кататься на лыжах.",
                "answers": ["зимой", "летом", "осенью"]
            },
            {
                "task_name": "Задание 7",
                "body": "Скажите, пожалуйста, ___________ уже закончили?",
                "answers": ["работа", "рабочие", "работать"]
            },
            {
                "task_name": "Задание 8",
                "body": "– Откуда ты приехал?\n– Я приехал _______________.",
                "answers": ["в Самарканде", "из Самарканда", "из Самарканд"]
            },
            {
                "task_name": "Задание 9",
                "body": "Мы приехали в Россию, __________ найти работу.",
                "answers": ["чтобы", "поэтому", "потому что"]
            }
        ],
        schema.SectionName.history: [
            {
                "task_name": "Задание 10",
                "body": "1 января в России празднуют",
                "answers": ["День России", "Новый год", "Международный женский день"]
            },
            {
                "task_name": "Задание 11",
                "body": "Город, который является столицей России - __________.",
                "answers": ["Москва", "Екатеринбург", "Самара"]
            },
            {
                "task_name": "Задание 12",
                "body": "Когда закончилась Великая Отечественная война?",
                "answers": ["в 1917 году", "в 1945 году", "в 1980 году"]
            },
            {
                "task_name": "Задание 13",
                "body": "СНГ было образовано после",
                "answers": ["распада СССР в 1991 году", "Великой Отечественной войны", "Российской революции 1917 года"]
            },
            {
                "task_name": "Задание 14",
                "body": "Укажите флаг Российской Федерации.",
                "answers": ["img31.jpg", "img32.jpg", "img33.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "task_name": "Задание 15",
                "body": "Какое право Конституция РФ гарантирует иностранцам?",
                "answers": ["голосовать на выборах","участвовать в суде","пользоваться родным языком"]
            },
            {
                "task_name": "Задание 16",
                "body": "Иностранец, работающий в России, должен платить налоги?",
                "answers": ["должен", "не должен", "может"]
            },
            {
                "task_name": "Задание 17",
                "body": "На территории Российской Федерации в отношении иностранного гражданина совершено преступление. Куда он должен обратиться за помощью?",
                "answers": ["в полицию", "в МИД", "в посольство своей страны"]
            },
            {
                "task_name": "Задание 18",
                "body": "Что нужно иметь иностранцу для постановки на учет в России?",
                "answers": ["только миграционную карту", "только паспорт", "паспорт и миграционную карту"]
            },
            {
                "task_name": "Задание 19",
                "body": "Если иностранец нарушил правила учета, какая будет ответственность?",
                "asnwers": ["дисциплинарная", "уголовная", "административная"]
            },
            {
                "task_name": "Задание 20",
                "body": "Административное выдворение из России для иностранцев устанавливает судья. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}

variant4 = {
    "variant_id": 4,
    "body": {
        schema.SectionName.listing: [
            {
                "task_name": "Задание 1",
                "header": "Прослушайте диалог и определите, где происходит разговор. Выберите правильный ответ.",
                "file_name": "file41.mp3",
                "body": "Они говорят",
                "answers": ["на улице", "на остановке", "в автобусе"]
            },
            {
                "task_name": "Задание 2",
                "header": "Прослушайте объявление и выберите правильный ответ.",
                "file_name": "file42.mp3",
                "body": "У администратора магазина можно",
                "answers": ["взять свой потерянный телефон", "купить новый телефон", "позвонить по телефону"]
            }
        ],
        schema.SectionName.reading: [
            {
                "task_name": "Задание 3",
                "header": "Прочитайте объявление и выберите правильный ответ.",
                "body": "Уважаемые жильцы дома №7!\nЛифт временно не работает!\n\nТакое объявление можно прочитать",
                "answers": ["в аптеке","в подъезде","в парке"]
            },
            {
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Меня зовут Динара. Я приехала с родителями из Таджикистана. Мой папа инженер, а мама учительница. В будущем я хочу быть доктором.\nДинара хочет быть",
                "answers": ["доктором","учительницей","инженером"]
            }
        ],
        schema.SectionName.writing: [
            {
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Мадина приехала из Узбекистана. Мадина – швея.\nВпишите нужное слово в анкету.\n\nАнкета",
                "answers": ["1. Как Вас зовут?	Меня зовут Мадина.","2. Откуда Вы приехали?   Я приехала из ___","3. Кто Вы по профессии?	Я швея."]
            }
        ],
        schema.SectionName.grammar: [
            {
                "task_name": "Задание 6",
                "body": "А.С. Пушкин родился летом, _______________.",
                "answers": ["6 июня", "6 апреля", "6 декабря"]
            },
            {
                "task_name": "Задание 7",
                "body": "В аптеке я купил __________.",
                "answers": ["телефон", "огурцы", "лекарство"]
            },
            {
                "task_name": "Задание 8",
                "body": "Ты знаешь, _______________ есть брат и сестра?",
                "answers": ["к нему", "у его", "у него"]
            },
            {
                "task_name": "Задание 9",
                "body": "Я не могу сегодня пойти на работу, _______________ я заболел.",
                "answers": ["чтобы", "потому что", "если"]
            }
        ],
        schema.SectionName.history: [
            {
                "task_name": "Задание 10",
                "body": "7 января в России празднуют",
                "answers": ["День России", "Международный женский день", "Рождество Христово"]
            },
            {
                "task_name": "Задание 11",
                "body": "Какой из этих городов находится в России?",
                "answers": ["София", "Владивосток", "Берлин"]
            },
            {
                "task_name": "Задание 12",
                "body": "Противник России в Отечественной войне 1812 года был:",
                "answers": ["Швеция", "Великобритания", "Франция"]
            },
            {
                "task_name": "Задание 13",
                "body": "Первый человек, полетевший в космос, был из",
                "answers": ["США", "СССР", "Китая"]
            },
            {
                "task_name": "Задание 14",
                "body": "Укажите флаг Российской Федерации.",
                "answers": ["img41.jpg", "img42.jpg", "img43.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "task_name": "Задание 15",
                "body": "Что имеет право делать иностранец в России?",
                "answers": ["быть пилотом гражданского самолета","работать на объектах, связанных с безопасностью","говорить на родном языке"]
            },
            {
                "task_name": "Задание 16",
                "body": "Где регистрируют брак в России?",
                "answers": ["в суде", "в ЗАГСе", "в полиции"]
            },
            {
                "task_name": "Задание 17",
                "body": "Потеряли паспорт. Куда обратиться?",
                "answers": ["в полицию и консульство", "в суд", "на работу"]
            },
            {
                "task_name": "Задание 18",
                "body": "Сколько времени дается для постановки на учет в России?",
                "answers": ["3 рабочих дня", "7 рабочих дней", "10 рабочих дней"]
            },
            {
                "task_name": "Задание 19",
                "body": "Какой кодекс регулирует наказание за преступление иностранца в России?",
                "asnwers": ["Уголовный кодекс России", "Уголовный кодекс страны иностранца", "Гражданский кодекс"]
            },
            {
                "task_name": "Задание 20",
                "body": "Иностранцев с ВИЧ депортируют из России. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}

variant5 = {
    "variant_id": 5,
    "body": {
        schema.SectionName.listing: [
            {
                "task_name": "Задание 1",
                "header": "Прослушайте диалог и определите, где происходит разговор. Выберите правильный ответ.",
                "file_name": "file51.mp3",
                "body": "Они говорят",
                "answers": ["в кинотеатре", "в магазине", "в гостинице"]
            },
            {
                "task_name": "Задание 2",
                "header": "Прослушайте объявление и выберите правильный ответ.",
                "file_name": "file52.mp3",
                "body": "Теперь банк будет работать",
                "answers": ["до 9 часов вечера", "как обычно", "до 21 мая"]
            }
        ],
        schema.SectionName.reading: [
            {
                "task_name": "Задание 3",
                "header": "Прочитайте объявление и выберите правильный ответ.",
                "body": "Технический перерыв 15 минут\n\nВы можете увидеть это объявление",
                "answers": ["в магазине","в самолёте","в парке"]
            },
            {
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Сабине сорок три года. Она приехала с семьей из Узбекистана. Дома она работала поваром. Её муж работает таксистом. Сабина планирует работать в школе поваром.\nКем будет работать Сабина?",
                "answers": ["таксистом","поваром","продавцом"]
            }
        ],
        schema.SectionName.writing: [
            {
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Карим Исмаилов хочет получить работу повара.\nВпишите нужное слово в его заявление.\n\nЗаявление\nПрошу принять меня на работу на должность",
                "answers": ["___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "task_name": "Задание 6",
                "body": "– Автобусная остановка находится здесь?\n– Нет, ___________________.",
                "answers": ["там", "здесь", "тот"]
            },
            {
                "task_name": "Задание 7",
                "body": "Мой брат работает в ресторане _____________________.",
                "answers": ["продавцом", "курьером", "инженером"]
            },
            {
                "task_name": "Задание 8",
                "body": "Извините, это ________ телефон?",
                "answers": ["Ваша", "Ваши", "Ваш"]
            },
            {
                "task_name": "Задание 9",
                "body": "Скажите, пожалуйста, _________ находится аптека?",
                "answers": ["где", "здесь", "там"]
            }
        ],
        schema.SectionName.history: [
            {
                "task_name": "Задание 10",
                "body": "23 февраля в России празднуют",
                "answers": ["Праздник Весны и Труда", "День защитника Отечества", "День России"]
            },
            {
                "task_name": "Задание 11",
                "body": "Какой из этих городов в России?",
                "answers": ["София", "Прага", "Новосибирск"]
            },
            {
                "task_name": "Задание 12",
                "body": "Когда началась Великая Отечественная война?",
                "answers": ["в 1812 году", "в 1917 году", "в 1941 году"]
            },
            {
                "task_name": "Задание 13",
                "body": "Кто участвовал в создании СНГ?",
                "answers": ["Иван Грозный", "Борис Ельцин", "Дмитрий Пожарский"]
            },
            {
                "task_name": "Задание 14",
                "body": "Укажите герб Российской Федерации.",
                "answers": ["img41.jpg", "img42.jpg", "img43.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "task_name": "Задание 15",
                "body": "Иностранный гражданин в Российской Федерации имеет право:",
                "answers": ["ознакомиться с документами, касающимися его прав","самостоятельно составлять документы","вносить изменения в документы"]
            },
            {
                "task_name": "Задание 16",
                "body": "Может ли иностранец купить недвижимость в России?",
                "answers": ["может", "не может", "только с разрешения суда"]
            },
            {
                "task_name": "Задание 17",
                "body": "Иностранец может жениться в России?",
                "answers": ["да", "да, только на гражданке РФ", "нет"]
            },
            {
                "task_name": "Задание 18",
                "body": "Если срок пребывания в России сокращен, за сколько дней нужно покинуть страну?",
                "answers": ["90 дней", "30 дней", "3 дня"]
            },
            {
                "task_name": "Задание 19",
                "body": "Если иностранец нарушил правила учета, какую ответственность он понесет?",
                "asnwers": ["дисциплинарную", "уголовную", "административную"]
            },
            {
                "task_name": "Задание 20",
                "body": "Иностранец, не уехавший из России вовремя, будет депортирован. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}


variants = [variant1,variant2,variant3,variant4,variant5]
answers1 = {
    1:2,
    2:3,
    3:2,
    4:1,
    5:"врач",
    6:1,
    7:3,
    8:2,
    9:1,
    10:2,
    11:3,
    12:3,
    13:2,
    14:2,
    15:2,
    16:1,
    17:2,
    18:2,
    19:2,
    20:2
}

answers2 = {
    1:2,
    2:2,
    3:2,
    4:1,
    5:"плотника",
    6:3,
    7:3,
    8:2,
    9:1,
    10:1,
    11:2,
    12:3,
    13:3,
    14:1,
    15:2,
    16:1,
    17:1,
    18:2,
    19:1,
    20:1
}

answers3 = {
    1:3,
    2:3,
    3:2,
    4:1,
    5:"кассир",
    6:1,
    7:2,
    8:2,
    9:1,
    10:2,
    11:1,
    12:2,
    13:1,
    14:1,
    15:3,
    16:1,
    17:1,
    18:3,
    19:3,
    20:1
}

answers4 = {
    1:3,
    2:1,
    3:2,
    4:1,
    5:"Узбекистана",
    6:1,
    7:3,
    8:3,
    9:2,
    10:3,
    11:2,
    12:3,
    13:2,
    14:2,
    15:3,
    16:2,
    17:1,
    18:2,
    19:1,
    20:2
}

answers5 = {
    1:1,
    2:1,
    3:1,
    4:2,
    5:"повара",
    6:1,
    7:2,
    8:3,
    9:1,
    10:2,
    11:3,
    12:3,
    13:2,
    14:2,
    15:1,
    16:1,
    17:1,
    18:3,
    19:3,
    20:1
}

answers = [answers1,answers2,answers3,answers4,answers5]