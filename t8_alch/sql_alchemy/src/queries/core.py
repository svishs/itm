from sqlalchemy import text, insert, select, update
from database import sync_engine, async_engine

from imp_models import metadata_obj, employees_table, workers_table


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True
    
def insert_data():
    with sync_engine.connect() as conn:
        #  стейтмент - insert, update, delete
        # query - select запрос
#         stmt = """INSERT INTO employees (address, sec_name, first_name,  surname, telephone, date_of_birth, job_title ) VALUES 
# ('г. Санкт-Петербург, ул. Северная, д. 7 кв. 9', 'Кольцов', 'Константин', 'Петрович', '+79192370507', '1999-01-12', 'директор'),
# ('г. Дзержинск, ул. Комсомольская, д. 30 кв. 29', 'Мовсесян', 'Эмиль', 'Юрьевич', '+79116748476', '1997-12-07', 'водитель'),
# ('г. Саранск, ул. Молодежная, д. 10 кв. 25', 'Дорофеев', 'Артём', 'Александрович', '+79174289056', '1980-04-03', 'менеджер'),
# ('г. Чебоксары, ул. Лесная, д. 17 кв. 6', 'Нефедова', 'Светлана', 'Анатольевна', '+79205188411', '1986-11-20', 'HR-менеджер'),
# ('г. Ярославль, ул. Заречная, д. 9 кв. 32', 'Якимцов', 'Дмитрий', 'Владимирович', '+79203162964', '1980-05-03', 'кладовщик'),
# ('г. Волгодонск, ул. Гагарина, д. 1 кв. 40', 'Чистякова', 'Елена', 'Алексеевна', '+79265341812', '1988-01-25', 'секретарь'),
# ('г. Тула, ул. Северная, д. 3 кв. 5', 'Рудакова', 'Светлана', 'Эдуардовна', '+79066421943', '1987-08-02', 'уборщица'),
# ('г. Сургут, ул. Октябрьская, д. 28 кв. 27', 'Матковский', 'Александр', 'Викторович', '+79224004723', '2000-03-10', 'менеджер по продажам'),
# ('г. Орёл, ул. Зеленая, д. 3 кв. 44', 'Яковлев', 'Дмитрий', 'Васильевич', '+79853000225', '1981-08-20', 'менеджер по продажам'),
# ('г. Челябинск, ул. Лесная, д. 19 кв. 38', 'Порохина', 'Мария', 'Владимировна', '+79034428960', '1985-11-02', 'менеджер по продажам'),
# ('г. Новочеркасск, ул. Октябрьская, д. 1 кв. 24', 'Фролова', 'Вера', 'Евгеньевна', '+79612627232', '1998-10-17', 'консультант'),
# ('г. Саратов, ул. Мира, д. 9 кв. 33', 'Веркина', 'Анастасия', 'Сергеевна', '+79535194334', '1981-08-02', 'юрист');
#         """
        # res = conn.execute(text(stmt))       
        stmt = insert(employees_table).values(
            [
                {"address": "г. Санкт-Петербург, ул. Северная, д. 7 кв. 9",
                 "sec_name":"Кольцов", 
                 "first_name": 'Константин',
                 "surname": 'Петрович',
                 'telephone': '+79192370507', 
                 'date_of_birth': '1999-01-12', 'job_title':'директор'},
            ]
        )
        res = conn.execute(stmt)
        conn.commit()


class SyncCore:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        # sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with sync_engine.connect() as conn:
            # stmt = """INSERT INTO workers (username) VALUES 
            #     ('Jack'),
            #     ('Michael');"""
            stmt = insert(workers_table).values(
                [
                    {"username": "Jack"},
                    {"username": "Michael"},
                ]
            )
            conn.execute(stmt)
            conn.commit()


    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_table) # Select * from workers
            res  = conn.execute(query)
            workers = res.all() # не нужно использовать scalars поскольку это не имеет большого смысла
            print(f'{workers=}')


    @staticmethod
    def update_worker( worker_id: int = 1, new_username:str = 'Misha'):
        with sync_engine.connect() as conn:
            # stmt = text('update workers set username = :username where id = :id ')
            # stmt = stmt.bindparams(username = new_username, id = worker_id)
            stmt = (
                update(workers_table)
                .values(username=new_username)
                # .where(workers_table.c.id==worker_id)
                .filter_by(id=worker_id)
            )
            
            conn.execute(stmt)
            conn.commit()

