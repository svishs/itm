from celery import Celery
from PIL import Image
import pytesseract
from database import sync_session_maker
from operations.models import Documents_text
from sqlalchemy import insert
# import os
# import logging
# logger = logging.getLogger(__name__)
celery = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@celery.task # для запуска из каталога src # celery -A tasks.celery_task worker --loglevel=INFO
def scan(image: str, id_doc: int ) -> None:
    """получение текста из картинки"""
    try:
        # current_dir = os.getcwd()
        # logger.info(''current_dir+image)
        # print(f'{current_dir=}')
        img = Image.open(image)
        extr_text = pytesseract.image_to_string(img)

        with sync_session_maker() as conn:
            stmt = insert(Documents_text).values(id_doc= id_doc, text = extr_text)
            conn.execute(stmt)
            conn.commit()
    except Exception as e:
        print(e)




