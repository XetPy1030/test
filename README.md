Открыть
Открываем в PyCharm директорию maindir
Выбираем виртуальное окружение.
Для этого заходим File/Settings/Project: maindir/Python Interpreter
Жмем "add interpreter", далее "add local interpreter", выбираем Poetry Environment, далее Existing Environment и находим наше окружение по имени или пути, созданное в 1-2 пунктах.
Указываем PyCharm где нужно применять Django (File/Settings/Languages & Frameworks)
Помечаем директорию src/ как ресурсную, для этого правой кнопкой мыши кликаем по src, наводим в появившемся окне "Mark Directory as" и выбираем Sources Root

Правила
Абсолютно все приложения django создаются внутри директории apps/
Внтры apps.py Настроить (
name = "apps.Название_приложения"
)

Внутри setting.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.Название приложения.apps.PaymentConfig'
]

внутри папки api/

auth/ - аунтификация для api, а также всякие permissions для эндпоинтов API и т.д.

v1/ - версия API, здесь собираются директории (python package, тождественные названию приложений в apps), в которых уже находятся views.py

Добавление пакета python:
   poetry add название_пакета
