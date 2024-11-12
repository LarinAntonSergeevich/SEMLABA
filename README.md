Проект SaberManager (без Docker)

## Описание

Это приложение реализует авторизацию через GitHub и Яндекс с помощью OAuth, а также использует PostgreSQL в качестве базы данных.

## Настройка окружения

### Шаг 1: Установка зависимостей

1. Создайте виртуальное окружение Python и установите зависимости из `requirements.txt`:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # активация виртуального окружения
    pip install -r requirements.txt
    ```

### Шаг 2: Регистрация OAuth-приложений

#### GitHub

1. Перейдите по ссылке для регистрации приложения GitHub: [https://github.com/settings/applications/new](https://github.com/settings/applications/new).
2. Заполните поля:
   - **Application name**: любое название, например, `SaberManager`.
   - **Homepage URL**: `http://127.0.0.1:5000`.
   - **Authorization callback URL**: `http://127.0.0.1:5000/github/callback`.
3. После создания сохраните `Client ID` и `Client Secret`.

#### Яндекс

1. Перейдите по ссылке для регистрации приложения Яндекс: [https://oauth.yandex.ru/client/new](https://oauth.yandex.ru/client/new).
2. Заполните поля:
   - **Название приложения**: любое название, например, `SaberManager`.
   - **Redirect URI**: `http://127.0.0.1:5000/yandex/callback`.
3. Сохраните `Client ID` и `Client Secret`.

### Шаг 3: Настройка конфигурации

Создайте конфигурацию OAuth в файле `config.py` для использования в приложении:

```python
class Config:
    SECRET_KEY = 'your_secret_key'
    
    # GitHub OAuth
    GITHUB_CLIENT_ID = 'ваш_client_id_от_GitHub'
    GITHUB_CLIENT_SECRET = 'ваш_client_secret_от_GitHub'
    
    # Яндекс OAuth
    YANDEX_CLIENT_ID = 'ваш_client_id_от_Яндекс'
    YANDEX_CLIENT_SECRET = 'ваш_client_secret_от_Яндекс'
    
    # Database URL
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:your_password@localhost:5432/TimeManager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Настройки почты
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''
```

> **Примечание**: Не забудьте заменить `your_password` на пароль пользователя `postgres` для вашей локальной базы данных.

### Шаг 4: Запуск приложения

1. Убедитесь, что PostgreSQL запущен и база данных `TimeManager` создана.
   
2. Выполните команду для запуска приложения:

    ```bash
    python main.py
    ```

3. Приложение будет доступно по адресу: [http://127.0.0.1:5000](http://127.0.0.1:5000).