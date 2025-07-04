import logging

logger = logging.getLogger(__name__)

import requests


API1_URL = "http://34.9.223.19:8000/translate/ru-kk/"


async def translate_text(text: str) -> str:
    """Функция для отправки текста на перевод через API1"""
    try:
        response = requests.post(
            API1_URL,
            json={"text": text, "target_language": "ru"}
        )
        response.raise_for_status()
        return response.json().get("translated_text", text)
    except Exception as e:
        print(f"Translation error: {e}")
        return text
