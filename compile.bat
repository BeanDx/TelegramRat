@echo off

pip install --upgrade pip
pip install pyinstaller
pip install aiogram
pip install requests
pip install opencv-python
pip install psutil
pip install GPUtil
pip install tabulate
pip install pycryptodome
pip install comtypes
pip install PyAutoGUI
pip install pycaw
pip install cryptography
pip install Pillow
pip install keyboard
pip install pyperclip
pip install pypiwin32
pip install wave
pip install pyttsx3
pip install pywin32

pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --version-file "version.py" --add-data "logs;logs/" --add-data "keyboards;keyboards/" --add-data "functions;functions/" --add-data "videoplayback.mp4;."  "main.py"


rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null