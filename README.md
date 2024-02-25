# установить виртуальное окружение
В терминал пишем:

python3 -m venv venv
# запускаем виртуалку
source venv/bin/activate - для Линуксов

venv\Scripts\activate - Для Виндусов
# Скачиваем все зависимости которые нужны
pip install -r requirements.txt
# Запускаем в dev режиме
cd Django4.2 

cd lyceum

python manage.py runserver
