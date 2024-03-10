# установить виртуальное окружение
В терминал пишем:

python3 -m venv venv
# запускаем виртуалку
source venv/bin/activate - для Линуксов

venv\Scripts\activate - Для Виндусов
# Скачиваем все зависимости которые нужны
pip install -r requirements.\prod.txt - для того чтобы запустить проект 

pip install -r  requirements\test.txt - для того чтобы протестировать проект

pip install -r  requirements\dev.txt - для разработки проекта
# Запускаем в dev режиме
cd lyceum

python manage.py runserver