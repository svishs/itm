
from database import get_async_session
from operations.models import Documents, Documents_text
from sqlalchemy import insert

full_filename = 'adfadfadfasdf'
async with get_async_session() as conn:
    stmt = insert(Documents).returning(Documents.id)
    print(stmt)
    res = conn.execute(stmt, {"path": full_filename})
    result = res.scalar()
    print(result)
    # conn.refresh(doc)
    # conn.commit()
    # insert_stmt = Docinsert(Documents).returning(Documents.id)
    # stmt = insert(Documents).values(Documents.path =full_filename )
    # insert_stmt = Documents.insert().returning(table.c.id)
    # result = conn.execute(stmt, values)
    conn.commit()

