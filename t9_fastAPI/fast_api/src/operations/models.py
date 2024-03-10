import datetime
from typing import Annotated
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

class Documents(Base):
    __tablename__ = 'documents'
    path: Mapped[str]
    date: Mapped[created_at]


class Documents_text(Base):
    __tablename__ = 'documents_text'
    id_doc: Mapped[int] = mapped_column(ForeignKey('documents.id', ondelete='CASCADE'), unique=True)
    text: Mapped[str]


