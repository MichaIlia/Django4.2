# Для начала работы нам нужно установить виртуальное окружение
Для этого в терминале необходимо прописать:

python3 -m venv venv

После чего у нас создастся папка с названием venv

# Далее нам нужно запустить виртуальное окружение исходя из того, какая у нас операционная система:
source venv/bin/activate - для Linux

venv\Scripts\activate - Для Windows

# Скачиваем зависимости для разных случае которые нам нужны:
pip install -r requirements.\prod.txt - для того чтобы запустить проект 

pip install -r  requirements\test.txt - для того чтобы протестировать проект

pip install -r  requirements\dev.txt - для разработки проекта

# Запускаем наш проект в dev режиме
cd lyceum

python manage.py runserver
