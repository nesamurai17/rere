from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = [types.KeyboardButton('Классы'),
          types.KeyboardButton('О нас'),
          types.KeyboardButton('Информация')]
keyboard1.add(*button)

TOKEN = "5329645145:AAE7I-W47YiF-RWccqi2yBPrwTn5RrIOmDo"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
  print('Бот вышел в онлайн')


@dp.message_handler(commands=['start','help'])
async def command_start(message : types.message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
    button = [types.KeyboardButton ('Классы'),
              types.KeyboardButton('О нас'),
              types.KeyboardButton('Информация')]
    keyboard.add(*button)
    await  message.answer('Здравствуйте, с вами MosObr, буду помогать вам в учебе.', reply_markup=keyboard)

@dp.message_handler(content_types=['text'])
async def bot_message(message : types.message):
    if message.chat.type == 'private':
        if message.text == 'О нас':
            await bot.send_message(message.chat.id, 'Бот разработан учениками 10-х IT классов ГБОУ Школы №2200: Тарасенко Юлией, Удалкиной Анной, Галицким Андреем, Кротовым Антоном.' )
        elif message.text == 'Информация':
            await bot.send_message(message.chat.id, 'Бот поможет Вам быстро найти нужную информацию, лучше усвоить и понять материал, а также самостоятельно разобраться в теме.')
        elif message.text == 'Классы':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = [types.KeyboardButton('9 (ОГЭ)'),
                      types.KeyboardButton('10-11'),
                      types.KeyboardButton('Главное меню')]
            keyboard.add(*button)
            await message.answer('В каком ты классе?', reply_markup=keyboard)
        elif message.text == '10-11':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = [types.KeyboardButton('Алгебра'),
                          types.KeyboardButton('Геометрия'),
                          types.KeyboardButton('Русский язык'),
                          types.KeyboardButton('Литература'),
                          types.KeyboardButton('Физика'),
                          types.KeyboardButton('Английский язык'),
                          types.KeyboardButton('Биология'),
                          types.KeyboardButton('Информатика'),
                          types.KeyboardButton('Химия'),
                          types.KeyboardButton('Главное меню')]
            keyboard.add(*button)
            await message.answer('Выбирай предмет, который не понял', reply_markup=keyboard)
        elif message.text == 'Алгебра':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text="Формулы(основные)", url='https://www.google.ru/url?sa=i&url=https%3A%2F%2Fege-paragraf.ru%2Fo-czentre%2Fpoleznaya-informacziya%2Fmatematicheskie-formulyi-po-algebre-i-geometrii-dlya-ege.html&psig=AOvVaw1q-Xay25Jbvgm1zs0WV6CS&ust=1645982302313000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLDLzoXwnfYCFQAAAAAdAAAAABAO'),
                      types.InlineKeyboardButton(text="Таблица(тригонометрических функций)", url='https://mathematics-tests.com/images/stories/matematika/10-klass/10-klass-formuli-privedeniya_2.jpg'),
                      types.InlineKeyboardButton(text='Таблица(свойства sin,cos,tg,ctg)', url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1z28uWH2oDvgin3uOD_mw6fAAY_-PlwU_kVuMjNdJNrLFtLbeXTdF6fmbFvsNdH3FrzA&usqp=CAU'),
                      types.InlineKeyboardButton(text='Тригонометрический круг', url='https://egemaximum.ru/wp-content/uploads/2013/02/87yhjh.jpg'),
                      types.InlineKeyboardButton(text='Формула(обратной тригонометрической функции', url='https://www.medius.ru/upload/iblock/bb2/bb2c492ac2dba94486bfff7474d5290c.jpg'),
                      types.InlineKeyboardButton(text='Определения',url='https://disk.yandex.ru/i/iZVhPG2VnJkafQ')]
            keyboard.add(*button)
            await message.answer("Выбирай тему, которую не понял", reply_markup=keyboard)
        elif message.text == 'Геометрия':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text="Таблицы(основные)", url='https://www.google.ru/url?sa=i&url=http%3A%2F%2Fshpargalkaege.ru%2Fgeometry-ege&psig=AOvVaw2w5lgRTuXtecOODkgmwYtq&ust=1645985572573000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLDN3pD9nfYCFQAAAAAdAAAAABAj'),
                      types.InlineKeyboardButton(text='Определения', url='https://disk.yandex.ru/i/geu7FuSfLdCR5g')]
            keyboard.add(*button)
            await message.answer('Выбирай тему, которую не понял', reply_markup=keyboard)
        elif message.text == 'Русский язык':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text='Клише сочинений', url='https://disk.yandex.ru/i/gslr1s5jKDAMIw'),
                      types.InlineKeyboardButton(text='Таблица(провописание н и нн)', url='https://disk.yandex.ru/i/pQsv8QPMNJS3Lw'),
                      types.InlineKeyboardButton(text='Таблица(Окончания количественных числителных)', url='https://disk.yandex.ru/i/kcGyCpPzqswIyA'),
                      types.InlineKeyboardButton(text='Таблица(Правописание приставок)', url='https://disk.yandex.ru/i/jP0alp8Jjknjzw'),
                      types.InlineKeyboardButton(text='Таблица(Склонение имен существительных)', url='https://disk.yandex.ru/i/cVFaKQzlKYzvmQ'),
                      types.InlineKeyboardButton(text='Определения и примеры', url='https://disk.yandex.ru/i/RPm34NDTVXcdsg')]
            keyboard.add(*button)
            await message.answer('Выбирай тему, которую не понял', reply_markup=keyboard)
        elif message.text == 'Литература':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text='Краткие содержание(Отцы и дети)', url='https://disk.yandex.ru/i/MoAamHg0-xR6-A'),
                      types.InlineKeyboardButton(text='Краткие содержание(Обломов)', url='https://disk.yandex.ru/i/qH-zz1sQl4iYqw'),
                      types.InlineKeyboardButton(text='Краткие содержание(Кому на руси жить хорошо)', url='https://disk.yandex.ru/i/ObM6nhBvJmJJjw'),
                      types.InlineKeyboardButton(text='Краткие содержание(Гроза)', url='https://disk.yandex.ru/i/H1gp7t5RC0Wz0A'),
                      types.InlineKeyboardButton(text='Краткие содержание(Бесприданница)', url='https://disk.yandex.ru/i/QhY-9z_FAB331A'),
                      types.InlineKeyboardButton(text='Краткие содержание(Идиот)', url='https://disk.yandex.ru/i/aLPC6JafnNqqgg'),
                      types.InlineKeyboardButton(text='Краткие содержание(Анна Каренина)', url='https://disk.yandex.ru/i/TYLGV8pa9RSIKA'),
                      types.InlineKeyboardButton(text='Краткие содержание(Вишневый сад)', url='https://disk.yandex.ru/i/LlrL_Shf2GCQ1A'),
                      types.InlineKeyboardButton(text='Определения',url='https://disk.yandex.ru/i/ya4OoeEpLRg0eg')]
            keyboard.add(*button)
            await message.answer('Выбирай тему, которую не понял', reply_markup=keyboard)
        elif message.text == 'Информатика':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text='Определения и примеры', url='https://disk.yandex.ru/i/CMDLpkbAZuRjbQ'),
                      types.InlineKeyboardButton(text='Теорема для программирования', url='https://ppt-online.org/839314'),
                      types.InlineKeyboardButton(text='Таблица(истиности)',url='https://nsportal.ru/sites/default/files/2019/05/08/logika.gif')]
            keyboard.add(*button)
            await message.answer('Выбирай тему, которую не понял', reply_markup=keyboard)
        elif message.text == 'Химия':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text='Определения', url='https://disk.yandex.ru/i/RVSV0M7lGf36Mg'),
                      types.InlineKeyboardButton(text='Формулы и опредления(основные реакции)', url='https://disk.yandex.ru/i/be8_prF8YpzB2w'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Определение элементного состава органических соединений.)',url='https://disk.yandex.ru/i/N2JDgPm7kSytUQ'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Получение и свойства ацетилена.)', url='https://disk.yandex.ru/i/zRsPhwK7oxCXJg'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Свойства белков.)', url='https://disk.yandex.ru/i/BPpbBSb7Uq1ytw'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Свойства глицерина.)',url='https://disk.yandex.ru/i/XMe61awd2F5yTg'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Свойства глюкозы.)', url='https://disk.yandex.ru/i/5AD0NaJAo-WN8A'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Свойства жиров.)', url='https://disk.yandex.ru/i/UWWD5W4P5Hl5OQ'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Свойства крахмала.)', url='https://disk.yandex.ru/i/qSWe041YaOED-g'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Свойства формальдегида.)', url='https://disk.yandex.ru/i/1s8D8cIlW4S6vQ'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Свойства уксусной кислоты.)', url='https://disk.yandex.ru/i/Ph2auhyI5zfDfQ'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Свойства этилового спирта.)', url='https://disk.yandex.ru/i/mQLa9FFnepp5bA'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Сравнение свойств растворов мыла и стирального порошка.)', url='https://disk.yandex.ru/i/AY2IbBbCUOsVNA'),
                      types.InlineKeyboardButton(text='Таблица(формулы и названия кислот и кислотных остатков)', url='https://2.downloader.disk.yandex.ru/preview/02ed4b6382ded6713461e17052e9fab97470c47d2846501d0e7d7978d4ae17e7/inf/0amebvjLlLZn7MmzYVpHOwMO9wX9Ni-KeFVZB9u4_d0No7pCPiUkXMQWDOeiCoWdUHRZjq3aMVinshU19oWjKA%3D%3D?uid=550374507&filename=химия%20таблица%20кислот.jpeg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1903x978'),
                      types.InlineKeyboardButton(text='Таблица(Менделеева)', url='https://1.downloader.disk.yandex.ru/preview/ac9d0ab93afe5f04c33b45ac99501ef0211f18d42a6df2f210cce61c5583f1d3/inf/nlBOJJDjiLnhqdOdPmRarnMsZck1qJyjZB6Noiu9kUTDWp8GBtgTxsxyKxL_JnO61lOpW87om5HpDOqFNRFxjA%3D%3D?uid=550374507&filename=химия%20таблица%20менделеева.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1920x978'),
                      types.InlineKeyboardButton(text='Таблица(Растворимости солец, кислот и оснвоаний в воде)', url='https://1.downloader.disk.yandex.ru/preview/df6b0cfb163b8dbc6207d8cbb672eb06d79ac23eb7fe494a72e66d658ab8f96e/inf/p76TzibeEmOZ2U3YJOrNarwyKB8GHPlTdgmG5i38p63b7arxbfVFtpYoHDiADl2mjTDHCdqSKbrbUrnRVkavSg%3D%3D?uid=550374507&filename=химия%20таблица%20растворимости.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1920x978')]
            keyboard.add(*button)
            await message.answer('Выбирай тему, которую не понял', reply_markup=keyboard)
        elif message.text == 'Биология':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text='Определения',url='https://disk.yandex.ru/i/lYYjoVIsQzkgXQ'),
                      types.InlineKeyboardButton(text='Таблица(белки)',url='https://4.downloader.disk.yandex.ru/preview/175fe7c9bfeb9ae2ed000eacd40eef0262c853569ad7c0006c54f1dd6566a8ae/inf/3ZB81_ueszNFgH-m8xTHNa96l4fzfH9cNbPm8OYTSfqPcoJS5KznL_yeaXThtkLLy9VHlb_EFBiyPs5wEX9-SQ%3D%3D?uid=550374507&filename=биология%20таблица%20белки.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1201x966'),
                      types.InlineKeyboardButton(text='Таблица', url='https://1.downloader.disk.yandex.ru/preview/c94474cbfc0c22e4c3e9f045f389688c71ee6f7ec7a6c9627be1e7647badc77e/inf/6NuMlxYhcfuegLTtv-OOw5FG8rvpzjOtnSj5D9ly0UC1qdlpj84eMtE1WsRtuzcttHNqH_T38ah7BKy16V7GUw%3D%3D?uid=550374507&filename=биология%20таблица%20сравнение%20клеток.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1920x978'),
                      types.InlineKeyboardButton(text='Таблица(строение животной клетки)', url='https://4.downloader.disk.yandex.ru/preview/ce77d7bf44e8338b06ec850e5b248253019c39705ee224324cc40d15f7b3dda7/inf/ICfx-t03nLJ0KvBvwzPGLskSaSPOz4TNDJzfM2AUSOeQCsIQGNtm71wUKR2FrhpD4S84_VRLO7CDbn_hn5m4Kg%3D%3D?uid=550374507&filename=биология%20таблица%20строение%20животной%20клетки.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1920x978'),
                      types.InlineKeyboardButton(text='Таблица(классы углеводов)', url='https://4.downloader.disk.yandex.ru/preview/1adcbb07554ed61f8aeb66d5e86140b8cea8bd56d86bb402f31809a2b179a619/inf/HWHTXq6E6RTD-__i9qilmshDCJ0jfzXnj8aoHQJfOIGrNJdV0XACa95Bh6IJyIt6Cy1cpy5xhOUTGhELTcuEOA%3D%3D?uid=550374507&filename=биология%20таблица%20углеводов.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1920x978'),
                      types.InlineKeyboardButton(text='Таблица(фазы митоза)', url='https://3.downloader.disk.yandex.ru/preview/6ddcc8b37a8d2989ee7a569e095c53471b5252c31d8c6f66781d2b901e874db0/inf/ezaDTV7QC1q0jzI85SAeJh87QHVeyz9IVTK0_V2QFm0YqIn8kjZIjJQWyA7ViIvy-sqMKqo88So6uLgQbPdp5A%3D%3D?uid=550374507&filename=биология%20таблица%20фазы%20митоза.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1903x978'),
                      types.InlineKeyboardButton(text='Таблица(функция белков)', url='https://3.downloader.disk.yandex.ru/preview/ce7f3024ca9e30a4fa9a178756c1af9bfb2f6fec619f18da0a59632e6e6d96ac/inf/Vd1tx7lt39QZ9KdDo2V4VzesND8yySsjcnmGe0EVeDAA5PChrvVn6_rD7XmhRtalQUCw4I1GKphn1ynZYkGuQg%3D%3D?uid=550374507&filename=биология%20таблица%20функции%20белков.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1903x978'),
                      types.InlineKeyboardButton(text='Таблица(хим состав клетки)', url='https://3.downloader.disk.yandex.ru/preview/47e0f4421b705623f2c196705bb10461065162278b502f4b2e5c8a14a1ff3fe9/inf/MSGTVspesV7tZHtRz39h7sA8O3ax7M7x_tip9zLpf0COEGlNbYtMKlW5c_DQCfUZRlyQFP5gLtFiGPS04V5ANQ%3D%3D?uid=550374507&filename=биология%20химический%20состав%20клетки%20таблица.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1903x978')]
            keyboard.add(*button)
            await message.answer('Выбирай тему, которую не понял', reply_markup=keyboard)
        elif message.text == 'Английский язык':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text='Клише писем',url='https://disk.yandex.ru/i/qeX5B7oLX1ow5Q'),
                      types.InlineKeyboardButton(text='Части речи', url='https://disk.yandex.ru/i/XpzySBFJX-9TKw'),
                      types.InlineKeyboardButton(text='Врмена', url='https://3.downloader.disk.yandex.ru/preview/971600f104a9574a0da454bfd00eae98a0adb8c3fec6f3bfcd17bbbfb9af078b/inf/QYxnnNyHdivUG9YueHQq_MfBBve1fQhXEaiacGOJZTfvaCAmkV6v_vu4DY6d5f94Rb1nlqsP3zRaBbOKPNkmxA%3D%3D?uid=550374507&filename=английский%20таблица%20времен.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=550374507&tknv=v2&size=1903x978')]
            keyboard.add(*button)
            await message.answer('Выбирай тему, которую не понял', reply_markup=keyboard)
        elif message.text == 'Физика':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            button = [types.InlineKeyboardButton(text='Определения и формулы', url='https://disk.yandex.ru/i/7_Bn4GLk41RoDA'),
                      types.InlineKeyboardButton(text='Формулы', url='https://disk.yandex.ru/i/6Dl2i2Z5sxWnJw'),
                      types.InlineKeyboardButton(text='Приставки Cи', url='https://sun9-82.userapi.com/impg/cAXf1PuvxhVpJrUtF14ut6hirEnOoOvu79XQNw/zK4EDsPboxI.jpg?size=686x513&quality=96&sign=f9f9356ee0fba1567402c589de736245&type=album'),
                      types.InlineKeyboardButton(text='Таблица(Силы в природе)', url='https://3.downloader.disk.yandex.ru/preview/924dd23c18bcdac206512111f92a3299ddacad265485c11546784b06d8d86a3c/inf/LHo0DAuIiCBSKG9CpGC4ZifbGeHmkucfhP3z4DuqgrFQEn95sEMszV7pyONTNmnjPuJf1Qa0eeVasSaqMoF4Lw%3D%3D?uid=550374507&filename=физика%20таблица%20сил.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=550374507&tknv=v2&size=1903x978'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Измерение ЭДС и внутреннего сопротивления источника тока.)', url='https://disk.yandex.ru/i/0AXHvvpPbme0Ow'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Изучение закона сохранения механической энергии.)',url='https://disk.yandex.ru/i/gCSAYFreftGE9g'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Изучение последовательного и параллельного сопротивления проводников.)', url='https://disk.yandex.ru/i/iI4d0YF-7eAMuA'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Опытная проверка закона Гей-Люссака.)',url='https://disk.yandex.ru/i/xhtBEvY_1K2-aw'),
                      types.InlineKeyboardButton(text='Лаборатораня работа(Изучение движения тела по окружности под действием сил упругости и тяжести.)',url='https://disk.yandex.ru/i/GXakJRTx4WBtuQ'),
                      types.InlineKeyboardButton(text='Изопроцессы',url='https://upload.wikimedia.org/wikipedia/ru/f/f5/Isoprocess.jpg')]
            keyboard.add(*button)
            await message.answer('Выбирай тему, которую не понял', reply_markup=keyboard)
        elif message.text == "9 (ОГЭ)":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = [types.KeyboardButton('Математика'),
                      types.KeyboardButton('Русский язык (ОГЭ)'),
                      types.KeyboardButton('Главное меню')]
            keyboard.add(*button)
            await message.answer('Выбери предмет для сдачи', reply_markup=keyboard)
        elif message.text == "Математика":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = [types.KeyboardButton('Номер 20'),
                      types.KeyboardButton('Номер 21'),
                      types.KeyboardButton('Номер 22'),
                      types.KeyboardButton('Номер 23'),
                      types.KeyboardButton('Номер 24'),
                      types.KeyboardButton('Номер 25'),
                      types.KeyboardButton('Главное меню')]
            keyboard.add(*button)
            await message.answer('Выбери номер', reply_markup=keyboard)

        elif message.text == "Русский язык (ОГЭ)":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = [types.KeyboardButton('Шаблоны сочинений'),
                      types.KeyboardButton('Правила'),
                      types.KeyboardButton('Главное меню')]
            keyboard.add(*button)
            await message.answer('Выбери нужный раздел', reply_markup=keyboard)

        elif message.text == 'Правила':
          img_from_file = open("imgR.txt")
          for img in img_from_file:
            await bot.send_photo(message.from_user.id, img)
          await message.answer('Готово', reply_markup=keyboard1)
        elif message.text == 'Шаблоны сочинений':
          await bot.send_photo(message.from_user.id, 'https://disk.yandex.ru/i/co4BEVVktQVzZw')
          await message.answer('Готово', reply_markup=keyboard1)






        elif message.text == 'Номер 20':
          img_from_file = open("img20.txt")
          number = 1
          for img in img_from_file:
            await bot.send_photo(message.from_user.id, img, '№20 Вариант ' + str(number) + ', задания взяты с сайта ФИПИ')
            number+=1
          await message.answer('Готово', reply_markup=keyboard1)

        elif message.text == 'Номер 21':
          img_from_file = open("img21.txt")
          number = 1
          for img in img_from_file:
            await bot.send_photo(message.from_user.id, img, '№21 Вариант ' + str(number) + ', задания взяты с сайта ФИПИ')
            number+=1
          await message.answer('Готово', reply_markup=keyboard1)

        elif message.text == 'Номер 22':
          img_from_file = open("img22.txt")
          number = 1
          for img in img_from_file:
            await bot.send_photo(message.from_user.id, img, '№22 Вариант ' + str(number) + ', задания взяты с сайта ФИПИ')
            number+=1
          await message.answer('Готово', reply_markup=keyboard1)

        elif message.text == 'Номер 23':
          img_from_file = open("img23.txt")
          number = 1
          for img in img_from_file:
            await bot.send_photo(message.from_user.id, img, '№23 Вариант ' + str(number) + ', задания взяты с сайта ФИПИ')
            number+=1
          await message.answer('Готово', reply_markup=keyboard1)

        elif message.text == 'Номер 24':
          img_from_file = open("img24.txt")
          number = 1
          for img in img_from_file:
            await bot.send_photo(message.from_user.id, img, '№24 Вариант ' + str(number) + ', задания взяты с сайта ФИПИ')
            number+=1
          await message.answer('Готово', reply_markup=keyboard1)

        elif message.text == 'Номер 25':
          img_from_file = open("img25.txt")
          number = 1
          for img in img_from_file:
            await bot.send_photo(message.from_user.id, img, '№25 Вариант ' + str(number) + ', задания взяты с сайта ФИПИ')
            number+=1
          await message.answer('Готово', reply_markup=keyboard1)


        elif message.text == 'Back':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = [types.KeyboardButton('Классы'),
                      types.KeyboardButton('О нас'),
                      types.KeyboardButton('Информация')]
            keyboard.add(*button)
            await message.answer('Здравствуйте, с вами MosObr, буду помогать вам в учебе.',reply_markup=keyboard)

        else:
          await message.answer('Такой команды нет, выбери из предложенных',reply_markup=keyboard1)







if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
