import logging
from datetime import datetime



# Создаем логгер
logger = logging.getLogger("main.middleware")


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логируем информацию о входящем запросе
        # session_id =  
        # logger.info(f"Incoming request: {request.method} {request.get_full_path()}")
        logger.info("Incoming request:method %s , path %s", request.method, request.path)

        # Обрабатываем запрос
        response = self.get_response(request)

        # Логируем информацию об ответе
        # logger.info(f"Outgoing response: {response.status_code} {response.reason_phrase}")
        logger.info("Outgoing response: %d %s", response.status_code , response.reason_phrase)

        return response