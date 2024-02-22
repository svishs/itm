from sqlalchemy import (
    Table, Column, Integer, String, 
    Date,
    MetaData)


metadata_obj = MetaData()

# императивный способ объявления моделей

employees_table = Table(
    "employees",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column('first_name', String ),
    Column('sec_name', String ),
    Column('surname', String ),
    Column('job_title', String ),
    Column('address', String),
    Column('telephone', String),
    Column('date_of_birth', Date)
)

workers_table = Table(
    "workers", 
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column('username', String )
)