import datetime
from typing import Optional, Annotated
from sqlalchemy import (
    Table, Column, Integer, String, DateTime, Date,
    Numeric, Index, CheckConstraint,
    MetaData, ForeignKey, func, text)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, str_256, num_10_2
import enum
from decimal import Decimal

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]



class EmployeesOrm(Base):
    __tablename__ = 'employees'
    id: Mapped[int]  = mapped_column(primary_key=True)
    first_name: Mapped[str]
    sec_name: Mapped[str]
    surname:Mapped[str]
    job_title:Mapped[str]
    address:Mapped[str]
    telephone:Mapped[str]
    date_of_birth: Mapped[datetime.date]
    
    # один ко многим  
    orders: Mapped[list['OrdersOrm']] = relationship(
        back_populates='empoloyer'
    )


class ClientsOrm(Base):
    __tablename__ = 'clients'
    id:Mapped[intpk]
    address:Mapped[str]
    telephone:Mapped[str]
    fio:Mapped[str]

    # o2m
    orders: Mapped[list['OrdersOrm']] = relationship(
        back_populates='client'
    )

class ProviderOrm(Base):
    __tablename__ = 'providers'
    id:Mapped[intpk]
    telephone:Mapped[str]
    address:Mapped[str]
    pa_name:Mapped[str]
    representative:Mapped[str]
    contact:Mapped[str]
    # o2m
    delyveries: Mapped[list['DeliveryOrm']] = relationship(
        back_populates='provider'
    )
    repr_cols = ('pa_name', 'representative', 'contact')


class DeliveryOrm(Base):
    __tablename__ = 'delivery'
    id:Mapped[intpk]
    pr_id: Mapped[Optional[int]] = mapped_column(ForeignKey('providers.id', ondelete='set null'))
    del_date:Mapped[datetime.date]

    # многие к одному
    provider: Mapped['ProviderOrm'] = relationship(
        back_populates='delyveries'
    )
    
    # один ко многим o2m
    products: Mapped[list['ProductsOrm']] = relationship(
        back_populates='delyvery'
    )
 



class ProductsOrm(Base):
    __tablename__ = 'products'
    id: Mapped[intpk]
    del_id: Mapped[Optional[int]] = mapped_column(ForeignKey('delivery.id', ondelete='set null'))
    prod_name: Mapped[str]
    specifications: Mapped[Optional[str]]
    descr: Mapped[Optional[str]] # nullable 
    img: Mapped[Optional[str]]
    purchase_price: Mapped[num_10_2]
    availability: Mapped[bool]
    amount: Mapped[int]
    selling_price: Mapped[num_10_2]
    total_cost: Mapped[Optional[num_10_2]]

    # многие к одному
    delyvery: Mapped['DeliveryOrm'] = relationship(
        back_populates='products'
    )

    # один ко многим
    orders: Mapped[list['OrdersOrm']] = relationship(
        back_populates='product'
    )

    # laptop_orders: Mapped[list['OrdersOrm']] = relationship(
    #     back_populates='orders_for_laptops',
    #     primaryjoin = 'and_()'

    # )
    

class OrdersOrm(Base):
    __tablename__ = 'orders'
    id:Mapped[intpk]
    emp_id:Mapped[Optional[int]] = mapped_column(ForeignKey('employees.id', ondelete='set null'))        
    prod_id:Mapped[Optional[int]] = mapped_column(ForeignKey('products.id', ondelete='set null'))       
    cl_id: Mapped[Optional[int]] = mapped_column(ForeignKey('clients.id', ondelete='set null'))
    reg_date: Mapped[datetime.date] 
    date_of_completion: Mapped[Optional[datetime.date]]

    # многие к одному 
    empoloyer: Mapped['EmployeesOrm'] = relationship(
        back_populates='orders'
    ) 
    
    product: Mapped['ProductsOrm'] = relationship(
        back_populates='orders'
    )
    
    client: Mapped['ClientsOrm'] = relationship(
        back_populates='orders'
    ) 

    orders_for_laptops: Mapped['ProductsOrm'] = relationship(
        # back_populates='laptop_orders',
        back_populates='orders',
        primaryjoin = 'and_(OrdersOrm.prod_id==ProductsOrm.id, ProductsOrm.prod_name.contains("ноутбук"))',
    )

class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    username: Mapped[str]

    resumes: Mapped[list["ResumesOrm"]] = relationship(
        back_populates="worker",
    )

    resumes_parttime: Mapped[list["ResumesOrm"]] = relationship(
        back_populates="worker",
        primaryjoin="and_(WorkersOrm.id == ResumesOrm.worker_id, ResumesOrm.workload == 'parttime')",
        order_by="ResumesOrm.id.desc()",
    )
    

class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    worker: Mapped["WorkersOrm"] = relationship(
        back_populates="resumes",
    )

    vacancies_replied: Mapped[list["VacanciesOrm"]] = relationship(
        back_populates="resumes_replied",
        secondary="vacancies_replies",
    )

    repr_cols_num = 2
    repr_cols = ("created_at", )

    __table_args__ = (
        Index("title_index", "title"),
        CheckConstraint("compensation > 0", name="checl_compensation_positive"),
    )


class VacanciesOrm(Base):
    __tablename__ = "vacancies"

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[Optional[int]]

    resumes_replied: Mapped[list["ResumesOrm"]] = relationship(
        back_populates="vacancies_replied",
        secondary="vacancies_replies",
    )


class VacanciesRepliesOrm(Base):
    __tablename__ = "vacancies_replies"

    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        primary_key=True,
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id", ondelete="CASCADE"),
        primary_key=True,
    )

    cover_letter: Mapped[Optional[str]]