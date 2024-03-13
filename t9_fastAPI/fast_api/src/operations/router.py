import os

from fastapi import APIRouter, Form, Depends

import base64
import uuid
from pydantic import BaseModel
from database import get_async_session
from operations.models import Documents, Documents_text

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, delete

from tasks.celery_task import scan

router = APIRouter(
    prefix="",
    tags=["API"]
)

@router.post("/upload_doc")
async def upload_doc(filename: str = Form(...), filedata: str = Form(...), session: AsyncSession = Depends(get_async_session)):
    """
   :param filename:  имя файла
   :param filedata: зашифрованные в b64 данные файла в виде строки
   :return: 
    """
    image_as_bytes = str.encode(filedata)  # convert string to bytes
    img_recovered = base64.b64decode(image_as_bytes)  # decode base64string
    ext = filename.split('.')[-1]
    old_filename = filename
    filename = "%s.%s" % (uuid.uuid4(), ext)
    full_filename = "../documents/" + filename
    rst = 0
    try:
        with open(full_filename, "wb") as f:
            f.write(img_recovered)
        # print('чекаем дальше')
        stmt = insert(Documents).values(path=full_filename).returning(Documents.id)
        # print(stmt)
        res = await session.execute(stmt)
        rst = res.scalar()
        # print('какой то результат ', rst)
        await session.commit()

    except Exception as e:
        # print(e)
        return {"message": "error",
                "text": "There was an error uploading the file"
                }
    # print(f"Successfuly uploaded {old_filename}, id doc = {rst}")
    return {
        "message": "Successfuly uploaded",
        "filename": old_filename,
        "doc_id": rst
    }

@router.get('/doc_analyse/{doc_id}')
async def doc_analyse(doc_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    """
    :description: Функция распознает текст из изображения
    :param doc_id: id загруженного ранее документа
    :return:
    """
    try:
        query = select(Documents.path).filter(Documents.id == doc_id)
        result = await session.execute(query)
        path = result.one_or_none()
        if path is None:
            return {'message': "error",
                    "text": f'документ c {doc_id=} не найден !'}
        path = path[0]
        # print('Путь к файлу == ', path)
        scan.delay(path, doc_id)
        # img_text = scan_text.get()
        return {'message': "success",
                "text": 'Изображение обрабатывается'}
    except Exception as e:
        # print(e)
        return {'message': 'error',
                "text": "неизвестная ошибка"}

@router.get('/all')
async def get_all(session: AsyncSession = Depends(get_async_session)):
    """
    :description: Функция выводит всё содержимое из таблицы Documents
    :return:
    """
    query = select(Documents)
    result = await session.execute(query)
    res_list = [r for r in result.scalars().all()]
    return {"message": "success",
            "items": res_list}


@router.get("/get_text/{doc_id}")
async def get_text(doc_id: int, session: AsyncSession = Depends(get_async_session)):
    """По id документа получает текст обработанной картинки из таблицы Document_text\n
       и возвращает этот текст"""
    # проверяем есть ли запись с таким id в таблице Documents
    query = select(Documents).filter(Documents.id == doc_id)
    res = await session.execute(query)
    result = res.one_or_none()
    if result is None:
        return {
            "message": "error",
             "text": f"Записи с {doc_id=}  не существует"
        }

    query = select(Documents_text.text).filter(Documents_text.id_doc == doc_id)
    res = await session.execute(query)
    result = res.one_or_none()
    if result is None:
        return {"message": "unknown",
                 "text":   f"Документа {doc_id=} найден, но не найдена связанная с ним запись. "
                           f"Возможно вы не задавали операцию расшифровки изображения, либо же расшифровка ещё обрабатывается."}
    else:
        return {"message": "success",
                "text": result[0]}


@router.delete('/delete_doc/{doc_id}')
async def delete_doc(doc_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Documents.path).filter(Documents.id == doc_id)
    res = await session.execute(query)
    result = res.one_or_none()
    print(result)
    if result is None:
        return {"message": "error",
                "text": f"Документа с {doc_id=} не существует"}
    else:
        # path = result
        os.remove(*result)
        stmt = delete(Documents).filter(Documents.id == doc_id)
        await session.execute(stmt)
        await session.commit()
        return {"message": "success",
                "text": f"Документ с {doc_id=} и связанное с ним изображение удалены"}