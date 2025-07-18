📄 API Document Translation Service

FastAPI сервис для перевода текста в DOCX файлах с сохранением форматирования
🚀 Основные возможности

    Принимает файлы формата .docx через POST-запрос

    Извлекает текст с сохранением структуры документа

    Переводит текст через внешнее API-переводчик

    Возвращает переведенный документ с оригинальным форматированием

⚙️ Технологии

    Python 3.9+

    FastAPI (веб-фреймворк)

    python-docx (работа с DOCX)

    Requests (HTTP-запросы)

    Pytest (тестирование)

Установка

    Клонируйте репозиторий:

bash

git clone https://github.com/IlyasSultanov/API_document_translation.git
cd API_document_translation

    Установите зависимости:

bash

pip install poetry

    Запустите сервер:

bash

uvicorn main:app --reload

📡 API Endpoints
POST /translate_docx/

Перевод DOCX документа

Параметры:

    file: DOCX файл для перевода (обязательно)

Ответ:

    Переведенный DOCX файл с префиксом translated_

Пример запроса (cURL):
bash

curl -X POST -F "file=@document.docx" http://localhost:8000/translate_docx/ --output translated.docx

🔧 Конфигурация

Настройки внешнего API переводчика можно изменить в файле:
text

src/config.py

Доступные параметры:
python

TRANSLATION_API_URL = "http://translation-service/api/translate"
TIMEOUT = 30  # сек

🧪 Тестирование

Запуск тестов:
bash

pytest tests/ -v

Покрытие тестами:
bash

pytest --cov=src tests/

🌐 Демо

Сервис доступен по адресу:
http://localhost:8000/docs
(автоматически сгенерированная документация Swagger UI)
📝 Пример использования
python

import requests

url = "http://localhost:8000/translate_docx/"
files = {"file": open("document.docx", "rb")}

response = requests.post(url, files=files)
with open("translated_document.docx", "wb") as f:
    f.write(response.content)

📌 Особенности реализации

    Сохранение оригинального форматирования документа

    Обработка больших файлов (постепенная загрузка)

    Логирование всех операций

    Поддержка асинхронных запросов