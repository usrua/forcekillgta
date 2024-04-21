import psutil
import pystray
import keyboard
import subprocess
import os
from PIL import Image

def force_kill_process(substring):
    for proc in psutil.process_iter(['pid', 'name']):
        if substring.lower() in proc.info['name'].lower():  # Зробити пошук нечутливим до регістру
            try:
                proc.kill()
                print(f"Процес {proc.info['name']} успішно примусово завершено.")
            except Exception as e:
                print(f"Помилка під час спроби примусового завершення процесу {proc.info['name']}: {e}")

def on_activate():
    force_kill_process("gta")

def on_exit():
    subprocess.call(["taskkill", "/F", "/PID", str(os.getpid())])

def create_tray_icon():
    icon_path = os.path.join(os.path.dirname(__file__), "sa.png")
    icon = Image.open(icon_path)
    menu = (pystray.MenuItem("Закрити GTA", on_activate), pystray.MenuItem("Закрити", on_exit))
    tray_icon = pystray.Icon("name", icon, "AntiBugGTA", menu)
    tray_icon.run()

keyboard.add_hotkey("ctrl+alt+f1", on_activate)  # Додаємо гарячі клавіші для активації функції on_activate
create_tray_icon()  # Запуск функції створення іконки в треї
