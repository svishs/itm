from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text, desc
from sqlalchemy.orm import aliased, contains_eager, joinedload, selectinload


from database import sync_engine, async_engine, session_factory, Base

from models import (ClientsOrm, EmployeesOrm, ProviderOrm, 
                    DeliveryOrm, OrdersOrm, ProductsOrm,
                    WorkersOrm, ResumesOrm)

from helper.helper_load_data import json_loader

class SyncORM:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        # sync_engine.echo = True

    

    @staticmethod
    def insert_data_in_tables():
        with session_factory() as session:
            sync_engine.echo = False
            cl_json = json_loader('./helper/clients.json')
            emp_json = json_loader('./helper/employees.json')
            prov_json = json_loader('./helper/provider.json')
            delivery_json = json_loader('./helper/delivery.json')
            orders_json =  json_loader('./helper/orders.json')
            prod_json =  json_loader('./helper/products.json')

            insert_clients = insert(ClientsOrm).values(cl_json)
            insert_emp = insert(EmployeesOrm).values(emp_json) 
            insert_prov = insert(ProviderOrm).values(prov_json) 
            insert_delivery = insert(DeliveryOrm).values(delivery_json) 
            insert_orders = insert(OrdersOrm).values(orders_json) 
            insert_prod = insert(ProductsOrm).values(prod_json) 

            
            session.execute(insert_clients)
            session.execute(insert_emp)
            session.execute(insert_prov)
            session.execute(insert_delivery)
            session.execute(insert_prod)
            session.execute(insert_orders)
            # session.execute(insert_resumes)
            session.commit()
            sync_engine.echo = True

            
    @staticmethod
    def select_managers():
        sync_engine.echo = True
        with session_factory() as session:
            query = (
                select(EmployeesOrm)
                # .where(EmployeesOrm.job_title.contains('менеджер'))
                .filter(EmployeesOrm.job_title.contains('менеджер'))
                )
            result = session.execute(query)
            print(f'{type(result)}')
            # cnt = result.count
            
            managers = result.scalars().all()
            cnt = len(managers)
            print(f'========= Найдено {cnt} записей ========')
            print(f'{managers=}')
        sync_engine.echo = False # отключим эхо


    @staticmethod
    def select_distinct_managers():
        sync_engine.echo = True
        with session_factory() as session:
            query = (
                select(EmployeesOrm.job_title).distinct()
                .where(EmployeesOrm.job_title.contains('менеджер'))
                )
            result = session.execute(query)
            print(f'{type(result)}')
            # cnt = result.count
            
            managers = result.scalars().all()
            cnt = len(managers)
            print(f'========= Найдено {cnt} записей ========')
            print(f'{managers=}')
        sync_engine.echo = False # отключим эхо

    @staticmethod
    def select_best_clients():
        '''
        select c.fio, sum(p.selling_price - p.purchase_price) as margin from orders o
            join clients c on o.cl_id = c.id
            join products p on o.prod_id = p.id
            group by c.fio
            order by margin desc;
        '''
        sync_engine.echo = True
        c = aliased(ClientsOrm)
        o = aliased(OrdersOrm)
        p = aliased(ProductsOrm)

        with session_factory() as session:
            query = (
                select(c.fio, 
                       func.sum(p.selling_price - p.purchase_price).label('margin'))
                .select_from(o)
                .join(c, o.cl_id == c.id)
                .join(p, p.id == o.prod_id)
                .group_by(c.fio)    
                .order_by(desc('margin'))                            
            )
            result = session.execute(query)
            print(f'{type(result)}')
            # cnt = result.count
            
            clients = result.all() # в данном случае scalars не заработало..
            cnt = len(clients)
            print(f'{clients=}')
            print(f'========= Найдено {cnt} записей ========')
            for cl in clients:
                fio = "{:<40}|  ".format(cl.fio)
                margin = "{:<10}|".format(cl.margin)
                print(fio + margin)
        sync_engine.echo = False # отключим эхо


    @staticmethod
    def select_emp_with_lazy_orders():
        sync_engine.echo = True
        with session_factory() as session:
            query = (
                select(EmployeesOrm)
            )
            #  используем скалярс -  
            # будет кортеж из одного объекта если без scalars
            # конвертируем к одному объекту
            result = session.execute(query).scalars().all()
            
            for res in result: # type: EmployeesOrm
                print(res.first_name, ' ', res.orders)

        sync_engine.echo = False


    @staticmethod
    def select_emp_with_joined_orders():
        # joinedload не подходит для o2m
        # он подходит для m2o  или o2o 
        print(f'Вызов  select_emp_with_joined_orders()')
        sync_engine.echo = True
        with session_factory() as session:
            query = (
                select(EmployeesOrm)
                .options(joinedload(EmployeesOrm.orders))
            )
            #  используем скалярс,  
            # будет кортеж из одного объекта если без scalars
            # конвертируем к одному объекту
            result = session.execute(query).unique().scalars().all() # используем unique (выполняется на уровне питона) для
            # того чтобы избавиться от дублей возвращаемых EmployyesOrm  
            
            for res in result: # type: EmployeesOrm
                print(res.first_name, ' ', res.orders) # в данном случае не выполняются доп запросы к БД 
                # все данные были выбраны при выполнении session.execute через left outer join 

        sync_engine.echo = False

    @staticmethod
    def select_emp_with_selectin_relationship():
        print(f'Вызов  select_emp_with_selectin_relationship')
        sync_engine.echo = True
        with session_factory() as session:
            query = (
                select(EmployeesOrm)
                .options(selectinload(EmployeesOrm.orders))
            )
            #  используем скалярс
            # будет кортеж из одного объекта, если без scalars
            # конвертируем к одному объекту
            result = session.execute(query).scalars().all()
            
            for res in result: # type: EmployeesOrm
                print(res.first_name, ' ', res.orders)

        sync_engine.echo = False


    @staticmethod
    def del_from_providers():
        print(f'Вызов  del_from_providers')
        with session_factory() as session:
            res = session.query(ProviderOrm).all()
            for pr in res:
                print(f'{pr= }')  # выведем всё что есть в бд до удаления.

            session.query(ProviderOrm).filter(ProviderOrm.pa_name=='Статус').delete()
            
            # проверяем предыдущий запрос повторно. По итогу он как бы удален.
            res = session.query(ProviderOrm).all()
            for pr in res:
                print(f'{pr= }')  # выведем всё что есть в бд до удаления.

            session.commit() # только сейчас делаем коммит

    @staticmethod
    def select_providers():
        print(f'Вызов  del_from_providers')
        with session_factory() as session:
            print(session.query(ProviderOrm).all())

    @staticmethod
    def get_laptop_orders():
        # галимый запрос, выбирает все записи из OrdersOrm, и вставляет пустые списки для тех заказов где не было ноутбуков.
        sync_engine.echo = True
        print(f'Вызов  get_laptop_orders')
        with session_factory() as session:
            query = (
                select(OrdersOrm)
                .options(selectinload(OrdersOrm.orders_for_laptops))
            )
            resp = session.execute(query)
            results = resp.unique().scalars().all()
            for res in results: #type: OrdersOrm
                print(f'{res.orders_for_laptops = }')

    @staticmethod
    def get_laptop_orders_contains_eager():
        #выполняет нормальный  inner join без лишнего мусора который валится в случае с left outer
        with session_factory() as session:
            query = (
                select(OrdersOrm)
                .join(OrdersOrm.product)
                .options(contains_eager(OrdersOrm.product))
                .filter(ProductsOrm.prod_name.contains('ноутбук'))
            )
            res = session.execute(query)
            results = res.unique().scalars().all()
            print(f'{results=}')


    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_michael = WorkersOrm(username="Michael")
            session.add_all([worker_jack, worker_michael])
            # flush отправляет запрос в базу данных
            # После flush каждый из работников получает первичный ключ id, который отдала БД
            # flush позволяет получать до коммита значения автогенерируемых полей
            #  с помощью relationship можно не прибегать к flush, но достигать такого же функционала

            session.flush()
            session.commit()
            

    @staticmethod
    def select_workers():
        with session_factory() as session:
            #  два способа.
            #  1. через session.get()
            # worker_id  = 1
            # worker_jack = session.get(WorkersOrm, worker_id)
            # worker_jack = session.get(WorkersOrm, {"id": worker_id})
            # worker_jack = session.get(WorkersOrm, (worker_id, 2))



            query = select(WorkersOrm)
            result = session.execute(query)
            # workers = result.all() # вернет список кортежей экземпляров объектов WorkersOrm
            #  т.е. экземпляры моделей [(<models.WorkerOrm....>, ),(<models.WorkerOrm....> ,)]
            # workers = result.all()[0][0] # к которым можно обращаться по индексам 
            # 


            workers = result.scalars().all()
            # [<models.WorkerOrm.... object at >, <models.WorkerOrm.... object at >]
            # print(f"{workers=}")

    @staticmethod
    def update_worker( worker_id: int = 1, new_username:str = 'Misha'):
        with session_factory() as session:
            worker_michael = session.get(WorkersOrm, worker_id)
            worker_michael.username = new_username
            # не надо описывать сырой sql запрос, биндить параметры, алкеми делает всё сама
            # session.add(worker_michael) # этого уже делать не нужно

            # на самом деле в таком варианте выполняется 2 
            # запроса - сначала получаем объект, потом делаем апдейт 

            #
            # session.expire(worker_michael) # отменяет все изменения объекта
            # # синхронная операция (НЕ асинхронная!)
            # session.expire_all() # отменяет изменения всех объектов

            # #
            # session.refresh(worker_michael) # возвращает то состояние которое находится в БД

            session.commit()


